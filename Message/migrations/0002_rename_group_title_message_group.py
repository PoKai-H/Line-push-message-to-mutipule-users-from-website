# Generated by Django 4.0.5 on 2022-07-01 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Message', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='group_title',
            new_name='group',
        ),
    ]