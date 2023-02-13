# Generated by Django 4.1.6 on 2023-02-12 14:22

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='item name')),
                ('description', models.CharField(max_length=2000, verbose_name='description')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=9, validators=[django.core.validators.MinValueValidator(0)], verbose_name='price')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PD', 'Payed')], default='DF', max_length=2, verbose_name='status')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL, verbose_name='buyer')),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='marketplace.item', verbose_name='items')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.AddIndex(
            model_name='item',
            index=models.Index(fields=['name'], name='marketplace_name_da70bd_idx'),
        ),
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['created'], name='marketplace_created_6ee8c4_idx'),
        ),
    ]
