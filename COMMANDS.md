# ⚡ دليل الأوامر السريع

## 🚀 التشغيل

### البدء السريع
```bash
python3 start.py
```

### القائمة التفاعلية
```bash
./menu.sh
```

### فهرس المشروع
```bash
python3 index.py
```

---

## 🧪 الاختبار

### اختبار شامل (يُنصح)
```bash
python3 comprehensive_api_test.py
```

### اختبار سريع OpenAI + Gemini
```bash
python3 test_both_apis.py
```

### اختبار API عام
```bash
python3 api_test.py
```

### اختبار OpenAI فقط
```bash
python3 test_openai_quick.py
```

---

## 💬 الأدوات

### مجموعة الأدوات الكاملة (دردشة + بحث + TTS)
```bash
python3 ai_toolkit.py
```

### عميل AI بسيط
```bash
python3 simple_ai_client.py
```

---

## 📚 التوثيق

### عرض دليل الأدوات (30k+ سطر)
```bash
ls -la system-prompts-and-models-of-ai-tools/
cat system-prompts-and-models-of-ai-tools/README.md
```

### قراءة الدليل الشامل
```bash
cat README.md
```

### دليل البدء السريع
```bash
cat QUICK_START.md
```

---

## ⚙️ الإعدادات

### عرض ملف .env
```bash
cat .env
cat config/.env
```

### تعديل ملف .env
```bash
nano .env
vim .env
```

### إعداد سريع
```bash
bash setup.sh
```

---

## 🔍 فحص النظام

### فحص حالة Python
```bash
python3 --version
pip3 --version
```

### تثبيت الحزم
```bash
pip3 install requests urllib3 python-dotenv
```

### فحص الاتصال
```bash
ping -c 3 google.com
curl -I https://api.openai.com
```

---

## 🎯 مهام سريعة

### 1. اختبار API
```bash
python3 -c "
import os
os.environ['OPENAI_API_KEY'] = 'your-key'
import urllib.request
req = urllib.request.Request('https://api.openai.com/v1/models', headers={'Authorization': 'Bearer ' + os.environ['OPENAI_API_KEY']})
print(urllib.request.urlopen(req).getcode())
"
```

### 2. عرض متغيرات البيئة
```bash
grep -E "(OPENAI|GEMINI|ANTHROPIC)" .env | grep -v "^#"
```

### 3. تشغيل جميع الاختبارات
```bash
for f in test_*.py; do echo "Running $f"; python3 "$f"; echo "---"; done
```

### 4. عرض الملفات الحديثة
```bash
ls -lt *.py *.sh *.md | head -20
```

---

## 🔑 الحصول على مفاتيح API

### OpenAI
```bash
# افتح المتصفح على:
https://platform.openai.com/api-keys

# ثم أضف المفتاح إلى .env:
echo "OPENAI_API_KEY=sk-your-key" >> .env
```

### Google Gemini
```bash
# افتح المتصفح على:
https://makersuite.google.com/app/apikey

# ثم أضف المفتاح:
echo "GEMINI_API_KEY=your-key" >> .env
```

### Anthropic Claude
```bash
# افتح المتصفح على:
https://console.anthropic.com/

# ثم أضف المفتاح:
echo "ANTHROPIC_API_KEY=your-key" >> .env
```

---

## 💡 نصائح سريعة

### نسخ سريع للمفتاح
```bash
# انسخ من .env
grep OPENAI_API_KEY .env

# أو من clipboard
xclip -selection clipboard -o  # Linux
pbpaste  # macOS
```

### إنشاء ملف .env جديد
```bash
cp config/.env .env
nano .env
```

### مراقبة استخدام API
```bash
# عرض ملف السجل
tail -f logs/api_usage.log 2>/dev/null || echo "No logs yet"
```

### اختبار اتصال سريع
```bash
python3 -c "import urllib.request; print('OK' if urllib.request.urlopen('https://google.com').getcode() == 200 else 'Failed')"
```

---

## 🆘 حل المشاكل

### خطأ "Module not found"
```bash
pip3 install --user requests python-dotenv
```

### خطأ "Permission denied"
```bash
chmod +x *.sh
chmod 600 .env
```

### خطأ "API key invalid"
```bash
# تأكد من صحة المفتاح
grep -v "^#" .env | grep "API_KEY"
# ثم تحقق من الموقع
```

### مفاتيح API مفقودة
```bash
# اعرض المفاتيح المفقودة
python3 index.py | grep -A20 "APIs المدعومة"
```

---

## 📊 إحصائيات

### عدد الملفات
```bash
echo "Python files: $(ls *.py 2>/dev/null | wc -l)"
echo "Shell scripts: $(ls *.sh 2>/dev/null | wc -l)"
echo "Docs: $(ls *.md 2>/dev/null | wc -l)"
```

### حجم المشروع
```bash
du -sh .  # حجم المشروع
du -sh system-prompts-and-models-of-ai-tools/  # حجم دليل الأدوات
```

### آخر تعديل
```bash
ls -lt *.py *.sh *.md | head -1
```

---

## 🎬 أمثلة عملية

### مثال 1: اختبار سريع
```bash
# 1. تشغيل
python3 start.py

# 2. اختر 1 (اختبار APIs سريع)
# 3. أو اختر 3 (مقارنة OpenAI + Gemini)
```

### مثال 2: الدردشة مع AI
```bash
# 1. أضف مفاتيح API
nano .env

# 2. شغل الأدوات
python3 ai_toolkit.py

# 3. اختر 1 (دردشة)
# 4. اختر النموذج (1-OpenAI, 2-Gemini, 3-Claude)
# 5. اكتب رسالتك
```

### مثال 3: البحث في الويب
```bash
# 1. أضف مفتاح Serper
echo "SERPER_API_KEY=your-key" >> .env

# 2. شغل الأدوات
python3 ai_toolkit.py

# 3. اختر 2 (البحث)
# 4. اختر 1 (Serper)
# 5. اكتب استعلامك
```

---

## 📞 المساعدة

### عرض المساعدة
```bash
./menu.sh  # ثم اختر 11
```

### عرض الفهرس
```bash
python3 index.py
```

### عرض README
```bash
cat README.md | less
```

### عرض الدليل السريع
```bash
cat QUICK_START.md
```

---

## 🚪 الخروج

للخروج من أي برنامج:
```bash
Ctrl + C
```

للقوائم التفاعلية:
```bash
اختر 0 أو اكتب exit
```

---

**🎯 ابدأ الآن**: `python3 start.py`
