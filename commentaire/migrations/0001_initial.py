# Generated by Django 4.2.9 on 2024-02-23 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('message', models.TextField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
