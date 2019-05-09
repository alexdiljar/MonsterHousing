# Generated by Django 2.2.1 on 2019-05-09 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
                ('zip', models.IntegerField()),
                ('city', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elevator', models.BooleanField()),
                ('garage', models.BooleanField()),
                ('near_bloodbank', models.BooleanField()),
                ('dungeon', models.BooleanField()),
                ('seacret_entrence', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=999)),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('rooms', models.IntegerField()),
                ('description', models.CharField(max_length=999)),
                ('p_image', models.CharField(max_length=999)),
                ('T_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Properties.Tags')),
                ('Ty_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Properties.Types')),
            ],
        ),
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=255)),
                ('house_no', models.IntegerField()),
                ('Cities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Properties.Cities')),
            ],
        ),
    ]