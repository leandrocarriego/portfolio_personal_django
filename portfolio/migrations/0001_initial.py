# Generated by Django 4.2.5 on 2023-09-07 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default=None, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('asunto', models.CharField(max_length=255)),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='cv', max_length=2)),
                ('cv', models.CharField(blank=True, default=None, max_length=255)),
                ('uploaded', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tecnologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default=None, max_length=100)),
                ('visible_en_home', models.BooleanField(default=False)),
                ('orden', models.IntegerField(blank=True, default=None, null=True)),
                ('icono', models.CharField(blank=True, default=None, max_length=255)),
            ],
            options={
                'ordering': ('orden',),
            },
        ),
        migrations.CreateModel(
            name='test_media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='test/', verbose_name='img')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('orden', models.IntegerField(blank=True, default=None, null=True)),
                ('descripcion', models.TextField(blank=True, default=None)),
                ('cliente', models.CharField(max_length=100)),
                ('publico', models.BooleanField(default=False)),
                ('link_proyecto', models.CharField(blank=True, default=None, max_length=255)),
                ('link_repositorio', models.CharField(blank=True, default=None, max_length=255)),
                ('imagen1', models.CharField(blank=True, default=None, max_length=255)),
                ('imagen2', models.CharField(blank=True, default=None, max_length=255)),
                ('imagen3', models.CharField(blank=True, default=None, max_length=255)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proyectos', to='portfolio.categoria')),
                ('tecnologias', models.ManyToManyField(related_name='proyectos', to='portfolio.tecnologia')),
            ],
            options={
                'ordering': ('orden',),
            },
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puesto', models.CharField(max_length=255)),
                ('empleador', models.CharField(max_length=255)),
                ('inicio', models.CharField(blank=True, default=None, max_length=255)),
                ('fin', models.CharField(blank=True, default='Actualmente', max_length=255)),
                ('descripcion', models.TextField(blank=True, default=None)),
                ('tecnologias', models.ManyToManyField(related_name='experiencias', to='portfolio.tecnologia')),
            ],
        ),
    ]