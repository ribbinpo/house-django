# Generated by Django 4.0.1 on 2022-04-20 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tb_house',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_house', models.CharField(max_length=255)),
                ('address_house', models.TextField()),
                ('detail_house', models.TextField()),
                ('photo_house', models.ImageField(default='', upload_to='photo')),
                ('price_house', models.IntegerField()),
                ('status_house', models.BooleanField()),
                ('date_house', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='tb_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname_user', models.CharField(max_length=255)),
                ('lastname_user', models.CharField(max_length=255)),
                ('age_user', models.IntegerField()),
                ('email_user', models.CharField(max_length=255)),
                ('phone_user', models.CharField(max_length=100)),
                ('sex_user', models.CharField(max_length=200)),
            ],
        ),
    ]
