# Generated by Django 3.1.7 on 2021-05-06 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'verbose_name_plural': 'Games'},
        ),
        migrations.AddField(
            model_name='collectible_instance',
            name='destroyed',
            field=models.BooleanField(default=False),
        ),
    ]
