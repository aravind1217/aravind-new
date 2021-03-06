# Generated by Django 3.2.5 on 2021-07-30 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CrudUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(blank=True, max_length=30)),
                ('last', models.CharField(blank=True, max_length=100)),
                ('short', models.CharField(blank=True, max_length=30)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('join_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image_url', models.URLField()),
                ('medium_url', models.URLField()),
                ('thumbnail_url', models.URLField()),
                ('team', models.CharField(max_length=30)),
                ('job_title', models.CharField(max_length=30)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('loggedIn', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
