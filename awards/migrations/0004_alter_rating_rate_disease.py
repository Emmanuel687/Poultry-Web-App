# Generated by Django 3.2.10 on 2022-04-21 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0003_rename_rate_content_rating_rate_disease'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rate_disease',
            field=models.PositiveSmallIntegerField(choices=[(5, '5.Killer'), (4, '4-Severe'), (3, '3-Moderate'), (2, '2-Trace'), (1, '1.Light')]),
        ),
    ]
