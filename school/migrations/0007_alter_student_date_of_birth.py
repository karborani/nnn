# Generated by Django 4.2.6 on 2023-10-14 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_rename_last_nam_student_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(max_length=8),
        ),
    ]
