# Generated by Django 4.2.6 on 2023-10-26 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('uid', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.basemodel')),
                ('todo_title', models.CharField(max_length=100)),
                ('todo_description', models.TextField()),
                ('is_done', models.BooleanField(default=False)),
            ],
            bases=('home.basemodel',),
        ),
    ]
