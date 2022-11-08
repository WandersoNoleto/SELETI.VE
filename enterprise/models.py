from django.db import models


class Technology(models.Model):
    technology = models.CharField(max_length=30, verbose_name="tecnologia")

    def __str__(self):
        return self.technology

class Enterprise(models.Model):
    choices_category = (
        ('M', 'Marketing'),
        ('N', 'Nutrição'),
        ('D', 'Design')
    )
    logo = models.ImageField(upload_to="logo_enterprise")
    name = models.CharField(max_length=30, verbose_name="nome")
    email = models.EmailField()
    city = models.CharField(max_length=30, verbose_name="cidade")
    technology = models.ManyToManyField(Technology, verbose_name="tecnologias")
    address = models.CharField(max_length=60, verbose_name="endereço")
    market_category = models.CharField(max_length=3, choices=choices_category, verbose_name="nicho_de_mercado")
    company_characteristics = models.TextField(verbose_name="caracteristicas_empresa")

    def __str__(self) -> str:
        return self.name

class Jobs(models.Model):
    choices_experience = (
        ('J', 'Júnior'),
        ('P', 'Pleno'),
        ('S', 'Sênior')
    )

    choices_status = (
        ('I', 'Interesse'),
        ('C', 'Currículo enviado'),
        ('E', 'Entrevista'),
        ('D', 'Desafio técnico'),
        ('F', 'Finalizado')
    )
    
    enterprise = models.ForeignKey(Enterprise, on_delete=models.DO_NOTHING, verbose_name="empresa")
    title = models.CharField(max_length=30, verbose_name="titulo")
    lvl_experience = models.CharField(max_length=2, choices=choices_experience, verbose_name="nivel_experiencia")
    final_date = models.DateField(verbose_name="data final")
    status = models.CharField(max_length=30, choices=choices_status)
    technologies_master = models.ManyToManyField(Technology, verbose_name="tecnologias_dominadas")
    Technology_study = models.ManyToManyField(Technology, related_name='estudar', verbose_name="tecnoligias_estudar")


    def __str__(self):
        return self.title