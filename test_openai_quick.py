#!/usr/bin/env python3
"""اختبار سريع لـ OpenAI API"""
import os
import urllib.request
import json

# استخدام مفتاح API من متغيرات البيئة
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    print("❌ OPENAI_API_KEY غير محدد")
    print("قم بتشغيل: export OPENAI_API_KEY='your_key_here'")
    exit(1)

print("🤖 اختبار OpenAI API...")
print("=" * 40)

try:
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": "مرحبا، قل مرحبا بالعربية"}
        ],
        "max_tokens": 50
    }

    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
    response = urllib.request.urlopen(req, timeout=10)
    result = json.loads(response.read().decode())

    print("✅ تم الاتصال بنجاح!")
    print("\n📝 الرد من OpenAI:")
    print("-" * 40)
    print(result["choices"][0]["message"]["content"])
    print("-" * 40)
    print("\n🎉 OpenAI يعمل بشكل ممتاز!")

except Exception as e:
    print(f"❌ خطأ: {e}")
