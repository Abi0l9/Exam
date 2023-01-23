# Generated by Django 4.1.5 on 2023-01-23 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exam_api", "0013_alter_month_name_alter_subject_year"),
    ]

    operations = [
        migrations.AddField(
            model_name="subject",
            name="yearsss",
            field=models.CharField(
                choices=[(2020, 2020), (2021, 2021), (2022, 2022)],
                default=1,
                max_length=20,
            ),
        ),
    ]