# Generated by Django 4.0.2 on 2022-02-10 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_educations_jobexperience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resent_work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('thumbnail_img', models.ImageField(upload_to='media/work/thumbnail')),
                ('popup_img', models.ImageField(upload_to='media/work/thumbnail')),
                ('popup_heding', models.CharField(max_length=100)),
                ('popup_description_one', models.CharField(max_length=300)),
                ('popup_description_two', models.CharField(max_length=300)),
                ('popup_product_link', models.CharField(max_length=200)),
            ],
        ),
    ]
