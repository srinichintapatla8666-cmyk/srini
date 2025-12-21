from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from.forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView   
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers 
import logging
from django.shortcuts import get_object_or_404
from django.utils import timezone

# Create your views here.   

logger = logging.getLogger(__name__)

# @login_required
# @cache_page(60 * 15)
# @vary_on_headers('User-Agent')
def index(request):
    # Geting items from database
    logger.info("Fetching all items from the database")
    logger.info(f"User [{timezone.now().isoformat()}] {request.user} requested item list from {request.META.get('REMOTE_ADDR')}")
    item_list = Item.objects.all()
    logger.debug(f"Found {item_list.count()} items")
    
    # print(item_list)
    paginator = Paginator(item_list, 5)
    # print('paginator', paginator)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)    
    # Creating context
    context = {
        # 'item_list': item_list,
        'page_obj': page_obj
        }
#     # Passing the context object to the render method along with the template
    return render(request, "myapp/index.html", context)

class IndexClassView(ListView):
    model = Item
    template_name = 'myapp/index.html'
    context_object_name = 'item_list'
    

def detail(request, id):

    logger.info(f"Fetching an item with id: {id}")
    try:
        item = get_object_or_404(Item, pk=id)
        logger.debug(f"item found {item.item_name} (${item.item_price})")
    except Exception as e:
        logger.error(f"Error fetching the item %$: $",id,e)
        raise
        # return HttpResponseNotFound(f"Item with id {id} not found")
    context = {
        'item': item
    }
    return render(request, "myapp/detail.html", context)


class FoodDetail(DetailView):
    model = Item
    template_name = 'myapp/detail.html'
    context_object_name = 'item'    



@login_required
def create_item(request):
    form = ItemForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('myapp:index') 
    context = {
        'form': form 
    }
    return render(request, "myapp/item-form.html", context )


class ItemCreateView(CreateView):
    model = Item
    template_name = 'myapp/item-form.html'
    fields = ['item_name','item_desc', 'item_price', 'item_image']
    success_url = '/myapp/'
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)




def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('myapp:index')
    context = {
        'form': form
    }
    return render(request, "myapp/item-form.html",context)


class ItemUpdateView(UpdateView):
    model = Item
    fields = ['item_name','item_desc', 'item_price', 'item_image']
    template_name_suffix = "_update_form"
    success_url = '/myapp/'

    def get_queryset(self):
        return Item.objects.filter(user_name = self.request.user)


def delete_item(request, id):
    item = Item.objects.get(id=id) 
    if request.method == 'POST':
        
        item.delete()
        return redirect('myapp:index')
    return render(request, "myapp/item-delete.html")

# class ItemDeleteView(DeleteView):
#     model = Item
#     success_url = '/myapp/'

class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('myapp:index')

def get_objets(request):
    for item in Item.objects.all():
        print(item.item_name)

def get_objets_optimised(request):  
    items = Item.objects.only('item_name')
    for item in items:
        print(item.item_name) 

