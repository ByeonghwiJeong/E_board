# Generated by Django 4.1 on 2022-08-31 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=45)),
                ("email", models.CharField(max_length=45)),
                ("password", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=40)),
                ("gender", models.IntegerField()),
                ("age", models.IntegerField()),
                ("authorization", models.IntegerField(default=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("connected_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"db_table": "users",},
        ),
        migrations.CreateModel(
            name="UserLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("gender", models.IntegerField()),
                ("age", models.IntegerField()),
                ("log_time", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.user"
                    ),
                ),
            ],
            options={"db_table": "logs",},
        ),
    ]