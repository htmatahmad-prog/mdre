#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔑 معالج إعداد API Keys - مرة واحدة فقط!
"""

import json
import os
from pathlib import Path

CONFIG_FILE = Path.home() / "config_keys.json"

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

    # Serper (اختياري)
    print("\n4️⃣  Serper API Key (للبحث - اختياري):")
    serper = input("   أدخل المفتاح (أو Enter للتخطي): ").strip()
    if serper:
        keys['serper'] = serper

    # Tavily (اختياري)
    print("\n5️⃣  Tavily API Key (للبحث - اختياري):")
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

    if not keys or not any(keys.values()):
        print("\n🔍 لم يتم العثور على مفاتيح محفوظة...")
        keys = setup_keys()
    else:
        print("\n✅ تم تحميل المفاتيح المحفوظة!")
        print(f"   OpenAI: {'✓' if keys.get('openai') else '✗'}")
        print(f"   Google: {'✓' if keys.get('google') else '✗'}")
        print(f"   Anthropic: {'✓' if keys.get('anthropic') else '✗'}")

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
