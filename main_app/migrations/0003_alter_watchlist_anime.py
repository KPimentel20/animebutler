# Generated by Django 4.0.4 on 2022-05-03 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_watchlist_anime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.anime'),
        ),
    ]
