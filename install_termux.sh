#!/bin/bash

# 📱 سكريبت التثبيت المحسن لـ Termux (Android)
# Termux-Optimized AI Tools Installation Script

set -e

# الألوان
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'

# إعدادات
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="$SCRIPT_DIR/install_termux_log_$(date +%Y%m%d_%H%M%S).log"

print_color() {
    echo -e "${2}${1}${NC}"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# فحص متطلبات Termux
check_termux_requirements() {
    print_color "🔍 فحص متطلبات Termux..." "$BLUE"

    # تحديث الحزم
    print_color "📦 تحديث حزم Termux..." "$YELLOW"
    pkg update -y
    pkg upgrade -y

    # تثبيت الحزم الأساسية
    print_color "📦 تثبيت الحزم الأساسية..." "$YELLOW"
    pkg install -y nodejs python git curl wget unzip tree

    # فحص Python
    if command_exists python; then
        PYTHON_VERSION=$(python --version)
        print_color "✅ Python: $PYTHON_VERSION" "$GREEN"
    else
        print_color "❌ Python غير متوفر" "$RED"
    fi

    # فحص Node.js
    if command_exists node; then
        NODE_VERSION=$(node --version)
        print_color "✅ Node.js: $NODE_VERSION" "$GREEN"
    else
        print_color "❌ Node.js غير متوفر" "$RED"
    fi

    # فحص npm
    if command_exists npm; then
        NPM_VERSION=$(npm --version)
        print_color "✅ npm: $NPM_VERSION" "$GREEN"
    else
        print_color "❌ npm غير متوفر" "$RED"
    fi
}

# تثبيت الأدوات المتوافقة مع Termux
install_termux_compatible_tools() {
    print_color "🤖 تثبيت الأدوات المتوافقة مع Termux..." "$BLUE"

    # تثبيت Claude Code إذا كان متوفراً
    if command_exists npm; then
        print_color "📦 محاولة تثبيت Claude Code..." "$YELLOW"
        if npm list -g @anthropic-ai/claude-code >/dev/null 2>&1; then
            print_color "✅ Claude Code مثبت بالفعل" "$GREEN"
        else
            npm install -g @anthropic-ai/claude-code 2>/dev/null && print_color "✅ تم تثبيت Claude Code" "$GREEN" || print_color "⚠️  فشل تثبيت Claude Code (قد يحتاج إعداد خاص)" "$YELLOW"
        fi
    fi

    # تثبيت Gemini CLI
    if command_exists npm; then
        print_color "📦 تثبيت Gemini CLI..." "$YELLOW"
        if npm list -g @google/generative-ai-cli >/dev/null 2>&1; then
            print_color "✅ Gemini CLI مثبت بالفعل" "$GREEN"
        else
            npm install -g @google/generative-ai-cli 2>/dev/null && print_color "✅ تم تثبيت Gemini CLI" "$GREEN" || print_color "⚠️  فشل تثبيت Gemini CLI" "$YELLOW"
        fi
    fi

    # تثبيت حزم Python المفيدة لـ AI
    print_color "🐍 تثبيت حزم Python للذكاء الاصطناعي..." "$YELLOW"
    pip install --upgrade pip

    # تثبيت حزم AI مفيدة
    AI_PACKAGES=(
        "openai"
        "anthropic"
        "google-generativeai"
        "requests"
        "python-dotenv"
        "rich"
        "click"
        "typer"
    )

    for package in "${AI_PACKAGES[@]}"; do
        if pip show "$package" >/dev/null 2>&1; then
            print_color "✅ $package مثبت بالفعل" "$GREEN"
        else
            print_color "📦 تثبيت $package..." "$YELLOW"
            pip install "$package" 2>/dev/null && print_color "✅ تم تثبيت $package" "$GREEN" || print_color "❌ فشل في تثبيت $package" "$RED"
        fi
    done

    # إنشاء سكريبت Python للمساعدة
    create_python_ai_helper
}

# إنشاء مساعد Python للذكاء الاصطناعي
create_python_ai_helper() {
    print_color "📜 إنشاء مساعد Python للذكاء الاصطناعي..." "$CYAN"

    cat > "$SCRIPT_DIR/ai_helper.py" << 'EOF'
#!/usr/bin/env python3
"""
🤖 مساعد Python للذكاء الاصطناعي في Termux
AI Helper for Termux
"""

import os
import sys
import json
import subprocess
from pathlib import Path

class AIAgentHelper:
    def __init__(self):
        self.tools = {}
        self.check_tools()

    def check_tools(self):
        """فحص الأدوات المتاحة"""
        print("🔍 فحص أدوات الذكاء الاصطناعي المتاحة...")
        print("=" * 50)

        # فحص Python packages
        python_packages = [
            "openai", "anthropic", "google.generativeai",
            "requests", "python-dotenv", "rich"
        ]

        for package in python_packages:
            try:
                __import__(package)
                print(f"✅ {package}: متوفر")
                self.tools[package] = True
            except ImportError:
                print(f"❌ {package}: غير متوفر")
                self.tools[package] = False

        # فحص أوامر CLI
        cli_tools = ["node", "npm", "git", "curl", "wget"]
        for tool in cli_tools:
            try:
                subprocess.run([tool, "--version"], capture_output=True, check=True)
                print(f"✅ {tool}: متوفر")
                self.tools[tool] = True
            except (subprocess.CalledProcessError, FileNotFoundError):
                print(f"❌ {tool}: غير متوفر")
                self.tools[tool] = False

    def test_openai_api(self, api_key=None):
        """اختبار OpenAI API"""
        if not self.tools.get("openai", False):
            print("❌ OpenAI package غير مثبت")
            return False

        if not api_key:
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                print("⚠️  مفتاح OpenAI API غير محدد")
                print("   صمه في OPENAI_API_KEY أو مرره كمعامل")
                return False

        try:
            import openai
            openai.api_key = api_key

            # اختبار بسيط
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "Hello"}],
                max_tokens=5
            )
            print("✅ OpenAI API: يعمل بشكل صحيح")
            return True
        except Exception as e:
            print(f"❌ OpenAI API: خطأ - {e}")
            return False

    def test_anthropic_api(self, api_key=None):
        """اختبار Anthropic API"""
        if not self.tools.get("anthropic", False):
            print("❌ Anthropic package غير مثبت")
            return False

        if not api_key:
            api_key = os.getenv("ANTHROPIC_API_KEY")
            if not api_key:
                print("⚠️  مفتاح Anthropic API غير محدد")
                print("   صمه في ANTHROPIC_API_KEY أو مرره كمعامل")
                return False

        try:
            import anthropic
            client = anthropic.Anthropic(api_key=api_key)

            # اختبار بسيط
            response = client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=5,
                messages=[{"role": "user", "content": "Hello"}]
            )
            print("✅ Anthropic API: يعمل بشكل صحيح")
            return True
        except Exception as e:
            print(f"❌ Anthropic API: خطأ - {e}")
            return False

    def test_gemini_api(self, api_key=None):
        """اختبار Gemini API"""
        if not self.tools.get("google.generativeai", False):
            print("❌ Google Generative AI package غير مثبت")
            return False

        if not api_key:
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                print("⚠️  مفتاح Gemini API غير محدد")
                print("   صمه في GEMINI_API_KEY أو مرره كمعامل")
                return False

        try:
            import google.generativeai as genai
            genai.configure(api_key=api_key)

            # اختبار بسيط
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content("Hello")
            print("✅ Gemini API: يعمل بشكل صحيح")
            return True
        except Exception as e:
            print(f"❌ Gemini API: خطأ - {e}")
            return False

    def create_env_template(self):
        """إنشاء قالب ملف .env"""
        env_template = """# 🔑 قالب البيئة لـ Termux
# Environment Template for Termux

# OpenAI API
OPENAI_API_KEY=your_openai_api_key_here

# Anthropic (Claude) API
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Google Gemini API
GEMINI_API_KEY=your_gemini_api_key_here

# إعدادات عامة
AI_MODEL_DEFAULT=gpt-3.5-turbo
AI_MAX_TOKENS=2048
AI_TEMPERATURE=0.7
AI_TIMEOUT=30

# إعدادات Termux
TERMUX_HOME=$HOME
TERMUX_PREFIX=$PREFIX
"""

        with open(".env.template", "w") as f:
            f.write(env_template)
        print("✅ تم إنشاء .env.template")

    def interactive_test(self):
        """اختبار تفاعلي"""
        print("\n🧪 اختبار تفاعلي لـ APIs")
        print("=" * 50)

        # إنشاء .env template
        self.create_env_template()

        # اختبار APIs
        self.test_openai_api()
        print()
        self.test_anthropic_api()
        print()
        self.test_gemini_api()

        print("\n💡 نصائح:")
        print("1. احصل على API keys من:")
        print("   - OpenAI: https://platform.openai.com/api-keys")
        print("   - Anthropic: https://console.anthropic.com/")
        print("   - Gemini: https://makersuite.google.com/app/apikey")
        print()
        print("2. احفظ مفاتيح API في ملف .env")
        print("3._source .env لتطبيق الإعدادات")

