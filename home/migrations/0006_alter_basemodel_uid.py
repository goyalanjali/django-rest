# Generated by Django 4.2.6 on 2023-10-29 09:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_todo_user_alter_basemodel_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basemodel',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('b74c5fb3-ab02-471b-8f4e-eb0238a9ac4b'), editable=False, primary_key=True, serialize=False),
        ),
    ]
