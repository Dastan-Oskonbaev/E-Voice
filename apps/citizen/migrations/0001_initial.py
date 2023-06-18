# Generated by Django 4.2.2 on 2023-06-18 00:34

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('election', '0001_initial'),
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referendum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('INN', models.PositiveSmallIntegerField(unique=True, verbose_name='INN')),
                ('biometry', models.CharField(max_length=100, verbose_name='Biometry')),
                ('photo', models.ImageField(upload_to='citizen/photo', verbose_name='Photo')),
                ('choice', models.CharField(choices=[(1, 'Accept'), (0, 'Reject')], max_length=100, verbose_name='Choice')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elections', to='election.election', verbose_name='Election')),
            ],
            options={
                'verbose_name': 'Referendum',
                'verbose_name_plural': 'Referendums',
            },
        ),
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('referendum_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='citizen.referendum')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Phone Number')),
                ('video', models.FileField(upload_to='citizen/video', verbose_name='Video')),
                ('status', models.CharField(choices=[('V', 'Verify'), ('A', 'Approved'), ('R', 'Refused')], max_length=100, verbose_name='Status')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidates', to='candidates.candidate', verbose_name='Candidate')),
            ],
            options={
                'verbose_name': 'Citizen',
                'verbose_name_plural': 'Citizens',
            },
            bases=('citizen.referendum', models.Model),
        ),
    ]