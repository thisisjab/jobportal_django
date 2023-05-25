# Generated by Django 4.2.1 on 2023-05-24 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='employer',
            options={'verbose_name': 'Employer', 'verbose_name_plural': 'Employers'},
        ),
        migrations.AlterModelOptions(
            name='job',
            options={'verbose_name': 'Job', 'verbose_name_plural': 'Jobs'},
        ),
        migrations.AlterModelOptions(
            name='jobcandidate',
            options={'verbose_name': 'Job Candidate', 'verbose_name_plural': 'Job Candidates'},
        ),
        migrations.RenameField(
            model_name='jobcandidate',
            old_name='age',
            new_name='birth_date',
        ),
    ]