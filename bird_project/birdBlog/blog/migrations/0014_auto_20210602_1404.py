# Generated by Django 3.1.2 on 2021-06-02 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_version_sibelius_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='sibelius_file',
            field=models.FileField(blank=True, upload_to='sibelius_files'),
        ),
    ]
