# Generated by Django 3.1.1 on 2020-10-11 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20201011_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyjob',
            name='company_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
