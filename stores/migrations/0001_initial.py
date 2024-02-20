# Generated by Django 5.0.1 on 2024-02-20 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('p_name', models.CharField(blank=True, default='', max_length=180, null=True)),
                ('p_startdate', models.DateField(blank=True, null=True)),
                ('p_enddate', models.DateField(blank=True, null=True)),
                ('img_url', models.URLField(blank=True, default='', null=True)),
                ('news_url', models.URLField(default='')),
                ('p_location', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('p_hashtag', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('p_chucheon', models.TextField(blank=True, null=True)),
                ('frontLat', models.FloatField(blank=True, default='37.486660', null=True)),
                ('frontLon', models.FloatField(blank=True, default='127.021762', null=True)),
                ('is_visible', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
