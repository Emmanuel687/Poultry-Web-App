# Generated by Django 3.2.10 on 2022-04-21 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0006_alter_rating_rate_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rate_content',
            field=models.PositiveSmallIntegerField(choices=[(10, '10-Outstanding'), (9, '9-Exceeds Expectations'), (8, '8-Excellent'), (7, '7-Good'), (6, '6-Barely Above Average'), (5, '5-Average'), (4, '4-Poor'), (3, '3-Awful'), (2, '2-Dreadful'), (1, '1-Troll')], default=1234),
        ),
    ]
