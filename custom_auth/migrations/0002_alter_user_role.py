# Generated by Django 5.0.6 on 2024-06-10 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("custom_auth", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("ADMIN", "Admin"), ("USER", "User"), ("AUTH", "Auth")],
                default="USER",
                max_length=10,
            ),
        ),
    ]