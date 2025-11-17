# 🔑 دليل مفاتيح API والتشغيل

## نظرة عامة
دليل شامل للحصول على مفاتيح API وإعداد جميع أدوات الذكاء الاصطناعي.

---

## 🔐 قائمة مفاتيح API المطلوبة

### 1. Claude Code (Anthropic)

#### كيفية الحصول على المفتاح:
1. **اذهب إلى**: https://console.anthropic.com/
2. **سجل حساب جديد** أو سجل دخول
3. **انتقل إلى**: API Keys section
4. **انقر**: "Create Key"
5. **انسخ المفتاح** واحفظه بأمان

#### الاستخدام:
```bash
# تعيين المفتاح
claude config set-api-key YOUR_API_KEY

# اختبار المفتاح
claude --help

# فحص حالة المفتاح
claude config check-api-key
```

#### التكلفة:
- **نسخة مجانية**: متوفرة
- **مدفوعة**: حسب الاستخدام
- **الحد الأقصى**: 5 API keys مجاناً

---

### 2. GitHub Copilot

#### كيفية الحصول على المفتاح:
1. **سجل دخول GitHub**: https://github.com/
2. **اشترك في Copilot**: https://github.com/features/copilot
3. **في VSCode**: Extensions → GitHub Copilot → Sign in
4. **اتبع التعليمات** للمصادقة

#### الاستخدام في VSCode:
```bash
# فتح VSCode
code my_project

# في VSCode:
# Ctrl+Shift+P → GitHub Copilot: Sign In
# أو: Extensions → GitHub Copilot → Sign In
```

#### التكلفة:
- **فردي**: $10/شهر
- **طلاب**: مجاني (مع إثبات الطالب)
- **شركات**: $19/مستخدم/شهر

---

### 3. Google Gemini

#### كيفية الحصول على المفتاح:
1. **اذهب إلى**: https://makersuite.google.com/app/apikey
2. **سجل دخول Google**
3. **انقر**: "Create API Key"
4. **انسخ المفتاح** واحفظه

#### الاستخدام:
```bash
# تعيين المفتاح
gemini config set-api-key YOUR_API_KEY

# اختبار المفتاح
gemini --help

# مثال على الاستخدام
gemini code generate "create a React login component"
```

#### التكلفة:
- **نسخة مجانية**: 15 طلبات/دقيقة
- **مدفوعة**: حسب الاستخدام
- **الحد الأقصى المجاني**: 60 طلبات/دقيقة

---

### 4. OpenAI API

#### كيفية الحصول على المفتاح:
1. **اذهب إلى**: https://platform.openai.com/api-keys
2. **سجل دخول OpenAI**
3. **انقر**: "Create new secret key"
4. **انسخ المفتاح** واحفظه

#### الاستخدام مع Codex CLI:
```bash
# تعيين المفتاح
export OPENAI_API_KEY=YOUR_API_KEY

# أو في ملف .env
echo "OPENAI_API_KEY=your_key_here" >> .env

# اختبار المفتاح
codex --help
```

#### التكلفة:
- **GPT-3.5**: $0.002/1K tokens
- **GPT-4**: $0.03/1K tokens
- **الحد الأقصى**: حسب حسابك

---

### 5. Windsurf (Codeium)

#### كيفية الحصول على المفتاح:
1. **اذهب إلى**: https://codeium.com/windsurf/
2. **حمّل Windsurf** أو استخدم الويب
3. **سجل حساب مجاني**
4. **انتقل إلى**: Account Settings
5. **انسخ API Key** إذا كان متوفراً

#### الاستخدام:
```bash
# تعيين المفتاح في Windsurf
# عبر واجهة البرنامج:
# Settings → Account → API Key

# أو عبر سطر الأوامر (إذا كان متوفراً)
windsurf config set-api-key YOUR_API_KEY
```

#### التكلفة:
- **نسخة مجانية**: متوفرة
- **Pro**: متوفر بميزات إضافية
- **Enterprise**: للشركات

---

### 6. Cursor Editor

#### كيفية الحصول على المفتاح:
1. **حمّل Cursor**: https://cursor.sh/
2. **ثبت البرنامج**
3. **سجل حساب مجاني**
4. **في Cursor**: Settings → Account
5. **انسخ API Key** إذا كان مطلوباً

#### الاستخدام:
```bash
# إنشاء مشروع جديد
cursor create my-project

# أو فتح مشروع موجود
cursor ./

# في Cursor Editor:
# Ctrl+K: فتح Chat AI
# Ctrl+L: سطر الأوامر AI
```

#### التكلفة:
- **نسخة مجانية**: متوفرة
- **Pro**: $20/شهر
- **Enterprise**: للشركات

---

## 🛠️ إعداد ملفات التكوين

