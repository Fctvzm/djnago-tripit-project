# Generated by Django 2.1.3 on 2018-11-25 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20181125_2033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itinerary',
            options={'ordering': ['trip']},
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='about_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='trip',
            name='recomendation',
            field=models.TextField(),
        ),
        migrations.AlterUniqueTogether(
            name='itinerary',
            unique_together={('trip', 'order')},
        ),
    ]