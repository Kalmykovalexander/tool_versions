# Generated by Django 3.2.5 on 2021-07-09 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tool',
            old_name='stage',
            new_name='id_stage',
        ),
        migrations.AlterField(
            model_name='tool',
            name='version',
            field=models.CharField(max_length=50),
        ),
    ]
