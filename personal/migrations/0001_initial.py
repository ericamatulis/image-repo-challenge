# Generated by Django 3.1.1 on 2021-05-09 17:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200, unique=True)),
                ('category_description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_sold', models.DecimalField(decimal_places=2, default=0, max_digits=999)),
                ('amount_spent', models.DecimalField(decimal_places=2, default=0, max_digits=999)),
                ('credit_left', models.DecimalField(decimal_places=2, default=100, max_digits=999)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, unique=True)),
                ('product_description', models.TextField(default='')),
                ('product_quantity', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=999, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0.01)])),
                ('product_image', models.ImageField(upload_to='images')),
                ('number_sold', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('amount_sold', models.DecimalField(decimal_places=2, default=0, max_digits=999, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('is_active', models.BooleanField(default=True)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=999, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('categories', models.ManyToManyField(blank=True, related_name='products', to='personal.Category')),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-is_active', '-product_quantity'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('price', models.DecimalField(decimal_places=2, max_digits=999, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0.01)])),
                ('total', models.DecimalField(decimal_places=2, max_digits=999)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('seller', models.CharField(max_length=200)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personal.product')),
            ],
        ),
        migrations.CreateModel(
            name='ChangeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_product', models.TextField(null=True)),
                ('new_product', models.TextField(null=True)),
                ('type_of_change', models.CharField(choices=[(1, 'Delete'), (2, 'Update'), (3, 'Add')], max_length=200)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('changed_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]