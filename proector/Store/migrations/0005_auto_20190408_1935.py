# Generated by Django 2.1.5 on 2019-04-08 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Store', '0004_categories_url_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'cart_items',
                'ordering': ['date_added'],
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('publishe_date', models.DateTimeField(verbose_name='date published')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('url_slug', models.CharField(default='default', max_length=31)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('news_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='Store.Categories')),
            ],
        ),
        migrations.RemoveField(
            model_name='blog_news',
            name='news_category',
        ),
        migrations.DeleteModel(
            name='Blog_news',
        ),
        migrations.AddField(
            model_name='like',
            name='liked',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked', to='Store.Product'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.Product'),
        ),
    ]
