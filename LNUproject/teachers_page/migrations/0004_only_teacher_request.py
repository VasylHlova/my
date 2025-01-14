# Generated by Django 4.2.17 on 2025-01-10 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers_page', '0003_user_remove_teacherinfo_teacher_id_delete_request_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Only_teacher',
            fields=[
                ('teacher_id', models.ForeignKey(limit_choices_to={'role': 'teacher'}, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='teachers_page.user')),
                ('phone_num', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, upload_to='teachers_photo')),
                ('position', models.CharField(max_length=100)),
                ('num_places_free', models.IntegerField()),
                ('sci_interests', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_text', models.TextField()),
                ('request_date', models.DateField(auto_now_add=True)),
                ('request_status', models.CharField(choices=[('pending', 'очікується'), ('accepted', 'прийнятий'), ('rejected', 'відхилений')], max_length=100)),
                ('theme', models.CharField(blank=True, max_length=100)),
                ('student_id', models.ForeignKey(limit_choices_to={'role': 'student'}, on_delete=django.db.models.deletion.CASCADE, to='teachers_page.user')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teachers_page.only_teacher')),
            ],
        ),
    ]