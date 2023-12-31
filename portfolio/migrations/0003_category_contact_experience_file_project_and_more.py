# Generated by Django 4.2.5 on 2023-09-09 18:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_tecnologia_icono'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255, verbose_name='Asunto')),
                ('message', models.TextField(verbose_name='Mensaje')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=255, verbose_name='Nombre del puesto')),
                ('employer', models.CharField(max_length=255, verbose_name='Empleador')),
                ('start', models.DateField(blank=True, null=True, verbose_name='Fecha de inicio')),
                ('end', models.DateField(blank=True, null=True, verbose_name='Fecha de finalización')),
                ('description', models.TextField(blank=True, default=None, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Experiencia',
                'verbose_name_plural': 'Experiencias',
                'ordering': ('-start',),
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('file', models.CharField(blank=True, default=None, max_length=255)),
                ('uploaded', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('priority', models.IntegerField(blank=True, null=True, verbose_name='Prioridad')),
                ('description', models.TextField(blank=True, default=None, verbose_name='Descripción')),
                ('client', models.CharField(max_length=100, verbose_name='Cliente')),
                ('project_link', models.CharField(blank=True, default=None, max_length=255, verbose_name='Link del proyecto')),
                ('repository_link', models.CharField(blank=True, default=None, max_length=255, verbose_name='Link del repositorio')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='portfolio.category')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'ordering': ('-priority',),
            },
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/projects_images/', verbose_name='Imágen')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='portfolio.project')),
            ],
            options={
                'verbose_name': 'Imágen de proyecto',
                'verbose_name_plural': 'Imágenes de proyectos',
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre')),
                ('visible', models.BooleanField(default=False, verbose_name='¿Visible en "Home"?')),
                ('priority', models.IntegerField(blank=True, null=True, verbose_name='Prioridad')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images/categories/', verbose_name='Icono')),
            ],
            options={
                'verbose_name': 'Tecnología',
                'verbose_name_plural': 'Tecnologías',
                'ordering': ('-priority',),
            },
        ),
        migrations.DeleteModel(
            name='Contacto',
        ),
        migrations.DeleteModel(
            name='CV',
        ),
        migrations.RemoveField(
            model_name='experiencia',
            name='tecnologias',
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='tecnologias',
        ),
        migrations.DeleteModel(
            name='test_media',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Experiencia',
        ),
        migrations.DeleteModel(
            name='Proyecto',
        ),
        migrations.DeleteModel(
            name='Tecnologia',
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(related_name='projects', to='portfolio.technology'),
        ),
        migrations.AddField(
            model_name='experience',
            name='technologies',
            field=models.ManyToManyField(related_name='experiences', to='portfolio.technology'),
        ),
    ]
