# Generated by Django 4.1.1 on 2022-10-25 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InterfaceApp', '0007_memodb'),
    ]

    operations = [
        migrations.AddField(
            model_name='performancedb',
            name='site',
            field=models.URLField(null=True),
        ),
        migrations.DeleteModel(
            name='MemoDB',
        ),
    ]
