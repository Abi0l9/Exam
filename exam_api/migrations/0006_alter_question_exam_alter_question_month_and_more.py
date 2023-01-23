# Generated by Django 4.1.5 on 2023-01-22 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("exam_api", "0005_remove_subject_exam_name_subject_exam_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="exam",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="questions",
                to="exam_api.exam",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="month",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="questions",
                to="exam_api.month",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="subject",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="questions",
                to="exam_api.subject",
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="year",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="questions",
                to="exam_api.year",
            ),
        ),
    ]
