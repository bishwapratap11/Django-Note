# Generated by Django 4.0 on 2021-12-25 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='description',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
    ]
