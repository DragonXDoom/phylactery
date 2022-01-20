# Generated by Django 3.2.11 on 2022-01-19 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0034_auto_20210216_2348'),
        ('blog', '0003_alter_blogpost_slug_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_sent', models.BooleanField(default=False)),
                ('flags', models.ManyToManyField(to='members.MemberFlag')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emailorders', to='blog.blogpost')),
            ],
        ),
    ]
