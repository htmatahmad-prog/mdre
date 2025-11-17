# 🚀 دليل أوامر تشغيل نماذج الذكاء الاصطناعي
# AI Models Usage Commands Guide

## 📋 جدول المحتويات

1. [OpenAI GPT](#1-openai-gpt)
2. [Google Gemini](#2-google-gemini)
3. [Anthropic Claude](#3-anthropic-claude)
4. [Hugging Face](#4-hugging-face)
5. [ElevenLabs TTS](#5-elevenlabs-tts)
6. [Search APIs](#6-search-apis)
7. [واجهة موحدة](#7-واجهة-موحدة)

---

## 1. 🤖 OpenAI GPT

### تشغيل تفاعلي بسيط:
```bash
python3 << 'EOF'
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

print("🤖 OpenAI Chat - اكتب 'exit' للخروج")
while True:
    user_input = input("\n👤 أنت: ")
    if user_input.lower() == 'exit':
        break

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )

    print(f"🤖 GPT: {response.choices[0].message.content}")
EOF
```

---

## 2. 🌟 Google Gemini

### تشغيل تفاعلي:
```bash
python3 << 'EOF'
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

print("🌟 Google Gemini - اكتب 'exit' للخروج")
chat = model.start_chat(history=[])

while True:
    user_input = input("\n👤 أنت: ")
    if user_input.lower() == 'exit':
        break

    response = chat.send_message(user_input)
    print(f"🌟 Gemini: {response.text}")
EOF
```

---

## 3. 🧠 Anthropic Claude

### تشغيل تفاعلي:
```bash
python3 << 'EOF'
from anthropic import Anthropic
import os

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

print("🧠 Claude Chat - اكتب 'exit' للخروج")
conversation = []

while True:
    user_input = input("\n👤 أنت: ")
    if user_input.lower() == 'exit':
        break

    conversation.append({"role": "user", "content": user_input})

    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=conversation
    )

    assistant_message = response.content[0].text
    conversation.append({"role": "assistant", "content": assistant_message})

    print(f"🧠 Claude: {assistant_message}")
EOF
```

---

## 4. 🤗 Hugging Face

### تحليل المشاعر:
```bash
python3 << 'EOF'
from transformers import pipeline

print("🤗 Sentiment Analysis")
classifier = pipeline("sentiment-analysis")

while True:
    text = input("\n📝 أدخل نص (أو 'exit'): ")
    if text.lower() == 'exit':
        break

    result = classifier(text)
    print(f"📊 النتيجة: {result}")
EOF
```

---

## 5. 🔊 ElevenLabs TTS

### تحويل نص لكلام:
```bash
python3 << 'EOF'
from elevenlabs import generate, save
import os

api_key = os.getenv('ELEVENLABS_API_KEY')

while True:
    text = input("\n📝 أدخل النص (أو 'exit'): ")
    if text.lower() == 'exit':
        break

    audio = generate(text=text, voice="Adam", api_key=api_key)
    filename = f"output_{hash(text)}.mp3"
    save(audio, filename)
    print(f"✅ تم الحفظ: {filename}")
EOF
```

---

## 6. 🔍 Search APIs

### Serper + Tavily:
```bash
python3 << 'EOF'
import requests
import os
import json

def serper_search(query):
    url = "https://google.serper.dev/search"
    headers = {
        'X-API-KEY': os.getenv('SERPER_API_KEY'),
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, json={'q': query})
    return response.json()

print("🔍 Search - اكتب 'exit' للخروج")
while True:
    query = input("\n🔎 ابحث عن: ")
    if query.lower() == 'exit':
        break

    results = serper_search(query)
    for item in results.get('organic', [])[:3]:
        print(f"\n📄 {item['title']}")
        print(f"🔗 {item['link']}")
        print(f"📝 {item['snippet'][:100]}...")
EOF
```

---

## 7. 🛠️ واجهة موحدة

### استخدام جميع النماذج معاً:
```bash
python3 << 'EOF'
from openai import OpenAI
import google.generativeai as genai
from anthropic import Anthropic
import os

# تهيئة
openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
gemini = genai.GenerativeModel('gemini-pro')
claude_client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

print("🤖 الواجهة الموحدة")
print("1. GPT  2. Gemini  3. Claude  4. الكل")

while True:
    choice = input("\nاختر (1-4) أو 'exit': ")
    if choice == 'exit':
        break

    msg = input("💬 رسالتك: ")

    if choice in ['1', '4']:
        r = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": msg}]
        )
        print(f"\n🤖 GPT: {r.choices[0].message.content}")

    if choice in ['2', '4']:
        r = gemini.generate_content(msg)
        print(f"\n🌟 Gemini: {r.text}")

    if choice in ['3', '4']:
        r = claude_client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1024,
            messages=[{"role": "user", "content": msg}]
        )
        print(f"\n🧠 Claude: {r.content[0].text}")
EOF
```

---

## 📦 أدوات المشروع الجاهزة

```bash
# تحميل المتغيرات البيئية
source .env

# اختبار شامل
python3 comprehensive_api_test.py

# أداة AI الشاملة
python3 ai_toolkit.py

# عميل بسيط
python3 simple_ai_client.py
```

---

## 🔧 استكشاف الأخطاء

### تحميل API Keys:
```bash
export $(cat .env | xargs)
```

### تثبيت المكتبات:
```bash
pip install openai google-generativeai anthropic transformers elevenlabs tavily-python requests
```

---

**✨ استمتع باستخدام الذكاء الاصطناعي!**
