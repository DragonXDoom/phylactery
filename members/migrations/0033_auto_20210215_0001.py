# Generated by Django 3.1.4 on 2021-02-14 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0032_auto_20210213_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rank',
            name='rank_name',
            field=models.CharField(choices=[('EXCLUDED', 'Excluded'), ('GATEKEEPER', 'Gatekeeper'), ('WEBKEEPER', 'Webkeeper'), ('COMMITTEE', 'Committee'), ('LIFE-MEMBER', 'Life Member'), ('PRESIDENT', 'President'), ('VICE-PRESIDENT', 'Vice President'), ('SECRETARY', 'Secretary'), ('TREASURER', 'Treasurer'), ('LIBRARIAN', 'Librarian'), ('FRESHER-REP', 'Fresher Rep'), ('OCM', 'OCM'), ('IPP', 'IPP (Immediate Past President)')], max_length=20, unique=True),
        ),
    ]
