# Generated by Django 4.2.1 on 2023-05-25 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_alter_jobcategory_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
