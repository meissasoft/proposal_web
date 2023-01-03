# Generated by Django 3.2.12 on 2023-01-03 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(default=None, max_length=10000)),
                ('tags', models.CharField(default=None, max_length=1000)),
                ('project_url_link', models.CharField(default=None, max_length=500)),
                ('languages', models.CharField(default=None, max_length=500)),
                ('platform', models.CharField(default=None, max_length=500)),
                ('project_github_link', models.CharField(default=None, max_length=500)),
                ('project_earning', models.CharField(default=None, max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]