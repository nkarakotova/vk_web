# Generated by Django 4.1.3 on 2022-11-16 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_member_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='avatar',
            field=models.ImageField(blank=True, default='img/korgi.jpg', upload_to='img/avatars'),
        ),
    ]