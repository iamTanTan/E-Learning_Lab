# Generated by Django 3.0.5 on 2021-03-04 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20200627_1511'),
        ('quizapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='courses',
            field=models.ForeignKey(default='dd390af4-07f1-4597-b48a-f585fd79289d', on_delete=django.db.models.deletion.CASCADE, to='courses.Courses'),
        ),
    ]