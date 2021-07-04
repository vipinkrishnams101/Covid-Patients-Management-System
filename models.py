from django.db import models
import datetime
class patients(models.Model):
	name=models.CharField(max_length=20)
	age=models.IntegerField()
	gender=models.CharField(max_length=20)
	address=models.CharField(max_length=50)
	mobilenumber=models.CharField(max_length=12)
	wardnumber=models.IntegerField()
# Create your models here.
class test(models.Model):
	name=models.CharField(max_length=20)
	testdate= models.DateField(default = datetime.datetime.now)
	testmode=models.CharField(max_length=20)
	testresult=models.CharField(max_length=20)
	currentstatus=models.CharField(max_length=20)
	symptoms=models.CharField(max_length=20)
class vac(models.Model):
	adharnum=models.CharField(max_length=50)
	name=models.CharField(max_length=50)
	gender=models.CharField(max_length=20)
	dob= models.DateField(default = datetime.datetime.now)




# Create your models here.
