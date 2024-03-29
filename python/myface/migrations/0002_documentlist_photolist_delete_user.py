# Generated by Django 4.0.1 on 2022-02-03 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myface', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='file/', verbose_name='ファイル')),
            ],
            options={
                'db_table': 'documentlist',
            },
        ),
        migrations.CreateModel(
            name='PhotoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photo/', verbose_name='フォト')),
            ],
            options={
                'db_table': 'photolist',
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
