# Generated by Django 4.0.4 on 2022-05-20 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comment_cmt_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='cmt_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post'),
        ),
    ]
