# Generated by Django 4.2.2 on 2023-06-18 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizen',
            name='status',
            field=models.CharField(choices=[('V', 'Verify'), ('A', 'Approved'), ('R', 'Refused')], default='V', max_length=100, verbose_name='Status'),
        ),
    ]