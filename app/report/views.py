from django.shortcuts import render, redirect
from django.http import FileResponse
from django.forms.models import model_to_dict
from .forms import ReportCreateForm, FilesFormSet, ConnectionsFormSet

from aws_requests_auth.aws_auth import AWSRequestsAuth

from jinja2 import Template

import pdfkit
import qrcode
import io
import base64
import os
import requests
import json
import pendulum

_EVENT_ID = os.getenv("EVENT_ID", None)
_AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY", None)
_AWS_SECRET = os.getenv("AWS_SECRET", None)
_REST_API = os.getenv("REST_API", None)
_BASE_URL = os.getenv("BASE_URL", None)

def index(request):
    return render(request, 'report/index.html')


def reportcreateview(request):
    if request.method == 'POST':
        reportform = ReportCreateForm(request.POST)
        if reportform.is_valid():
            report = reportform.save(commit=False)
            filesform = FilesFormSet(request.POST, instance=report)
            connectionsform = ConnectionsFormSet(request.POST, instance=report)
            if filesform.is_valid() and connectionsform.is_valid():
                report.save()
                filesform.save()
                connectionsform.save()
            data = pre_process(report, filesform.cleaned_data, connectionsform.cleaned_data)
            print(pendulum.now())
            api_result = send_api(data)
            print(pendulum.now())
            pdf = run_template(data)
            print(pendulum.now())
            return FileResponse(pdf, as_attachment=True, filename='report.pdf')
        return redirect('index-view')
    else:
        filesform = FilesFormSet()
        connectionsform = ConnectionsFormSet()
        reportform = ReportCreateForm()
    context = {
        'report': reportform,
        'files': filesform,
        'connections': connectionsform,
    }
    return render(request, 'report/report-create.html', context)


def send_api(data):
    auth = AWSRequestsAuth(aws_access_key=_AWS_ACCESS_KEY,
                        aws_secret_access_key=_AWS_SECRET,
                        aws_host=_REST_API,
                        aws_region='us-west-2',
                        aws_service='execute-api')
    headers = {'Content-Type': 'application/json'}
    response = requests.post(f'{_REST_API}/exploit/api/{_EVENT_ID}/generate_report/',
                            auth=auth, headers=headers, json=data)
    return response


def pre_process(report_obj, files, connections):
    url = f"{_BASE_URL}/image/mdv/{_EVENT_ID}/{report_obj.id}/report.pdf"
    qr_png = generate_qr(url)
    data = {}
    started_str = str(report_obj.started).split(" ")[0]
    ended_str = str(report_obj.ended).split(" ")[0]
    data['malware_name'] = report_obj.malware_name
    data['category'] = report_obj.category
    data['group'] = report_obj.group
    data['investigator_name'] = report_obj.investigator_name
    data['summary'] = report_obj.summary
    data['started'] = started_str
    data['ended'] = ended_str
    for file in files:
        del file['report']
        del file['id']
        del file['DELETE']
    for conn in connections:
        del conn['report']
        del conn['id']
        del conn['DELETE']
    data['files'] = files
    data['connections'] = connections
    data['qr_png'] = qr_png
    data['report_id'] = str(report_obj.id)
    return data


def run_template(report):
    html_path = generate_report_html(report)
    pdf_path = html2pdf(html_path, pdf_path=f"./report/templates/report/forms/report.pdf")
    pdf = open(pdf_path, 'rb')
    return pdf


def generate_report_html(report):
    with open(f'./report/templates/report/forms/template.html','r') as t:
        html_template = t.read()
    template = Template(html_template)
    rendered = template.render(**report)
    html_path = f'./report/templates/report/forms/report.html'
    with open(html_path,'w') as out:
        out.write(rendered)
    return html_path


def html2pdf(html_path, pdf_path):
    """
    Convert html to pdf using pdfkit which is a wrapper of wkhtmltopdf
    """
    options = {
        'page-size': 'Letter',
        'margin-top': '0.35in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None,
    }
    with open(html_path) as f:
        pdfkit.from_file(f, pdf_path, options=options)
    return pdf_path


def generate_qr(id):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=4,
        border=4,
    )
    qr.add_data(id)
    qr.make(fit=True)
    img = qr.make_image()
    buffered = io.BytesIO()
    img.save(buffered, format="png")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str