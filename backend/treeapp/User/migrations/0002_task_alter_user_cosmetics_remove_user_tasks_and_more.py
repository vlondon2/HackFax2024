# Generated by Django 5.0.1 on 2024-02-17 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('xp', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='cosmetics',
            field=models.JSONField(),
        ),
        migrations.RemoveField(
            model_name='user',
            name='tasks',
        ),
        migrations.AddField(
            model_name='user',
            name='tasks',
            field=models.ManyToManyField(to='User.task'),
        ),
    ]
