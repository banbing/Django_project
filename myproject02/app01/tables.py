from app01.models import DataInfo
import django_tables2 as tables


class DataInfotable(tables.Table):
    class Meta:
        model = DataInfo
        attrs = {"class": "paleblue"}
