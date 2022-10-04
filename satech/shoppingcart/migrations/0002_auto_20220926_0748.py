# Generated by Django 3.2.7 on 2022-09-26 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shoppingcart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateField(auto_now_add=True)),
                ('complete', models.BooleanField(blank=True, default=False, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shoppingcart.customer')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='coupon_code',
        ),
        migrations.RemoveField(
            model_name='product',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='product',
            name='discount_percent',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shoppingcart.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shoppingcart.product')),
            ],
        ),
    ]
