# Generated by Django 2.2 on 2019-06-21 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='fullname_engg',
        ),
        migrations.RemoveField(
            model_name='report',
            name='username_engg',
        ),
        migrations.AddField(
            model_name='report',
            name='engg',
            field=models.CharField(default='not given', max_length=100),
        ),
    ]