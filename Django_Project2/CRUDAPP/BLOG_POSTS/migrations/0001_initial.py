# Generated by Django 2.2.5 on 2021-01-26 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(max_length=100)),
                ('blog_author', models.CharField(max_length=100)),
            ],
        ),
    ]
