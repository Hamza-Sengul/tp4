# Generated by Django 5.0.6 on 2024-08-26 20:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0011_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='community_images/')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='mainpage.community')),
            ],
        ),
    ]