def main():
    helper = AIAgentHelper()
    helper.interactive_test()

if __name__ == "__main__":
    main()
EOF

    chmod +x "$SCRIPT_DIR/ai_helper.py"
    print_color "✅ تم إنشاء ai_helper.py" "$GREEN"
}

# إعداد ملفات التكوين لـ Termux
setup_termux_config() {
    print_color "⚙️  إعداد ملفات التكوين لـ Termux..." "$BLUE"

    # إنشاء مجلد التكوين
    mkdir -p "$SCRIPT_DIR/config"
    mkdir -p "$SCRIPT_DIR/data"
    mkdir -p "$SCRIPT_DIR/logs"

    # إنشاء ملف البيئة
    cat > "$SCRIPT_DIR/.env" << 'EOF'
# 🔑 ملف بيئة Termux - AI Tools
# Termux Environment File - AI Tools

# OpenAI API
OPENAI_API_KEY=your_openai_api_key_here

# Anthropic (Claude) API
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Google Gemini API
GEMINI_API_KEY=your_gemini_api_key_here

# إعدادات عامة
AI_MODEL_DEFAULT=gpt-3.5-turbo
AI_MAX_TOKENS=2048
AI_TEMPERATURE=0.7
AI_TIMEOUT=30

# إعدادات Termux
TERMUX_HOME=$HOME
TERMUX_PREFIX=$PREFIX
AI_CACHE_DIR=$HOME/.ai-cache
AI_DATA_DIR=$HOME/.ai-data
EOF

    # إعداد .gitignore
    cat > "$SCRIPT_DIR/.gitignore" << 'EOF'
# Termux AI Tools .gitignore

# ملفات البيئة
.env
.env.local
*.key
*.pem

# مجلدات البيانات
.ai-cache/
.ai-data/
logs/
node_modules/

# ملفات النظام
.DS_Store
Thumbs.db
*.tmp
*.temp

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.egg-info/
dist/
build/
EOF

    print_color "✅ تم إعداد ملفات التكوين" "$GREEN"
}

