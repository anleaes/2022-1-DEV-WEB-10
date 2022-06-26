from django.shortcuts import render, get_object_or_404, redirect
from .forms import SpecialtyForm
from .models import Specialty

# Create your views here.
def add_specialty(request):
    template_name = 'specialties/add_specialty.html'
    context = {}
    if request.method == 'POST':
        form = SpecialtyForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('specialties:list_specialties')
    form = SpecialtyForm()
    context['form'] = form
    return render(request, template_name, context)

def list_specialties(request):
    template_name = 'specialties/list_specialties.html'
    specialties = Specialty.objects.filter()
    context = {
        'specialties': specialties
    }
    return render(request, template_name, context)

def edit_specialty(request, id_specialty):
    template_name = 'specialties/add_specialty.html'
    context ={}
    specialty = get_object_or_404(Specialty, id=id_specialty)
    if request.method == 'POST':
        form = SpecialtyForm(request.POST, instance=specialty)
        if form.is_valid():
            form.save()
            return redirect('specialties:list_specialties')
    form = SpecialtyForm(instance=specialty)
    context['form'] = form
    return render(request, template_name, context)

def delete_specialty(request, id_specialty):
    specialty = Specialty.objects.get(id=id_specialty)
    specialty.delete()
    return redirect('specialties:list_specialties')