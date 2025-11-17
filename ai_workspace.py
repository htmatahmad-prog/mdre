#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🤖 AI Workspace - مساحة عمل الذكاء الاصطناعي الشاملة
نظام متكامل يدمج جميع نماذج AI مع البحث والملفات وتحرير الكود
"""

import os
import sys
from openai import OpenAI
import google.generativeai as genai
from anthropic import Anthropic
import requests
import json
from pathlib import Path

class AIWorkspace:
    """مساحة عمل شاملة للذكاء الاصطناعي"""

    def __init__(self):
        """تهيئة جميع النماذج"""
        print("🚀 جاري تحميل مساحة العمل...")

        # تحميل المفاتيح
        self.load_keys()

        # تهيئة النماذج
        self.init_models()

        # تهيئة أدوات البحث
        self.init_search()

        # المحادثة الحالية
        self.conversation = []
        self.current_model = None

        print("✅ تم التحميل بنجاح!\n")

    def load_keys(self):
        """تحميل مفاتيح API"""
        self.openai_key = os.getenv('OPENAI_API_KEY')
        self.google_key = os.getenv('GOOGLE_API_KEY')
        self.anthropic_key = os.getenv('ANTHROPIC_API_KEY')
        self.serper_key = os.getenv('SERPER_API_KEY')
        self.tavily_key = os.getenv('TAVILY_API_KEY')

    def init_models(self):
        """تهيئة جميع النماذج المتاحة"""
        self.models = {}

        # OpenAI Models
        if self.openai_key:
            self.openai_client = OpenAI(api_key=self.openai_key)
            self.models.update({
                'gpt-4': {'name': 'GPT-4', 'client': 'openai', 'desc': 'الأقوى والأذكى'},
                'gpt-4-turbo': {'name': 'GPT-4 Turbo', 'client': 'openai', 'desc': 'سريع وقوي'},
                'gpt-3.5-turbo': {'name': 'GPT-3.5 Turbo', 'client': 'openai', 'desc': 'سريع ورخيص'},
            })

        # Google Models
        if self.google_key:
            genai.configure(api_key=self.google_key)
            self.models.update({
                'gemini-pro': {'name': 'Gemini Pro', 'client': 'google', 'desc': 'قوي ومتعدد الوسائط'},
                'gemini-1.5-pro': {'name': 'Gemini 1.5 Pro', 'client': 'google', 'desc': 'الأحدث والأقوى'},
            })

        # Anthropic Models
        if self.anthropic_key:
            self.claude_client = Anthropic(api_key=self.anthropic_key)
            self.models.update({
                'claude-3-opus': {'name': 'Claude 3 Opus', 'client': 'anthropic', 'desc': 'الأذكى'},
                'claude-3-sonnet': {'name': 'Claude 3.5 Sonnet', 'client': 'anthropic', 'desc': 'متوازن'},
                'claude-3-haiku': {'name': 'Claude 3 Haiku', 'client': 'anthropic', 'desc': 'سريع'},
            })

    def init_search(self):
        """تهيئة محركات البحث"""
        self.search_engines = {}

        if self.serper_key:
            self.search_engines['serper'] = True

        if self.tavily_key:
            self.search_engines['tavily'] = True

    def show_models(self):
        """عرض النماذج المتاحة"""
        print("\n" + "="*60)
        print("📋 النماذج المتاحة:")
        print("="*60)

        for i, (model_id, info) in enumerate(self.models.items(), 1):
            print(f"{i}. {info['name']}")
            print(f"   ID: {model_id}")
            print(f"   الوصف: {info['desc']}")
            print()

    def select_model(self):
        """اختيار النموذج"""
        self.show_models()

        while True:
            choice = input("اختر رقم النموذج (أو اكتب ID مباشرة): ").strip()

            # إذا اختار رقم
            if choice.isdigit():
                idx = int(choice) - 1
                models_list = list(self.models.keys())
                if 0 <= idx < len(models_list):
                    self.current_model = models_list[idx]
                    print(f"\n✅ تم اختيار: {self.models[self.current_model]['name']}\n")
                    return

            # إذا كتب ID
            elif choice in self.models:
                self.current_model = choice
                print(f"\n✅ تم اختيار: {self.models[self.current_model]['name']}\n")
                return

            print("❌ اختيار غير صحيح، حاول مرة أخرى")

    def chat(self, message, use_search=False):
        """الدردشة مع النموذج المختار"""
        if not self.current_model:
            print("❌ لم يتم اختيار نموذج! استخدم select_model() أولاً")
            return None

        # إضافة نتائج البحث إذا طُلب ذلك
        if use_search:
            search_results = self.search(message)
            if search_results:
                message = f"{message}\n\nنتائج البحث:\n{search_results}"

        model_info = self.models[self.current_model]
        client_type = model_info['client']

        try:
            # OpenAI
            if client_type == 'openai':
                response = self.openai_client.chat.completions.create(
                    model=self.current_model,
                    messages=[{"role": "user", "content": message}]
                )
                return response.choices[0].message.content

            # Google Gemini
            elif client_type == 'google':
                model = genai.GenerativeModel(self.current_model)
                response = model.generate_content(message)
                return response.text

            # Anthropic Claude
            elif client_type == 'anthropic':
                response = self.claude_client.messages.create(
                    model=self.current_model,
                    max_tokens=4096,
                    messages=[{"role": "user", "content": message}]
                )
                return response.content[0].text

        except Exception as e:
            return f"❌ خطأ: {str(e)}"

    def search(self, query):
        """البحث في الإنترنت"""
        results = []

        # Serper Search
        if 'serper' in self.search_engines:
            try:
                url = "https://google.serper.dev/search"
                headers = {
                    'X-API-KEY': self.serper_key,
                    'Content-Type': 'application/json'
                }
                response = requests.post(url, headers=headers, json={'q': query})
                data = response.json()

                for item in data.get('organic', [])[:3]:
                    results.append(f"- {item['title']}: {item['snippet']}")
            except:
                pass

        return "\n".join(results) if results else None

    def read_file(self, file_path):
        """قراءة محتوى ملف"""
        try:
            path = Path(file_path)
            if not path.exists():
                return f"❌ الملف غير موجود: {file_path}"

            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            return content
        except Exception as e:
            return f"❌ خطأ في القراءة: {str(e)}"

    def write_file(self, file_path, content):
        """كتابة محتوى إلى ملف"""
        try:
            path = Path(file_path)
            path.parent.mkdir(parents=True, exist_ok=True)

            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)

            return f"✅ تم حفظ الملف: {file_path}"
        except Exception as e:
            return f"❌ خطأ في الكتابة: {str(e)}"

    def analyze_code(self, file_path):
        """تحليل كود من ملف"""
        content = self.read_file(file_path)
        if content.startswith("❌"):
            return content

        prompt = f"""حلل هذا الكود وأعطني:
