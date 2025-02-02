# Generated by Django 5.0.6 on 2024-06-20 20:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RaceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('M_E123', 'Men E123'), ('M_3', 'Men 3rd'), ('M_4', 'Men 4th'), ('W_E123', 'Women E123'), ('W_34', 'Women 3/4')], max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.event')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.racecategory')),
            ],
        ),
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('current_division', models.CharField(choices=[('0', 'Elite'), ('1', '1st'), ('2', '2nd'), ('3', '3rds'), ('4', '4ths')], max_length=1)),
                ('bc_num', models.IntegerField(unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('current_team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_riders', to='profiles.team')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.season'),
        ),
        migrations.CreateModel(
            name='TeamMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.rider')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.team')),
            ],
        ),
        migrations.CreateModel(
            name='SeasonPoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.PositiveIntegerField()),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.rider')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.season')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.team')),
            ],
            options={
                'unique_together': {('season', 'rider')},
            },
        ),
        migrations.CreateModel(
            name='RaceResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.PositiveIntegerField()),
                ('time', models.DurationField()),
                ('points', models.PositiveIntegerField()),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.race')),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.rider')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.team')),
            ],
            options={
                'unique_together': {('race', 'rider')},
            },
        ),
    ]
