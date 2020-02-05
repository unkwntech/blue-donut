# Generated by Django 3.0.3 on 2020-02-05 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EVEData',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='eve', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EVEUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_id', models.BigIntegerField(db_index=True, unique=True)),
                ('name', models.CharField(db_index=True, max_length=64, unique=True)),
                ('alliance_id', models.BigIntegerField(default=0)),
                ('corporation_id', models.BigIntegerField(default=0)),
                ('esi_updated', models.DateTimeField(auto_now=True)),
                ('scope_read_location', models.BooleanField(default=0)),
                ('scope_write_waypoint', models.BooleanField(default=0)),
                ('scope_search_structures', models.BooleanField(default=0)),
                ('scope_read_structures', models.BooleanField(default=0)),
                ('access_token', models.CharField(max_length=8192)),
                ('refresh_token', models.CharField(max_length=8192)),
                ('token_expiry', models.DateTimeField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
