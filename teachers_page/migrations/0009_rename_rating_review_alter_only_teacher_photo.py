# Generated by Django 4.2.17 on 2025-01-11 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers_page', '0008_rating'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rating',
            new_name='Review',
        ),
        migrations.AlterField(
            model_name='only_teacher',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='teacher_photos/'),
        ),
    ]