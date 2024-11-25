from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from product_app.forms import LoginRegister, CustomerForm, CategoryForm, ItemForm, ReviewForm
from product_app.models import Customer, Category, Item, Quantity_1, Review, Paymoney


def Home(request):
    return render(request,'index.html')


def Dashb(request):
    return render(request,'dash.html')


def Customerlogin(request):
    login_form = LoginRegister()
    customer_form = CustomerForm()
    if request.method == "POST":
        login_form = LoginRegister(request.POST)
        customer_form = CustomerForm(request.POST)

        if login_form.is_valid() and customer_form.is_valid():
            user2 = login_form.save(commit=False)
            user2.is_user = True
            user2.save()
            user1 = customer_form.save(commit=False)
            user1.user_1 = user2
            user1.save()

    return render(request,'cust_reg.html',{'login_form': login_form, 'customer_form': customer_form})


def ad_base(request):
    return render(request,'admin/ad_base.html')


def cust_base(request):
    data = Customer.objects.get(user_1=request.user)
    return render(request, 'customer/cust_base.html', {'data': data})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('ad_base')
            elif user.is_user:
                return redirect('cust_base')

        else:
            messages.info(request,'invalid credentials')
    return render(request,'login.html')


def Item_category (request):
    category_form = CategoryForm()
    if request.method == "POST":
        category_form  = CategoryForm(request.POST, request.FILES)
        if category_form .is_valid():
            category_form .save()
            return redirect('ad_base')
    return render(request, 'admin/category.html', {"form": category_form})


def Categ_view(request):
    data = Category.objects.all()
    return render(request, 'admin/categ_view.html', {'data': data})


def Categ_delt(request,id):
    if request.method == "POST":
        data=Category.objects.get(id=id)
        data.delete()
        return redirect("Categ_view")


def Categ_update(request,id):
    categ=Category.objects.get(id=id)
    form=CategoryForm(instance=categ)
    if request.method == "POST":
        form=CategoryForm(request.POST,request.FILES,instance=categ)
        if form.is_valid():
            form.save()
            return redirect("Categ_view")
    return render(request,"admin/categ_update.html",{"form":form})


def User_categview(request):
    data=Category.objects.all()
    return render(request,'customer/viewcateg.html',{'data':data})


def Add_products(request):
    item_form = ItemForm()
    if request.method == "POST":
        item_form = ItemForm(request.POST,request.FILES)
        if item_form.is_valid():
            item_form.save()
            return redirect('Add_products')
    return render(request, 'customer/add_products.html', {"form": item_form})


def view_products(request):
    data = Item.objects.all()
    return render(request,"customer/productview.html",{"data":data})


def update_product(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(instance=item)
    if request.method == "POST":
        form = ItemForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            form.save()
    return render(request,'customer/productupdate.html',{"form":form})


def delete_product(request,id):
    if request.method == "POST":
        data=Item.objects.get(id=id)
        data.delete()
        return redirect("view_products")


def Approve_req(request,id):
        c = Category.objects.get(id=id)
        std = request.user

        u = Customer.objects.get(user_1=std)

        v = Item.objects.filter(user=u,category=c)

        if v.exists():
            messages.info(request, 'you have already requested to join')
            return redirect('view_products')


        else:
            if request.method == "POST":
                obj = Item()
                obj.user= u
                obj.category= c
                obj.save()

                messages.info(request, 'Approve request send successfully')


        return render(request,'customer/request.html',{'show':v})


def req_view(request):
    data=Item.objects.all()
    return render(request,'admin/reqview.html',{'data':data})


def admapprove(request,id):
    data=Item.objects.get(id=id)
    if request.method == "POST":
        data.approval_status=1
        data.save()
        return redirect("req_view")


def admreject(request,id):
    data=Item.objects.get(id=id)
    if request.method == "POST":
        data.approval_status=2
        data.save()
        return redirect("req_view")


def add_categ(request,id):

    k=Item.objects.filter(category=id)
    return render(request,'customer/catview.html',{'data': k})


def single_product(request,id):
    t=Item.objects.get(id=id)
    u=request.user
    c=Customer.objects.get(user_1=u)
    q=Quantity_1.objects.filter(item_1=t,customer_1=c)
    qty= request.POST.get('data')

    if request.method == "POST":
        obj = Quantity_1()
        obj.item_1 = t
        obj.customer_1=c
        obj.quantity = qty
        obj.save()

        messages.info(request, 'Item added to the cart')
        return redirect("single_product",id=t.id)
    return render(request, 'customer/singleproduct.html', {'data': t})


def Cart_view(request):
    data=Quantity_1.objects.all()
    return render(request,"customer/cart_view.html",{"data":data})


def remove(request,id):
    if request.method == "POST":
        data = Quantity_1.objects.get(id=id)
        data.delete()
        return redirect("Cart_view")


def payment(request,id):
    q=Quantity_1.objects.get(id=id)
    u = request.user
    c = Customer.objects.get(user_1=u)
    p = Paymoney.objects.filter(quantity_2=q)
    adrs=request.POST.get("data1")
    cano = request.POST.get("data2")
    cvno = request.POST.get("data3")
    tp=(q.item_1.price)*(q.quantity)

    if request.method == 'POST':
        obj = Paymoney()
        obj.quantity_2=q
        obj.address=adrs
        obj.total_price=tp
        obj.card_no=cano
        obj.cvv=cvno
        obj.save()
        q.item_1.in_stock = (q.item_1.in_stock) - (q.quantity)
        q.item_1.save()
        q.product_status = 1
        q.save()


    return render(request, 'customer/pay.html', {'data':q,'total':tp})


def admin_pay_view(request):
    data=Paymoney.objects.all()
    return render(request,'admin/pay_view.html',{'data':data})


def Cust_review(request):
    form = ReviewForm()
    u = request.user
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.customer_2 = u
            data.save()
    return render(request, "customer/review.html", {"form": form})


def cust_review_view(request):
    u=request.user.id
    data = Review.objects.filter(customer_2=u)
    return render(request, 'customer/revview.html', {"data": data})


def Review_view(request):
    data=Review.objects.all()
    return render(request, "admin/review_view.html", {"data": data})


def search(request):
    if request.GET.get('search1'): #write your form name here
        find=request.GET.get('search1')
        try:
            items=Item.objects.filter(product_name__icontains=find)
            return render(request,"customer/search.html",{"view":items})
        except:
            return render(request,"customer/search.html",{"view":items})
    else:
        return render(request, "customer/search.html")


@login_required(login_url='login_view')
def logout_view(request):
    logout(request)
    return redirect('login_view')










































