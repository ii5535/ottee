# Generated by Django 4.1.3 on 2022-11-10 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_species_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=4)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('images', models.ImageField(blank=True, null=True, upload_to='images')),
                ('Monthly_rent', models.FloatField(default=0.0)),
                ('administration_cost', models.FloatField(default=0.0)),
                ('room', models.CharField(max_length=30)),
                ('floor', models.FloatField(default=0.0)),
                ('hitter', models.CharField(max_length=20)),
                ('parking', models.FloatField(default=0.0)),
                ('Veranda', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=40)),
                ('number', models.CharField(max_length=11)),
                ('distance', models.CharField(max_length=30)),
                ('option', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Species',
        ),
        migrations.AddField(
            model_name='comment',
            name='home',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.home'),
        ),
    ]