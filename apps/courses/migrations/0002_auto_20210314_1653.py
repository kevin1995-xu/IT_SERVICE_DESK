# Generated by Django 2.2 on 2021-03-14 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_org',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.CourseOrg', verbose_name='支撑团队'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.Teacher', verbose_name='讲师'),
        ),
        migrations.CreateModel(
            name='BannerCourse',
            fields=[
            ],
            options={
                'verbose_name': '轮播教程',
                'verbose_name_plural': '轮播教程',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('courses.course',),
        ),
    ]
