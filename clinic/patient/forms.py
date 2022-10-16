from django import forms

from clinic import settings
from patient.models import Patient, PatientComments
from django.forms import DateField, DateInput
from django.contrib.admin import widgets


class AddPatientForm(forms.ModelForm):
    bdate = DateField(label='День рождения', input_formats=settings.DATE_FORMAT,
                      widget=DateInput(attrs={'type': 'date', 'value': '2000-01-01'},  ))
    date_of_issue = DateField(label='Дата выдачи', input_formats=settings.DATE_FORMAT,
                      widget=DateInput(attrs={'type': 'date', 'value': '2000-01-01'}, ))
    class Meta:
        model = Patient
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddPatientForm, self).__init__(*args, **kwargs)
        self.fields['bdate'].widget = widgets.AdminDateWidget()
        self.fields['date_of_issue'].widget = widgets.AdminDateWidget()
        for field_name, field in self.fields.items():
            if field_name != 'is_active':
                field.widget.attrs['class'] = 'form-control'


class PatientCommentForm(forms.ModelForm):
    class Meta:
        model = PatientComments
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super(PatientCommentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['cols'] = '110'
            field.widget.attrs['rows'] = '6'
