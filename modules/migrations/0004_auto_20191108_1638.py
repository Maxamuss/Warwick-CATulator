# Generated by Django 2.2 on 2019-11-08 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0003_auto_20191108_1601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assessmentgroup',
            old_name='Assessment_group_name',
            new_name='assessment_group_name',
        ),
        migrations.AlterField(
            model_name='module',
            name='academic_year',
            field=models.CharField(choices=[('19/20', '19/20'), ('18/19', '18/19'), ('17/18', '17/18'), ('16/17', '16/17'), ('15/16', '15/16')], default='19/20', max_length=5),
        ),
    ]
