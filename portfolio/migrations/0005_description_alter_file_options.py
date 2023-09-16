# Generated by Django 4.2.5 on 2023-09-09 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_file_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Descripción',
                'verbose_name_plural': 'Descripción',
            },
        ),
        migrations.AlterModelOptions(
            name='file',
            options={'ordering': ('-uploaded',), 'verbose_name': 'Archivo', 'verbose_name_plural': 'Archivos'},
        ),
    ]
