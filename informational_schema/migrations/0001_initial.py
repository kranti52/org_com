# Generated by Django 2.2.6 on 2019-10-06 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SystemObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_type', models.CharField(choices=[('issue', 'Issue'), ('product', 'Product'), ('metric', 'Metric')], max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('systemobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='informational_schema.SystemObject')),
                ('title', models.CharField(db_index=True, max_length=255, unique=True)),
                ('category', models.CharField(choices=[('general', 'General'), ('product', 'Product'), ('metric', 'Metric'), ('other', 'Other')], max_length=255)),
            ],
            bases=('informational_schema.systemobject',),
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('systemobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='informational_schema.SystemObject')),
                ('title', models.CharField(db_index=True, max_length=255, unique=True)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
            ],
            bases=('informational_schema.systemobject',),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('systemobject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='informational_schema.SystemObject')),
                ('title', models.CharField(db_index=True, max_length=255, unique=True)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
            ],
            bases=('informational_schema.systemobject',),
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='map_first_object', to='informational_schema.SystemObject')),
                ('second_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='map_second_object', to='informational_schema.SystemObject')),
            ],
            options={
                'unique_together': {('first_object', 'second_object')},
            },
        ),
    ]