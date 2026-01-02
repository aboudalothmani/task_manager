# نظام إدارة المهام

مشروع ويب بسيط لبناء نظام إدارة المهام باستخدام Django. المشروع مكتوب باللغة العربية ويتم تنفيذه وفق معمارية MTV.

إرشادات إعداد المشروع (بالعربية):

1. إنشاء بيئة افتراضية وتفعيلها:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. تثبيت المتطلبات:

```powershell
pip install -r requirements.txt
```

3. تطبيق الترحيلات وإنشاء قاعدة البيانات:

```powershell
python manage.py makemigrations
python manage.py migrate
```

4. إنشاء مستخدم مدير (اختياري لإنشاء بيانات أولية):

```powershell
python manage.py createsuperuser
```

5. تشغيل الخادم المحلي:

```powershell
python manage.py runserver
```

بعد التشغيل: افتح المتصفح على `http://127.0.0.1:8000/`، يمكنك التسجيل ثم إدارة مهامك.
