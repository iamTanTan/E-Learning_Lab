# Generated by Django 3.0.5 on 2021-03-07 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discussion_board', '0002_auto_20210306_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent_discussion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='discussion_board.Discussion'),
        ),
    ]
