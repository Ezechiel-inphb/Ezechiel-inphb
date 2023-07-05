# Generated by Django 4.2.1 on 2023-06-05 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number_of_quest', models.IntegerField()),
                ('time', models.IntegerField(help_text='La durée du quiz en minutes')),
                ('score', models.IntegerField(help_text='le score en %')),
            ],
        ),
    ]
