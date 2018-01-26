# Generated by Django 2.0rc1 on 2018-01-25 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Localizr', '0008_auto_20180123_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='localizedstring',
            name='status',
            field=models.IntegerField(choices=[(0, 'Published'), (1, 'Pending'), (3, 'Draft')], default=3),
        ),
    ]
