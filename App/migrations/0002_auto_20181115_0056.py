# Generated by Django 2.1.2 on 2018-11-14 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='semester',
            field=models.CharField(choices=[('ONE', 'I'), ('TWO', 'II'), ('THREE', 'III'), ('FOUR', 'IV'), ('FIVE', 'V'), ('SIX', 'VI'), ('SEVEN', 'VII'), ('EIGHT', 'VIII')], default='', max_length=100),
        ),
    ]
