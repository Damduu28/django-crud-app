# Generated by Django 4.1.7 on 2023-05-07 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_alter_crud_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='crud',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
