from django.urls import path

from product_app import views

urlpatterns = [
    path("",views.Home,name='Home'),
    path("Dashb",views.Dashb,name='Dashb'),
    path("Customerlogin",views.Customerlogin,name='Customerlogin'),
    path("ad_base",views.ad_base, name='ad_base'),
    path("cust_base",views.cust_base, name='cust_base'),
    path("login_view",views.login_view, name="login_view"),
    path("Item_category",views.Item_category, name="Item_category"),
    path("Categ_view",views.Categ_view, name="Categ_view"),
    path("Categ_delt/<int:id>/",views.Categ_delt, name="Categ_delt"),
    path("Categ_update/<int:id>/",views.Categ_update, name="Categ_update"),
    path("User_categview",views.User_categview, name="User_categview"),
    path("Add_products",views.Add_products, name="Add_products"),
    path("view_products",views.view_products, name="view_products"),
    path("update_product/<int:id>/",views.update_product, name="update_product"),
    path("delete_product/<int:id>/",views.delete_product, name="delete_product"),
    path("Approve_req/<int:id>/",views.Approve_req, name="Approve_req"),
    path("req_view",views.req_view, name="req_view"),
    path("admapprove/<int:id>/",views.admapprove, name="admapprove"),
    path("admreject/<int:id>/",views.admreject, name="admreject"),
    path("add_categ/<int:id>/", views.add_categ, name="add_categ"),
    path("single_product/<int:id>/", views.single_product, name="single_product"),
    path("Cart_view",views.Cart_view,name="Cart_view"),
    path("remove/<int:id>/",views.remove,name='remove'),
    path("payment/<int:id>/", views.payment, name='payment'),
    path("Cust_review", views.Cust_review, name='Cust_review'),
    path("cust_review_view", views.cust_review_view, name='cust_review_view'),
    path("Review_view", views.Review_view, name='Review_view'),
    path("search", views.search, name='search'),
    path("admin_pay_view", views.admin_pay_view, name='admin_pay_view'),
    path("logout_view",views.logout_view,name="logout_view"),




   ]