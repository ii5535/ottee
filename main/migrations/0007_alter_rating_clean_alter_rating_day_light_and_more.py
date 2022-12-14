# Generated by Django 4.1.3 on 2022-11-12 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_comment_cate_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='clean',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='day_light',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='hit',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='noise',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='optionrate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='secu',
            field=models.FloatField(default=0.0),
        ),
    ]
