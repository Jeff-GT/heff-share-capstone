# Generated by Django 5.1.5 on 2025-02-20 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mods', '0006_modtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='modlist',
            name='modtags',
            field=models.ManyToManyField(blank=True, to='mods.modtag'),
        ),
    ]
