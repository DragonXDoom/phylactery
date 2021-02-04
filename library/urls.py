from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views
from dal import autocomplete
from taggit.models import Tag

app_name = 'library'
urlpatterns = [
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='detail-id'),
    path('tag/<int:pk>/', views.AllItemsByTag.as_view(), name='tag-list'),
    path('item/<slug:slug>/', views.item_detail, name='detail-slug'),
    path('test-autocomplete/', views.TagAutocomplete.as_view(), name='select2_taggit'),
    path('item_q/', views.LibraryItemAutocomplete.as_view(), name='item-autocomplete'),
    path('borrow/', views.borrow_view, name='borrow'),
    path('borrow/2/', views.borrow_view_2, name='borrow-2'),
    path('borrow/3/', views.borrow_view_3, name='borrow-3'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('overview/', views.overview_view, name='overview'),
    path('return/<int:pk>/', views.return_item_view, name='return-items'),
    path('', views.AllItemsView.as_view(), name='library-home'),
]
