from django.shortcuts import render, redirect

from main.models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse


import json
from django.core.serializers.json import DjangoJSONEncoder





# Create your views here.
def login_message_required(function):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, "로그인한 사용자만 이용할 수 있습니다.")
            return redirect(settings.LOGIN_URL)
        return function(request, *args, **kwargs)
    return wrap

def login_view(request):
    if request.method == "GET":
        return render(request, "home/login.html")
    elif request.method == "POST":
        print(request.POST.get("id"))
        print(request.POST.get("pw"))
        user = authenticate(username=request.POST.get("id"), password=request.POST.get("pw"))
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect("/login/")
@login_message_required
def main(request):
    if request.method == "GET":
        return render(request, "home/index.html")

# buy_view
def buy_view(request):
    if request.method == "GET":
        buy_data = buy_info.objects.filter()
        client_data = client_info.objects.all()
        context = {
            "buy_datas" : buy_data,
            "clients" : client_data
        }
        return render(request, "home/buy_view.html", context)
def buy_create(request):
    if request.method == "POST":
        print(request.POST)
        client_db = client_info.objects.get(client_id=request.POST.get("client_id"))
        if request.POST.get("item_id") == "":
            item_db = item_info()
            item_db.client_id = client_db
            item_db.serial_number = request.POST.get("item_serial_number")
            item_db.item_name = request.POST.get("item_name")
            item_db.count = request.POST.get("count")
            item_db.save()
        else:
            item_db = item_info.objects.get(item_id=request.POST.get("item_id"))
            item_db.count = int(item_db.count) + int(request.POST.get("count"))
            item_db.save()
        buy_db = buy_info()
        buy_db.client_id = client_db
        buy_db.item_id = item_db
        buy_db.buy_date = request.POST.get("buy_date")
        buy_db.count = request.POST.get("count")
        buy_db.unit_price = request.POST.get("unit_price")
        
        if request.POST.get("vat_check") == "on":
            buy_db.vat_check = "1"
            buy_db.total_money = int(request.POST.get("unit_price"))*int(request.POST.get("count"))
        elif request.POST.get("vat_check") == "false":
            buy_db.vat_check = "0"
            buy_db.total_money = int(round(int(request.POST.get("unit_price"))*1.1))*int(request.POST.get("count"))
        buy_db.save()
        
        context = json.dumps({"code" : 200}, cls=DjangoJSONEncoder)
        return HttpResponse(context, content_type = "application/json")
def buy_delete(request):
    if request.method == "POST":
        return redirect("")
def buy_modify(request):
    if request.method == "POST":
        return redirect("")

# sale_view
def sale_view(request):
    if request.method == "GET":
        return render(request, "home/sale_view.html")
def sale_create(request):
    if request.method == "POST":
        return redirect("")
def sale_delete(request):
    if request.method == "POST":
        return redirect("")
def sale_modify(request):
    if request.method == "POST":
        return redirect("")



# Client View
def client_view(request):
    if request.method == "GET":
        client_data = client_info.objects.all()
        context = {
            "clients" : client_data
            }
        return render(request, "home/client_view.html", context)

def client_create(request):
    if request.method == "POST":
        client_db = client_info()
        client_db.client_corp_name  = request.POST.get("client_corp_name")
        client_db.client_name       = request.POST.get("client_name")
        client_db.client_number     = request.POST.get("client_number")
        client_db.client_address    = request.POST.get("client_address")
        client_db.client_type       = request.POST.get("client_type")
        client_db.client_job_type   = request.POST.get("client_job_type")
        client_db.client_email      = request.POST.get("client_email")
        client_db.client_sub_email  = request.POST.get("client_sub_email")
        client_db.client_tel        = request.POST.get("client_tel")
        client_db.client_sub_tel    = request.POST.get("client_sub_tel")
        client_db.client_fax        = request.POST.get("client_fax")
        client_db.etc               = request.POST.get("etc")
        client_db.save()
        return redirect("/client/")

def client_delete(request):
    if request.method == "POST":
        client_id_data = request.POST.get("client_id")
        client_db = client_info.objects.get(client_id = client_id_data)
        client_db.delete()
        return redirect("/client/")

def client_modify(request):
    if request.method == "POST":
        client_db = client_info.objects.get(client_id = request.POST.get("client_id"))
        client_db.client_corp_name  = request.POST.get("client_corp_name")
        client_db.client_name       = request.POST.get("client_name")
        client_db.client_number     = request.POST.get("client_number")
        client_db.client_address    = request.POST.get("client_address")
        client_db.client_type       = request.POST.get("client_type")
        client_db.client_job_type   = request.POST.get("client_job_type")
        client_db.client_email      = request.POST.get("client_email")
        client_db.client_sub_email  = request.POST.get("client_sub_email")
        client_db.client_tel        = request.POST.get("client_tel")
        client_db.client_sub_tel    = request.POST.get("client_sub_tel")
        client_db.client_fax        = request.POST.get("client_fax")
        client_db.etc               = request.POST.get("etc")
        client_db.save()        
        return redirect("/client/")










def search_items(request):
    if request.method == "GET":
        client_id = request.GET.get("client_id")
        print(client_id)
        # client_db = client_info.objects.get(client_id=client_id)
        items_data = item_info.objects.filter(client_id=client_id)
        item_list = []
        for i in items_data:
            data = {
                "item_id" : i.item_id,
                "client_id" : i.client_id.client_id,
                "item_name" : i.item_name,
                "serial_number" : i.serial_number,
                "item_type" : i.item_type,
                "count" : i.count,
            }
            item_list.append(data)
        print(item_list)
        data = {
            "items_data" : item_list
        }


        context = json.dumps(item_list, cls=DjangoJSONEncoder)
        return HttpResponse(context, content_type = "application/json")




