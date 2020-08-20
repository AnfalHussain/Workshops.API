# Generated by Django 3.1 on 2020-08-19 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200819_0108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='api.registration')),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workshops', to='api.workshop')),
            ],
        ),
        migrations.DeleteModel(
            name='Basket',
        ),
    ]