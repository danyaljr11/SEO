# Generated by Django 4.2.16 on 2024-10-29 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=355)),
                ('summary', models.CharField(max_length=5000)),
                ('description', models.CharField(max_length=5000)),
                ('photo', models.ImageField(upload_to='images/')),
                ('link', models.URLField(blank=True, null=True)),
                ('link_title', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
