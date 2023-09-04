# Generated by Django 4.2.4 on 2023-09-04 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("phonebook_app", "0014_rename_name_location_neighbourhood_location_city"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="location",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="phonebook_app.location",
            ),
        ),
    ]