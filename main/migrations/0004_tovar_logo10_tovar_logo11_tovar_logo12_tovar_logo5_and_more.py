# Generated by Django 5.0 on 2024-03-11 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_category_partner_feedback_message_tovar'),
    ]

    operations = [
        migrations.AddField(
            model_name='tovar',
            name='logo10',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AddField(
            model_name='tovar',
            name='logo11',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AddField(
            model_name='tovar',
            name='logo12',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AddField(
            model_name='tovar',
            name='logo5',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AddField(
            model_name='tovar',
            name='logo6',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AddField(
            model_name='tovar',
            name='logo7',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AddField(
            model_name='tovar',
            name='logo8',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
        migrations.AddField(
            model_name='tovar',
            name='logo9',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
    ]