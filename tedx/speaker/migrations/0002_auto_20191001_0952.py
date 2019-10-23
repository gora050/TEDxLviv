# Generated by Django 2.2.3 on 2019-10-01 09:52

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('speaker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speakers', to='event.Event'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='photo',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/photos'), upload_to=''),
        ),
    ]
