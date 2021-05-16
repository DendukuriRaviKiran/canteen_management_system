"""Canteen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views






urlpatterns = [ 
    path('', views.home, name="Welcome"),
    path('alogin/', views.alogin, name="alogin"), 
    path('stdreg/', views.stdreg, name="stdreg"),    
    path('greg/', views.greg, name="greg"),    
    path('signupaction/', views.signupaction, name="signupaction"),
    path('gsignupaction/', views.gsignupaction, name="gsignupaction"),
    path('slogin/', views.slogin, name="slogin"),    
    path('stdloginaction/', views.stdloginaction, name="stdloginaction"),
    path('stdhome/', views.stdhome, name="stdhome"),
    
    path('glogin/', views.glogin, name="glogin"),    
    path('gloginaction/', views.gloginaction, name="gloginaction"),
    path('ghome/', views.ghome, name="ghome"),
    
    path('adminhome/', views.adminhome, name="adminhome"),
    path('stdhome2/', views.stdhome2, name="stdhome2"),
    path('ghome2/', views.ghome2, name="ghome2"),
    path('adminloginaction/', views.adminlogindef, name="adminloginactiondef"),
    path('addcategory/', views.addcategory, name="addcategory"),
    path('additem/', views.additem, name="additem"),
    path('addcataction/', views.addcataction, name="addcataction"),
    path('additemaction/', views.additemaction, name="additemaction"),
    path('shome/', views.shome, name="shome"),
    path('slogout/', views.slogout, name="slogout"),
    path('glogout/', views.glogout, name="glogout"),
    path('viewitems/', views.viewitems, name="viewitems"),
    path('aviewitem/', views.aviewitems, name="aviewitems"),
    path('viewcatitems/<str:cat>/', views.viewcatitems, name="viewcatitems"),
    path('aviewcatitems/<str:cat>/', views.aviewcatitems, name="aviewcatitems"),
    path('addcart/', views.addcart, name="addcart"),
    path('viewcart/', views.viewcart, name="viewcart"),
    path('purchase/', views.purchase, name="purchase"),
    path('gpurchase/', views.gpurchase, name="gpurchase"),
    path('vieworders/', views.vieworders, name="vieworders"),
    path('viewotp/<str:op>/', views.viewotp, name="viewotp"),
    path('noted/', views.noted, name="noted"),
    path('searchotp/', views.searchotp, name="searchotp"),
    path('closeotp/', views.closeotp, name="closeotp"),
    path('sales/', views.salesdef, name="sales"),
    path('uploaddataset/', views.uploaddataset, name="uploaddataset"),
    path('xlupload/', views.xlupload, name="xlupload"),
    path('ixlupload/', views.ixlupload, name="ixlupload"),
    path('viewdataset/', views.viewdataset, name="viewdataset"),
    path('msales/', views.msales, name="msales"),
    path('msaleprediction/', views.msaleprediction, name="msaleprediction"),
    
    path('psalespred/', views.psalespred, name="psalespred"),
    path('psalespredview/', views.psalespredview, name="psalespredview"),
    path('feedbackdef/<str:pid>/', views.feedbackdef, name="feedbackdef"),
    path('submitfeedback/', views.submitfeedback, name="submitfeedback"),
    path('viewsentiment/', views.viewsentiment, name="viewsentiment"),


    path('gviewitems/', views.gviewitems, name="gviewitems"),
    path('gaddcart/', views.gaddcart, name="gaddcart"),
    path('gviewcart/', views.gviewcart, name="gviewcart"),
    path('psales/', views.psales, name="psales"),
    
]

