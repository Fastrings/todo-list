# Generated by Django 4.1.7 on 2023-02-28 15:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0007_alter_item_options_list_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='shared_with',
            field=models.ManyToManyField(related_name='shared_lists', to=settings.AUTH_USER_MODEL),
        ),
    ]
