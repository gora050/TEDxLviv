# Generated by Django 2.2.6 on 2019-12-08 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partner', '0001_initial'),
        ('event', '0002_auto_20191203_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('order', models.IntegerField(default=1)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partnergroups', to='event.Event')),
                ('partners', models.ManyToManyField(related_name='partnergroups', to='partner.Partner')),
            ],
        ),
    ]
