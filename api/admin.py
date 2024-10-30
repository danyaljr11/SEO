from django.contrib import admin
from api.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('header_en', 'header_ar')
    fieldsets = (
        ("English Content", {
            'fields': ('header_en', 'summary_en', 'description_en', 'link_title_en')
        }),
        ("Arabic Content", {
            'fields': ('header_ar', 'summary_ar', 'description_ar', 'link_title_ar')
        }),
        ("Other Information", {
            'fields': ('photo', 'link')
        }),
    )


admin.site.register(Article, ArticleAdmin)
