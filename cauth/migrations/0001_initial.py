# Generated by Django 4.0.4 on 2022-09-30 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True, verbose_name='Email')),
                ('username', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Username')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=150, verbose_name='Last Name')),
                ('rate_plan', models.CharField(choices=[('free', 'Бесплатный'), ('base', 'Базовый'), ('professional', 'Профессиональный')], default='free', max_length=13, verbose_name='Rate plan')),
                ('telegram_id', models.CharField(blank=True, max_length=128, null=True, verbose_name='Telegram ID')),
                ('discord_id', models.CharField(blank=True, max_length=128, null=True, verbose_name='Discord ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is Staff')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created t')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
