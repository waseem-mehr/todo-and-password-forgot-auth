# Generated by Django 3.1 on 2020-08-25 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('todo_id', models.AutoField(primary_key=True, serialize=False)),
                ('todo_text', models.TextField(max_length=255, null=True)),
            ],
        ),
    ]