# Generated by Django 4.2.1 on 2023-06-17 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0026_alter_addcommentaire_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatgHoly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
    ]
