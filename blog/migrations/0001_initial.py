# Generated by Django 4.2 on 2023-05-04 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('excerpt', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='images/')),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_added'],
            },
        ),
    ]