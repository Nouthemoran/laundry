
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm



def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customer_list.html', {'customers': customers})

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer:read')
    else:
        form = CustomerForm()
    return render(request, 'customer/create_customer.html', {'form': form})

def update_customer(request, id_cust):
    customer = get_object_or_404(Customer, id_cust=id_cust)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer:read')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer/update_customer.html', {'form': form})

def delete_customer(request, id_cust):
    customer = get_object_or_404(Customer, id_cust=id_cust)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer:read')  # Menggunakan nama rute 'customer:customer_list'
    return render(request, 'customer/delete_customer.html', {'customer': customer})
