from django.db import models
from django.utils import timezone


class Description(models.Model):
    class Meta:
        verbose_name = "Descripción"
        verbose_name_plural = "Descripción"

    description = models.TextField(verbose_name='Descripción')

    def __str__(self):
        return self.description


class Technology(models.Model):
    class Meta:
        verbose_name = "Tecnología"
        verbose_name_plural = "Tecnologías"
        ordering = ("-priority",)

    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Nombre')
    visible = models.BooleanField(default=False, verbose_name='¿Visible en "Home"?')
    priority = models.IntegerField(blank=True, null=True, verbose_name='Prioridad')
    icon = models.ImageField(upload_to="images/categories/", blank=True, null=True, verbose_name='Icono')

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ("name",)

    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Nombre')

    def __str__(self):
        return self.name


class Project(models.Model):
    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ("-priority",)

    title = models.CharField(max_length=100, verbose_name='Título')
    priority = models.IntegerField(blank=True, null=True, verbose_name='Prioridad')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='projects', null=True, blank=True)
    technologies = models.ManyToManyField(Technology, related_name='projects')
    description = models.TextField(blank=True, default=None, verbose_name='Descripción')
    client = models.CharField(max_length=100, verbose_name='Cliente')
    project_link = models.CharField(max_length=255, blank=True, default=None, verbose_name='Link del proyecto')
    repository_link = models.CharField(max_length=255, blank=True, default=None, verbose_name='Link del repositorio')

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    class Meta:
        verbose_name = "Imágen de proyecto"
        verbose_name_plural = "Imágenes de proyectos"

    image = models.ImageField(upload_to='images/projects_images/', verbose_name='Imágen')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')


class Experience(models.Model):
    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"
        ordering = ("-start",)

    position = models.CharField(max_length=255, verbose_name='Nombre del puesto')
    employer = models.CharField(max_length=255, verbose_name='Empleador')
    start = models.DateField(null=True, blank=True, verbose_name='Fecha de inicio')
    end = models.DateField(null=True, blank=True, verbose_name='Fecha de finalización')
    description = models.TextField(blank=True, default=None, verbose_name='Descripción')
    technologies = models.ManyToManyField(Technology, related_name='experiences')

    def __str__(self):
        return self.position


class Contact(models.Model):
    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
        ordering = ("-date",)

    name = models.CharField(max_length=255, verbose_name='Nombre')
    email = models.EmailField()
    subject = models.CharField(max_length=255, verbose_name='Asunto')
    message = models.TextField(verbose_name='Mensaje')
    date = models.DateField(default=timezone.now, verbose_name='Fecha')

    def __str__(self):
        return self.subject


class File(models.Model):
    class Meta:
        verbose_name = "Archivo"
        verbose_name_plural = "Archivos"
        ordering = ("-uploaded",)

    name = models.CharField(max_length=100, blank=True, null=True)
    file = models.FileField(upload_to='documents/', blank=True, null=True)
    uploaded = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
