# Generated by Django 2.2.13 on 2021-06-22 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('categ_id', models.AutoField(primary_key=True, serialize=False)),
                ('Categ_name', models.CharField(max_length=16)),
                ('Categ_desc', models.CharField(max_length=120)),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='credited_customer',
            fields=[
                ('cust_contact', models.IntegerField(primary_key=True, serialize=False)),
                ('cust_id', models.IntegerField()),
                ('fname', models.CharField(max_length=16)),
                ('lname', models.CharField(max_length=16)),
                ('address', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('prod_name', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('Sell_price', models.FloatField()),
                ('buy_price', models.FloatField()),
                ('prod_category', models.CharField(max_length=16)),
                ('date_in', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='cash_sales',
            fields=[
                ('trans_id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_quantity', models.FloatField()),
                ('prod_unit_price', models.FloatField()),
                ('total_price', models.FloatField()),
                ('trans_date', models.DateTimeField(auto_now=True)),
                ('prod_name', models.ForeignKey(on_delete='CASCADE', to='main.product')),
            ],
        ),
        migrations.CreateModel(
            name='credits',
            fields=[
                ('prod_name', models.ForeignKey(on_delete='CASCADE', primary_key=True, serialize=False, to='main.product')),
                ('prod_quantity', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('due_date', models.DateTimeField()),
                ('date_credited', models.DateTimeField(auto_now=True)),
                ('cust_contact', models.ForeignKey(on_delete='CASCADE', to='main.credited_customer')),
            ],
        ),
    ]
