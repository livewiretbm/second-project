from django.db import models


# Create your models here.
class Enquiry(models.Model):
    name=models.CharField(max_length=30,help_text="Name should be within 30 letters",verbose_name="Enter Name:")
    email=models.EmailField(unique=True,help_text="Give correct Email id",verbose_name="Enter Email:")
    phone=models.BigIntegerField(help_text="Phone number should be in 10 digits",verbose_name="Enter Phone number:")
    Address=models.TextField(verbose_name="Current Address:")
    date=models.DateTimeField(auto_now=True)
    courses=models.CharField(max_length=30,default='python',choices=[('Java',"java SE-8"),
                                                                     ('Python','Python3'),
                                                                     ("C","C"),
                                                                     ("C++","C++"),
                                                                     ('Django','Django FrameWork')])
class student(models.Model):
    stdid=models.CharField(max_length=10,unique=True)
    name=models.CharField(max_length=20)
    phone=models.BigIntegerField()
    email=models.EmailField()
    course=models.CharField(max_length=20,
                            choices=[('Java','Java'),
                                     ('Python','Python'),
                                     ('C','C')],default='python')
    fees=models.IntegerField()


