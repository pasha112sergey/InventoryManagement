from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout, login
from .models import Inventory
from django.contrib.auth.decorators import login_required
from .forms import AddInventoryForm, UpdateInventoryForm, RegisterForm



@login_required
def inventory_list(request):
    inventories = Inventory.objects.filter(user=request.user)
    context = {
        "title" : "Inventory List",
        "inventories" : inventories
    }
    return render(request, 'inventory/inventory_list.html', context = context)

@login_required
def custom_logout_view(request):
    logout(request)  # Logs out the user
    return render(request, 'inventory_system/logout.html')  # Renders the logout template

@login_required
def per_product_view(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    context = {
        'inventory' : inventory
    }
    return render(request, "inventory/per_product.html", context=context)

@login_required
def add_product(request):
    if request.method == 'POST':
        add_form = AddInventoryForm(data=request.POST)
        if add_form.is_valid():
            new_inventory = add_form.save(commit=False)
            new_inventory.user = request.user
            new_inventory.sales = float(add_form.data['cost_per_item']) * float(add_form.data['quantity_sold'])
            new_inventory.save()
            return redirect('/inventory/')
    else:
        add_form = AddInventoryForm()
    return render(request, "inventory/inventory_add.html", {"form" : add_form})

@login_required
def delete_inventory(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if inventory.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this item.")
    inventory.delete()
    return redirect('/inventory/')


@login_required
def update_inventory(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        updateForm = UpdateInventoryForm(data=request.POST)
        if updateForm.is_valid():
            inventory.name = updateForm.data['name']
            inventory.quantity_in_stock = updateForm.data['quantity_in_stock']
            inventory.quantity_sold = updateForm.data['quantity_sold']
            inventory.cost_per_item = updateForm.data['cost_per_item']
            inventory.sales = float(inventory.cost_per_item) * float(inventory.quantity_sold)
            inventory.save()
            return redirect(f'/inventory/per_product/{pk}')
    else:
        updateForm = UpdateInventoryForm(instance=inventory)
    context = {"form": updateForm}
    return render(request, "inventory/inventory_update.html", context=context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('inventory_list')  # Redirect to a relevant page
    else:
        form = RegisterForm()
    return render(request, 'inventory/register.html', {'form': form})