#!/bin/bash

# 📱 سكريبت التثبيت المُصحح لـ Termux
# Fixed Termux Installation Script

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
LOG_FILE="$SCRIPT_DIR/install_fixed_log_$(date +%Y%m%d_%H%M%S).log"

print_color() {
    echo -e "${2}${1}${NC}"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# فحص البيئة الحالية
check_termux_environment() {
    print_color "🔍 فحص بيئة Termux..." "$BLUE"

    echo "🖥️  معلومات النظام:"
    echo "OS: $(uname -o)"
    echo "Kernel: $(uname -r)"
    echo "Architecture: $(uname -m)"
    echo "Home: $HOME"
    echo "Prefix: $PREFIX"
    echo ""

    # فحص Python
    if command_exists python; then
        PYTHON_VERSION=$(python --version)
        PYTHON_PATH=$(which python)
        print_color "✅ Python: $PYTHON_VERSION" "$GREEN"
        print_color "   المسار: $PYTHON_PATH" "$CYAN"
    else
        print_color "❌ Python غير متوفر" "$RED"
    fi

    # فحص Node.js
    if command_exists node; then
        NODE_VERSION=$(node --version)
        NODE_PATH=$(which node)
        print_color "✅ Node.js: $NODE_VERSION" "$GREEN"
        print_color "   المسار: $NODE_PATH" "$CYAN"
    else
        print_color "❌ Node.js غير متوفر" "$RED"
    fi

    # فحص npm
    if command_exists npm; then
        NPM_VERSION=$(npm --version)
        NPM_PATH=$(which npm)
        print_color "✅ npm: $NPM_VERSION" "$GREEN"
        print_color "   المسار: $NPM_PATH" "$CYAN"
    else
        print_color "❌ npm غير متوفر" "$RED"
    fi

    # فحص Git
    if command_exists git; then
        GIT_VERSION=$(git --version)
        print_color "✅ Git: $GIT_VERSION" "$GREEN"
    else
        print_color "❌ Git غير متوفر" "$RED"
    fi
}

# تثبيت حزم Python باستخدام pip محلي
install_python_packages_local() {
    print_color "🐍 تثبيت حزم Python محلياً..." "$BLUE"

    # إنشاء مجلد للمكتبات المحلية
    LOCAL_PYTHON_DIR="$HOME/.local/lib/python3.12/site-packages"
    mkdir -p "$LOCAL_PYTHON_DIR"

    # تحديث pip محلياً
    print_color "📦 تحديث pip..." "$YELLOW"
    python -m ensurepip --upgrade --user 2>/dev/null || true
    python -m pip install --upgrade pip --user 2>/dev/null || true

    # قائمة الحزم الأساسية
    PACKAGES=(
        "requests"
        "python-dotenv"
        "rich"
        "click"
        "typer"
        "urllib3"
        "certifi"
        "charset-normalizer"
        "idna"
    )

    for package in "${PACKAGES[@]}"; do
        if python -c "import $package" 2>/dev/null; then
            print_color "✅ $package مثبت بالفعل" "$GREEN"
        else
            print_color "📦 تثبيت $package..." "$YELLOW"
            if python -m pip install --user "$package" 2>/dev/null; then
                print_color "✅ تم تثبيت $package" "$GREEN"
            else
                print_color "❌ فشل في تثبيت $package" "$RED"
            fi
        fi
    done

    # محاولة تثبيت حزم AI (قد تفشل لكن هذا طبيعي)
    AI_PACKAGES=(
        "openai"
        "anthropic"
        "google-generativeai"
    )

    print_color "🤖 محاولة تثبيت حزم AI..." "$YELLOW"
    for package in "${AI_PACKAGES[@]}"; do
        print_color "📦 محاولة تثبيت $package..." "$YELLOW"
        if python -m pip install --user "$package" 2>/dev/null; then
            print_color "✅ تم تثبيت $package" "$GREEN"
        else
            print_color "⚠️  فشل تثبيت $package (قد تحتاج تثبيت يدوي)" "$YELLOW"
        fi
    done
}

# إنشاء مساعد Python شامل
create_comprehensive_python_helper() {
    print_color "📜 إنشاء مساعد Python شامل..." "$CYAN"

    cat > "$SCRIPT_DIR/termux_ai_helper.py" << 'EOF'
#!/usr/bin/env python3
"""
🤖 مساعد شامل للذكاء الاصطناعي في Termux
Comprehensive AI Helper for Termux
"""

import os
import sys
import json
import subprocess
import platform
from pathlib import Path

class TermuxAIHelper:
    def __init__(self):
        self.tools = {}
        self.python_packages = {}
        self.system_info = self.get_system_info()
        self.check_all_tools()

    def get_system_info(self):
        """الحصول على معلومات النظام"""
        return {
            "platform": platform.system(),
            "python_version": sys.version,
            "home": os.environ.get("HOME", ""),
            "prefix": os.environ.get("PREFIX", ""),
            "termux": os.path.exists("/data/data/com.termux")
        }

    def run_command(self, cmd, timeout=5):
        """تشغيل أمر والتحقق من النتيجة"""
        try:
            result = subprocess.run(
                cmd.split(),
                capture_output=True,
                text=True,
                timeout=timeout
            )
            return {
                "success": result.returncode == 0,
                "stdout": result.stdout.strip(),
                "stderr": result.stderr.strip(),
                "returncode": result.returncode
            }
        except subprocess.TimeoutExpired:
            return {"success": False, "stdout": "", "stderr": "Timeout"}
        except Exception as e:
            return {"success": False, "stdout": "", "stderr": str(e)}

    def check_system_tools(self):
        """فحص أدوات النظام"""
        print("🔧 فحص أدوات النظام:")
        print("=" * 40)

        tools = ["python", "node", "npm", "git", "curl", "wget", "unzip"]
        for tool in tools:
            if self.command_exists(tool):
                version_cmd = f"{tool} --version"
                result = self.run_command(version_cmd)
                if result["success"]:
                    version = result["stdout"].split('\n')[0]
                    print(f"✅ {tool}: {version}")
                    self.tools[tool] = True
                else:
                    print(f"⚠️  {tool}: متوفر لكن لا يعمل")
                    self.tools[tool] = False
            else:
                print(f"❌ {tool}: غير متوفر")
                self.tools[tool] = False

    def command_exists(self, cmd):
        """فحص وجود أمر"""
        return subprocess.run(["which", cmd], capture_output=True).returncode == 0

    def check_python_packages(self):
        """فحص حزم Python"""
        print("\n🐍 فحص حزم Python:")
        print("=" * 40)

        # حزم أساسية
        basic_packages = [
            "sys", "os", "json", "subprocess", "requests",
            "urllib", "http", "datetime", "pathlib"
        ]

        # حزم AI (اختيارية)
        ai_packages = [
            "openai", "anthropic", "google.generativeai",
            "google.generativeai.generative_models"
        ]

        all_packages = basic_packages + ai_packages

        for package in all_packages:
            try:
                __import__(package)
                status = "مثبت ✅"
                self.python_packages[package] = True
            except ImportError:
                if package in ai_packages:
                    status = "غير متوفر (AI package) ⚠️"
                else:
                    status = "غير متوفر ❌"
                self.python_packages[package] = False

            print(f"{package}: {status}")

    def create_simple_api_tester(self):
        """إنشاء مختبئ API بسيط"""
        print("\n🔧 إنشاء مختبئ API بسيط...")

        api_tester = """#!/usr/bin/env python3
import os
import sys
import requests

def test_openai_api(api_key=None):
    if not api_key:
        api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ OpenAI API key غير محدد")
        return False

    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": "Hello"}],
            "max_tokens": 5
        }
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=10
        )
        if response.status_code == 200:
            print("✅ OpenAI API: يعمل بشكل صحيح")
            return True
        else:
            print(f"❌ OpenAI API: خطأ {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ OpenAI API: خطأ - {e}")
        return False

def test_gemini_api(api_key=None):
    if not api_key:
        api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ Gemini API key غير محدد")
        return False

    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
        data = {
            "contents": [{
                "parts": [{"text": "Hello"}]
            }]
        }
        response = requests.post(url, json=data, timeout=10)
        if response.status_code == 200:
            print("✅ Gemini API: يعمل بشكل صحيح")
            return True
        else:
            print(f"❌ Gemini API: خطأ {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Gemini API: خطأ - {e}")
        return False

if __name__ == "__main__":
    print("🧪 اختبار APIs...")
    test_openai_api()
    test_gemini_api()
"""

        with open("api_tester.py", "w") as f:
            f.write(api_tester)

        os.chmod("api_tester.py", 0o755)
        print("✅ تم إنشاء api_tester.py")

    def create_simple_ai_client(self):
        """إنشاء عميل AI بسيط"""
        print("\n🤖 إنشاء عميل AI بسيط...")

        ai_client = """#!/usr/bin/env python3
import os
import requests

class SimpleAIClient:
    def __init__(self):
        self.openai_key = os.getenv("OPENAI_API_KEY")
        self.gemini_key = os.getenv("GEMINI_API_KEY")

    def chat_openai(self, message, model="gpt-3.5-turbo"):
        if not self.openai_key:
            return "OpenAI API key غير محدد"

        try:
            headers = {
                "Authorization": f"Bearer {self.openai_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": model,
                "messages": [{"role": "user", "content": message}],
                "max_tokens": 150
            }
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )

            if response.status_code == 200:
                result = response.json()
                return result["choices"][0]["message"]["content"]
            else:
                return f"خطأ: {response.status_code}"
        except Exception as e:
            return f"خطأ في الاتصال: {e}"

    def chat_gemini(self, message):
        if not self.gemini_key:
            return "Gemini API key غير محدد"

        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={self.gemini_key}"
            data = {
                "contents": [{
                    "parts": [{"text": message}]
                }]
            }
            response = requests.post(url, json=data, timeout=30)

            if response.status_code == 200:
                result = response.json()
                return result["candidates"][0]["content"]["parts"][0]["text"]
            else:
                return f"خطأ: {response.status_code}"
        except Exception as e:
            return f"خطأ في الاتصال: {e}"

def main():
    client = SimpleAIClient()

    print("🤖 عميل AI بسيط")
    print("اكتب 'exit' للخروج")
    print("=" * 30)

    while True:
        user_input = input("أنت: ").strip()

        if user_input.lower() in ['exit', 'quit', 'خروج']:
            print("وداعاً!")
            break

        if not user_input:
            continue

        # جرب OpenAI أولاً
        print("🤖 OpenAI: ", end="")
        response = client.chat_openai(user_input)
        print(response[:100] + "..." if len(response) > 100 else response)

        print("\n🤖 Gemini: ", end="")
        response = client.chat_gemini(user_input)
        print(response[:100] + "..." if len(response) > 100 else response)
        print()

if __name__ == "__main__":
    main()
"""

        with open("simple_ai_client.py", "w") as f:
            f.write(ai_client)

        os.chmod("simple_ai_client.py", 0o755)
        print("✅ تم إنشاء simple_ai_client.py")

    def create_env_template(self):
        """إنشاء قالب ملف البيئة"""
        print("\n📝 إنشاء قالب ملف البيئة...")

        env_template = """# 🔑 ملف بيئة Termux - AI Tools
# Termux Environment File - AI Tools

# OpenAI API
OPENAI_API_KEY=your_openai_api_key_here

# Google Gemini API
GEMINI_API_KEY=your_gemini_api_key_here

# إعدادات عامة
AI_MODEL_DEFAULT=gpt-3.5-turbo
AI_MAX_TOKENS=150
AI_TEMPERATURE=0.7
AI_TIMEOUT=30

# Termux specific
TERMUX_HOME=$HOME
TERMUX_PREFIX=$PREFIX
AI_CACHE_DIR=$HOME/.ai-cache
"""

        with open(".env.template", "w") as f:
            f.write(env_template)

        print("✅ تم إنشاء .env.template")

    def interactive_session(self):
        """جلسة تفاعلية"""
        print("\n🎯 جلسة تفاعلية:")
        print("=" * 50)

        # إنشاء الملفات
        self.create_env_template()
        self.create_simple_api_tester()
        self.create_simple_ai_client()

        print("\n📋 ما تم إنشاؤه:")
        print("1. .env.template - قالب ملف البيئة")
        print("2. api_tester.py - مختبئ APIs")
        print("3. simple_ai_client.py - عميل AI بسيط")

        print("\n📚 الخطوات التالية:")
        print("1. انسخ .env.template إلى .env")
        print("2. أضف مفاتيح API الحقيقية في .env")
        print("3. source .env لتطبيق الإعدادات")
        print("4. python3 api_tester.py لاختبار APIs")
        print("5. python3 simple_ai_client.py للاستخدام")

        print("\n🔗 للحصول على API keys:")
        print("- OpenAI: https://platform.openai.com/api-keys")
        print("- Gemini: https://makersuite.google.com/app/apikey")

    def run_all_checks(self):
        """تشغيل جميع الفحوصات"""
        print("🧪 بدء الفحص الشامل لنظام Termux...")
        print("=" * 60)

        self.check_system_tools()
        self.check_python_packages()
        self.interactive_session()

        print("\n🎉 انتهى الفحص الشامل!")
        print("🚀 ابدأ في استخدام أدوات الذكاء الاصطناعي!")

def main():
    helper = TermuxAIHelper()
    helper.run_all_checks()

if __name__ == "__main__":
    main()
EOF

    chmod +x "$SCRIPT_DIR/termux_ai_helper.py"
    print_color "✅ تم إنشاء termux_ai_helper.py" "$GREEN"
}

# إنشاء سكريبت إعداد سريع
create_quick_setup_script() {
    print_color "📜 إنشاء سكريبت الإعداد السريع..." "$CYAN"

    cat > "$SCRIPT_DIR/quick_setup_termux.sh" << 'EOF'
#!/bin/bash

echo "🚀 إعداد سريع لأدوات الذكاء الاصطناعي في Termux"
echo "=================================================="

# فحص الأدوات الأساسية
echo "🔍 فحص الأدوات الأساسية..."

check_tool() {
    if command -v "$1" >/dev/null 2>&1; then
        echo "✅ $1 متوفر"
        return 0
    else
        echo "❌ $1 غير متوفر"
        return 1
    fi
}

check_tool "python" || echo "   قم بتثبيت python: pkg install python"
check_tool "node" || echo "   قم بتثبيت nodejs: pkg install nodejs"
check_tool "npm" || echo "   npm يجب أن يكون مثبت مع nodejs"
check_tool "git" || echo "   قم بتثبيت git: pkg install git"

# إنشاء مجلد للمشروع
echo ""
echo "📁 إنشاء مجلد المشروع..."
mkdir -p ~/ai-tools-termux
cd ~/ai-tools-termux

# نسخ الملفات من المجلد الحالي
echo "📋 نسخ الملفات..."

# إنشاء ملف البيئة
cat > .env << 'ENVFILE'
# AI Tools Environment Variables
OPENAI_API_KEY=your_openai_key_here
GEMINI_API_KEY=your_gemini_key_here
AI_MODEL_DEFAULT=gpt-3.5-turbo
AI_MAX_TOKENS=150
AI_TIMEOUT=30
ENVFILE

# إنشاء ملف README بسيط
cat > README.md << 'READMEFILE'
# أدوات الذكاء الاصطناعي في Termux

## البدء السريع

1. احصل على API keys من:
   - OpenAI: https://platform.openai.com/api-keys
   - Gemini: https://makersuite.google.com/app/apikey

2. أضف المفاتيح إلى ملف .env

3. اختبر APIs:
   ```bash
   python3 termux_ai_helper.py
   ```

4. استخدم العميل البسيط:
   ```bash
   python3 simple_ai_client.py
   ```

## ملاحظات
- تأكد من وجود اتصال إنترنت
- راجع ملف .env للتأكد من صحة المفاتيح
- استخدم source .env لتطبيق الإعدادات
READMEFILE

echo ""
echo "✅ تم إعداد مجلد المشروع في: ~/ai-tools-termux"
echo ""
echo "🎯 الخطوات التالية:"
echo "1. اذهب إلى المجلد: cd ~/ai-tools-termux"
echo "2. احصل على API keys من المواقع المذكورة"
echo "3. أضف المفاتيح إلى ملف .env"
echo "4. شغل: python3 termux_ai_helper.py"
echo ""
echo "🎉 ابدأ في استخدام AI في Termux!"
EOF

    chmod +x "$SCRIPT_DIR/quick_setup_termux.sh"
    print_color "✅ تم إنشاء quick_setup_termux.sh" "$GREEN"
}

# الدالة الرئيسية
main() {
    print_color "📱 بدء التثبيت المُصحح لـ Termux" "$PURPLE"
    echo "=============================================="
    echo "📁 مجلد العمل: $SCRIPT_DIR"
    echo "=============================================="
    echo ""

    # فحص البيئة
    check_termux_environment
    echo ""

    # تثبيت الحزم
    install_python_packages_local
    echo ""

    # إنشاء المساعدين
    create_comprehensive_python_helper
    echo ""

    # إنشاء سكريبت الإعداد السريع
    create_quick_setup_script
    echo ""

    # تشغيل مساعد Python
    print_color "🧪 تشغيل مساعد Python..." "$BLUE"
    python3 "$SCRIPT_DIR/termux_ai_helper.py"
    echo ""

    # انتهاء التثبيت
    print_color "🎉 تم الانتهاء من التثبيت المُصحح لـ Termux!" "$GREEN"
    echo "=============================================="
    echo "🤖 مساعد Python: python3 termux_ai_helper.py"
    echo "⚡ إعداد سريع: ./quick_setup_termux.sh"
    echo "📚 اقرأ: TERMUX_QUICK_START.md"
    echo "=============================================="
}

# معالجة المعاملات
if [[ "$1" == "--help" ]]; then
    echo "📱 سكريبت التثبيت المُصحح لـ Termux"
    echo ""
    echo "الاستخدام:"
    echo "  $0              # تثبيت شامل"
    echo "  $0 --help       # عرض هذه المساعدة"
    exit 0
fi

# تشغيل التثبيت
main "$@"