# إنشاء سكريبتات مساعدة لـ Termux
create_termux_scripts() {
    print_color "📜 إنشاء سكريبتات مساعدة لـ Termux..." "$CYAN"

    # سكريبت الاختبار السريع
    cat > "$SCRIPT_DIR/test_termux_ai.sh" << 'EOF'
#!/bin/bash

echo "🧪 اختبار أدوات الذكاء الاصطناعي في Termux..."
echo "==============================================="

# فحص الأدوات المثبتة
echo "📦 الأدوات المثبتة:"
command -v python3 >/dev/null && echo "✅ Python3" || echo "❌ Python3"
command -v node >/dev/null && echo "✅ Node.js" || echo "❌ Node.js"
command -v npm >/dev/null && echo "✅ npm" || echo "❌ npm"
command -v git >/dev/null && echo "✅ Git" || echo "❌ Git"

# فحص حزم Python
echo ""
echo "🐍 حزم Python:"
python3 -c "import openai" 2>/dev/null && echo "✅ OpenAI" || echo "❌ OpenAI"
python3 -c "import anthropic" 2>/dev/null && echo "✅ Anthropic" || echo "❌ Anthropic"
python3 -c "import google.generativeai" 2>/dev/null && echo "✅ Gemini" || echo "❌ Gemini"

# تشغيل مساعد Python
echo ""
echo "🤖 تشغيل مساعد Python..."
python3 ai_helper.py
EOF

    chmod +x "$SCRIPT_DIR/test_termux_ai.sh"

    # سكريبت إعداد API keys
    cat > "$SCRIPT_DIR/setup_api_keys_termux.sh" << 'EOF'
#!/bin/bash

echo "🔑 إعداد مفاتيح API في Termux..."

# إنشاء أو تحديث ملف .env
if [ ! -f ".env" ]; then
    cp config/.env.template .env
    echo "✅ تم إنشاء ملف .env من القالب"
else
    echo "📝 ملف .env موجود بالفعل"
fi

# تحرير ملف .env
echo "📝 فتح ملف .env للتحرير..."
echo "   أضف مفاتيح API الحقيقية:"
echo "   - OpenAI: https://platform.openai.com/api-keys"
echo "   - Anthropic: https://console.anthropic.com/"
echo "   - Gemini: https://makersuite.google.com/app/apikey"

# اختيار محرر
if command -v nano >/dev/null; then
    nano .env
elif command -v vim >/dev/null; then
    vim .env
else
    echo "لم يتم العثور على محرر. استخدم: nano .env أو vim .env"
fi

echo "✅ تم إعداد ملف .env"
echo "💡 تذكر: source .env لتطبيق الإعدادات"
EOF

    chmod +x "$SCRIPT_DIR/setup_api_keys_termux.sh"

    print_color "✅ تم إنشاء سكريبتات Termux المساعدة" "$GREEN"
}

