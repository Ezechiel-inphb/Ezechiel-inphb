# Generated by Django 4.2.1 on 2023-06-16 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_alter_comment_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Commentaire',
        ),
    ]
