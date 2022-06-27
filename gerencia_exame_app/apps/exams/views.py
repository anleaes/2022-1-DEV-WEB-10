from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import ExamForm
from .models import Exam

# Create your views here.
@login_required(login_url='/contas/login/')
def add_exam(request):
    template_name = 'exams/add_exam.html'
    context = {}
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('exams:list_exams')
    form = ExamForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_exams(request):
    template_name = 'exams/list_exams.html'
    exams = Exam.objects.filter()
    context = {
        'exams': exams
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_exam(request, id_exam):
    template_name = 'exams/add_exam.html'
    context ={}
    exam = get_object_or_404(Exam, id=id_exam)
    if request.method == 'POST':
        form = ExamForm(request.POST, instance=exam)
        if form.is_valid():
            form.save()
            return redirect('exams:list_exams')
    form = ExamForm(instance=exam)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_exam(request, id_exam):
    exam = Exam.objects.get(id=id_exam)
    exam.delete()
    return redirect('exams:list_exams')