# Generated by Django 4.0.2 on 2023-10-09 19:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coaching',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('website', models.URLField(blank=True, max_length=100, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='coaching_logo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionPaper',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('total_marks', models.IntegerField()),
                ('time', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('coaching', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coaching.coaching')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('marks', models.IntegerField()),
                ('coaching', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coaching.coaching')),
                ('question_paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coaching.questionpaper')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('coaching', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coaching.coaching')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total_marks', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('coaching', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coaching.coaching')),
                ('question_paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coaching.questionpaper')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coaching.subjects')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('marks', models.IntegerField()),
                ('date', models.DateField()),
                ('coaching', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coaching.coaching')),
                ('question_paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coaching.questionpaper')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coaching.subjects')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coaching.test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestResultDetails',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('answer', models.CharField(max_length=100)),
                ('is_correct', models.BooleanField(default=False)),
                ('coaching', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coaching.coaching')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coaching.questions')),
                ('question_paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coaching.questionpaper')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coaching.subjects')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coaching.test')),
                ('test_result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coaching.testresult')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='questions',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coaching.subjects'),
        ),
        migrations.AddField(
            model_name='questionpaper',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coaching.subjects'),
        ),
    ]
