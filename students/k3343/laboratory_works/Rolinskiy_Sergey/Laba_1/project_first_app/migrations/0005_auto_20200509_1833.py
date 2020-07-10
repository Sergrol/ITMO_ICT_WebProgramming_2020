# Generated by Django 3.0.4 on 2020-05-09 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='datein',
            field=models.DateField(default='2006-06-06'),
        ),
        migrations.AddField(
            model_name='comment',
            name='dateout',
            field=models.DateField(default='2006-06-06'),
        ),
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default='1', max_length=2),
        ),
    ]