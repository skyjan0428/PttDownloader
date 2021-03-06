# Generated by Django 2.2.4 on 2019-08-14 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_auto_20190814_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='url',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.CreateModel(
            name='KeyWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('category', models.ManyToManyField(to='record.Category')),
            ],
        ),
    ]
