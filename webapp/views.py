from django.shortcuts import render, redirect
from django.db.models import Count
from .models import student
from .models import category
from .models import cart
from .models import items
from .models import otp
from .models import sales
from .models import feedback
from .models import guest
from .models import productsales

from .SVMPrediction import SVMPrediction
from .Freq import CountFrequency
from .Graphs3 import viewg
import xlrd
from .timeseries import rmsValue
import matplotlib.pyplot as plt

# Create your views here.
def home(request):
	return render(request, 'index.html')
def alogin(request):
	return render(request, 'admin.html')

def slogin(request):
	return render(request, 'student.html')
def glogin(request):
	return render(request, 'guest.html')

def stdreg(request):
	return render(request, 'signup.html')
def greg(request):
	return render(request, 'gsignup.html')
def signupaction(request):
	email=request.POST['mail']
	pwd=request.POST['pwd']
	zip=request.POST['zip']
	name=request.POST['name']
	age=request.POST['age']
	gen=request.POST['gen']

		
	d=guest.objects.filter(email__exact=email).count()
	d1=student.objects.filter(email__exact=email).count()
	if d>0 or d1>0:
		return render(request, 'signup.html',{'msg':"Email Already Registered"})
	else:
		d=student(name=name,email=email,pwd=pwd,zip=zip,gender=gen,age=age)
		d.save()
		return render(request, 'signup.html',{'msg':"Register Success, You can Login.."})

	return render(request, 'signup.html',{'msg':"Register Success, You can Login.."})

def gsignupaction(request):
	email=request.POST['mail']
	pwd=request.POST['pwd']
	zip=request.POST['zip']
	name=request.POST['name']
	age=request.POST['age']
	gen=request.POST['gen']

		
	d=guest.objects.filter(email__exact=email).count()
	d1=student.objects.filter(email__exact=email).count()
	if d>0 or d1>0:
		return render(request, 'gsignup.html',{'msg':"Email Already Registered"})
	else:
		d=guest(name=name,email=email,pwd=pwd,zip=zip,gender=gen,age=age)
		d.save()
		return render(request, 'gsignup.html',{'msg':"Register Success, You can Login.."})

	return render(request, 'gsignup.html',{'msg':"Register Success, You can Login.."})

def stdloginaction(request):
	if request.method=='POST':
		uid=request.POST['mail']
		pwd=request.POST['pwd']
		d=student.objects.filter(email__exact=uid).filter(pwd__exact=pwd).count()
		
		if d>0:
			d=student.objects.filter(email__exact=uid)
			request.session['email']=uid
			
			request.session['name']=d[0].name
			return render(request, 'std_home.html',{'data': d[0]})

		else:
			return render(request, 'student.html',{'msg':"Login Fail"})

	else:
		return render(request, 'student.html')
def gloginaction(request):
	if request.method=='POST':
		uid=request.POST['mail']
		pwd=request.POST['pwd']
		d=guest.objects.filter(email__exact=uid).filter(pwd__exact=pwd).count()
		
		if d>0:
			d=guest.objects.filter(email__exact=uid)
			request.session['gemail']=uid
			
			request.session['name']=d[0].name
			return render(request, 'g_home.html',{'data': d[0]})

		else:
			return render(request, 'guest.html',{'msg':"Login Fail"})

	else:
		return render(request, 'student.html')
def adminlogindef(request):
	if request.method=='POST':
		uid=request.POST['uid']
		pwd=request.POST['pwd']
		
		if uid=='admin' and pwd=='admin':
			request.session['adminid']='admin'
			return render(request, 'admin_home.html')

		else:
			return render(request, 'admin.html',{'msg':"Login Fail"})

	else:
		return render(request, 'admin.html')
def stdhome(request):
	if "email" in request.session:
		uid=request.session["email"]
		d=student.objects.filter(email__exact=uid)
		return render(request, 'std_home.html',{'data': d[0]})

	else:
		return render(request, 'student.html')
