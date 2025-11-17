#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🤖 AI Workspace Pro - النسخة المحسّنة
مع المزيد من الميزات والنماذج
"""

import os
import sys
from openai import OpenAI
import google.generativeai as genai
from anthropic import Anthropic
import requests
import json
from pathlib import Path
import base64
from io import BytesIO

class AIWorkspacePro:
    """مساحة عمل AI محسّنة مع ميزات متقدمة"""

    def __init__(self):
        """تهيئة جميع النماذج والميزات"""
        print("🚀 جاري تحميل AI Workspace Pro...")

        self.load_keys()
        self.init_models()
        self.init_search()
        self.init_image_models()
        self.conversation = []
        self.current_model = None

        print("✅ تم التحميل بنجاح!\n")

    def load_keys(self):
        """تحميل مفاتيح API من ملف الإعدادات أو متغيرات البيئة"""
        # محاولة التحميل من ملف الإعدادات أولاً
        config_file = Path.home() / "config_keys.json"
        keys = {}

        if config_file.exists():
            try:
                with open(config_file, 'r') as f:
                    keys = json.load(f)
                print("✅ تم تحميل المفاتيح من الملف المحفوظ")
            except:
                pass

        # استخدام المفاتيح من الملف أو متغيرات البيئة
        self.openai_key = keys.get('openai') or os.getenv('OPENAI_API_KEY')
        self.google_key = keys.get('google') or os.getenv('GOOGLE_API_KEY')
        self.anthropic_key = keys.get('anthropic') or os.getenv('ANTHROPIC_API_KEY')
        self.serper_key = keys.get('serper') or os.getenv('SERPER_API_KEY')
        self.tavily_key = keys.get('tavily') or os.getenv('TAVILY_API_KEY')
        self.elevenlabs_key = os.getenv('ELEVENLABS_API_KEY')
        self.replicate_key = os.getenv('REPLICATE_API_KEY')

        # إذا لم توجد مفاتيح، اعرض رسالة
        if not (self.openai_key or self.google_key or self.anthropic_key):
            print("\n⚠️  تحذير: لم يتم العثور على مفاتيح API!")
            print("   شغّل: python3 setup_keys.py  لإعداد المفاتيح\n")

    def init_models(self):
        """تهيئة جميع النماذج"""
        self.models = {}

        # OpenAI Models
        if self.openai_key:
            self.openai_client = OpenAI(api_key=self.openai_key)
            self.models.update({
                'gpt-4': {'name': 'GPT-4', 'client': 'openai', 'desc': '🧠 الأقوى - للمهام المعقدة'},
                'gpt-4-turbo': {'name': 'GPT-4 Turbo', 'client': 'openai', 'desc': '⚡ سريع وقوي'},
                'gpt-4o': {'name': 'GPT-4o', 'client': 'openai', 'desc': '🎯 الأحدث من OpenAI'},
                'gpt-3.5-turbo': {'name': 'GPT-3.5 Turbo', 'client': 'openai', 'desc': '💨 سريع ورخيص'},
            })

        # Google Models
        if self.google_key:
            genai.configure(api_key=self.google_key)
            self.models.update({
                'gemini-pro': {'name': 'Gemini Pro', 'client': 'google', 'desc': '🌟 قوي ومتعدد الوسائط'},
                'gemini-1.5-pro': {'name': 'Gemini 1.5 Pro', 'client': 'google', 'desc': '🚀 الأحدث والأقوى'},
                'gemini-1.5-flash': {'name': 'Gemini 1.5 Flash', 'client': 'google', 'desc': '⚡ سريع جداً'},
            })

        # Anthropic Models
        if self.anthropic_key:
            self.claude_client = Anthropic(api_key=self.anthropic_key)
            self.models.update({
                'claude-3-opus-20240229': {'name': 'Claude 3 Opus', 'client': 'anthropic', 'desc': '👑 الأذكى'},
                'claude-3-5-sonnet-20241022': {'name': 'Claude 3.5 Sonnet', 'client': 'anthropic', 'desc': '⭐ متوازن ومتطور'},
                'claude-3-haiku-20240307': {'name': 'Claude 3 Haiku', 'client': 'anthropic', 'desc': '💨 سريع وفعال'},
            })

    def init_search(self):
        """تهيئة محركات البحث"""
        self.search_engines = {}
        if self.serper_key:
            self.search_engines['serper'] = True
        if self.tavily_key:
            self.search_engines['tavily'] = True

    def init_image_models(self):
        """تهيئة نماذج الصور"""
        self.image_models = {}

        if self.openai_key:
            self.image_models['dall-e-3'] = {
                'name': 'DALL-E 3',
                'desc': 'توليد صور عالية الجودة'
            }
            self.image_models['dall-e-2'] = {
                'name': 'DALL-E 2',
                'desc': 'توليد صور سريع'
            }

    def show_models(self):
        """عرض النماذج المتاحة"""
        print("\n" + "="*70)
        print("📋 النماذج المتاحة للدردشة:")
        print("="*70)

        for i, (model_id, info) in enumerate(self.models.items(), 1):
            print(f"{i:2d}. {info['name']:<25} - {info['desc']}")

        print("\n" + "="*70)
        print("🎨 نماذج توليد الصور:")
        print("="*70)

        for model_id, info in self.image_models.items():
            print(f"  • {info['name']:<25} - {info['desc']}")

        print()

    def select_model(self):
        """اختيار النموذج"""
        self.show_models()

        while True:
            choice = input("اختر رقم النموذج (أو اكتب ID): ").strip()

            if choice.isdigit():
                idx = int(choice) - 1
                models_list = list(self.models.keys())
                if 0 <= idx < len(models_list):
                    self.current_model = models_list[idx]
                    print(f"\n✅ تم اختيار: {self.models[self.current_model]['name']}\n")
                    return

            elif choice in self.models:
                self.current_model = choice
                print(f"\n✅ تم اختيار: {self.models[self.current_model]['name']}\n")
                return

            print("❌ اختيار غير صحيح، حاول مرة أخرى")

    def chat(self, message, use_search=False, stream=False):
        """الدردشة مع النموذج"""
        if not self.current_model:
            print("❌ لم يتم اختيار نموذج!")
            return None

        # إضافة نتائج البحث
        if use_search:
            search_results = self.search(message)
            if search_results:
                message = f"{message}\n\nنتائج البحث:\n{search_results}"

        model_info = self.models[self.current_model]
        client_type = model_info['client']

        try:
            # OpenAI
            if client_type == 'openai':
                if stream:
                    return self._chat_openai_stream(message)
                else:
                    response = self.openai_client.chat.completions.create(
                        model=self.current_model,
                        messages=[{"role": "user", "content": message}]
                    )
                    return response.choices[0].message.content

            # Google Gemini
            elif client_type == 'google':
                model = genai.GenerativeModel(self.current_model)
                if stream:
                    return self._chat_gemini_stream(model, message)
                else:
                    response = model.generate_content(message)
                    return response.text

            # Anthropic Claude
            elif client_type == 'anthropic':
                if stream:
                    return self._chat_claude_stream(message)
                else:
                    response = self.claude_client.messages.create(
                        model=self.current_model,
                        max_tokens=4096,
                        messages=[{"role": "user", "content": message}]
                    )
                    return response.content[0].text

        except Exception as e:
            return f"❌ خطأ: {str(e)}"

    def _chat_openai_stream(self, message):
        """دردشة OpenAI مع streaming"""
        print(f"\n🤖 {self.models[self.current_model]['name']}: ", end='', flush=True)

        stream = self.openai_client.chat.completions.create(
            model=self.current_model,
            messages=[{"role": "user", "content": message}],
            stream=True
        )

        full_response = ""
        for chunk in stream:
            if chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                print(content, end='', flush=True)
                full_response += content

        print()  # newline
        return full_response

    def _chat_gemini_stream(self, model, message):
        """دردشة Gemini مع streaming"""
        print(f"\n🤖 {self.models[self.current_model]['name']}: ", end='', flush=True)

        response = model.generate_content(message, stream=True)

        full_response = ""
        for chunk in response:
            if chunk.text:
                print(chunk.text, end='', flush=True)
                full_response += chunk.text

        print()
        return full_response

    def _chat_claude_stream(self, message):
        """دردشة Claude مع streaming"""
        print(f"\n🤖 {self.models[self.current_model]['name']}: ", end='', flush=True)

        full_response = ""
        with self.claude_client.messages.stream(
            model=self.current_model,
            max_tokens=4096,
            messages=[{"role": "user", "content": message}]
        ) as stream:
            for text in stream.text_stream:
                print(text, end='', flush=True)
                full_response += text

        print()
        return full_response

    def search(self, query):
        """البحث في الإنترنت"""
        results = []

        # Serper
        if 'serper' in self.search_engines:
            try:
                url = "https://google.serper.dev/search"
                headers = {
                    'X-API-KEY': self.serper_key,
                    'Content-Type': 'application/json'
                }
                response = requests.post(url, headers=headers, json={'q': query}, timeout=10)
                data = response.json()

                for item in data.get('organic', [])[:5]:
                    results.append(f"📄 {item['title']}\n   {item['snippet']}\n   🔗 {item['link']}")
            except:
                pass

        # Tavily
        if 'tavily' in self.search_engines and not results:
            try:
                from tavily import TavilyClient
                client = TavilyClient(api_key=self.tavily_key)
                response = client.search(query, max_results=5)

                for item in response.get('results', []):
                    results.append(f"📄 {item['title']}\n   {item['content'][:200]}...\n   🔗 {item['url']}")
            except:
                pass

        return "\n\n".join(results) if results else None

    def generate_image(self, prompt, model='dall-e-3', size='1024x1024'):
        """توليد صورة"""
        if not self.openai_key:
            return "❌ مفتاح OpenAI غير متوفر"

        try:
            print(f"🎨 جاري توليد الصورة...")

            response = self.openai_client.images.generate(
                model=model,
                prompt=prompt,
                size=size,
                quality="standard" if model == "dall-e-2" else "hd",
                n=1,
            )

            image_url = response.data[0].url

            # حفظ الصورة
            img_response = requests.get(image_url)
            filename = f"generated_image_{hash(prompt)}.png"

            with open(filename, 'wb') as f:
                f.write(img_response.content)

            return f"✅ تم توليد الصورة: {filename}\n🔗 {image_url}"

        except Exception as e:
            return f"❌ خطأ: {str(e)}"

    def text_to_speech(self, text, voice='alloy'):
        """تحويل نص لكلام"""
        if not self.openai_key:
            return "❌ مفتاح OpenAI غير متوفر"

        try:
            print(f"🔊 جاري تحويل النص لكلام...")

            response = self.openai_client.audio.speech.create(
                model="tts-1",
                voice=voice,
                input=text
            )

            filename = f"speech_{hash(text)}.mp3"
            response.stream_to_file(filename)

            return f"✅ تم حفظ الملف الصوتي: {filename}"

        except Exception as e:
            return f"❌ خطأ: {str(e)}"

    def analyze_image(self, image_path, question="صف هذه الصورة"):
        """تحليل صورة"""
        if not self.openai_key:
            return "❌ مفتاح OpenAI غير متوفر"

        try:
            print(f"🔍 جاري تحليل الصورة...")

            # قراءة الصورة
            with open(image_path, "rb") as image_file:
                base64_image = base64.b64encode(image_file.read()).decode('utf-8')

            response = self.openai_client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": question},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=1000
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"❌ خطأ: {str(e)}"

    def read_file(self, file_path):
        """قراءة ملف"""
        try:
            path = Path(file_path)
            if not path.exists():
                return f"❌ الملف غير موجود: {file_path}"

            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            return content
        except Exception as e:
            return f"❌ خطأ: {str(e)}"

    def write_file(self, file_path, content):
        """كتابة ملف"""
        try:
            path = Path(file_path)
            path.parent.mkdir(parents=True, exist_ok=True)

            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)

            return f"✅ تم حفظ الملف: {file_path}"
        except Exception as e:
            return f"❌ خطأ: {str(e)}"

    def analyze_code(self, file_path):
        """تحليل كود"""
        content = self.read_file(file_path)
        if content.startswith("❌"):
            return content

        prompt = f"""حلل هذا الكود بشكل شامل:

