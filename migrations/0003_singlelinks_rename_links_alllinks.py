# Generated by Django 4.1 on 2022-09-07 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0002_links'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Links',
            new_name='AllLinks',
        ),
    ]
