# Generated by Django 3.2.6 on 2022-05-24 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportconnectionsmodel',
            name='url_ip',
        ),
        migrations.AddField(
            model_name='reportconnectionsmodel',
            name='ip',
            field=models.GenericIPAddressField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reportconnectionsmodel',
            name='url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
