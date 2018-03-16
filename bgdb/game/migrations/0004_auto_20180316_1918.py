# Generated by Django 2.0.3 on 2018-03-16 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20180316_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='artists',
            field=models.ManyToManyField(blank=True, related_name='games', to='game.Artist', verbose_name='artists'),
        ),
        migrations.AddField(
            model_name='game',
            name='designers',
            field=models.ManyToManyField(blank=True, related_name='games', to='game.Designer', verbose_name='designers'),
        ),
        migrations.AddField(
            model_name='game',
            name='honors',
            field=models.ManyToManyField(blank=True, related_name='games', to='game.Honor', verbose_name='honors'),
        ),
        migrations.AddField(
            model_name='game',
            name='publishers',
            field=models.ManyToManyField(blank=True, related_name='games', to='game.Publisher', verbose_name='publishers'),
        ),
    ]
