# Generated by Django 3.1.1 on 2020-10-11 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20201011_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjob',
            name='applied_for',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
