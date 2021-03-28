from django.contrib import admin
from root.models import Gallery, Service, UserInfos, seoLinks, Leads
# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_title', 'service_url']
    readonly_fields = ["service_url", 'Image_preview']

    def thumbnail_preview(self, obj):
        return obj.Image_preview
    thumbnail_preview.allow_tags = True


class UserInfosAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # if there's already an entry, do not allow adding
        count = UserInfos.objects.all().count()
        if count == 0:
            return True

        return False


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'Image_preview', "image_title", "image_description")
    readonly_fields = ('Image_preview', )

    def thumbnail_preview(self, obj):
        return obj.Image_preview
    thumbnail_preview.allow_tags = True


class seoLinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'contentLength', 'url')
    readonly_fields = ('contentLength', )

    def thumbnailWordCounter(self, obj):
        return obj.contentLength
    thumbnailWordCounter.allow_tags = True


class LeadsAdmin(admin.ModelAdmin):
    list_display = ['mail', 'send_date']
    readonly_fields = ('firstName', 'lastName', 'phone',
                       'mail', 'interestedBy', 'message', 'send_date',)


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Leads, LeadsAdmin)
admin.site.register(UserInfos, UserInfosAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(seoLinks, seoLinksAdmin)