def ghome(request):
	if "gemail" in request.session:
		uid=request.session["gemail"]
		d=guest.objects.filter(email__exact=uid)
		return render(request, 'g_home.html',{'data': d[0]})

	else:
		return render(request, 'student.html')
def adminhome(request):
	if "adminid" in request.session:
		
		return render(request, 'admin_home.html')

	else:
		return render(request, 'student.html')
def stdhome2(request):
	if "email" in request.session:
		uid=request.session["email"]
		d=student.objects.filter(email__exact=uid)
		return render(request, 'std_home.html',{'data': d[0],'msg':'Item Addedd to Cart Successfully..'})
	else:
		return render(request, 'student.html')
	
def ghome2(request):
	if "gemail" in request.session:
		uid=request.session["gemail"]
		
		d=guest.objects.filter(email__exact=uid)
		return render(request, 'g_home.html',{'data': d[0],'msg':'Item Addedd to Cart Successfully..'})
	else:
		return render(request, 'guest.html')
	
def addcategory(request):
	
	d=category.objects.all()
	return render(request, 'addcat.html',{'data': d})

def addcataction(request):
	if request.method=='POST':
		name=request.POST['name']
		d=category(catname=name)
		d.save()
	return redirect('addcategory')
def additem(request):
	
	d1=category.objects.all()
	d2=items.objects.all()
	return render(request, 'additem.html',{'cat': d1,'item':d2})
	
def additemaction(request):
	if request.method=='POST':
		cat=request.POST['cat']
		name=request.POST['name']
		cost=request.POST['cost']
		type=request.POST['type']
		image=request.FILES['itemimage']

		d=items(catname=cat,itemname=name,itemtype=type,itemcost=cost,photo=image,ratingval=0)
		print('------------',d.photo)
		d.save()
	return redirect('additem')

def slogout(request):
	try:
		del request.session['email']
	except:
		pass
	return render(request, 'student.html')
def glogout(request):
	try:
		del request.session['gemail']
	except:
		pass
	return render(request, 'guest.html')
def shome(request):
	if "email" in request.session:
		email=request.session["email"]
		d=student.objects.filter(email__exact=email)
		return render(request, 'std_home.html',{'data': d[0]})

	else:
		return redirect('slogout')
def viewitems(request):
	if "email" in request.session:

		d1=category.objects.all()
		d2=items.objects.all()	

		return render(request, 'viewitems.html',{'cat': d1,'item':d2})

	else:
		return redirect('slogout')
def gviewitems(request):
	if "gemail" in request.session:

		d1=category.objects.all()
		d2=items.objects.all()	

		return render(request, 'gviewitems.html',{'cat': d1,'item':d2})

	else:
		return redirect('slogout')


def aviewitems(request):
	if "adminid" in request.session:

		d1=category.objects.all()
		d2=items.objects.all()		
		return render(request, 'aviewitems.html',{'cat': d1,'item':d2})

	else:
		return redirect('alogin')
def viewcatitems(request,cat):
	if "email" in request.session:

		d2=items.objects.filter(catname__exact=cat)
		d1=category.objects.all()
		#d2=items.objects.all()		
		return render(request, 'viewitems.html',{'cat': d1,'item':d2})

	else:
		return redirect('slogout')


def aviewcatitems(request,cat):
	if "adminid" in request.session:

		d2=items.objects.filter(catname__exact=cat)
		d1=category.objects.all()
		#d2=items.objects.all()		
		return render(request, 'aviewitems.html',{'cat': d1,'item':d2})

	else:
		return redirect('slogout')



def addcart(request):
	if "email" in request.session:
		email=request.session["email"]
		name=request.session["name"]
		iname=request.POST['name']
		icost=request.POST['cost']
		id=request.POST['id']
		tot=request.POST['tot']
		icost=int(icost)
		tot=int(tot)
		tcost=icost*tot
		tcost=str(tcost)
		d=cart(sname=name,semail=email,itemname=iname,itemcost=str(icost),tot=str(tot),totcost=tcost,status='new')
		d.save()

		name=request.session["name"]	
		return redirect('stdhome2')

	else:
		return redirect('slogout')

