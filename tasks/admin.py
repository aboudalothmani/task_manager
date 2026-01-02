from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """تسجيل نموذج Task في لوحة الإدارة مع عرض الحقول المهمة."""
    list_display = ("title", "icon_preview", "icon", "user", "completed", "created_at")
    list_filter = ("completed", "created_at")
    search_fields = ("title", "description", "user__username")

    def icon_preview(self, obj):
        if obj.icon_image:
            from django.utils.html import format_html
            return format_html('<img src="{}" style="width:36px;height:36px;border-radius:6px;object-fit:cover;" />', obj.icon_image.url)
        return obj.icon

    icon_preview.short_description = "أيقونة"
