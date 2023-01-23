# Generated by Django 4.1.5 on 2023-01-23 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exam_api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="answer",
            name="correct",
        ),
        migrations.RemoveField(
            model_name="answer",
            name="text",
        ),
        migrations.AddField(
            model_name="answer",
            name="answer",
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name="answer",
            name="option_1",
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name="answer",
            name="option_2",
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name="answer",
            name="option_3",
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name="answer",
            name="option_4",
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name="question",
            name="question_text",
            field=models.TextField(db_index=True),
        ),
    ]
