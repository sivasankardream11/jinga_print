from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'name':"SANJU"}
    return render(request,'jinja.html',context=d)
