# Generated by Django 3.2.4 on 2021-06-11 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_api_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='budget',
            field=models.DecimalField(decimal_places=10, default=1000.234, max_digits=19),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='college',
            name='type',
            field=models.CharField(choices=[('NAT', 'National'), ('PRV', 'Private')], default='NAT', max_length=3),
        ),
    ]
