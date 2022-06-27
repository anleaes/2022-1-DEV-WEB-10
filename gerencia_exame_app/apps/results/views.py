from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ResultForm, ResultItemForm
from .models import Result , ResultItem, Exam, Patient

# Create your views here.
@login_required(login_url='/contas/login/')
def add_result(request, id_patient):
    template_name = 'results/add_result.html'
    context = {}
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.patient = Patient.objects.get(id=id_patient)
            f.save()
            form.save_m2m()
            return redirect('results:list_results')
    form = ResultForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_results(request):
    template_name = 'results/list_results.html'
    results = Result.objects.filter()
    result_items = ResultItem.objects.filter()
    exams = Exam.objects.filter()
    patients = Patient.objects.filter()
    context = {
        'results': results,
        'result_items': result_items,
        'exams': exams,
        'patients': patients
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_result(request, id_result):
    result = Result.objects.get(id=id_result)
    result.delete()
    return redirect('results:list_results')

@login_required(login_url='/contas/login/')
def add_result_item(request, id_result):
    template_name = 'results/add_result_item.html'
    context = {}
    if request.method == 'POST':
        form = ResultItemForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.result = Result.objects.get(id=id_result)
            f.save()
            form.save_m2m()
            return redirect('results:list_results')
    form = ResultItemForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_result_item(request, id_result_item):
    resultitem = ResultItem.objects.get(id=id_result_item)
    resultitem.delete()
    return redirect('results:list_results')

@login_required(login_url='/contas/login/')
def edit_result_status(request, id_result):
    template_name = 'results/edit_result_status.html'
    context ={}
    result = get_object_or_404(Result, id=id_result)
    if request.method == 'POST':
        form = ResultForm(request.POST, instance=result)
        if form.is_valid():
            form.save()
            return redirect('results:list_results')
    form = ResultForm(instance=result)
    context['form'] = form
    return render(request, template_name, context)