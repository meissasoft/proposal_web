# Generated by Django 3.2.12 on 2022-12-27 07:21

from django.db import migrations, models
import proposalapi.models


class Migration(migrations.Migration):

    dependencies = [
        ('proposalapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=proposalapi.models.nameFile),
        ),
    ]