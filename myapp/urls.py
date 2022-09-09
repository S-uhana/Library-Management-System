from django.urls import path,include
from . import views

urlpatterns = [
   path("",views.Index,name="index"),
   path("home",views.Home,name="home"),
   path("insert",views.Insert,name="insert"),
   path("insertData",views.InsertData,name="insertData"),
   path("showpage",views.ShowPage,name="showpage"),
   path("edit",views.Edit,name="edit"),
   path("editpage/<int:pk>",views.EditPage,name="editpage"),
   path("update/<int:pk>",views.UpdateData,name="update"),
   path("delete/<int:pk>",views.Deletedata,name="delete"),
   path("admin",views.AdminHome,name="admin"),
   path("registeruser",views.RegisterUser,name="registeruser"),
   path("studshow",views.StudShow,name="studshow"),
   path("login",views.LoginUser,name="login"),
  
]
