# Generated by Django 5.1.1 on 2024-09-25 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=100, verbose_name="书名")),
                ("description", models.TextField(verbose_name="书籍简介")),
                (
                    "image",
                    models.ImageField(
                        upload_to="book/images/", verbose_name="书籍海报"
                    ),
                ),
                ("url", models.URLField(blank=True, verbose_name="电子书资源")),
            ],
            options={
                "verbose_name": "读书",
                "verbose_name_plural": "读书",
            },
        ),
    ]
