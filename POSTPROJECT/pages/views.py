from django.shortcuts import render,redirect
from .forms import Student,StudentForm

# Create your views here.

def insertdata(request):
    if request.method == 'POST':

        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/postsubmit')
    else:
        form = StudentForm()
        return render(request,'showform.html',{'form':form})

def mainpage(request):
    frm = StudentForm()
    return render(request,'mainpage.html',{'frm':frm})

def show(request):
    student =Student.objects.all()
    return render(request,'showpost.html',{'student':student})

def mydata(request):
    data = Student.objects.filter(name=request.POST['dropdown'])
    return render(request,'author.html',{'data':data})