def gaddcart(request):
	if "gemail" in request.session:
		email=request.session["gemail"]
		name=request.session["name"]
		iname=request.POST['name']
		icost=request.POST['cost']
		id=request.POST['id']
		tot=request.POST['tot']
		icost=int(icost)
		tot=int(tot)
		tcost=icost*tot
		tcost=str(tcost)
		d=cart(sname=name,semail=email,itemname=iname,itemcost=str(icost),tot=str(tot),totcost=tcost,status='new')
		d.save()

		name=request.session["name"]	
		return redirect('ghome2')

	else:
		return redirect('glogout')

def viewcart(request):
	if "email" in request.session:
		email=request.session["email"]
		d1=cart.objects.filter(semail=email).filter(status='new')
		t=0
		for d in d1:
			t=t+int(d.totcost)
		name=request.session["name"]	
		return render(request, 'viewcart.html',{'data': d1,'totcost':t})

	else:
		return redirect('slogout')
def gviewcart(request):
	if "gemail" in request.session:
		email=request.session["gemail"]
		d1=cart.objects.filter(semail=email).filter(status='new')
		t=0
		for d in d1:
			t=t+int(d.totcost)
		name=request.session["name"]	
		return render(request, 'gviewcart.html',{'data': d1,'totcost':t})

	else:
		return redirect('glogout')

def purchase(request):
	if "email" in request.session:
		import datetime
		x = datetime.datetime.now()
		date_=str(x.day)+'-'+str(x.month)+'-'+str(x.year)
		email=request.session["email"]
		import random as r
		op=""
		for i in range(6):
			op+=str(r.randint(1,9))
		print(op)
		d1=cart.objects.filter(semail=email).filter(status='new').update(otp=op)
		d1=cart.objects.filter(semail=email).update(status='done')
		d=otp(otp=op,decision='New',delivery='non',dat_e=date_)
		d.save()
		return render(request, 'viewcartsucc.html',{'otp': op})

	else:
		return redirect('slogout')

def gpurchase(request):
	if "gemail" in request.session:
		import datetime
		x = datetime.datetime.now()
		date_=str(x.day)+'-'+str(x.month)+'-'+str(x.year)
		email=request.session["gemail"]
		import random as r
		op=""
		for i in range(6):
			op+=str(r.randint(1,9))
		print(op)
		d1=cart.objects.filter(semail=email).filter(status='new').update(otp=op)
		d1=cart.objects.filter(semail=email).update(status='done')
		d=otp(otp=op,decision='New',delivery='non',dat_e=date_)
		d.save()
		return render(request, 'gviewcartsucc.html',{'otp': op})

	else:
		return redirect('glogout')


def vieworders(request):
	if "adminid" in request.session:
		import datetime
		x = datetime.datetime.now()
		date_=str(x.day)+'-'+str(x.month)+'-'+str(x.year)
		d1=otp.objects.filter(decision='New').filter(dat_e=date_)
		return render(request, 'vieworders.html',{'data': d1})

	else:
		return redirect('slogout')
def viewotp(request,op):
	if "adminid" in request.session:
		import datetime
		x = datetime.datetime.now()
		date_=str(x.day)+'-'+str(x.month)+'-'+str(x.year)
		t=0
		d1=cart.objects.filter(otp=op)
		for d in d1:
			t=t+int(d.totcost)		
		return render(request, 'viewotp.html',{'data': d1,'totcost':t,'otp':op})

	else:
		return redirect('slogout')
def noted(request):
	if "adminid" in request.session:
		
		import datetime
		x = datetime.datetime.now()
		date_=str(x.day)+'-'+str(x.month)+'-'+str(x.year)
		ym=str(x.year)+''+str(x.month)
		
		op=request.GET['otp']
		totcost=request.GET['totcost']
		d1=otp.objects.filter(otp=op).update(decision='done')
		
	
		d1=sales.objects.filter(yearmonth=ym)
		amt=0
		for d2 in d1:
			amt=d2.tamt
		amt=int(amt)
		amt=amt+int(totcost)


		d1=sales.objects.filter(yearmonth=ym).update(tamt=str(amt))

		return redirect('adminhome')

	else:
		return redirect('slogout')
