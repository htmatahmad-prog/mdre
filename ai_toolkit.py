#!/usr/bin/env python3
"""
🧰 مجموعة أدوات الذكاء الاصطناعي الشاملة
Comprehensive AI Toolkit for Termux
استخدم هذا السكريبت للوصول لجميع APIs في مكان واحد
"""

import os
import sys
import json
import time
from datetime import datetime
from typing import Dict, List, Optional

# ألوان النص
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(text: str):
    print(f"\n{Colors.HEADER}{'='*70}{Colors.END}")
    print(f"{Colors.HEADER}{text.center(70)}{Colors.END}")
    print(f"{Colors.HEADER}{'='*70}{Colors.END}\n")

def print_success(text: str):
    print(f"{Colors.GREEN}✅ {text}{Colors.END}")

def print_error(text: str):
    print(f"{Colors.FAIL}❌ {text}{Colors.END}")

def print_warning(text: str):
    print(f"{Colors.WARNING}⚠️  {text}{Colors.END}")

def print_info(text: str):
    print(f"{Colors.BLUE}ℹ️  {text}{Colors.END}")

class AIToolkit:
    """مجموعة أدوات الذكاء الاصطناعي"""

    def __init__(self):
        self.apis = {}
        self.load_apis()
        self.check_apis()

    def load_apis(self):
        """تحميل جميع APIs المتاحة"""
        # OpenAI
        if os.getenv('OPENAI_API_KEY'):
            try:
                import urllib.request
                self.apis['openai'] = {
                    'available': True,
                    'status': 'متاح',
                    'type': 'LLM',
                    'models': 79
                }
            except:
                self.apis['openai'] = {'available': False, 'status': 'خطأ', 'type': 'LLM'}

        # Gemini
        if os.getenv('GEMINI_API_KEY'):
            try:
                import urllib.request
                self.apis['gemini'] = {
                    'available': True,
                    'status': 'متاح',
                    'type': 'LLM',
                    'models': 50
                }
            except:
                self.apis['gemini'] = {'available': False, 'status': 'خطأ', 'type': 'LLM'}

        # Anthropic
        if os.getenv('ANTHROPIC_API_KEY'):
            try:
                self.apis['anthropic'] = {
                    'available': True,
                    'status': 'متاح',
                    'type': 'LLM',
                    'models': 'Claude 3'
                }
            except:
                self.apis['anthropic'] = {'available': False, 'status': 'خطأ', 'type': 'LLM'}

        # Hugging Face
        if os.getenv('HUGGINGFACE_API_KEY'):
            try:
                self.apis['huggingface'] = {
                    'available': True,
                    'status': 'متاح',
                    'type': 'Models',
                    'models': '50,000+'
                }
            except:
                self.apis['huggingface'] = {'available': False, 'status': 'خطأ', 'type': 'Models'}

        # Serper
        if os.getenv('SERPER_API_KEY'):
            self.apis['serper'] = {
                'available': True,
                'status': 'متاح',
                'type': 'Search',
                'limit': '2,500/month'
            }

        # Tavily
        if os.getenv('TAVILY_API_KEY'):
            self.apis['tavily'] = {
                'available': True,
                'status': 'متاح',
                'type': 'Search',
                'limit': '1,000/month'
            }

        # ElevenLabs
        if os.getenv('ELEVENLABS_API_KEY'):
            self.apis['elevenlabs'] = {
                'available': True,
                'status': 'متاح',
                'type': 'TTS',
                'limit': '10,000 chars/month',
                'voices': 20
            }

        # GitHub Copilot
        if os.getenv('GITHUB_COPILOT_TOKEN') and os.getenv('GITHUB_COPILOT_TOKEN') != 'your_copilot_token_here':
            self.apis['github_copilot'] = {
                'available': True,
                'status': 'متاح',
                'type': 'IDE Extension',
                'cost': '$10/month'
            }
        else:
            self.apis['github_copilot'] = {
                'available': False,
                'status': 'يتطلب VSCode',
                'type': 'IDE Extension'
            }

    def check_apis(self):
        """فحص حالة جميع APIs"""
        print_header("🔍 فحص APIs المتاحة")

        available_count = 0
        for name, info in self.apis.items():
            if info['available']:
                print_success(f"{name.replace('_', ' ').title()}: {info['status']}")
                if 'models' in info:
                    print(f"   📦 {info['models']} نموذج متاح")
                if 'limit' in info:
                    print(f"   📊 {info['limit']}")
                available_count += 1
            else:
                print_error(f"{name.replace('_', ' ').title()}: {info['status']}")

        print(f"\n{Colors.CYAN}الإجمالي: {available_count}/{len(self.apis)} APIs متاحة{Colors.END}")
        return available_count

    def chat_with_ai(self):
        """الدردشة مع الذكاء الاصطناعي"""
        print_header("💬 الدردشة مع الذكاء الاصطناعي")

        print_info("اختر النموذج:")
        print("1. OpenAI (GPT-3.5-turbo)")
        print("2. Google Gemini")
        print("3. Anthropic Claude")
        print("4. جميع النماذج (مقارنة)")

        choice = input("\nاختيارك (1-4): ").strip()

        message = input("\nرسالتك: ").strip()
        if not message:
            print_error("لم تكتب رسالة!")
            return

        if choice == "1" and self.apis.get('openai', {}).get('available'):
            self._chat_openai(message)
        elif choice == "2" and self.apis.get('gemini', {}).get('available'):
            self._chat_gemini(message)
        elif choice == "3" and self.apis.get('anthropic', {}).get('available'):
            self._chat_anthropic(message)
        elif choice == "4":
            self._chat_all_models(message)
        else:
            print_error("اختيار غير صحيح أو النموذج غير متاح")

    def _chat_openai(self, message):
        """دردشة مع OpenAI"""
        print_info("الدردشة مع OpenAI...")
        print(f"{Colors.BOLD}أنت: {message}{Colors.END}")
        print(f"{Colors.GREEN}OpenAI: {Colors.END}", end="")

        try:
            import urllib.request
            import json

            api_key = os.getenv('OPENAI_API_KEY')
            url = "https://api.openai.com/v1/chat/completions"
            headers = {
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            }
            data = {
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": message}],
                "max_tokens": 150
            }

            req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
            with urllib.request.urlopen(req, timeout=30) as response:
                result = json.loads(response.read().decode())
                reply = result["choices"][0]["message"]["content"]
                print(reply)
        except Exception as e:
            print_error(f"خطأ: {str(e)[:50]}")

    def _chat_gemini(self, message):
        """دردشة مع Gemini"""
        print_info("الدردشة مع Gemini...")
        print(f"{Colors.BOLD}أنت: {message}{Colors.END}")
        print(f"{Colors.CYAN}Gemini: {Colors.END}", end="")

        try:
            import urllib.request
            import json

            api_key = os.getenv('GEMINI_API_KEY')
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
            data = {
                "contents": [{
                    "parts": [{"text": message}]
                }]
            }

            req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'))
            with urllib.request.urlopen(req, timeout=30) as response:
                result = json.loads(response.read().decode())
                reply = result["candidates"][0]["content"]["parts"][0]["text"]
                print(reply)
        except Exception as e:
            print_error(f"خطأ: {str(e)[:50]}")

    def _chat_anthropic(self, message):
        """دردشة مع Claude"""
        print_info("الدردشة مع Claude...")
        print(f"{Colors.BOLD}أنت: {message}{Colors.END}")
        print(f"{Colors.PURPLE}Claude: {Colors.END}", end="")

        try:
            import urllib.request
            import json

            api_key = os.getenv('ANTHROPIC_API_KEY')
            url = "https://api.anthropic.com/v1/messages"
            headers = {
                'x-api-key': api_key,
                'Content-Type': 'application/json',
                'anthropic-version': '2023-06-01'
            }
            data = {
                'model': 'claude-3-haiku-20240307',
                'max_tokens': 150,
                'messages': [{'role': 'user', 'content': message}]
            }

            req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
            with urllib.request.urlopen(req, timeout=30) as response:
                result = json.loads(response.read().decode())
                reply = result["content"][0]["text"]
                print(reply)
        except Exception as e:
            print_error(f"خطأ: {str(e)[:50]}")

    def _chat_all_models(self, message):
        """دردشة مع جميع النماذج"""
        print_info("مقارنة جميع النماذج...")
        print(f"{Colors.BOLD}السؤال: {message}{Colors.END}\n")

        if self.apis.get('openai', {}).get('available'):
            print(f"{Colors.GREEN}=== OpenAI ==={Colors.END}")
            self._chat_openai(message)
            print()

        if self.apis.get('gemini', {}).get('available'):
            print(f"{Colors.CYAN}=== Gemini ==={Colors.END}")
            self._chat_gemini(message)
            print()

        if self.apis.get('anthropic', {}).get('available'):
            print(f"{Colors.PURPLE}=== Claude ==={Colors.END}")
            self._chat_anthropic(message)
            print()

    def search_the_web(self):
        """البحث في الويب"""
        print_header("🔍 البحث في الويب")

        print_info("اختر محرك البحث:")
        print("1. Serper (Google Search)")
        print("2. Tavily (AI Search)")

        choice = input("\nاختيارك (1-2): ").strip()
        query = input("\nما تبحث عنه؟ ").strip()

        if not query:
            print_error("لم تكتب بحث!")
            return

        if choice == "1" and self.apis.get('serper', {}).get('available'):
            self._search_serper(query)
        elif choice == "2" and self.apis.get('tavily', {}).get('available'):
            self._search_tavily(query)
        else:
            print_error("اختيار غير صحيح أو محرك البحث غير متاح")

    def _search_serper(self, query):
        """بحث مع Serper"""
        print_info("جاري البحث مع Serper...")
        try:
            import urllib.request
            import json

            api_key = os.getenv('SERPER_API_KEY')
            url = "https://google.serper.dev/search"
            headers = {
                'X-API-KEY': api_key,
                'Content-Type': 'application/json'
            }
            data = {'q': query, 'num': 5}

            req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
            with urllib.request.urlopen(req, timeout=15) as response:
                result = json.loads(response.read().decode())
                print(f"\n{Colors.BOLD}نتائج البحث عن: {query}{Colors.END}\n")
                for i, item in enumerate(result.get('organic', [])[:5], 1):
                    print(f"{Colors.CYAN}{i}. {item.get('title', 'بدون عنوان')}{Colors.END}")
                    print(f"   {item.get('snippet', 'بدون وصف')}")
                    print(f"   {Colors.BLUE}{item.get('link', '')}{Colors.END}\n")
        except Exception as e:
            print_error(f"خطأ في البحث: {str(e)[:50]}")

    def _search_tavily(self, query):
        """بحث مع Tavily"""
        print_info("جاري البحث مع Tavily...")
        try:
            import urllib.request
            import json

            api_key = os.getenv('TAVILY_API_KEY')
            url = "https://api.tavily.com/search"
            headers = {'Content-Type': 'application/json'}
            data = {
                'api_key': api_key,
                'query': query,
                'search_depth': 'advanced',
                'include_answer': True
            }

            req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
            with urllib.request.urlopen(req, timeout=15) as response:
                result = json.loads(response.read().decode())
                print(f"\n{Colors.BOLD}نتائج البحث عن: {query}{Colors.END}\n")

                if result.get('answer'):
                    print(f"{Colors.GREEN}الإجابة:{Colors.END}")
                    print(f"{result['answer']}\n")

                print(f"{Colors.CYAN}المصادر:{Colors.END}")
                for i, item in enumerate(result.get('results', [])[:5], 1):
                    print(f"{i}. {item.get('title', 'بدون عنوان')}")
                    print(f"   {item.get('url', '')}")
                    print()
        except Exception as e:
            print_error(f"خطأ في البحث: {str(e)[:50]}")

    def text_to_speech(self):
        """تحويل النص إلى كلام"""
        print_header("🔊 تحويل النص إلى كلام")

        if not self.apis.get('elevenlabs', {}).get('available'):
            print_error("ElevenLabs API غير متاح")
            return

        text = input("النص المراد تحويله: ").strip()
        if not text:
            print_error("لم تكتب نصاً!")
            return

        print_info("جاري تحويل النص إلى كلام...")
        try:
            import urllib.request
            import json

            api_key = os.getenv('ELEVENLABS_API_KEY')
            url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"
            headers = {
                'xi-api-key': api_key,
                'Content-Type': 'application/json'
            }
            data = {
                "text": text,
                "model_id": "eleven_multilingual_v2",
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.5
                }
            }

            req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
            with urllib.request.urlopen(req, timeout=30) as response:
                audio = response.read()
                filename = f"audio_{int(time.time())}.mp3"
                with open(filename, 'wb') as f:
                    f.write(audio)
                print_success(f"تم حفظ الملف: {filename}")
                print_info(f"استخدم 'mpv {filename}' للاستماع")
        except Exception as e:
            print_error(f"خطأ في التحويل: {str(e)[:50]}")

    def analyze_text(self):
        """تحليل النصوص"""
        print_header("📊 تحليل النصوص")

        if not self.apis.get('huggingface', {}).get('available'):
            print_error("Hugging Face API غير متاح")
            return

        text = input("النص المراد تحليله: ").strip()
        if not text:
            print_error("لم تكتب نصاً!")
            return

        print_info("جاري تحليل النص...")
        try:
            import urllib.request
            import json

            api_key = os.getenv('HUGGINGFACE_API_KEY')
            url = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
            headers = {
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            }
            data = [text]

            req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers=headers)
            with urllib.request.urlopen(req, timeout=30) as response:
                result = json.loads(response.read().decode())
                print(f"\n{Colors.BOLD}تحليل المشاعر:{Colors.END}")
                for item in result[0]:
                    label = item['label']
                    score = item['score']
                    emoji = "😊" if label == "POSITIVE" else "😔"
                    print(f"{emoji} {label}: {score:.2%}")
        except Exception as e:
            print_error(f"خطأ في التحليل: {str(e)[:50]}")

    def show_menu(self):
        """عرض القائمة الرئيسية"""
        print_header("🧰 مجموعة أدوات الذكاء الاصطناعي")
        print(f"{Colors.BOLD}مرحباً بك في مجموعة أدوات الذكاء الاصطناعي!{Colors.END}")
        print(f"التاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        print("الخيارات المتاحة:")
        print(f"{Colors.GREEN}1.{Colors.END} 💬 الدردشة مع الذكاء الاصطناعي")
        print(f"{Colors.GREEN}2.{Colors.END} 🔍 البحث في الويب")
        print(f"{Colors.GREEN}3.{Colors.END} 🔊 تحويل النص إلى كلام")
        print(f"{Colors.GREEN}4.{Colors.END} 📊 تحليل النصوص")
        print(f"{Colors.GREEN}5.{Colors.END} 📋 فحص حالة APIs")
        print(f"{Colors.GREEN}0.{Colors.END} 🚪 خروج")

    def run(self):
        """تشغيل البرنامج"""
        while True:
            self.show_menu()
            choice = input(f"\n{Colors.BOLD}اختر رقماً (0-5): {Colors.END}").strip()

            if choice == "1":
                self.chat_with_ai()
            elif choice == "2":
                self.search_the_web()
            elif choice == "3":
                self.text_to_speech()
            elif choice == "4":
                self.analyze_text()
            elif choice == "5":
                self.check_apis()
            elif choice == "0":
                print_success("وداعاً! 👋")
                break
            else:
                print_error("اختيار غير صحيح!")

            input(f"\n{Colors.CYAN}اضغط Enter للعودة للقائمة الرئيسية...{Colors.END}")

def main():
    """الدالة الرئيسية"""
    # تحميل متغيرات البيئة من config/.env
    env_file = os.path.join(os.path.dirname(__file__), 'config', '.env')
    if os.path.exists(env_file):
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    if value and value != "your_" + key.lower() + "_here":
                        os.environ[key] = value

    # تشغيل مجموعة الأدوات
    toolkit = AIToolkit()
    toolkit.run()

if __name__ == "__main__":
    main()