### 1. ملف .env الشامل
```bash
# ملف .env - احفظه في مجلد مشروعك
# احرص على عدم مشاركته في Git

# 🔑 Claude Code
CLAUDE_API_KEY=sk-ant-your_claude_key_here

# 🔑 GitHub Copilot
# (يتم إعداده تلقائياً في VSCode)
# GITHUB_COPILOT_TOKEN=your_token_here

# 🔑 Google Gemini
GEMINI_API_KEY=your_gemini_key_here

# 🔑 OpenAI (للأدوات التي تحتاجها)
OPENAI_API_KEY=sk-your_openai_key_here

# 🔑 Windsurf
WINDSURF_API_KEY=your_windsurf_key_here

# 🔑 Cursor
# (يتم إعداده تلقائياً)
# CURSOR_API_KEY=your_cursor_key_here

# ⚙️ إعدادات عامة
AI_CACHE_ENABLED=true
AI_LOG_LEVEL=info
AI_TIMEOUT=30000
AI_MODEL_DEFAULT=gpt-3.5-turbo
AI_RESPONSE_MAX_TOKENS=4096
```

### 2. إعداد مفاتيح API برمجياً
```bash
#!/bin/bash
# setup_api_keys.sh

echo "🔑 إعداد مفاتيح API..."

# دالة للحصول على إدخال آمن
get_api_key() {
    local service=$1
    local varname=$2

    echo -n "أدخل مفتاح $service (اتركه فارغاً لتخطي): "
    read -s input
    echo ""

    if [ -n "$input" ]; then
        echo "$varname=$input" >> .env
        echo "✅ تم حفظ مفتاح $service"
    else
        echo "⏭️  تم تخطي $service"
    fi
}

# إنشاء ملف .env جديد
cat > .env << 'EOF'
# 🔑 مفاتيح API - تم إنشاؤه تلقائياً
# احرص على عدم مشاركة هذا الملف

EOF

# إعداد المفاتيح
get_api_key "Claude Code" "CLAUDE_API_KEY"
get_api_key "Google Gemini" "GEMINI_API_KEY"
get_api_key "OpenAI" "OPENAI_API_KEY"
get_api_key "Windsurf" "WINDSURF_API_KEY"

# تعيين صلاحيات آمنة
chmod 600 .env

echo ""
echo "✅ تم حفظ المفاتيح في ملف .env"
echo "⚠️  احرص على عدم مشاركة هذا الملف!"
```

### 3. إعداد VSCode للإضافات
```json
// ~/.vscode/settings.json
{
    "github.copilot.inlineSuggest.enable": true,
    "github.copilot.advanced": {
        "listCount": 10,
        "inlineSuggestCount": 3
    },
    "copilot.chat.followups.enabled": true,
    "copilot.chat.codeblock.inlineWrap": true,
    "editor.inlineSuggest.enabled": true,

    // Claude Code Settings (إذا كان متوفراً)
    "claude.apiKey": "${env:CLAUDE_API_KEY}",
    "claude.enableMemory": true,

    // Gemini Settings
    "gemini.apiKey": "${env:GEMINI_API_KEY}",
    "gemini.enableInline": true,

    // إعدادات عامة
    "editor.fontSize": 14,
    "editor.tabSize": 2,
    "editor.insertSpaces": true,
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000
}
```

---

## 🧪 اختبار المفاتيح

### سكريبت اختبار شامل
```bash
#!/bin/bash
# test_api_keys.sh

echo "🧪 اختبار مفاتيح API..."

# اختبار Claude Code
echo ""
echo "🔍 اختبار Claude Code:"
if command -v claude &> /dev/null; then
    claude config check-api-key
else
    echo "❌ Claude Code غير مثبت"
fi

# اختبار GitHub Copilot
echo ""
echo "🔍 اختبار GitHub Copilot:"
if [ -d "$HOME/.vscode" ]; then
    echo "✅ VSCode مثبت"
    # يمكن اختباره عبر VSCode نفسه
else
    echo "❌ VSCode غير مثبت"
fi

# اختبار Gemini CLI
echo ""
echo "🔍 اختبار Gemini CLI:"
if command -v gemini &> /dev/null; then
    gemini --help | head -5
else
    echo "❌ Gemini CLI غير مثبت"
fi

# اختبار Codex CLI
echo ""
echo "🔍 اختبار Codex CLI:"
if command -v codex &> /dev/null; then
    codex --help | head -5
else
    echo "❌ Codex CLI غير مثبت"
fi

# فحص ملف .env
echo ""
echo "🔍 فحص ملف .env:"
if [ -f ".env" ]; then
    echo "✅ ملف .env موجود"
    echo "🔒 صلاحيات الملف: $(ls -l .env | cut -d' ' -f1)"

    # فحص المفاتيح
    if grep -q "CLAUDE_API_KEY=" .env; then
        echo "✅ مفتاح Claude محفوظ"
    else
        echo "❌ مفتاح Claude مفقود"
    fi

    if grep -q "GEMINI_API_KEY=" .env; then
        echo "✅ مفتاح Gemini محفوظ"
    else
        echo "❌ مفتاح Gemini مفقود"
    fi

    if grep -q "OPENAI_API_KEY=" .env; then
        echo "✅ مفتاح OpenAI محفوظ"
    else
        echo "❌ مفتاح OpenAI مفقود"
    fi
else
    echo "❌ ملف .env غير موجود"
fi
```

