# Generated by Django 2.2.8 on 2020-01-15 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0006_merge_20191228_2306'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='yeargrade',
            options={'ordering': ['-year']},
        ),
    ]