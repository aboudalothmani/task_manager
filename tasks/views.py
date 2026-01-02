from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse

from .models import Task
from .forms import TaskForm, UserRegisterForm


def signup(request):
    """عرض ومعالجة نموذج تسجيل المستخدم الجديد."""
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # تسجيل دخول المستخدم تلقائيًا بعد التسجيل
            login(request, user)
            messages.success(request, "تم إنشاء الحساب وتسجيل الدخول بنجاح.")
            return redirect("tasks:task_list")
    else:
        form = UserRegisterForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def task_list(request):
    """عرض قائمة مهام المستخدم الحالي فقط."""
    tasks = Task.objects.filter(user=request.user).order_by("-created_at")
    # إحصاءات بسيطة للوحة القيادة
    total = tasks.count()
    completed = tasks.filter(completed=True).count()
    pending = total - completed
    # متوسط المدة منذ الإنشاء (باليوم) — حسبة تقريبية
    from django.utils.timezone import now
    durations = [ (now() - t.created_at).total_seconds() for t in tasks ]
    avg_days = None
    if durations:
        import statistics
        avg_seconds = statistics.mean(durations)
        avg_days = round(avg_seconds / 86400, 2)
    else:
        avg_days = 0

    context = {
        "tasks": tasks,
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": pending,
        "avg_duration_days": avg_days,
    }
    return render(request, "tasks/task_list.html", context)


@login_required
def task_create(request):
    """إنشاء مهمة جديدة وربطها بالمستخدم الحالي."""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("tasks:task_list")
    else:
        form = TaskForm()
    return render(request, "tasks/task_form.html", {"form": form})


@login_required
def task_update(request, pk):
    """تعديل مهمة؛ لا يمكن للمستخدم تعديل مهمة ليست له."""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("tasks:task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/task_form.html", {"form": form, "task": task})


@login_required
def task_delete(request, pk):
    """تأكيد وحذف مهمة للمستخدم الحالي فقط."""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect("tasks:task_list")
    return render(request, "tasks/task_confirm_delete.html", {"task": task})


@login_required
def toggle_complete(request, pk):
    """تبديل حالة إكمال المهمة (مكتملة/غير مكتملة)."""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect("tasks:task_list")
