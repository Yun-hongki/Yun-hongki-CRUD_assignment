# Generated by Django 4.1.7 on 2023-03-31 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_body_blog_content_alter_blog_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='blog'),
        ),
    ]