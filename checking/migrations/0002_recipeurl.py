# Generated by Django 2.2.12 on 2020-06-02 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=2000)),
            ],
        ),
    ]