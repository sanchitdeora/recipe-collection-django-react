# Generated by Django 2.2.12 on 2020-05-29 04:55

import checking.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('ingredients', djongo.models.fields.ArrayModelField(model_container=checking.models.Ingredient)),
                ('nutritions', djongo.models.fields.ArrayModelField(model_container=checking.models.Nutrition)),
                ('instructions', models.TextField()),
            ],
        ),
    ]
