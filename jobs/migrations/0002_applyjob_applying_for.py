# Generated by Django 3.1.1 on 2020-10-11 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyjob',
            name='applying_for',
            field=models.CharField(choices=[('Web Design', 'Web Design'), ('Graphic Design', 'Graphic Design'), ('Web Developing', 'Web Developing'), ('Software Engineering', 'Software Engineering'), ('HR', 'HR'), ('Marketing', 'Marketing')], max_length=30, null=True),
        ),
    ]
