# Generated by Django 5.1.5 on 2025-02-15 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mods', '0003_rename_modupload_modlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='modlist',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media/uploads'),
        ),
    ]