1. ملخص عن وظيفة الكود
2. المشاكل والأخطاء المحتملة
3. اقتراحات للتحسين
4. أفضل الممارسات

الكود:
```
{content}
```
"""
        return self.chat(prompt)

    def edit_code(self, file_path, instruction):
        """تعديل كود"""
        content = self.read_file(file_path)
        if content.startswith("❌"):
            return content

        prompt = f"""عدّل هذا الكود حسب التعليمات التالية:
{instruction}

الكود الحالي:
```
{content}
```

أعطني الكود المعدّل فقط، بدون شرح إضافي.
"""

        new_code = self.chat(prompt)

        # حفظ نسخة احتياطية
        backup_path = f"{file_path}.backup"
        self.write_file(backup_path, content)

        # حفظ الكود الجديد
        result = self.write_file(file_path, new_code)
        return f"{result}\n✅ نسخة احتياطية: {backup_path}"

    def compare_models(self, question):
        """مقارنة إجابات النماذج المختلفة"""
        print("\n" + "="*70)
        print("🔄 جاري المقارنة بين النماذج...")
        print("="*70 + "\n")

        original_model = self.current_model
        results = {}

        # جرب مع كل نموذج
        for model_id, info in list(self.models.items())[:3]:  # أول 3 نماذج
            self.current_model = model_id
            print(f"⏳ {info['name']}...")

            response = self.chat(question)
            results[info['name']] = response

        # عرض النتائج
        print("\n" + "="*70)
        print("📊 النتائج:")
        print("="*70 + "\n")

        for model_name, response in results.items():
            print(f"🤖 {model_name}:")
            print(f"{response[:200]}...")
            print("\n" + "-"*70 + "\n")

        # إرجاع النموذج الأصلي
        self.current_model = original_model

    def interactive_mode(self):
        """الوضع التفاعلي المحسّن"""
        print("\n" + "="*70)
        print("🤖 مرحباً في AI Workspace Pro - النسخة المحسّنة")
        print("="*70)
        print("""
