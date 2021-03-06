# Generated by Django 4.0.3 on 2022-05-05 02:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer_services', '0004_inquiry_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='writer',
        ),
        migrations.AddField(
            model_name='answer',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='답변작성자', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='inquiry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer_services.inquiry'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='질문작성자'),
        ),
    ]
