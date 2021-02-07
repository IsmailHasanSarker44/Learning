# Generated by Django 3.1.5 on 2021-02-01 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_name', models.CharField(max_length=100)),
                ('candidate_skill', models.TextField(max_length=1000)),
                ('candidate_projects', models.TextField(max_length=1000)),
                ('candidate_experienct', models.CharField(max_length=200)),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.job')),
            ],
        ),
    ]