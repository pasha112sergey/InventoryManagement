from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from .models import Inventory
from django.contrib.auth.decorators import login_required

@login_required
def inventory_list(request):
    inventories = Inventory.objects.all()
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
