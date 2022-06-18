# Generated by Django 2.2 on 2022-05-29 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadline', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=1000)),
                ('choice_A', models.CharField(max_length=255)),
                ('choice_B', models.CharField(max_length=255)),
                ('choice_C', models.CharField(max_length=255)),
                ('choice_D', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=20)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Problem')),
            ],
        ),
    ]