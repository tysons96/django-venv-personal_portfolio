# Generated by Django 3.0 on 2021-07-02 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_rename_image_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='static/portfolio'),
        ),
    ]
