from django import forms
from django.forms.models import inlineformset_factory, BaseInlineFormSet
from .models import ReportModel, ReportFilesModel, ReportConnectionsModel

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, ButtonHolder, HTML

from django.utils import timezone

class ReportCreateForm(forms.ModelForm):
    url = "create-report-view"
    title = "Malware Analysis Report Sheet"

    class Meta:
        model = ReportModel
        fields = [
            'malware_name',
            'category',
            'group',
            'investigator_name',
            'started',
            'ended',
            'summary',
        ]
        widgets = {
            'malware_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Malware name'
            }),
            'category': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Malware Category'
            }),
            'group': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Malware Group'
            }),
            'investigator_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Author Name'
            }),
            'started': forms.DateInput(attrs={
                'type': 'date'
            }),
            'ended': forms.DateInput(attrs={
                'type': 'date'
            }),
            'summary': forms.Textarea(attrs={
                'rows':4, 
                'class': 'form-control',
                'placeholder': 'Key observations, recommendations and possible limitations'}),
        }

    def __init__(self, *args, **kwargs):
        super(ReportCreateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('malware_name', css_class='form-group col-md-4 mb-0'),
                Column('category', css_class='form-group col-md-4 mb-0'),
                Column('group', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('investigator_name', css_class='form-group col-md-4 mb-0'),
                Column('started', css_class='form-group col-md-4 mb-0'),
                Column('ended', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            'summary',
        )


class ReportFilesForm(forms.ModelForm):
    
    class Meta:
        model = ReportFilesModel
        fields = [
            'file',
            'hash',
            'notes',
        ]
        widgets = {
            'file': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'File name, type, size'
            }),
            'hash': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'File hashes'
            }),
            'notes': forms.Textarea(attrs={
                'rows':4, 
                'class': 'form-control',
                'placeholder': 'Additional Notes'
            })
        }

    def __init__(self, *args, **kwargs):
        super(ReportFilesForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('file', css_class='form-group col-md-4 mb-0'),
                Column('hash', css_class='form-group col-md-4 mb-0'),
                Column('notes', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
        )



class ReportConnectionsForm(forms.ModelForm):

    class Meta:
        model = ReportConnectionsModel
        fields = [
            'url',
            'ip',
            'notes',
        ]
        widgets = {
            'url': forms.URLInput(attrs={
                'lable': 'Link',
                'class': 'form-control',
                'placeholder': 'Enter valid URL'
            }),
            'ip': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter valid IP'
            }),
            'notes': forms.Textarea(attrs={
                'rows':4, 
                'class': 'form-control',
                'placeholder': 'Additional Notes'
            })
        }
        labels = {
            'url': 'Link',
            'ip': 'IP'
        }

    def __init__(self, *args, **kwargs):
        super(ReportConnectionsForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('url', css_class='form-group col-md-4 mb-0'),
                Column('ip', css_class='form-group col-md-4 mb-0'),
                Column('notes', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
        )


FilesFormSet = inlineformset_factory(
    ReportModel,
    ReportFilesModel,
    ReportFilesForm,
    fields=('file',
            'hash',
            'notes',
            ),
    extra=1,
)


ConnectionsFormSet = inlineformset_factory(
    ReportModel,
    ReportConnectionsModel,
    ReportConnectionsForm,
    fields=('url',
            'ip',
            'notes',
            ),
    extra=1,
)


