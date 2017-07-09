from django.contrib import admin

from .models import Review, Wine

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('wine', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']


admin.site.register(Wine) #cannot modify Wine from admin
admin.site.register(Review, ReviewAdmin) #can modify Review using ReviewAdmin
