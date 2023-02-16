from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Item
from .forms import NewItemForm

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, inventory__gt=0).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
    })

@login_required
def new(request):
    form=NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Nuevo artículo',
    })