#!/usr/bin/env python3
"""اختبار سريع لكلا OpenAI و Gemini APIs"""
import os
import urllib.request
import json

def test_openai(message):
    """اختبار OpenAI API"""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        return "OpenAI API key غير محدد"

    try:
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": message}],
            "max_tokens": 80
        }

        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
        response = urllib.request.urlopen(req, timeout=15)
        result = json.loads(response.read().decode())

        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"خطأ OpenAI: {str(e)[:100]}"

def test_gemini(message):
    """اختبار Gemini API"""
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        return "Gemini API key غير محدد"

    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
        data = {
            "contents": [{
                "parts": [{"text": message}]
            }]
        }

        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'))
        response = urllib.request.urlopen(req, timeout=15)
        result = json.loads(response.read().decode())

        return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"خطأ Gemini: {str(e)[:100]}"

def main():
    print("🤖 اختبار كلا من OpenAI و Gemini APIs")
    print("=" * 50)

    message = "مرحبا، اكتب لي جملة ترحيب قصيرة بالعربية"

    print(f"\n📝 الرسالة المرسلة: {message}")
    print("\n" + "=" * 50)

    print("\n🤖 OpenAI Response:")
    print("-" * 50)
    openai_response = test_openai(message)
    print(openai_response)

    print("\n🌟 Gemini Response:")
    print("-" * 50)
    gemini_response = test_gemini(message)
    print(gemini_response)

    print("\n" + "=" * 50)
    print("✅ تم الاختبار بنجاح!")

if __name__ == "__main__":
    main()
