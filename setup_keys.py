#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔑 معالج إعداد API Keys - مرة واحدة فقط!
"""

import json
import os
from pathlib import Path

# مسار ملف حفظ المفاتيح (يمكن تخصيصه عبر متغير البيئة API_KEYS_FILE)
CONFIG_FILE = Path(os.getenv('API_KEYS_FILE', Path.home() / "config_keys.json"))

def load_keys():
    """تحميل المفاتيح المحفوظة"""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_keys(keys):
    """حفظ المفاتيح"""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(keys, f, indent=2)
    os.chmod(CONFIG_FILE, 0o600)  # حماية الملف
    print("\n✅ تم حفظ المفاتيح بنجاح!")

def setup_keys():
    """إعداد المفاتيح لأول مرة"""
    print("\n" + "="*70)
    print("🔑 إعداد API Keys - مرة واحدة فقط!")
    print("="*70)
    print("\nستُحفظ المفاتيح وتُستخدم تلقائياً في المرات القادمة\n")

    keys = {}

    # OpenAI
    print("1️⃣  OpenAI API Key (للـ GPT-4, DALL-E):")
    print("   احصل عليه من: https://platform.openai.com/api-keys")
    openai = input("   أدخل المفتاح (أو Enter للتخطي): ").strip()
    if openai:
        keys['openai'] = openai

    # Google
    print("\n2️⃣  Google API Key (للـ Gemini):")
    print("   احصل عليه من: https://makersuite.google.com/app/apikey")
    google = input("   أدخل المفتاح (أو Enter للتخطي): ").strip()
    if google:
        keys['google'] = google

    # Anthropic
    print("\n3️⃣  Anthropic API Key (للـ Claude):")
    print("   احصل عليه من: https://console.anthropic.com")
    anthropic = input("   أدخل المفتاح (أو Enter للتخطي): ").strip()
    if anthropic:
        keys['anthropic'] = anthropic

    # Groq
    print("\n4️⃣  Groq API Key (للنماذج السريعة):")
    print("   احصل عليه من: https://console.groq.com")
    groq = input("   أدخل المفتاح (أو Enter للتخطي): ").strip()
    if groq:
        keys['groq'] = groq

    # Minimax
    print("\n5️⃣  Minimax API Key (للنماذج المتقدمة):")
    print("   احصل عليه من: https://api.minimax.io")
    minimax = input("   أدخل المفتاح (أو Enter للتخطي): ").strip()
    if minimax:
        keys['minimax'] = minimax
        # Group ID مطلوب لـ Minimax
        group_id = input("   أدخل Minimax Group ID: ").strip()
        if group_id:
            keys['minimax_group_id'] = group_id

    # Cohere
    print("\n6️⃣  Cohere API Key (للمهام التجارية):")
    print("   احصل عليه من: https://dashboard.cohere.ai")
    cohere = input("   أدخل المفتاح (أو Enter للتخطي): ").strip()
    if cohere:
        keys['cohere'] = cohere

    # Serper (اختياري)
    print("\n7️⃣  Serper API Key (للبحث - اختياري):")
    serper = input("   أدخل المفتاح (أو Enter للتخطي): ").strip()
    if serper:
        keys['serper'] = serper

    # Tavily (اختياري)
    print("\n8️⃣  Tavily API Key (للبحث - اختياري):")
    tavily = input("   أدخل المفتاح (أو Enter للتخطي): ").strip()
    if tavily:
        keys['tavily'] = tavily

    if not keys:
        print("\n⚠️  لم يتم إدخال أي مفاتيح!")
        return None

    save_keys(keys)
    return keys

def check_and_setup():
    """فحص وإعداد المفاتيح إذا لزم الأمر"""
    keys = load_keys()

    # التحقق من وجود مفاتيح حقيقية (وليس placeholders)
    valid_keys = {}
    for key, value in keys.items():
        if value and not value.startswith('your_') and value != 'your_' + key + '_api_key_here':
            valid_keys[key] = value

    if not keys or not valid_keys:
        print("\n🔍 لم يتم العثور على مفاتيح محفوظة...")
        keys = setup_keys()
    else:
        print("\n✅ تم تحميل المفاتيح المحفوظة!")
        print(f"   OpenAI: {'✓' if valid_keys.get('openai') else '✗'}")
        print(f"   Google: {'✓' if valid_keys.get('google') else '✗'}")
        print(f"   Anthropic: {'✓' if valid_keys.get('anthropic') else '✗'}")
        print(f"   Groq: {'✓' if valid_keys.get('groq') else '✗'}")
        print(f"   Minimax: {'✓' if valid_keys.get('minimax') else '✗'}")
        print(f"   Cohere: {'✓' if valid_keys.get('cohere') else '✗'}")

    return keys

if __name__ == '__main__':
    keys = check_and_setup()

    if keys:
        print("\n" + "="*70)
        print("🎉 الإعداد مكتمل!")
        print("="*70)
        print("\nيمكنك الآن تشغيل:")
        print("  python3 ai_workspace_pro.py      # للـ Terminal")
        print("  python3 ai_workspace_mobile.py   # للويب/الهاتف")
