# Generated by Django 4.0 on 2021-12-26 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_notes_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
