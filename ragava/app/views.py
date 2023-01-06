from django.shortcuts import render

# Create your views here.
def bro(request):
    
 d={'a':(1,2,3),'b':(4,5,6)}
    return render(request,'bro.html',d)
    