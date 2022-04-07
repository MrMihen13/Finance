# Generated by Django 4.0.3 on 2022-03-19 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_cost_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cost',
            name='category_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.category', verbose_name='Category'),
            preserve_default=False,
        ),
    ]