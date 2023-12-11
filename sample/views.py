from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import *
from time import *
from sample.forms import *

#for classt views
from sample.models import *
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView




# Create your views here.
def mainpage(request):
    return render(request,'home.html')
def aboutpage(request):
    return render(request,'about.html',{'now':ctime,'name':'kalai','place':'chEnnai'})
def coursepage(request):
    course=["Python","Java","Django","Web Designing"]
    return render(request,'course.html',{'cor':course})
def enquirypage(request):
    fm = EnquiryForm(request.POST or None)
    if fm.is_valid():
        fm.save()
        return HttpResponse("saved successfully")
    return render(request,'enquiry.html',{"myform":fm})
@login_required()
def viewEnquiries(request):
    data = Enquiry.objects.all()
    return render(request,'enquries.html',{'data':data})
@login_required()
def editEnquiry(request,id):
    data=get_object_or_404(Enquiry,pk=id)
    myform=EnquiryForm(request.POST or None, instance=data)
    if myform.is_valid():
        myform.save()
        return redirect('/enquiries/')
    return render(request,'edit.html',{'myform':myform})
@login_required()
def deleteEnquiry(request,id):
    data=get_object_or_404(Enquiry,pk=id)
    if request.method =="POST":
        data.delete()
        return redirect('/enquiries/')
    return render(request,'delete.html',{'data':data})

#classy views:
#Create
class Addstudent(CreateView):
    model = student
    template_name = 'addstudent.html'
    success_url = reverse_lazy('home')
    fields = '__all__'
#Read
class Viewstudent(ListView):
    model = student
    template_name = 'Viewstudent.html'
    context_object_name = 'data'
#update:
class updatestudents(UpdateView):
    model = student
    fields = '__all__'
    template_name = 'update.html'
    success_url = reverse_lazy('view')
    def get_object(self, queryset=None):
        obj=get_object_or_404(student,stdid=self.kwargs['id'])
        return obj

#Delete:
class deletestudent(DeleteView):
    model = student
    fields ='__all__'
    template_name = 'deletestu.html'
    success_url = reverse_lazy('view')
    def get_object(self, queryset=None):
        obj=get_object_or_404(student,pk=self.kwargs['id'])
        return obj
'''
def signuppage(request):
    frm=UserCreationForm(request.POST or None)
    if frm.is_valid():
        frm.save()
        return HttpResponse('User Added')
    return render(request,'singup.html',{'myform':frm})
'''
def signuppage(request):
    frm=signupform(request.POST or None)
    if frm.is_valid():
        frm.save()
        return HttpResponse("User Added")
    return render(request,'singup.html',{'myform':frm})

def staffpage(request):
    return render(request,'staff.html')