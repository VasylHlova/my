# Generated by Django 4.2.17 on 2025-01-10 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers_page', '0006_alter_user_department_alter_user_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='department',
            new_name='faculty',
        ),
        migrations.AlterField(
            model_name='only_teacher',
            name='photo',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='only_teacher',
            name='sci_interests',
            field=models.TextField(blank=True),
        ),
    ]
