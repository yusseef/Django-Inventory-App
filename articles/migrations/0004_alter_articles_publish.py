# Generated by Django 4.1.4 on 2022-12-12 21:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_articles_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='publish',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
