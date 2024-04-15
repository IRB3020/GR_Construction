# Generated by Django 4.2 on 2024-04-05 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('Active', 'First-Time Customer'), ('Active', 'Returning Customer'), ('Finished', 'Business Finished'), ('Finished', 'Business Pulled')], max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
