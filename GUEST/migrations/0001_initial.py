# Generated by Django 3.2.4 on 2021-07-28 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0002_library'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=250)),
                ('date', models.DateField(auto_now=True)),
                ('libraryname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.library')),
            ],
        ),
    ]
