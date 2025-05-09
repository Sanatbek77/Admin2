from .models import Product, Category, Store, Contact, Combo
from modeltranslation.translator import TranslationOptions,register


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Store)
class StoreTranslationOptions(TranslationOptions):
    fields = ('store_name', 'descriptions')


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'description')


@register(Combo)
class ComboTranslationOptions(TranslationOptions):
    fields = ('combo_name', 'description')
