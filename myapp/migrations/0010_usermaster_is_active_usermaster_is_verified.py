# Generated by Django 4.0.2 on 2022-09-09 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_rename_name_book_bname'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermaster',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usermaster',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]