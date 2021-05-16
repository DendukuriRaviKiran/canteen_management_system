from django.db import models
from PIL import Image


# Create your models here.
class student(models.Model):
	name=models.CharField(max_length=100);
	email=models.CharField(max_length=100);
	pwd=models.CharField(max_length=100);
	zip=models.CharField(max_length=100);
	gender=models.CharField(max_length=100);
	age=models.CharField(max_length=100);

class guest(models.Model):
	name=models.CharField(max_length=100);
	email=models.CharField(max_length=100);
	pwd=models.CharField(max_length=100);
	zip=models.CharField(max_length=100);
	gender=models.CharField(max_length=100);
	age=models.CharField(max_length=100);

class category(models.Model):
	catname=models.CharField(max_length=100);

class items(models.Model):
	id = models.AutoField(primary_key=True);
	catname=models.CharField(max_length=100);
	itemname=models.CharField(max_length=100);
	itemtype=models.CharField(max_length=100);
	itemcost=models.CharField(max_length=100);
	photo = models.CharField(max_length=100);
	ratingval=models.CharField(max_length=100);

class cart(models.Model):
	sno = models.AutoField(primary_key=True);
	sname=models.CharField(max_length=100);
	semail=models.CharField(max_length=100);
	itemname=models.CharField(max_length=100);
	itemcost=models.CharField(max_length=100);
	tot = models.CharField(max_length=100);
	totcost = models.CharField(max_length=100);
	status = models.CharField(max_length=100);
	otp = models.CharField(max_length=100);
class otp(models.Model):
	otp = models.CharField(max_length=100);
	decision = models.CharField(max_length=100);
	delivery = models.CharField(max_length=100);
	dat_e=models.CharField(max_length=100);
class sales(models.Model):
	year = models.CharField(max_length=100);
	month = models.CharField(max_length=100);
	yearmonth = models.CharField(primary_key=True,max_length=100);
	tamt = models.CharField(max_length=100);

class productsales(models.Model):
	year = models.CharField(max_length=100);
	month = models.CharField(max_length=100);
	yearmonth = models.CharField(max_length=100);
	tamt = models.CharField(max_length=100);
	prod = models.CharField(max_length=100);
	


class feedback(models.Model):
	pid = models.CharField(max_length=100);
	review = models.CharField(max_length=1000);
	ratingval=models.CharField(max_length=100);



	
	


	
	

