# Generated by Django 4.2.17 on 2025-01-10 22:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers_page', '0007_rename_department_user_faculty_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('rating_date', models.DateField(auto_now_add=True)),
                ('student_id', models.ForeignKey(limit_choices_to={'role': 'student'}, on_delete=django.db.models.deletion.CASCADE, to='teachers_page.user')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers_page.only_teacher')),
            ],
        ),
    ]
