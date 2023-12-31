# Generated by Django 4.2.4 on 2023-08-25 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProfessorStudent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('team', models.CharField(max_length=100)),
                ('number', models.FloatField()),
                ('position', models.CharField(max_length=100)),
                ('age', models.FloatField()),
                ('height', models.CharField(max_length=100)),
                ('weight', models.FloatField()),
                ('college', models.CharField(blank=True, max_length=100, null=True)),
                ('salary', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
