# Generated by Django 3.1.2 on 2020-10-16 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_text', models.TextField()),
                ('event_type', models.CharField(choices=[('financial', 'Financial'), ('fun', 'Fun'), ('accident', 'Accident'), ('payment', 'Payment'), ('life', 'Life')], default='financial', max_length=300)),
                ('event_image', models.ImageField(upload_to='events')),
                ('event_background', models.ImageField(upload_to='events')),
            ],
        ),
    ]
