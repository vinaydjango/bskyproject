# Generated by Django 2.1.5 on 2019-07-04 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtorapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(upload_to='photos'),
        ),
    ]
