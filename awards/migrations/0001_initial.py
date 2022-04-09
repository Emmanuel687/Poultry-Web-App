# Generated by Django 3.2.7 on 2022-04-09 09:55

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(null=True)),
                ('profile_photo', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='profile_photo')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('project_image', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='project_image')),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=200, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('prof_ref', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='awards.profile')),
            ],
            options={
                'ordering': ['pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(null=True)),
                ('rate_design', models.PositiveSmallIntegerField(choices=[(10, '10-Outstanding'), (9, '9-Exceeds Expectations'), (8, '8-Excellent'), (7, '7-Good'), (6, '6-Barely Above Average'), (5, '5-Average'), (4, '4-Poor'), (3, '3-Awful'), (2, '2-Dreadful'), (1, '1-Troll')])),
                ('rate_usability', models.PositiveSmallIntegerField(choices=[(10, '10-Outstanding'), (9, '9-Exceeds Expectations'), (8, '8-Excellent'), (7, '7-Good'), (6, '6-Barely Above Average'), (5, '5-Average'), (4, '4-Poor'), (3, '3-Awful'), (2, '2-Dreadful'), (1, '1-Troll')])),
                ('rate_content', models.PositiveSmallIntegerField(choices=[(10, '10-Outstanding'), (9, '9-Exceeds Expectations'), (8, '8-Excellent'), (7, '7-Good'), (6, '6-Barely Above Average'), (5, '5-Average'), (4, '4-Poor'), (3, '3-Awful'), (2, '2-Dreadful'), (1, '1-Troll')])),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='awards.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
