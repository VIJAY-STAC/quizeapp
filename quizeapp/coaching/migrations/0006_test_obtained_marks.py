# Generated by Django 4.0.2 on 2023-10-11 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaching', '0005_remove_testresultdetails_test_result_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='obtained_marks',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
    ]
