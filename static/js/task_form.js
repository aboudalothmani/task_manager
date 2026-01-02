document.addEventListener('DOMContentLoaded', function () {
  const iconInput = document.querySelector('input[name="icon"]');
  const preview = document.querySelector('.icon-preview');

  if (!iconInput || !preview) return;

  function renderPreview(value) {
    // تنظيف القيمة
    const val = (value || '').trim();
    // إذا كانت قيمة فارغة، عرض أيقونة افتراضية
    if (!val) {
      preview.textContent = '📝';
      preview.className = 'icon-preview';
      return;
    }

    // إذا كانت تبدو كاسم أيقونة من bootstrap-icons (مثال: bi-alarm)
    if (val.startsWith('bi-') || val.startsWith('bi ')) {
      // نظف الفئة وأضف عنصر <i>
      const cls = val.replace(/^bi\s*/, '').replace(/^bi-/, 'bi-');
      preview.innerHTML = '';
      const i = document.createElement('i');
      i.className = 'bi ' + cls;
      i.style.fontSize = '22px';
      preview.appendChild(i);
      preview.classList.add('icon-preview');
      return;
    }

    // افتراضياً نعرض النص كإيموجي/رمز نصي آمن
    preview.textContent = val;
    preview.className = 'icon-preview';
  }

  // تهيئة المعاينة بالقيمة الحالية
  renderPreview(iconInput.value);

  // استمع للتغييرات مع تأخير بسيط
  let timeout = null;
  iconInput.addEventListener('input', function (e) {
    clearTimeout(timeout);
    const v = e.target.value;
    timeout = setTimeout(() => renderPreview(v), 150);
  });

  // دعم معاينة الملف المرفوع
  const fileInput = document.querySelector('input[name="icon_image"]');
  if (fileInput) {
    fileInput.addEventListener('change', function (e) {
      const f = e.target.files && e.target.files[0];
      if (!f) return renderPreview(iconInput.value);
      const reader = new FileReader();
      reader.onload = function (ev) {
        preview.innerHTML = '';
        const img = document.createElement('img');
        img.src = ev.target.result;
        img.style.width = '100%';
        img.style.height = '100%';
        img.style.objectFit = 'cover';
        preview.appendChild(img);
      };
      reader.readAsDataURL(f);
    });
  }

  // Icon picker quick buttons
  const choices = document.querySelectorAll('.icon-choice');
  choices.forEach(btn => {
    btn.addEventListener('click', function () {
      const v = this.getAttribute('data-icon');
      // إذا كانت bi- نضعها في الحقل النصي كاسم أيقونة
      if (v.startsWith('bi-')) {
        iconInput.value = v;
        iconInput.dispatchEvent(new Event('input'));
      } else {
        iconInput.value = v;
        iconInput.dispatchEvent(new Event('input'));
      }
    });
  });
});