✨ الميزات الجديدة:
  /image      - توليد صورة بالذكاء الاصطناعي
  /vision     - تحليل صورة
  /voice      - تحويل نص لكلام
  /compare    - مقارنة إجابات النماذج
  /stream     - دردشة مع عرض مباشر

📋 الأوامر الأساسية:
  /models     - اختيار النموذج
  /search     - البحث في الإنترنت
  /read       - قراءة ملف
  /write      - كتابة ملف
  /analyze    - تحليل كود
  /edit       - تعديل كود
  /help       - المساعدة
  /exit       - خروج

💡 نصيحة: اكتب سؤالك مباشرة للدردشة!
""")

        # اختيار النموذج
        self.select_model()

        while True:
            try:
                user_input = input("\n💬 أنت: ").strip()

                if not user_input:
                    continue

                # الأوامر
                if user_input.startswith('/'):
                    cmd = user_input.split()[0].lower()

                    if cmd == '/exit':
                        print("\n👋 إلى اللقاء!")
                        break

                    elif cmd == '/models':
                        self.select_model()

                    elif cmd == '/search':
                        query = input("🔍 ما تريد البحث عنه؟ ")
                        print("\n⏳ جاري البحث...")
                        results = self.search(query)
                        if results:
                            print(f"\n📊 نتائج البحث:\n\n{results}")
                        else:
                            print("❌ لم يتم العثور على نتائج")

                    elif cmd == '/image':
                        prompt = input("🎨 صف الصورة التي تريدها: ")
                        result = self.generate_image(prompt)
                        print(f"\n{result}")

                    elif cmd == '/vision':
                        image_path = input("📷 مسار الصورة: ")
                        question = input("❓ ماذا تريد أن تعرف عن الصورة؟ (اضغط Enter للوصف العام): ")
                        if not question:
                            question = "صف هذه الصورة بالتفصيل"
                        result = self.analyze_image(image_path, question)
                        print(f"\n🔍 التحليل:\n{result}")

                    elif cmd == '/voice':
                        text = input("📝 النص المراد تحويله: ")
                        voice = input("🎙️ الصوت (alloy/echo/fable/onyx/nova/shimmer) [Enter=alloy]: ").strip() or 'alloy'
                        result = self.text_to_speech(text, voice)
                        print(f"\n{result}")

                    elif cmd == '/compare':
                        question = input("❓ السؤال للمقارنة: ")
                        self.compare_models(question)

                    elif cmd == '/stream':
                        message = input("💬 رسالتك: ")
                        self.chat(message, stream=True)

                    elif cmd == '/read':
                        file_path = input("📄 اسم الملف: ")
                        content = self.read_file(file_path)
                        print(f"\n📄 المحتوى:\n{content[:1000]}{'...' if len(content) > 1000 else ''}")

                    elif cmd == '/write':
                        file_path = input("📄 اسم الملف: ")
                        print("📝 اكتب المحتوى (Enter ثم Ctrl+D للإنهاء):")
                        lines = []
                        try:
                            while True:
                                lines.append(input())
                        except EOFError:
                            pass
                        content = "\n".join(lines)
                        result = self.write_file(file_path, content)
                        print(f"\n{result}")

                    elif cmd == '/analyze':
                        file_path = input("📄 ملف الكود: ")
                        print("\n⏳ جاري التحليل...")
                        result = self.analyze_code(file_path)
                        print(f"\n📊 التحليل:\n{result}")

                    elif cmd == '/edit':
                        file_path = input("📄 ملف الكود: ")
                        instruction = input("📝 ماذا تريد تعديله؟ ")
                        print("\n⏳ جاري التعديل...")
                        result = self.edit_code(file_path, instruction)
                        print(f"\n{result}")

                    elif cmd == '/help':
                        print("""