1. ملخص عن وظيفة الكود
2. المشاكل المحتملة
3. اقتراحات للتحسين

الكود:
```
{content}
```
"""
        return self.chat(prompt)

    def edit_code(self, file_path, instruction):
        """تعديل كود حسب التعليمات"""
        content = self.read_file(file_path)
        if content.startswith("❌"):
            return content

        prompt = f"""عدّل هذا الكود حسب التعليمات التالية:
{instruction}

الكود الحالي:
```
{content}
```

أعطني الكود المعدّل فقط، بدون شرح.
"""

        new_code = self.chat(prompt)

        # حفظ نسخة احتياطية
        backup_path = f"{file_path}.backup"
        self.write_file(backup_path, content)

        # حفظ الكود الجديد
        return self.write_file(file_path, new_code)

    def interactive_mode(self):
        """الوضع التفاعلي الكامل"""
        print("\n" + "="*60)
        print("🤖 مرحباً في مساحة العمل التفاعلية")
        print("="*60)
        print("""
الأوامر المتاحة:
  /models     - عرض واختيار النموذج
  /search     - البحث في الإنترنت
  /read       - قراءة ملف
  /write      - كتابة ملف
  /analyze    - تحليل كود
  /edit       - تعديل كود
  /help       - المساعدة
  /exit       - خروج

أو اكتب سؤالك مباشرة للدردشة!
""")

        # اختيار النموذج في البداية
        self.select_model()

        while True:
            try:
                user_input = input("\n💬 أنت: ").strip()

                if not user_input:
                    continue

                # الأوامر الخاصة
                if user_input.startswith('/'):
                    cmd = user_input.split()[0].lower()

                    if cmd == '/exit':
                        print("\n👋 إلى اللقاء!")
                        break

                    elif cmd == '/models':
                        self.select_model()

                    elif cmd == '/search':
                        query = input("🔍 ما تريد البحث عنه؟ ")
                        results = self.search(query)
                        if results:
                            print(f"\n📊 نتائج البحث:\n{results}")
                        else:
                            print("❌ لم يتم العثور على نتائج")

                    elif cmd == '/read':
                        file_path = input("📄 اسم الملف: ")
                        content = self.read_file(file_path)
                        print(f"\n{content[:500]}..." if len(content) > 500 else content)

                    elif cmd == '/write':
                        file_path = input("📄 اسم الملف: ")
                        print("📝 اكتب المحتوى (Enter ثم Ctrl+D للإنهاء):")
                        content_lines = []
                        try:
                            while True:
                                line = input()
                                content_lines.append(line)
                        except EOFError:
                            pass
                        content = "\n".join(content_lines)
                        result = self.write_file(file_path, content)
                        print(result)

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
                        print(result)

                    elif cmd == '/help':
                        print("""
🆘 المساعدة:

الأوامر:
  /models     - اختيار نموذج مختلف (GPT-4, Gemini, Claude, ...)
  /search     - البحث عن معلومات في الإنترنت
  /read       - قراءة محتوى ملف
  /write      - كتابة/إنشاء ملف جديد
  /analyze    - تحليل ملف كود
  /edit       - تعديل ملف كود حسب تعليماتك
  /help       - عرض هذه المساعدة
  /exit       - الخروج

الدردشة:
  اكتب أي سؤال مباشرة وسيجيب النموذج المختار

مثال:
  اشرح لي الذكاء الاصطناعي
  اكتب لي كود Python لحساب فيبوناتشي
  """)

                    else:
                        print("❌ أمر غير معروف. اكتب /help للمساعدة")

                # الدردشة العادية
                else:
                    print(f"\n⏳ {self.models[self.current_model]['name']} يفكر...")
                    response = self.chat(user_input)
                    print(f"\n🤖 {self.models[self.current_model]['name']}: {response}")

            except KeyboardInterrupt:
                print("\n\n👋 إلى اللقاء!")
                break
            except Exception as e:
                print(f"\n❌ خطأ: {str(e)}")


def main():
    """البرنامج الرئيسي"""
    # تحميل المتغيرات البيئية
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except:
        pass

    # إنشاء مساحة العمل
    workspace = AIWorkspace()

    # الوضع التفاعلي
    workspace.interactive_mode()


if __name__ == "__main__":
    main()
