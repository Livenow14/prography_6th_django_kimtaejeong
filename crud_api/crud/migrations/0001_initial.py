# Generated by Django 2.1.2 on 2020-03-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(db_column='NO', primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, db_column='TITLE', max_length=200, null=True)),
                ('description', models.CharField(blank=True, db_column='CONTENT', max_length=1000, null=True)),
                ('created_time', models.DateField(blank=True, db_column='CREATED_DATE', null=True)),
            ],
        ),
    ]
