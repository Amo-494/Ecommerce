# Generated by Django 3.2.7 on 2022-09-26 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0002_auto_20220926_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pics'),
        ),
    ]