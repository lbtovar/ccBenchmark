# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 18:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Benchmark',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('version', models.CharField(max_length=20)),
                ('effective_date', models.DateField(verbose_name=b'effective')),
                ('technology', models.CharField(choices=[(b'db', b'Database'), (b'web', b'Web Server'), (b'app', b'Application Server'), (b'dev', b'Application Security & Development'), (b'svc', b'Application Services'), (b'cloud', b'Cloud Services'), (b'browser', b'Browser'), (b'desk', b'Desktop')], max_length=10)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_id', models.CharField(max_length=5)),
                ('title', models.CharField(max_length=200)),
                ('scored', models.BooleanField(default=False)),
                ('profile', models.CharField(choices=[(b'1', b'Level 1'), (b'2', b'Level 2')], max_length=10)),
                ('cci_number', models.CharField(blank=True, max_length=25, null=True)),
                ('description', models.TextField()),
                ('rationale', models.TextField(blank=True, null=True)),
                ('audit', models.TextField(blank=True, null=True)),
                ('commands', models.TextField(blank=True, null=True)),
                ('remediation', models.TextField(blank=True, null=True)),
                ('impact', models.TextField(blank=True, null=True)),
                ('default', models.TextField(blank=True, null=True)),
                ('references', models.TextField(blank=True, null=True)),
                ('benchmark', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='controls.Benchmark')),
            ],
            options={
                'ordering': ('doc_id',),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('poc', models.CharField(max_length=50)),
                ('due_date', models.DateField(verbose_name=b'analysis due')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Remediation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[(b'NR', b'Not Reviewed'), (b'Y', b'Yes'), (b'N', b'No'), (b'NA', b'Not Applicable')], max_length=20)),
                ('action', models.TextField(blank=True, null=True)),
                ('who', models.CharField(blank=True, max_length=50, null=True)),
                ('remediation_date', models.DateField(blank=True, null=True, verbose_name=b'remediation date')),
                ('control', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remediation_control', to='controls.Control')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remediation_project', to='controls.Project')),
            ],
            options={
                'ordering': ('control_id',),
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sect_id', models.CharField(blank=True, max_length=10, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('benchmark', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='controls.Benchmark')),
                ('section', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='controls.Section')),
            ],
            options={
                'ordering': ('sect_id',),
            },
        ),
        migrations.AddField(
            model_name='project',
            name='controls',
            field=models.ManyToManyField(through='controls.Remediation', to='controls.Control'),
        ),
        migrations.AddField(
            model_name='control',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='controls.Section'),
        ),
        migrations.AlterUniqueTogether(
            name='remediation',
            unique_together=set([('project', 'control')]),
        ),
        migrations.AlterUniqueTogether(
            name='control',
            unique_together=set([('benchmark', 'doc_id')]),
        ),
    ]
