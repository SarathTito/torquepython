# Generated by Django 4.1.4 on 2023-01-26 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("torqueapp", "0007_func_cust"),
    ]

    operations = [
        migrations.AddField(
            model_name="func",
            name="img1",
            field=models.ImageField(default="aacc", upload_to="gallery"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="func", name="cust", field=models.TextField(),
        ),
    ]