🆘 دليل الاستخدام:

✨ ميزات جديدة:
  /image      - توليد صورة (DALL-E 3)
  /vision     - تحليل صورة (GPT-4 Vision)
  /voice      - تحويل نص لكلام
  /compare    - مقارنة بين 3 نماذج
  /stream     - عرض الرد مباشرة أثناء الكتابة

📋 أوامر أساسية:
  /models     - اختيار نموذج مختلف
  /search     - بحث في الإنترنت
  /read       - قراءة ملف
  /write      - كتابة ملف
  /analyze    - تحليل كود
  /edit       - تعديل كود

💡 للدردشة العادية: اكتب سؤالك مباشرة
                        """)

                    else:
                        print("❌ أمر غير معروف. اكتب /help للمساعدة")

                # الدردشة العادية
                else:
                    print(f"\n⏳ {self.models[self.current_model]['name']} يفكر...")
                    response = self.chat(user_input)
                    print(f"\n🤖 {self.models[self.current_model]['name']}:\n{response}")

            except KeyboardInterrupt:
                print("\n\n👋 إلى اللقاء!")
                break
            except Exception as e:
                print(f"\n❌ خطأ: {str(e)}")


def main():
    """البرنامج الرئيسي"""
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except:
        pass

    workspace = AIWorkspacePro()
    workspace.interactive_mode()


if __name__ == "__main__":
    main()
