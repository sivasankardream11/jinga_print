from django.shortcuts import render

# Create your views here.
def user(request):
    d={'name':"raju"}
    return render(request,'user.html',context=d)
