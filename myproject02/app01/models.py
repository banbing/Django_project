from django.db import models
from django.utils import timezone
#


class DataInfo(models.Model):
    register_num = models.CharField(max_length=64, null=True)
    customer = models.CharField(max_length=64, null=True)
    SERVER_TYPE = (
        (1, "SDH/MSTP"),
        (2, "VSEP"),
        (3, "高速行情"),
        (4, "沪港通"),
        (5, "数据中心"),
        (6, "自用线路")

    )
    server_type = models.CharField(choices=SERVER_TYPE, max_length=24, null=True)
    APPLY_BASIS = (
        (1, "BMS"),
        (2, "业务流程单")
    )
    apply_basis = models.CharField(max_length=24, choices=APPLY_BASIS, null=True)
    APPLY_TYPE = (
        (1, "新开"),
        (2, "撤销"),
        (3, "搬迁"),
        (4, "升速"),
        (5, "降速")
    )
    apply_type = models.CharField(max_length=4, choices=APPLY_TYPE, null=True)
    speed = models.CharField(max_length=10, null=True)
    LINE_TYPE = (
        (1, "MSTP"),
        (2, "SDH"),
        (3, "互联网"),
        (4, "裸光纤")
    )
    line_type = models.CharField(max_length=8, choices=LINE_TYPE, null=True)
    AREA = (
        (1, "本地"),
        (2, "长途")
    )
    area = models.CharField(max_length=4, choices=AREA, null=True)
    nonrecurring_expense = models.IntegerField(null=True)
    monthly_fee = models.FloatField(null=True)
    billing_begin = models.DateField(null=True)
    billing_end = models.DateField(null=True)
    local_address = models.CharField(max_length=128, null=True)
    remote_address = models.CharField(max_length=128, null=True)
    vlan = models.IntegerField(null=True)
    username = models.CharField(max_length=32, null=True)
    phone_num = models.CharField(max_length=64, null=True)
    apply_date = models.DateField(null=True)
    contract_num = models.CharField(max_length=64, null=True)
    first_confirm_date = models.DateField(null=True)
    apply_seal_date = models.DateField(null=True)
    seal_date = models.DateField(null=True)
    ems_date = models.DateField(null=True)
    order_num = models.CharField(max_length=64, null=True)
    receive_order_date = models.DateField(null=True)
    line_num = models.CharField(max_length=64, null=True)
    construct_date = models.DateField(null=True)
    complete_date = models.DateField(null=True)
    YES_NO = (
        (1, "是"),
        (2, "否")
    )
    notice_customer = models.CharField(max_length=4, choices=YES_NO, null=True)
    isp_report = models.CharField(max_length=4, choices=YES_NO, null=True)
    note = models.CharField(max_length=128, null=True)