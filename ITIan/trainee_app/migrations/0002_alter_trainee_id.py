# Generated by Django 5.1.6 on 2025-03-11 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
