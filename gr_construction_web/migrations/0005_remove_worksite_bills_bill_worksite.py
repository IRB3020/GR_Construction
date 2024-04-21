# Generated by Django 4.2 on 2024-04-20 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gr_construction_web', '0004_rename_final_shot_worksite_finished_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worksite',
            name='bills',
        ),
        migrations.AddField(
            model_name='bill',
            name='worksite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bills', to='gr_construction_web.worksite'),
        ),
    ]
