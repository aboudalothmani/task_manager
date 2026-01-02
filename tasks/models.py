from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """نموذج يمثل مهمة مرتبطة بمستخدم.

    الحقول:
    - user: المستخدم الذي تملك المهمة
    - title: عنوان المهمة
    - description: وصف اختياري
    - completed: حالة المهمة (مكتملة/غير مكتملة)
    - created_at: وقت الإنشاء التلقائي
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    # حقل للأيقونة: يسمح بوضع إيموجي أو اسم أيقونة صغير لتمثيل المهمة
    icon = models.CharField(max_length=50, blank=True, default="")
    # حقل لرفع صورة الأيقونة إن رغب المستخدم (الترجيح على الحقل النصي)
    icon_image = models.ImageField(upload_to="task_icons/", blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def duration(self):
        """ترجع مدة زمنية منذ إنشاء المهمة (مفيدة للتقارير)."""
        from django.utils.timezone import now

        return now() - self.created_at

    def __str__(self):
        return self.title
