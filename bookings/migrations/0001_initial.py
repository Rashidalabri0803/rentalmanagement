# Generated by Django 5.0.2 on 2024-11-17 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='تاريخ البدء')),
                ('end_date', models.DateField(verbose_name='تاريخ النهاية')),
                ('is_approved', models.BooleanField(default=False, verbose_name='مقبول')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث')),
            ],
        ),
    ]