#!/usr/bin/env python3
"""
🧪 اختبار سريع لأدوات الذكاء الاصطناعي في Termux
Quick AI Tools Test for Termux
"""

import os
import sys
import subprocess
import platform

def print_status(message, status):
    """طباعة رسالة مع حالة"""
    colors = {
        'success': '\033[32m✅',
        'error': '\033[31m❌',
        'warning': '\033[33m⚠️',
        'info': '\033[34m📋',
        'end': '\033[0m'
    }
    print(f"{colors.get(status, '')} {message} {colors['end']}")

def check_system_info():
    """فحص معلومات النظام"""
    print_status("معلومات النظام", "info")
    print("=" * 40)
    print(f"النظام: {platform.system()}")
    print(f"الإصدار: {platform.release()}")
    print(f"المعمارية: {platform.machine()}")
    print(f"Python: {sys.version}")
    print(f"المجلد الرئيسي: {os.environ.get('HOME', 'غير محدد')}")
    print(f"مجلد Termux: {os.environ.get('PREFIX', 'غير محدد')}")
    print()

def check_basic_tools():
    """فحص الأدوات الأساسية"""
    print_status("فحص الأدوات الأساسية", "info")
    print("=" * 40)

    tools = {
        'python': 'python --version',
        'node': 'node --version',
        'npm': 'npm --version',
        'git': 'git --version',
        'curl': 'curl --version',
        'wget': 'wget --version'
    }

    for tool, command in tools.items():
        try:
            result = subprocess.run(
                command.split(),
                capture_output=True,
                text=True,
                timeout=5
            )
            if result.returncode == 0:
                version = result.stdout.split('\n')[0]
                print_status(f"{tool}: {version}", "success")
            else:
                print_status(f"{tool}: لا يعمل", "error")
        except Exception as e:
            print_status(f"{tool}: خطأ - {e}", "error")
    print()

def check_python_packages():
    """فحص حزم Python"""
    print_status("فحص حزم Python", "info")
    print("=" * 40)

    packages_to_check = {
        'requests': 'HTTP requests',
        'urllib': 'URL handling',
        'json': 'JSON processing',
        'subprocess': 'Process management',
        'os': 'Operating system interface',
        'sys': 'System parameters',
        'pathlib': 'Object-oriented filesystem paths'
    }

    for package, description in packages_to_check.items():
        try:
            __import__(package)
            print_status(f"{package}: متوفر ({description})", "success")
        except ImportError:
            print_status(f"{package}: غير متوفر ({description})", "error")

    print()

def create_simple_api_test():
    """إنشاء اختبار API بسيط"""
    print_status("إنشاء اختبار API بسيط", "info")
    print("=" * 40)

    api_test_code = '''#!/usr/bin/env python3
"""
اختبار بسيط لـ APIs في Termux
"""
import os
import sys

def test_environment():
    """فحص متغيرات البيئة"""
    print("🔍 فحص متغيرات البيئة...")

    env_vars = [
        'OPENAI_API_KEY',
        'GEMINI_API_KEY',
        'ANTHROPIC_API_KEY'
    ]

    for var in env_vars:
        value = os.getenv(var)
        if value:
            # إظهار أول 10 أحرف فقط للأمان
            safe_value = value[:10] + "..." if len(value) > 10 else value
            print(f"✅ {var}: {safe_value}")
        else:
            print(f"⚠️  {var}: غير محدد")
    print()

def test_http_connection():
    """اختبار الاتصال بالإنترنت"""
    print("🌐 اختبار الاتصال بالإنترنت...")
    import urllib.request

    try:
        response = urllib.request.urlopen('https://httpbin.org/get', timeout=5)
        if response.getcode() == 200:
            print("✅ الاتصال بالإنترنت: يعمل")
            return True
        else:
            print(f"❌ الاتصال بالإنترنت: خطأ HTTP {response.getcode()}")
            return False
    except Exception as e:
        print(f"❌ الاتصال بالإنترنت: خطأ - {e}")
        return False

def test_openai_api():
    """اختبار OpenAI API"""
    print("🤖 اختبار OpenAI API...")

    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ OPENAI_API_KEY غير محدد")
        return False

    import urllib.request
    import json

    try:
        url = "https://api.openai.com/v1/models"
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req, timeout=10)

        if response.getcode() == 200:
            print("✅ OpenAI API: يعمل بشكل صحيح")
            return True
        else:
            print(f"❌ OpenAI API: خطأ HTTP {response.getcode()}")
            return False
    except Exception as e:
        print(f"❌ OpenAI API: خطأ - {e}")
        return False

def test_gemini_api():
    """اختبار Gemini API"""
    print("🌟 اختبار Gemini API...")

    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("❌ GEMINI_API_KEY غير محدد")
        return False

    import urllib.request

    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req, timeout=10)

        if response.getcode() == 200:
            print("✅ Gemini API: يعمل بشكل صحيح")
            return True
        else:
            print(f"❌ Gemini API: خطأ HTTP {response.getcode()}")
            return False
    except Exception as e:
        print(f"❌ Gemini API: خطأ - {e}")
        return False

def main():
    print("🧪 اختبار شامل لأدوات الذكاء الاصطناعي")
    print("=" * 50)

    test_environment()

    if test_http_connection():
        print()
        test_openai_api()
        test_gemini_api()

    print()
    print("💡 للحصول على API keys:")
    print("   OpenAI: https://platform.openai.com/api-keys")
    print("   Gemini: https://makersuite.google.com/app/apikey")
    print()
    print("📝 لحفظ API key:")
    echo "OPENAI_API_KEY=your_key_here" >> ~/.bashrc
    source ~/.bashrc

if __name__ == "__main__":
    main()
'''

    with open("api_test.py", "w") as f:
        f.write(api_test_code)

    os.chmod("api_test.py", 0o755)
    print_status("تم إنشاء api_test.py", "success")
    print()

