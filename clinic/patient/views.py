from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from patient.forms import AddPatientForm, PatientCommentForm
from patient.models import Patient
from datetime import datetime


def dogovor2str(request, pk):
    title = 'Гастроцентр "Здоровье" - Согласие на обработку персоональных данных'
    patient = get_object_or_404(Patient, pk=pk)
    dt = datetime.now()
    day = dt.day
    year = dt.year

    context = {
        'title': title,
        'patient': patient,
        'day': day,
        'year': year,

    }

    return render(request, 'patient/dogovor2str.html', context)


def opd(request, pk):
    title = 'Гастроцентр "Здоровье" - Согласие на обработку персоональных данных'
    patient = get_object_or_404(Patient, pk=pk)

    context = {
        'title': title,
        'patient': patient,

    }

    return render(request, 'patient/opd.html', context)


def patients(request):
    title = 'Гастроцентр "Здоровье" - Пациенты'
    all_patients = Patient.objects.all()
    search_query = request.GET.get('query')
    if not search_query:
        search_query = ''

    if search_query != '':
        all_patients = Patient.objects.filter(lastname__contains=search_query)

    context = {
        'title': title,
        'all_patients': all_patients,

    }

    return render(request, 'patient/patients.html', context)


def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    title = f'Гастроцентр "Здоровье" - Карточка пациента {patient.lastname} {patient.firstname} {patient.middlename}'
    patients_form = AddPatientForm(request.POST, request.FILES, instance=patient)
    comment = PatientCommentForm(request.POST, request.FILES)

    if request.method == 'POST' and 'submit_client' or 'submit_comment' in request.POST:
        if patients_form.is_valid() and comment.is_valid():
            comment_form = comment.save(commit=False)
            if comment_form.comment != '':
                comment_form.patient_comment = Patient.objects.get(id=pk)
                patients_form.save()
                comment_form.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                patients_form.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        patients_form = AddPatientForm(instance=patient)
        comment = PatientCommentForm()

    context = {
        'title': title,
        'update_form': patients_form,
        'patient': patient,
        'comment': comment,

    }

    return render(request, 'patient/patient_detail.html', context=context)


def add_patient(request):
    title = f'Гастроцентр "Здоровье" - создание карточки пациента'
    patient_form = AddPatientForm

    if request.method == 'POST':
        patient_form = AddPatientForm(request.POST, request.FILES)
        if patient_form.is_valid:
            patient_form.save()
            return HttpResponseRedirect(reverse('patient:patients'))

    context = {
        'title': title,
        'form': patient_form,
        'user': request.user,
    }

    return render(request, 'patient/add_patient.html', context=context)
