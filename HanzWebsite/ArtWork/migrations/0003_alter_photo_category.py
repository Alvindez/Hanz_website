# Generated by Django 4.2.7 on 2023-11-02 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArtWork', '0002_rename_photos_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ArtWork.category'),
        ),
    ]
