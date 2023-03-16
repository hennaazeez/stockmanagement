from django.urls import path

from stock_app import views

urlpatterns = [
    path("",views.index,name="index"),
    path("index1", views.index1, name="index1"),
    path("loginpage", views.loginpage, name="loginpage"),
    path("adminbase", views.adminbase, name="adminbase"),
    path("add_stock", views.add_stock, name="add_stock"),
    path("view_stock", views.view_stock, name="view_stock"),
    path("update/<int:id>/", views.update, name="update"),
    path("delete/<int:id>/", views.delete, name="delete"),

    path("admin_view_customer", views.admin_view_customer, name="admin_view_customer"),

    path("customers", views.customers, name="customers"),
    path("customerbase", views.customerbase, name="customerbase"),
    path("customer_registration", views.customer_registration, name="customer_registration"),
    path("customer_data", views.customer_data, name="customer_data"),
    path("logout_view", views.logout_view, name="logout_view"),

]