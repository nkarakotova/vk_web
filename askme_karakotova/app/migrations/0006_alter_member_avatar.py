# Generated by Django 4.1.3 on 2022-11-16 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_member_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='avatar',
            field=models.ImageField(blank=True, default='static/img/korgi.jpg', upload_to='app/static/img'),
        ),
    ]
