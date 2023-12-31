# Generated by Django 4.2.4 on 2023-09-23 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='courses',
            field=models.CharField(choices=[('Java', 'java SE-8'), ('Python', 'Python3'), ('C', 'C'), ('C++', 'C++'), ('Django', 'Django FrameWork')], default='python', max_length=30),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='Address',
            field=models.TextField(verbose_name='Current Address:'),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='email',
            field=models.EmailField(help_text='Give correct Email id', max_length=254, unique=True, verbose_name='Enter Email:'),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='name',
            field=models.CharField(help_text='Name should be within 30 letters', max_length=30, verbose_name='Enter Name:'),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='phone',
            field=models.BigIntegerField(help_text='Phone number should be in 10 digits', verbose_name='Enter Phone number:'),
        ),
    ]
