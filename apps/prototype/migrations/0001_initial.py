# Generated by Django 2.0.3 on 2018-03-22 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_engaged', models.IntegerField(null=True)),
                ('sunk', models.IntegerField(null=True)),
                ('damaged', models.IntegerField(null=True)),
                ('vessel', models.CharField(blank=True, choices=[('C', 'Cruisers'), ('D', 'Destroyers'), ('M', 'Minesweepers'), ('A', 'Anti-submarine')], max_length=1)),
                ('note', models.TextField(blank=True, help_text='Any information on demand', max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
