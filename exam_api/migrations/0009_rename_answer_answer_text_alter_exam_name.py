# Generated by Django 4.1.5 on 2023-01-22 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exam_api", "0008_remove_answer_exam_remove_answer_month_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="answer",
            old_name="answer",
            new_name="text",
        ),
        migrations.AlterField(
            model_name="exam",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]