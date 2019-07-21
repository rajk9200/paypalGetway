from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import Contacts
# Create your views here.
from django.contrib import messages
def ayu(request):
    return render(request,'1.html')

def add_contact(request):
    form =ContactForm(request.POST or None)
    if form.is_valid():
        mobile =form.cleaned_data.get('phone_no')
        form.save()
        messages.add_message(request, messages.INFO, f'{ mobile} , Conact added.')

        return redirect('show_contact')
    return render(request,'add-contact.html',{'form':form})

def show_contacts(request):
    contacts =Contacts.objects.all()
    return render(request,'show-contacts.html',{'contacts':contacts})

def delete_contact(request,id=None):
    if request.method =='POST':
        con =Contacts.objects.get(id=id)
        con.delete()
        return redirect('show_contact')
    message="are "
    return render(request,'delete.html',{'message':message})


def update_contact(request,id=None):
    con =Contacts.objects.get(id=id)
    form =ContactForm(request.POST or None, instance=con)
    if form.is_valid():
        mobile =form.cleaned_data.get('phone_no')
        form.save()
        messages.add_message(request, messages.INFO, f'{ mobile} , Conact added.')

        return redirect('show_contact')
    return render(request,'add-contact.html',{'form':form})