# Generated by Django 4.0.6 on 2022-07-21 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_tag_article_category_article_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название тега'),
        ),
    ]
