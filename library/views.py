from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, StrTagValue, StaticTag, IntTagValues, StrTagThrough
from django.http import HttpResponseBadRequest
from django.views import generic


# Create your views here.

class AllItemsView(generic.ListView):
    template_name = 'library/item_list_view.html'
    context_object_name = 'items_list'
    model = Item
    paginate_by = 20


class AllItemsByStrTag(generic.ListView):
    template_name = 'library/item_list_view.html'
    context_object_name = 'items_list'
    model = Item

    def get_queryset(self):
        self.tag = get_object_or_404(StrTagThrough, pk=self.kwargs['pk'])
        return Item.objects.filter(strtags__tag=self.tag.tag, strtags__value=self.tag.value).order_by('item_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "All items with the tag {0}".format(str(self.tag))
        return context



class ItemDetailView(generic.DetailView):
    model = Item
    template_name = 'library/item_detail_view.html'


def item_detail(request, item_id=None, slug=None):
    if item_id is not None:
        item = get_object_or_404(Item, pk=item_id)
        return redirect(item)
    elif slug is not None:
        item = get_object_or_404(Item, item_slug=slug)
    else:
        return HttpResponseBadRequest("Invalid request")
    return render(request, 'library/item_detail_view.html', {'item': item})


def item_list(request, page=1, qs=None):
    # Shows a list of all items, sorted alphabetically, in pages of 10
    # 0-9, 10-19, etc.
    if not qs:
        qs = Item.objects.all()
    items_list = qs.order_by('item_name')[(page-1)*10:(page*10)-1]
    return render(request, 'library/item_list_view.html', {'items_list': items_list})
