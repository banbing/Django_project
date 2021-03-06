# Generated by Django 2.1.1 on 2018-10-29 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_datainfo_seal_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datainfo',
            name='apply_basis',
            field=models.CharField(choices=[(1, 'BMS'), (2, '业务流程单')], max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='apply_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='apply_seal_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='apply_type',
            field=models.CharField(choices=[(1, '新开'), (2, '撤销'), (3, '搬迁'), (4, '升速'), (5, '降速')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='area',
            field=models.CharField(choices=[(1, '本地'), (2, '长途')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='billing_begin',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='billing_end',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='complete_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='construct_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='contract_num',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='customer',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='ems_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='first_confirm_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='isp_report',
            field=models.CharField(choices=[(1, '是'), (2, '否')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='line_num',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='line_type',
            field=models.CharField(choices=[(1, 'MSTP'), (2, 'SDH'), (3, '互联网'), (4, '裸光纤')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='local_address',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='monthly_fee',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='nonrecurring_expense',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='note',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='notice_customer',
            field=models.CharField(choices=[(1, '是'), (2, '否')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='order_num',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='phone_num',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='receive_order_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='register_num',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='remote_address',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='server_type',
            field=models.CharField(choices=[(1, 'SDH/MSTP'), (2, 'VSEP'), (3, '高速行情'), (4, '沪港通'), (5, '数据中心'), (6, '自用线路')], max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='speed',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='username',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='datainfo',
            name='vlan',
            field=models.IntegerField(null=True),
        ),
    ]
