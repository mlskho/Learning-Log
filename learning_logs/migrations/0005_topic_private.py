# Generated by Django 4.1.1 on 2023-01-05 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_topic_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]
