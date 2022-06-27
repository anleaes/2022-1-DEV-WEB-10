from django.db import models
from exams.models import Exam
from patients.models import Patient


# Create your models here.
class Result(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = (
        ('Disponivel', 'Indisponivel'),
    )
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, null=True, blank=True, default='Em andamento')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    result_item = models.ManyToManyField(Exam, through='ResultItem', blank=True)
    
    class Meta:
        verbose_name = 'Resultado'
        verbose_name_plural = 'Resultados'
        ordering =['-created_on']

    def __str__(self):
        return self.status 


class ResultItem(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    result = models.ForeignKey(Result, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item de resultado'
        verbose_name_plural = 'Itens de resultado'
        ordering =['id']

    def __str__(self):
        return self.exam