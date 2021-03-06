# Generated by Django 2.2.4 on 2019-10-23 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comments', to='comments.Comment', verbose_name='Coment'),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Create at', verbose_name='Create at'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='Slug of the title', max_length=150, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='Post Title', max_length=150, unique=True, verbose_name='Post Title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Updating data', verbose_name='Updated at'),
        ),
    ]