---

## 🔒 نصائح الأمان

### 1. حماية المفاتيح
```bash
# لا تحفظ المفاتيح في Git
echo ".env" >> .gitignore

# تعيين صلاحيات آمنة
chmod 600 .env

# استخدام متغيرات البيئة
export CLAUDE_API_KEY=$(cat .env | grep CLAUDE_API_KEY | cut -d'=' -f2)
```

### 2. تدوير المفاتيح دورياً
```bash
# تدوير مفتاح (كل 3-6 أشهر)
echo "🔄 تدوير مفاتيح API..."
read -p "هل تريد تدوير مفتاح معين؟ (y/n): " -n 1 -r

# حذف مفتاح قديم
# (من لوحة تحكم الخدمة)

# إنشاء مفتاح جديد
# وحفظه في .env
```

### 3. مراقبة الاستخدام
```bash
# مراقبة استخدام Claude
claude config usage

# مراقبة استخدام GitHub Copilot
# عبر لوحة تحكم GitHub

# مراقبة استخدام Gemini
# عبر Google AI Studio
```

---

## ❌ حل مشاكل المفاتيح

### مشاكل شائعة:

#### 1. "Invalid API Key"
```bash
# تحقق من صحة المفتاح
# تأكد من عدم وجود مسافات أو رموز إضافية
# تحقق من صحة المفتاح في لوحة التحكم
```

#### 2. "Rate Limit Exceeded"
```bash
# انتظر قليلاً قبل المحاولة مرة أخرى
# أو ترقية الخطة للحصول على حدود أعلى
```

#### 3. "Access Denied"
```bash
# تحقق من الصلاحيات في لوحة التحكم
# تأكد من تفعيل الفوترة
# تحقق من انتهاء صلاحية البطاقة الائتمانية
```

### حلول سريعة:
```bash
# إعادة تعيين المفتاح
claude config set-api-key NEW_KEY

# فحص حالة المفتاح
claude config check-api-key

# تحديث الـ npm packages
npm update -g @anthropic-ai/claude-code

# إعادة تثبيت الأدوات
./install_all_tools.sh --force
```

---

## 💰 تقدير التكاليف

### التكاليف الشهرية المتوقعة:

#### للمبتدئين (استخدام قليل):
- **GitHub Copilot**: $10/شهر
- **Claude Code**: $0-10 (حسب الاستخدام)
- **المجموع**: $10-20/شهر

#### للمتوسطين (استخدام متوسط):
- **GitHub Copilot**: $10/شهر
- **Claude Code**: $20-30/شهر
- **OpenAI API**: $15-25/شهر
- **المجموع**: $45-65/شهر

#### للمحترفين (استخدام مكثف):
- **GitHub Copilot Pro**: $10/شهر
- **Claude Code Pro**: $50-100/شهر
- **OpenAI API**: $50-100/شهر
- **Cursor Pro**: $20/شهر
- **المجموع**: $130-230/شهر

### نصائح لتوفير المال:
1. **استخدم الأدوات المجانية أولاً**: Cline, Bolt
2. **راقب استخدامك**: تجنب الإنفاق الزائد
3. **جرب النماذج الأرخص**: GPT-3.5 بدلاً من GPT-4
4. **استفد من العروض**: للطلاب والمؤسسات التعليمية
5. **استخدم API محلية**: عند الإمكان

---

## 📞 الدعم والمساعدة

### عند الحاجة للمساعدة:

#### GitHub Copilot:
- **الوثائق**: https://docs.github.com/en/copilot
- **الدعم**: https://support.github.com/
- **GitHub Discussions**: مجتمع المستخدمين

#### Claude Code:
- **الوثائق**: https://docs.anthropic.com/en/docs/claude-code
- **GitHub**: https://github.com/anthropics/claude-code
- **Discord**: مجتمع Anthropic

#### OpenAI:
- **الوثائق**: https://platform.openai.com/docs
- **Community**: https://community.openai.com/
- **Support**: عبر لوحة التحكم

#### Gemini:
- **الوثائق**: https://ai.google.dev/
- **Google AI Studio**: https://makersuite.google.com/
- **Community**: منتديات Google AI

---

## 🎯 خلاصة المفاتيح

### الأولوية للبدء:
1. **GitHub Copilot** - الأهم للمبتدئين
2. **Claude Code** - قوي ومرن
3. **Gemini** - مجاني وسهل
4. **OpenAI** - للخيارات المتقدمة

### الترتيب الأمثل:
1. **اشترك في GitHub Copilot** ($10/شهر)
2. **احصل على مفتاح Claude** (مجاني/مدفوع)
3. **جرب Gemini** (مجاني)
4. **أضف OpenAI** حسب الحاجة

### نصيحة أخيرة:
ابدأ بالأساسيات (GitHub Copilot + Claude Code) ثم أضف أدوات أخرى حسب احتياجك وميزانيتك.

---

**🚀 احفظ هذا الدليل للمراجعة المستقبلية!**
