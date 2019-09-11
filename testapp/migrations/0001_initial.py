# Generated by Django 2.2 on 2019-06-21 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname_staff', models.CharField(max_length=50)),
                ('username_staff', models.CharField(max_length=50)),
                ('fullname_engg', models.CharField(max_length=50)),
                ('username_engg', models.CharField(max_length=50)),
                ('total_points', models.IntegerField()),
                ('feedbacktxt', models.TextField(max_length=500)),
            ],
        ),
    ]