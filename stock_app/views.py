from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
from stock_app.forms import Login_form, register_form1, stockform
from stock_app.models import register, stock


def index(request):
    return render(request,"index.html")

@login_required(login_url='loginpage')
def index1(request):
    return render(request,"index1.html")

def loginpage(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        password=request.POST.get("pass")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect("adminbase")
            if user.is_customer:
                return redirect("customerbase")

        else:
            messages.info(request,"no user found")

    return render(request,"login.html")


@login_required(login_url='loginpage')
def adminbase(request):
    return render(request,"admin/admin base.html")

@login_required(login_url='loginpage')
def admin_view_customer(request):
    data=register.objects.all
    print(data)
    return render(request,"admin/admin_view_customerdata.html",{"data":data})

@login_required(login_url='loginpage')
def add_stock(request):
    form = stockform()
    print(form)
    if request.method == 'POST':
        form=stockform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("view_stock")
    return render(request,'admin/add_stock.html',{'form':form})


@login_required(login_url='loginpage')
def view_stock(request):
    data=stock.objects.all()
    return render(request,'admin/view_stock.html',{'data':data})

@login_required(login_url='loginpage')
def update(request,id):
    a = stock.objects.get(id=id)
    form = stockform(instance=a)
    if request.method == 'POST':
        form =stockform(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('view_stock')

    return render(request,'admin/update.html',{'form':form})

@login_required(login_url='loginpage')
def delete(request,id):
    wn = stock.objects.get(id=id)
    wn.delete()
    return redirect("view_stock")



@login_required(login_url='loginpage')
def customers(request):
    return render(request,"customers.html")

@login_required(login_url='loginpage')
def customerbase(request):
    return render(request,"customer/customer base.html")


def customer_registration(request):
    form1 = Login_form()
    form2 =register_form1()
    if request.method =="POST":
        form1 = Login_form(request.POST)
        form2 = register_form1(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            a = form1.save(commit=False)
            a.is_customer = True
            a.save()
            user1 = form2.save(commit=False)
            user1.user = a
            user1.save()
            return redirect('loginpage')

    return render(request,"customer/customers.html",{'form1': form1,'form2':form2})

@login_required(login_url='loginpage')
def customer_data(request):
    data=stock.objects.all
    print(data)
    return render(request,"customer/customers_data.html",{"data":data})

def logout_view(request):
    logout(request)
    return redirect("loginpage")