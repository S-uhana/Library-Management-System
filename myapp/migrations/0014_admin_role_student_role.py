# Generated by Django 4.0.2 on 2022-09-09 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_rename_cpassword_admin_cpassword_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='role',
            field=models.CharField(default='Admin', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='role',
            field=models.CharField(default='Student', max_length=50),
        ),
    ]
