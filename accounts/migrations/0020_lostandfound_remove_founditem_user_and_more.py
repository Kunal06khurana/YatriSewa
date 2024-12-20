# Generated by Django 5.1.1 on 2024-11-14 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_remove_lostfounditem_status_lostfounditem_date_lost_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LostAndFound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('L', 'Lost'), ('F', 'Found')], default='L', max_length=1)),
                ('contact_info', models.CharField(max_length=255)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='founditem',
            name='user',
        ),
        migrations.DeleteModel(
            name='LostFoundItem',
        ),
        migrations.RemoveField(
            model_name='lostitem',
            name='user',
        ),
        migrations.DeleteModel(
            name='FoundItem',
        ),
        migrations.DeleteModel(
            name='LostItem',
        ),
    ]
