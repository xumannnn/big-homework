# Generated by Django 5.2 on 2025-07-02 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                ("title", models.CharField(max_length=200, verbose_name="电影名称")),
                ("category", models.CharField(max_length=100, verbose_name="分类")),
                ("link", models.URLField(verbose_name="下载链接")),
                (
                    "update_time",
                    models.DateTimeField(auto_now=True, verbose_name="更新时间"),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="简介"),
                ),
                ("score", models.FloatField(default=0, verbose_name="评分")),
            ],
            options={
                "verbose_name": "电影",
                "verbose_name_plural": "电影列表",
                "ordering": ["-update_time"],
            },
        ),
    ]
