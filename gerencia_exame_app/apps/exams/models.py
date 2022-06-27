from django.db import models
from specialties.models import Specialty

# Create your models here.
class Exam(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    is_active = models.BooleanField('Ativo', default=False)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Exame'
        verbose_name_plural = 'Exames'
        ordering =['id']

    def __str__(self):
        return self.name