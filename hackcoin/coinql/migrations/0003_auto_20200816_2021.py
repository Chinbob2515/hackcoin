# Generated by Django 3.0.7 on 2020-08-16 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coinql', '0002_auto_20200816_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='predecessor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='coinql.Node'),
        ),
    ]
