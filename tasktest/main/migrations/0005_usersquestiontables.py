# Generated by Django 4.2.11 on 2024-05-09 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersQuestionTables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ip', models.CharField(max_length=50, verbose_name='ip')),
                ('current_question', models.IntegerField(verbose_name='current_question_number')),
            ],
        ),
    ]