# إنشاء دليل البدء السريع لـ Termux
create_termux_guide() {
    print_color "📚 إنشاء دليل البدء السريع لـ Termux..." "$CYAN"

    cat > "$SCRIPT_DIR/TERMUX_QUICK_START.md" << 'EOF'
# 📱 دليل البدء السريع - أدوات الذكاء الاصطناعي في Termux

## نظرة عامة
هذا الدليل مخصص لاستخدام أدوات الذكاء الاصطناعي في بيئة Termux على Android.

---

## ⚡ البدء السريع

### 1. تشغيل التثبيت
```bash
# تشغيل التثبيت المحسن لـ Termux
./install_termux.sh
```

### 2. إعداد مفاتيح API
```bash
# إعداد مفاتيح API
./setup_api_keys_termux.sh

# أو تحرير الملف يدوياً
nano .env
```

### 3. اختبار النظام
```bash
# اختبار شامل
./test_termux_ai.sh

# أو استخدام مساعد Python
python3 ai_helper.py
```

---

## 🛠️ الأدوات المتوافقة مع Termux

### Python Packages:
- **openai** - OpenAI API
- **anthropic** - Anthropic (Claude) API
- **google.generativeai** - Google Gemini API
- **requests** - HTTP requests
- **python-dotenv** - إدارة متغيرات البيئة
- **rich** - عرض جميل في Terminal

### Node.js Packages (إذا كان متوفراً):
- **@anthropic-ai/claude-code** - Claude Code CLI
- **@google/generative-ai-cli** - Gemini CLI

---

## 🔑 إعداد مفاتيح API

### OpenAI:
1. اذهب إلى: https://platform.openai.com/api-keys
2. أنشئ مفتاح API جديد
3. احفظ المفتاح في ملف .env

### Anthropic (Claude):
1. اذهب إلى: https://console.anthropic.com/
2. أنشئ حساب جديد أو سجل دخول
3. أنشئ API key
4. احفظ المفتاح في ملف .env

### Google Gemini:
1. اذهب إلى: https://makersuite.google.com/app/apikey
2. سجل دخول Google
3. أنشئ API key
4. احفظ المفتاح في ملف .env

---

## 💻 الاستخدام اليومي

### تحميل ملف البيئة:
```bash
source .env
```

### اختبار APIs:
```bash
python3 ai_helper.py
```

### استخدام OpenAI في Python:
```python
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
```

### استخدام Anthropic في Python:
```python
import anthropic
import os

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=100,
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.content[0].text)
```

### استخدام Gemini في Python:
```python
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Hello!")
print(response.text)
```

---

## 📱 نصائح لاستخدام Termux

### 1. إدارة الحزم
```bash
# تحديث الحزم
pkg update && pkg upgrade

# البحث عن حزم
pkg search python

# تثبيت حزم إضافية
pkg install python-dev
```

### 2. حفظ الإعدادات
```bash
# إنشاء نسخة احتياطية من .env
cp .env ~/.termux/.env_backup

# حفظ قائمة الحزم المثبتة
pkg list-installed > installed_packages.txt
```

### 3. تحسين الأداء
```bash
# تنظيف cache
pkg autoclean
pkg autoremove

# فحص مساحة التخزين
df -h $HOME
```

---

## 🚨 حل المشاكل الشائعة

### مشكلة: "Permission denied"
```bash
# إعطاء صلاحيات التنفيذ
chmod +x *.sh
```

### مشكلة: "Package not found"
```bash
# تحديث مصادر الحزم
pkg update

# البحث عن بدائل
pkg search python
```

### مشكلة: "API key invalid"
```bash
# فحص ملف .env
cat .env

# تحميل المتغيرات
source .env

# اختبار المفتاح
python3 ai_helper.py
```

### مشكلة: "Import error"
```bash
# إعادة تثبيت الحزمة
pip install --upgrade package_name

# فحص Python path
python3 -c "import sys; print(sys.path)"
```

---

## 🎯 مثال عملي: بوت بسيط

```python
#!/usr/bin/env python3
# simple_ai_bot.py

import os
import sys
import openai

def get_response(prompt, api_key=None):
    """الحصول على رد من OpenAI"""
    if not api_key:
        api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return "خطأ: مفتاح API غير محدد"

    try:
        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"خطأ: {e}"

def main():
    print("🤖 بوت الذكاء الاصطناعي البسيط")
    print("اكتب 'exit' للخروج")
    print("=" * 40)

    while True:
        user_input = input("أنت: ").strip()

        if user_input.lower() in ['exit', 'quit', 'خروج']:
            print("وداعاً!")
            break

        if not user_input:
            continue

        print("🤖 Bot: ", end="")
        response = get_response(user_input)
        print(response)
        print()

if __name__ == "__main__":
    main()
```

---

## 📞 الدعم والمساعدة

### موارد مفيدة:
- **Termux Wiki**: https://wiki.termux.com/
- **OpenAI Docs**: https://platform.openai.com/docs
- **Anthropic Docs**: https://docs.anthropic.com/
- **Gemini Docs**: https://ai.google.dev/

### للمساعدة:
1. راجع ملف `test_termux_ai.sh` للفحص الشامل
2. استخدم `python3 ai_helper.py` للاختبار التفاعلي
3. راجع ملفات السجل للتفاصيل

---

## 🎉 خلاصة

مع Termux، يمكنك استخدام أدوات الذكاء الاصطناعي القوية على هاتفك Android!

### الخطوات التالية:
1. **حصل على API keys** من الخدمات المختلفة
2. **اختبر الاتصال** باستخدام ai_helper.py
3. **ابدأ في البرمجة** مع Python وAI APIs
4. **طور تطبيقاتك** الخاصة

**🚀 استمتع بالبرمجة مع AI في Termux!**
EOF

    print_color "✅ تم إنشاء دليل Termux" "$GREEN"
}

