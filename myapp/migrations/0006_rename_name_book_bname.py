# Generated by Django 4.0.2 on 2022-09-09 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_bname_book_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Name',
            new_name='bname',
        ),
    ]