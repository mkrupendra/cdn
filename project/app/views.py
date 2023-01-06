from django.shortcuts import render

# Create your views here.
def project(request):
    d={'key':'darling'}
    return render(request,'kkk.html',context=d)
