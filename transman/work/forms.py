#coding:utf-8
from django import forms
from .models import TransRec,Card,OutRec

class ScanForm(forms.Form):
    qrcode=forms.CharField(label=("二维码"),required=True)

class NewForm(forms.ModelForm):
    def __init__(self,mine_queryset,*args,**kwargs):
        super(NewForm,self).__init__(*args,**kwargs)
        self.fields['mine'].queryset=mine_queryset
    class Meta:
        model=TransRec
        fields=[
            'car_no',
            'driver_name',
            'contact_info',
            'mine',
            'coal_type',
            'scale',
            'unit',
        ]
        labels={
            'car_no':'车牌号',
            'driver_name':'驾驶员姓名',
            'contact_info':'联系方式',
            'mine':'出发煤矿',
            'coal_type':'煤类型',
            'scale':'目标磅房',
            'unit':'单价',
        }

class OutForm(forms.ModelForm):
    class Meta:
        model=OutRec
        fields=[
            'car_no',
            'driver_name',
            'contact_info',
            'amount',
            'unit',
            'qrcode'
        ]
        labels={
            'car_no':'车牌号',
            'driver_name':'驾驶员姓名',
            'contact_info':'联系方式',
            'amount':'出货量',
            'unit':'单价',
            'qrcode':'二维码'
        }

class ArriveForm(forms.ModelForm):
    def __init__(self,qrcode,*args,**kwargs):
        super(ArriveForm,self).__init__(*args,**kwargs)
        self.fields['qrcode']=forms.CharField(widget=forms.HiddenInput(),initial=qrcode)
    class Meta:
        model=TransRec
        fields=[
            'setoff_amount',
            'arrive_amount',
        ]
        labels={
            'setoff_amount':'矿发量',
            'arrive_amount':'实收量'
        }

class SelectCardForm(forms.Form):
    qrcode=forms.CharField(widget=forms.HiddenInput())
    card=forms.ModelChoiceField(label=('油卡'),queryset=Card.objects.all())

class PayForm(forms.Form):
    qrcode=forms.CharField(widget=forms.HiddenInput())
    payfor=forms.CharField(widget=forms.HiddenInput())

class SearchForm(forms.Form):
    def __init__(self,opscales,opaccounts,*args,**kwargs):
        super(SearchForm,self).__init__(*args,**kwargs)
        self.fields['opscale']=forms.ModelChoiceField(label='磅房操作员',queryset=opscales)
        self.fields['opaccount']=forms.ModelChoiceField(label='财务操作员',queryset=opaccounts)
    setoff_time_begin=forms.DateField(label='出发时间范围 从')
    setoff_time_end=forms.DateField(label='至')
    car_no=forms.CharField(label='车牌号',max_length=10)
