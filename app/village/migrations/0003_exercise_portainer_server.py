# Generated by Django 3.2.6 on 2022-04-04 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('village', '0002_village_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='portainer_server',
            field=models.CharField(default='PWDCRACK01', max_length=64),
            preserve_default=False,
        ),
    ]
