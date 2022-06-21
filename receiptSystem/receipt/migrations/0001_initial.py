# Generated by Django 3.2.5 on 2022-06-19 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('cost', models.FloatField(default=0)),
                ('location', models.CharField(max_length=6)),
                ('creation_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