def searchotp(request):
	if "adminid" in request.session:
		
		op=request.POST['otp']

		d1=otp.objects.filter(otp=op).filter(decision='done').filter(delivery='non').count()
		
		if d1>0:
			print('in if==========================')
			d2=cart.objects.filter(otp=op)
			t=0
			for d in d2:
				t=t+int(d.totcost)
			return render(request, 'searchotp.html',{'data': d2,'totcost':t,'otp':op})
		else:
			return render(request, 'vieworders.html',{'msg':'No Results'})

	else:
		return redirect('slogout')


def closeotp(request):
	if "adminid" in request.session:
		
		op=request.GET['otp']
		print('--------------',op)
		d1=otp.objects.filter(otp=op).update(delivery='done')
		
		return render(request, 'vieworders.html',{'msg':'Process Complete'})

	else:
		return redirect('slogout')
def salesdef(request):
	if "adminid" in request.session:

		return render(request, 'sales.html')

	else:
		return redirect('slogout')
def uploaddataset(request):
	if "adminid" in request.session:

		return render(request, 'uploaddataset.html')

	else:
		return redirect('slogout')
def xlupload(request):
	if "adminid" in request.session:
		file=request.POST['file']
		file="D:\\"+file
		book = xlrd.open_workbook(file)
		sheet = book.sheet_by_index(0)
		#sales.objects.all().delete()
		for r in range(1, sheet.nrows):
			f0 = sheet.cell(r, 0).value
			f1 = sheet.cell(r, 1).value
			f2 = sheet.cell(r, 2).value
			f3 = sheet.cell(r, 3).value
			d=sales(year=int(f0),month=int(f1),yearmonth=int(f2),tamt=int(f3))
			d.save()
			
		return render(request, 'uploaddataset.html',{'msg':"Dataset Uploaded Successfully"})
	else:
		return render(request, 'admin.html')
def ixlupload(request):
	if "adminid" in request.session:
		file=request.POST['file']
		file="D:\\"+file
		book = xlrd.open_workbook(file)
		sheet = book.sheet_by_index(0)
		#sales.objects.all().delete()
		for r in range(1, sheet.nrows):
			f0 = sheet.cell(r, 0).value
			f1 = sheet.cell(r, 1).value
			f2 = sheet.cell(r, 2).value
			f3 = sheet.cell(r, 3).value
			f4 = sheet.cell(r, 4).value
			d=productsales(year=int(f0),month=int(f1),yearmonth=int(f2),tamt=int(f3),prod=f4)
			d.save()
			
		return render(request, 'uploaddataset.html',{'msg':"Dataset Uploaded Successfully"})
	else:
		return render(request, 'admin.html')

def viewdataset(request):
	if "adminid" in request.session:
		data=sales.objects.all()
		return render(request, 'viewdataset.html',{'data':data})
		
	else:
		return render(request, 'admin.html')

def msales(request):
	if "adminid" in request.session:
		return render(request, 'msales.html')
		
	else:
		return render(request, 'admin.html')

def msaleprediction(request):
	if "adminid" in request.session:
		m=request.POST['month']
		print(m)
		m=m.split('-')
		y=int(m[0])
		m=int(m[1])
		print(m)
		d1=sales.objects.filter(month=m).order_by('year')
		data=[]
		years=[]
		for d in d1:
			data.append(int(d.tamt))
			years.append(int(d.year))
		print(data)
		pr=rmsValue(data)
		print(pr)
		pr=int(pr)
		data.append(pr)
		years.append(y)
		plt.plot( years,data)
		plt.xlabel('Year')
		plt.ylabel('Sales in Amount')
		plt.title('Sales Monthly Prediction')
		plt.show()

		fig = plt.figure(dpi=80)
		ax = fig.add_subplot(1,1,1)
		years,data
		table_data=[]
		for d in range(len(years)):
			table_data.append([years[d],data[d]])

		"""table_data=[
			["matched gt", 10],
			["unmatched gt", 20],
			["total gt", 30],
			["mean_precision", 0.6],
			["mean_recall", 0.4]
		]"""
		table = ax.table(cellText=table_data, loc='center')
		table.set_fontsize(14)
		table.scale(1,4)
		ax.axis('off')
		plt.show()

		return redirect('sales')

	else:
		return render(request, 'admin.html')
			

