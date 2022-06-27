from django.shortcuts import render, get_object_or_404, redirect
from .forms import PatientForm
from .models import Patient
# Create your views here.

def add_patient(request):
    template_name = 'patients/add_patient.html'
    context = {}
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('patients:list_patients')
    form = PatientForm()
    context['form'] = form
    return render(request, template_name, context)

def list_patients(request):
    template_name = 'patients/list_patients.html'
    patients = Patient.objects.filter()
    context = {
        'patients': patients,
    }
    return render(request, template_name, context)

def edit_patient(request, id_patient):
    template_name = 'patients/add_patient.html'
    context ={}
    patient = get_object_or_404(Patient, id=id_patient)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patients:list_patients')
    form = PatientForm(instance=patient)
    context['form'] = form
    return render(request, template_name, context)

def delete_patient(request, id_patient):
    patient = Patient.objects.get(id=id_patient)
    patient.delete()
    return redirect('patients:list_patients')
