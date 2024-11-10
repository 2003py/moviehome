# Generated by Django 4.2.16 on 2024-09-20 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_name', models.CharField(default='', max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='部门')),
                ('building', models.CharField(default='', max_length=15, verbose_name='楼栋')),
                ('budget', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='预算')),
                ('cachet', models.CharField(default='', max_length=200, verbose_name='公章')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '学院部门',
                'verbose_name_plural': '学院/部门',
            },
        ),
    ]