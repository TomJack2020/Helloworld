# Generated by Django 4.2 on 2023-05-21 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_prettynum_alter_userinfo_depart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prettynum',
            old_name='perice',
            new_name='price',
        ),
    ]