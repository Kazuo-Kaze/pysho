# Generated by Django 4.0.4 on 2022-05-15 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('shortDis', models.TextField()),
                ('slug', models.SlugField()),
                ('readMin', models.CharField(max_length=255)),
                ('firstPara', models.TextField()),
                ('secondPara', models.TextField()),
                ('thirdPara', models.TextField()),
                ('imageFirst', models.ImageField(null=True, upload_to='')),
                ('fourthPara', models.TextField(blank=True)),
                ('fifthPara', models.TextField(blank=True)),
                ('sixthPara', models.TextField(blank=True)),
                ('imageSecond', models.ImageField(blank=True, null=True, upload_to='')),
                ('seventhPara', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
