from jinja2 import Template

from weasyprint import HTML


def run_template():
    file_name = 'report_test'
    report = {'malware_name': 'name', 'category': 'cat', 'group': 'grouppie', 'investigator_name': 'liu', 'started': "2022.05.25", 'ended': "2022.05.25", 'summary': 'summa', 'files': [], 'connections': []}
    html_path = generate_report_html(file_name, report)
    HTML(html_path).write_pdf(f"./report/templates/report/forms/{file_name}.pdf")



def generate_report_html(file_name, report):
    with open(f'./report/templates/report/forms/template.html','r') as t:
        html_template = t.read()
    template = Template(html_template)
    rendered = template.render(**report)
    html_path = f'./report/templates/report/forms/{file_name}.html'
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

run_template()