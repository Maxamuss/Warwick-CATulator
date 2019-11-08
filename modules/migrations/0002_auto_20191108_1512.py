# Generated by Django 2.2 on 2019-11-08 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='assessment_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='assessments', to='modules.AssessmentGroup'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assessmentgroup',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessment_groups', to='modules.Module'),
        ),
    ]