def create_simple_ai_client():
    """إنشاء عميل AI بسيط"""
    print_status("إنشاء عميل AI بسيط", "info")
    print("=" * 40)

    ai_client_code = '''#!/usr/bin/env python3
"""
عميل AI بسيط لـ Termux
Simple AI Client for Termux
"""
import os
import sys

class SimpleAI:
    def __init__(self):
        self.openai_key = os.getenv('OPENAI_API_KEY')
        self.gemini_key = os.getenv('GEMINI_API_KEY')

    def chat_openai(self, message):
        """دردشة مع OpenAI"""
        if not self.openai_key:
            return "OpenAI API key غير محدد"

        import urllib.request
        import json

        try:
            url = "https://api.openai.com/v1/chat/completions"
            headers = {
                'Authorization': f'Bearer {self.openai_key}',
                'Content-Type': 'application/json'
            }
            data = {
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": message}],
                "max_tokens": 100
            }

            req = urllib.request.Request(url, json=data, headers=headers)
            response = urllib.request.urlopen(req, timeout=30)
            result = json.loads(response.read().decode())

            return result["choices"][0]["message"]["content"]
        except Exception as e:
            return f"خطأ OpenAI: {e}"

    def chat_gemini(self, message):
        """دردشة مع Gemini"""
        if not self.gemini_key:
            return "Gemini API key غير محدد"

        import urllib.request

        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={self.gemini_key}"
            data = {
                "contents": [{
                    "parts": [{"text": message}]
                }]
            }

            req = urllib.request.Request(url, json=data)
            response = urllib.request.urlopen(req, timeout=30)
            result = json.loads(response.read().decode())

            return result["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            return f"خطأ Gemini: {e}"

def main():
    ai = SimpleAI()

    print("🤖 عميل AI بسيط لـ Termux")
    print("اكتب 'exit' للخروج")
    print("=" * 30)

    while True:
        try:
            user_input = input("أنت: ").strip()

            if user_input.lower() in ['exit', 'quit', 'خروج']:
                print("وداعاً! 👋")
                break

            if not user_input:
                continue

            print("🤖 OpenAI: ", end="")
            response = ai.chat_openai(user_input)
            print(response[:150] + "..." if len(response) > 150 else response)

            print("🌟 Gemini: ", end="")
            response = ai.chat_gemini(user_input)
            print(response[:150] + "..." if len(response) > 150 else response)
            print()

        except KeyboardInterrupt:
            print("\\nوداعاً! 👋")
            break
        except Exception as e:
            print(f"خطأ عام: {e}")

if __name__ == "__main__":
    main()
'''

    with open("simple_ai_client.py", "w") as f:
        f.write(ai_client_code)

    os.chmod("simple_ai_client.py", 0o755)
    print_status("تم إنشاء simple_ai_client.py", "success")
    print()

def create_env_template():
    """إنشاء قالب ملف البيئة"""
    print_status("إنشاء قالب ملف البيئة", "info")
    print("=" * 40)

    env_template = """# 🔑 قالب ملف البيئة لـ Termux AI Tools
# Termux AI Tools Environment Template

# OpenAI API Key
# احصل عليه من: https://platform.openai.com/api-keys
OPENAI_API_KEY=your_openai_api_key_here

# Google Gemini API Key
# احصل عليه من: https://makersuite.google.com/app/apikey
GEMINI_API_KEY=your_gemini_api_key_here

# Anthropic (Claude) API Key
# احصل عليه من: https://console.anthropic.com/
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# إعدادات عامة
AI_MODEL_DEFAULT=gpt-3.5-turbo
AI_MAX_TOKENS=150
AI_TEMPERATURE=0.7
AI_TIMEOUT=30

# Termux specific
TERMUX_HOME=$HOME
TERMUX_PREFIX=$PREFIX
"""

    with open(".env.template", "w") as f:
        f.write(env_template)

    print_status("تم إنشاء .env.template", "success")
    print()

def main():
    """الدالة الرئيسية"""
    print("🚀 اختبار وإعداد أدوات الذكاء الاصطناعي في Termux")
    print("=" * 60)
    print()

    # فحص النظام
    check_system_info()

    # فحص الأدوات
    check_basic_tools()

    # فحص الحزم
    check_python_packages()

    # إنشاء الملفات المساعدة
    create_simple_api_test()
    create_simple_ai_client()
    create_env_template()

    # ملخص نهائي
    print_status("تم الانتهاء من الإعداد!", "success")
    print("=" * 60)
    print()
    print("📋 ما تم إنشاؤه:")
    print("1. api_test.py - اختبار APIs")
    print("2. simple_ai_client.py - عميل AI بسيط")
    print("3. .env.template - قالب ملف البيئة")
    print()
    print("🎯 الخطوات التالية:")
    print("1. احصل على API keys من:")
    print("   - OpenAI: https://platform.openai.com/api-keys")
    print("   - Gemini: https://makersuite.google.com/app/apikey")
    print("   - Anthropic: https://console.anthropic.com/")
    print()
    print("2. أنشئ ملف .env:")
    print("   cp .env.template .env")
    print("   nano .env  # أضف API keys الحقيقية")
    print()
    print("3. اختبر APIs:")
    print("   python3 api_test.py")
    print()
    print("4. ابدأ في الاستخدام:")
    print("   python3 simple_ai_client.py")
    print()
    print("🎉 استمتع بالذكاء الاصطناعي في Termux!")

if __name__ == "__main__":
    main()
