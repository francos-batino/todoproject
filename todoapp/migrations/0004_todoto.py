# Generated by Django 3.0.4 on 2022-12-25 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_todo_done'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('done', models.BooleanField(default=False)),
                ('priority', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.Todo')),
            ],
        ),
    ]