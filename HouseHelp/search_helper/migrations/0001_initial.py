# Generated by Django 3.1.5 on 2021-02-25 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contact_no', models.IntegerField()),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brooming', models.BooleanField(default='false')),
                ('mopping', models.BooleanField(default='false')),
                ('utensil_cleaning', models.BooleanField(default='false')),
                ('washing_clothes', models.BooleanField(default='false')),
                ('cooking', models.BooleanField(default='false')),
                ('babysitting', models.BooleanField(default='false')),
            ],
        ),
        migrations.CreateModel(
            name='Helper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact_no', models.IntegerField()),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('password', models.CharField(max_length=20)),
                ('years_of_experience', models.IntegerField()),
                ('religion', models.CharField(max_length=50)),
                ('works', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='search_helper.works')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brooming', models.BooleanField(default='false')),
                ('mopping', models.BooleanField(default='false')),
                ('utensil_cleaning', models.BooleanField(default='false')),
                ('washing_clothes', models.BooleanField(default='false')),
                ('cooking', models.BooleanField(default='false')),
                ('babysitting', models.BooleanField(default='false')),
                ('cutomer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search_helper.customer')),
                ('helper_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search_helper.helper')),
            ],
        ),
    ]
