# Generated by Django 4.2.2 on 2023-06-20 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_language_course_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='language',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]
