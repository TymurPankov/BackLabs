# Generated by Django 4.0.4 on 2022-05-20 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_cmt_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]