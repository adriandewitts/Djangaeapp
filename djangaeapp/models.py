from django.db import models
from django.contrib import admin

def register():
    admin.site.register(MinimalPair, AuthorAdmin)

class MinimalPair(models.Model):
    word_a = models.CharField(max_length = 32)
    word_b = models.CharField(max_length = 32)
    exclude = models.BooleanField(default = False)
    confirmed = models.BooleanField(default = True)
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)
    client_id = models.CharField(max_length = 40, default = 'admin')

    class Meta:
        db_table = 'MinimalPair'

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('word_a', 'word_b', 'confirmed', 'exclude', 'created_at', 'updated_at')
    fields = ['word_a', 'word_b', 'confirmed', 'exclude', 'client_id', 'created_at', 'updated_at']
    ordering = ['word_a', 'word_b']
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ['word_a', 'word_b']