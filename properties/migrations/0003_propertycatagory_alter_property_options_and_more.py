# Generated by Django 5.0.3 on 2024-11-18 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyCatagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='اسم الفئة')),
                ('description', models.TextField(blank=True, verbose_name='وصف الفئة')),
            ],
            options={
                'verbose_name': 'فئة العقار',
                'verbose_name_plural': 'فئات العقارات',
            },
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'ordering': ['-created_at'], 'verbose_name': 'عقار', 'verbose_name_plural': 'العقارات'},
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='properties/', verbose_name='الصورة')),
                ('caption', models.CharField(blank=True, max_length=255, verbose_name='وصف الصورة')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='properties.property', verbose_name='العقار')),
            ],
            options={
                'verbose_name': 'صورة العقار',
                'verbose_name_plural': 'صور العقارات',
            },
        ),
    ]
