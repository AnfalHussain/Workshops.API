# Generated by Django 3.1 on 2020-08-19 00:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=350)),
                ('image', models.ImageField(upload_to='')),
                ('price', models.PositiveIntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='WorkshopRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workshops', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=3, max_digits=8, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('payment_status', models.CharField(choices=[('FAILED', 'Failed'), ('SUCCESSFUL', 'Successful'), ('PENDING', 'Pending')], default='Pending', max_length=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('middle_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('gender', models.CharField(choices=[('FEMALE', 'Female'), ('MALE', 'Male')], default='Female', max_length=8)),
                ('nationality', models.CharField(max_length=150)),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('secondary_contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('civil_id_number', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('birthdate', models.DateField()),
                ('governorate', models.CharField(choices=[('AHMADI', 'Ahmadi'), ('AL_ASIMAH', 'Al-Asimah'), ('FARWANIYA', 'Farwaniya'), ('HAWALLI', 'Hawalli'), ('JAHRA', 'Jahra'), ('MUBARAK_AL_KABEER', 'Mubarak Al-Kabeer')], default='Ahmadi', max_length=20)),
                ('area', models.CharField(max_length=150)),
                ('education_level', models.CharField(max_length=150)),
                ('major', models.CharField(blank=True, max_length=150, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='baskets', to='api.registration')),
                ('workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workshops', to='api.workshop')),
            ],
        ),
    ]
