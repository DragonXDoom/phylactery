from django.contrib import admin

# Register your models here.
from .models import Item, BorrowRecord, ExternalBorrowingRecord, ItemBaseTags, ItemComputedTags, TagParent
from .forms import ItemTaggitForm, BaseTagForm, ComputedTagForm


class ItemBaseTagInline(admin.TabularInline):
    model = ItemBaseTags
    form = BaseTagForm


class ItemComputedTagInline(admin.TabularInline):
    model = ItemComputedTags
    form = ComputedTagForm
    readonly_fields = ('computed_tags',)


class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    form = ItemTaggitForm
    inlines = [ItemBaseTagInline, ItemComputedTagInline]

    class Media:
        # These scripts were going to load anyway,
        # but this needs to be here, otherwise
        # they'd load in the wrong order.
        js = [
            'admin/js/jquery.init.js',
            'autocomplete_light/jquery.init.js',
        ]


admin.site.register(Item, ItemAdmin)
admin.site.register(BorrowRecord)
admin.site.register(ExternalBorrowingRecord)
admin.site.register(TagParent)
