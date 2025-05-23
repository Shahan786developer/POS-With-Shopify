# Generated by Django 4.2.7 on 2023-11-10 16:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posapp', '0004_alter_product_unique_together_alter_product_name_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('user', 'code')},
        ),
        migrations.AlterUniqueTogether(
            name='subcategory',
            unique_together={('user', 'code')},
        ),
    ]
