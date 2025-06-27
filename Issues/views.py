from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def issue_list(request):
    context={"show":Issues.objects.all()
    }
    return render(request,"issue_list.html",context)

def issue_create(request):
    #context={"show":Issues.objects.all()
    #}

    if request.method=="POST":
        form=Issue_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("issues/issue/list/")
    else:
        form=Issue_Form()
    
    return render(request,"issue_form.html",{'form': form})

def issue_update(request,id):
    update_issue=Issues.objects.get(id=id)
    #context={
        #"show":Issues(isinstance=update_issue)
    #}

    if request.method=="POST":
        form=Issue_Form(request.POST,instance=update_issue)
        if form.is_valid():
            form.save()
            return redirect("issues/issue/list/")
    else:
        form=Issue_Form(instance=update_issue)
    context={"form": form}    
    
    return render(request,"issue_form.html",context)
            
    
