from django.shortcuts import render, redirect

from main.models import client_info, buy_info
# Create your views here.




def main(request):
    if request.method == "GET":
        return render(request, "home/index.html")

# buy_view
def buy_view(request):
    if request.method == "GET":
        buy_data = buy_info.objects.filter()
        client_data = client_info.objects.all()
        context = {
            "buy_data" : buy_data,
            "clients" : client_data
        }
        return render(request, "home/buy_view.html", context)
def buy_create(request):
    if request.method == "POST":
        return redirect("")
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




