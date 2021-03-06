# Generated by Django 3.1 on 2020-08-20 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200820_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('FEMALE', 'Female'), ('MALE', 'Male')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='governorate',
            field=models.CharField(choices=[('AHMADI', 'Ahmadi'), ('AL_ASIMAH', 'Al-Asimah'), ('FARWANIYA', 'Farwaniya'), ('HAWALLI', 'Hawalli'), ('JAHRA', 'Jahra'), ('MUBARAK_AL_KABEER', 'Mubarak Al-Kabeer')], max_length=20, null=True),
        ),
    ]
