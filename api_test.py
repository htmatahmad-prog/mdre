#!/usr/bin/env python3
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
    print("   export OPENAI_API_KEY=your_key_here")
    print("   echo 'export OPENAI_API_KEY=your_key_here' >> ~/.bashrc")

if __name__ == "__main__":
    main()
