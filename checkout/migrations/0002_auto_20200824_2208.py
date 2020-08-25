# Generated by Django 3.1 on 2020-08-24 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='full_name',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='postcode',
        ),
        migrations.AddField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