# الدالة الرئيسية
main() {
    print_color "📱 بدء التثبيت المحسن لـ Termux" "$PURPLE"
    echo "=============================================="
    echo "📁 مجلد العمل: $SCRIPT_DIR"
    echo "📋 ملف السجل: $LOG_FILE"
    echo "=============================================="
    echo ""

    # فحص النظام
    check_termux_requirements
    echo ""

    # تثبيت الأدوات
    install_termux_compatible_tools
    echo ""

    # إعداد التكوين
    setup_termux_config
    echo ""

    # إنشاء السكريبتات
    create_termux_scripts
    echo ""

    # إنشاء الدليل
    create_termux_guide
    echo ""

    # انتهاء التثبيت
    print_color "🎉 تم الانتهاء من التثبيت لـ Termux!" "$GREEN"
    echo "=============================================="
    echo "📚 اقرأ: TERMUX_QUICK_START.md"
    echo "🧪 اختبر: ./test_termux_ai.sh"
    echo "🔑 إعداد API: ./setup_api_keys_termux.sh"
    echo "🤖 مساعد Python: python3 ai_helper.py"
    echo "=============================================="
}

# معالجة المعاملات
if [[ "$1" == "--help" ]]; then
    echo "📱 سكريبت التثبيت المحسن لـ Termux"
    echo ""
    echo "الاستخدام:"
    echo "  $0              # تثبيت شامل"
    echo "  $0 --help       # عرض هذه المساعدة"
    exit 0
fi

# تشغيل التثبيت
main "$@"
