from django.contrib import admin
from .models import ChaiVariety,chaiReview,store,certificate

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = chaiReview
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name','type','date_added')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name','location')
    filter_horizontal = ('chai_varieties',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai','certificate_number')

admin.site.register(ChaiVariety, ChaiVarietyAdmin)
admin.site.register(certificate, ChaiCertificateAdmin)
admin.site.register(store, StoreAdmin)