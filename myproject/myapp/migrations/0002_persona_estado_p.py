# Generated by Django 4.1 on 2023-04-26 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='estado_p',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
