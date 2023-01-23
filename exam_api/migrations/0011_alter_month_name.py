# Generated by Django 4.1.5 on 2023-01-23 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exam_api", "0010_alter_month_name_alter_subject_name_alter_year_year"),
    ]

    operations = [
        migrations.AlterField(
            model_name="month",
            name="name",
            field=models.CharField(
                choices=[
                    ("MAY/JUN", "MAY/JUNE"),
                    ("JUN/JUL", "JUNE/JULY"),
                    ("OCT/NOV", "OCTOBER/NOVEMBER"),
                    ("Others", "Others"),
                ],
                max_length=20,
                unique=True,
            ),
        ),
    ]