from django.shortcuts import render

# Create your views here.
def conditional(request):
    d={'a':1001,'b':20}
    return render(request,'conditional.html',context=d)

def ifelse(request):
    d={'a':10,'b':20}
    return render(request,'ifelse.html',context=d)

def ifelif(request):
    d={'a':10,'b':60,'c':30}
    return render(request,'ifelif.html',context=d)

def nestedif(request):
    d={'a':10,'b':60,'c':30}
    return render(request,'nestedif.html',context=d)


def forloop(request):
    d={'name':'Hari'}
    return render(request,'forloop.html',context=d)