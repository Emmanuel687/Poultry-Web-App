# Generated by Django 3.2.10 on 2022-04-21 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0009_alter_rating_rate_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='rate_design',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='rate_usability',
        ),
    ]
