# Generated by Django 4.2.13 on 2024-07-27 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
        ('change_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_master',
            name='email',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='signup.signup_master'),
        ),
    ]
