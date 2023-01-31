# Generated by Django 4.1.4 on 2023-01-30 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(blank=True, max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('Gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1)),
                ('age', models.IntegerField()),
                ('phonenumber', models.IntegerField()),
                ('image', models.FileField(upload_to='images/')),
                ('bloodgroup', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=10)),
                ('timesofdonate', models.CharField(max_length=200)),
                ('diseases', models.CharField(max_length=100)),
                ('donatedate', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
