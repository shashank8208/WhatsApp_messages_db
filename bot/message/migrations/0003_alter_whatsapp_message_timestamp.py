# Generated by Django 3.2.13 on 2022-05-03 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20220502_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whatsapp_message',
            name='timestamp',
            field=models.TextField(),
        ),
    ]