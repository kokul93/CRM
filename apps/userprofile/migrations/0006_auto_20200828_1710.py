# Generated by Django 3.1 on 2020-08-28 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20200828_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='author',
            new_name='user',
        ),
    ]