def psalespred(request):
	if "adminid" in request.session:
		d=productsales.objects.order_by().values_list('prod').distinct()
		print(d)
		data=[]
		for d1 in d:
			print(d1[0])
			data.append(d1[0])

		return render(request, 'psalespred.html',{'data':data})
		
	else:
		return render(request, 'admin.html')

def psalespredview(request):
	if "adminid" in request.session:
		p=request.POST['prod']
		m=request.POST['month']
		print(m,p)
		m=m.split('-')
		y=int(m[0])
		m=int(m[1])
		print(m,'month')
		d1=productsales.objects.filter(month=m).filter(prod=p).order_by('year')
		data=[]
		years=[]
		for d in d1:
			data.append(int(d.tamt))
			years.append(int(d.year))
		print(data,'<<<<<<<<<<<<<<<<<<<<<<<<<<')
		pr=rmsValue(data)
		print(pr)
		pr=int(pr)
		data.append(pr)
		years.append(y)
		plt.plot( years,data)
		plt.xlabel('Year')
		plt.ylabel('Sales in Amount')
		plt.title('Sales Monthly Prediction')
		plt.show()

		fig = plt.figure(dpi=80)
		ax = fig.add_subplot(1,1,1)
		years,data
		table_data=[]
		for d in range(len(years)):
			table_data.append([years[d],data[d]])

		"""table_data=[
			["matched gt", 10],
			["unmatched gt", 20],
			["total gt", 30],
			["mean_precision", 0.6],
			["mean_recall", 0.4]
		]"""
		table = ax.table(cellText=table_data, loc='center')
		table.set_fontsize(14)
		table.scale(1,4)
		ax.axis('off')
		plt.show()

		return redirect('sales')

	else:
		return render(request, 'admin.html')
			



def feedbackdef(request, pid):
	print('--------------------->',pid)
	d=feedback.objects.filter(pid__exact=pid)
	return render(request, 'feedback.html',{'pid':pid,'data':d})

def submitfeedback(request):
	if "email" in request.session:
		pid=request.POST["pid"]
		review=request.POST["review"]
		rating=request.POST['rating']
		d=feedback(pid=pid,review=review,ratingval=rating)
		d.save()
		rating=float(rating)
		d2=items.objects.filter(id=pid)
		for d3 in d2:
			ratingval=d3.ratingval
		ratingval=float(ratingval)
			
		print(ratingval,'ratingval')
		ratingval=(ratingval+rating)/2
		
		d1=items.objects.filter(id=pid).update(ratingval=ratingval)



		d=feedback.objects.filter(pid__exact=pid)
		return render(request, 'feedback.html',{'pid':pid,'data':d})

	else:
		return redirect('slogout')


def viewsentiment(request):
	if "email" in request.session:
		pid=request.GET["pid"]
		d2=feedback.objects.filter(pid=pid)
		reviews=[]
		for d3 in d2:
			review=d3.review
			reviews.append(review)
		data=SVMPrediction.detecting(reviews)

		
			
		print(data,'')
		st=CountFrequency(data)
		viewg(st)



		d=feedback.objects.filter(pid__exact=pid)
		return render(request, 'feedback.html',{'pid':pid,'data':d})

	else:
		return redirect('slogout')
def psales(request):
	
	d=cart.objects.values('itemname').annotate(dcount=Count('itemname')).order_by('dcount')
	dd={}
	for d1 in d:
		print(d1)
		#print(d1.itemname,d1.dcount)
		dd[d1['itemname']]=d1['dcount']
	print(dd)
	viewg(dd)
	return redirect('sales')
	
