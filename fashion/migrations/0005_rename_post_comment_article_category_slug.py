# Generated by Django 4.2.18 on 2025-02-05 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fashion', '0004_alter_article_created_on_alter_article_updated_on_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='article',
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
