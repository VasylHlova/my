# Generated by Django 4.2.17 on 2025-01-10 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers_page', '0004_only_teacher_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='only_teacher',
            name='teacher_id',
            field=models.OneToOneField(limit_choices_to={'role': 'teacher'}, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='teachers_page.user'),
        ),
    ]