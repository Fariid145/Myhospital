# Generated by Django 3.1 on 2020-09-17 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('work', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='first_name',
            new_name='job_title',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='name',
        ),
        migrations.RemoveField(
            model_name='labtest',
            name='Patient',
        ),
        migrations.RemoveField(
            model_name='medicalrecords',
            name='text_result',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='email',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='role',
        ),
        migrations.AddField(
            model_name='doctor',
            name='staff',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.RESTRICT, to='work.staff'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='labtest',
            name='medical_records',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.RESTRICT, to='work.medicalrecords'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicalrecords',
            name='test_required',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='user',
            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.RESTRICT, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointments',
            name='appointment_reference',
            field=models.UUIDField(default=uuid.UUID('e202c2c8-6ea5-4071-94e9-6d7e1d37b624'), editable=False),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_group',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='genotype',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='occupation',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_id',
            field=models.UUIDField(default=uuid.UUID('ab425efb-0222-4dff-8fbb-9e52f722efc3'), editable=False),
        ),
        migrations.CreateModel(
            name='LabTech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='work.staff')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
