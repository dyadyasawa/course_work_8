# Generated by Django 4.2.2 on 2024-06-28 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habit", "0005_alter_habit_number_of_executions"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="number_of_executions",
            field=models.IntegerField(
                default=1, verbose_name="Количество выполнений в неделю"
            ),
        ),
    ]
