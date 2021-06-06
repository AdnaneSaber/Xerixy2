from django.contrib import admin
from root.models import *
from adminsortable2.admin import SortableAdminMixin
# Register your models here.

admin.site.site_header = 'Xerixy Admin'


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_title', 'service_url', "Image_preview"]
    readonly_fields = ("service_url", 'Image_preview',)

    def thumbnail_preview(self, obj):
        return obj.Image_preview
    thumbnail_preview.allow_tags = True


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'Image_preview', "image_title", "image_description")
    readonly_fields = ('Image_preview', )

    def thumbnail_preview(self, obj):
        return obj.Image_preview
    thumbnail_preview.allow_tags = True


class NewAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'post_url']
    readonly_fields = ["post_url", ]


class UserInfosAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = UserInfo.objects.all().count()
        if count == 0:
            return True

        return False


class GitAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = GitAccount.objects.all().count()
        if count == 0:
            return True

        return False


class MaintenanceAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = Maintenance.objects.all().count()
        if count == 0:
            return True
        return False


class seoLinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'contentLength', 'url')
    readonly_fields = ('contentLength', )
    user = UserInfo.objects.first()
    fieldsets = (
            (None, {
                'fields': ('title','url','content','meta_title','meta_description','contentLength'),
                'description':
                    f"""
                    <h3>{{{{site_name}}}} : {user.nom_sur_site}</h3>
                    <h3>{{{{email}}}} : {user.email}</h3>
                    <h3>{{{{phone}}}} : {user.phone}</h3>
                    <h3>{{{{adresse}}}} : {user.adresse_local}</h3>
                    """
            }),
        )
    def thumbnailWordCounter(self, obj):
        return obj.contentLength
    thumbnailWordCounter.allow_tags = True


class LeadsAdmin(admin.ModelAdmin):
    list_display = ['mail', 'send_date']
    readonly_fields = ('firstName', 'lastName', 'phone',
                       'mail', 'interestedBy', 'message', 'send_date',)


class PageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'page_title', 'page_url']
    readonly_fields = ('page_url',)
    ordering = ['my_order']


class CombinationAdmin(admin.ModelAdmin):
    
    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = Combination.objects.all().count()
        if count == 0:
            return True
        return False
    pass

class PageContentAdmin(admin.ModelAdmin):
    list_filter = ('page', )
    list_display = ['id', 'content_title', 'page']
    ordering = ['id']


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(New, NewAdmin)
admin.site.register(PhoneClick)
admin.site.register(Page, PageAdmin)
admin.site.register(PageContent, PageContentAdmin)
admin.site.register(Lead, LeadsAdmin)
admin.site.register(UserInfo, UserInfosAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(SeoLink, seoLinksAdmin)
admin.site.register(Maintenance, MaintenanceAdmin)
admin.site.register(GitAccount, GitAdmin)
admin.site.register(Combination,CombinationAdmin)