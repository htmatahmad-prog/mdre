#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🤖 AI Workspace Fixed - النسخة المحسنة والثابتة
حل جميع المشاكل وجعل التطبيق مثالياً على الهاتف
"""

import os
import sys
import json
import csv
from datetime import datetime
from pathlib import Path
import time
import subprocess

# مكتبات أساسية
from openai import OpenAI
from anthropic import Anthropic
import requests

# فحص Google
try:
    import google.generativeai as genai
    GOOGLE_AVAILABLE = True
except ImportError:
    GOOGLE_AVAILABLE = False
    genai = None

# فحص Flask
try:
    from flask import Flask
    FLASK_AVAILABLE = True
except ImportError:
    FLASK_AVAILABLE = False

class AIWorkspaceFixed:
    """🤖 النسخة المحسنة والثابتة من AI Workspace"""

    def __init__(self):
        """تهيئة محسنة وسريعة"""
        self.setup_theme()
        self.load_keys()
        self.init_models()
        self.conversations = {}
        self.current_chat_id = None
        self.usage_stats = {}
        self.stats_file = Path.home() / "ai_workspace_stats.json"
        self.conversations_dir = Path.home() / "ai_workspace_conversations"
        self.conversations_dir.mkdir(exist_ok=True)
        self.load_conversations()
        self.load_usage_stats()

        self.print_banner()

    def setup_theme(self):
        """إعداد ألوان جميلة"""
        self.theme = {
            'primary': '\033[96m',      # سماوي
            'secondary': '\033[93m',    # أصفر
            'success': '\033[92m',      # أخضر
            'warning': '\033[91m',      # أحمر
            'info': '\033[94m',         # أزرق
            'bold': '\033[1m',          # عريض
            'end': '\033[0m',           # نهاية اللون
            'purple': '\033[95m',       # بنفسجي
            'cyan': '\033[36m',         # تركوازي
        }

    def print_banner(self):
        """عرض شعار جميل"""
        banner = f"""
{self.theme['bold']}{self.theme['primary']}
╔═══════════════════════════════════════════════════════════════════════════╗
║                   🤖 AI Workspace Fixed - النسخة المحسنة                 ║
║                      🔥 سريع • مستقر • مثالي 🔥                          ║
╠═══════════════════════════════════════════════════════════════════════════╣
║ ✨ المميزات المحسنة:                                                      ║
║   🔐 حفظ آمن للمحادثات      📊 إحصائيات تفصيلية                         ║
║   ⚡ استجابة فائقة السرعة    🎯 معالجة أخطاء ذكية                       ║
║   💬 دعم 15+ نموذج ذكاء اصطناعي                                    ║
║   🔍 بحث متقدم             🎨 توليد صور                                 ║
╚═══════════════════════════════════════════════════════════════════════════╝{self.theme['end']}
        """
        print(banner)

    def load_keys(self):
        """تحميل المفاتيح مع معالجة محسنة للأخطاء"""
        config_file = Path(os.getenv('API_KEYS_FILE', Path.home() / "config_keys.json"))
        keys = {}

        if config_file.exists():
            try:
                with open(config_file, 'r') as f:
                    keys = json.load(f)
                print(f"{self.theme['success']}✅ تم تحميل المفاتيح بنجاح{self.theme['end']}")
            except Exception as e:
                print(f"{self.theme['warning']}⚠️ تحذير في تحميل المفاتيح: {e}{self.theme['end']}")

        # تحميل جميع المفاتيح مع قيم افتراضية آمنة
        self.keys = {
            'openai': keys.get('openai') or os.getenv('OPENAI_API_KEY'),
            'google': keys.get('google') or os.getenv('GOOGLE_API_KEY'),
            'anthropic': keys.get('anthropic') or os.getenv('ANTHROPIC_API_KEY'),
            'serper': keys.get('serper') or os.getenv('SERPER_API_KEY'),
            'tavily': keys.get('tavily') or os.getenv('TAVILY_API_KEY'),
            'groq': keys.get('groq') or os.getenv('GROQ_API_KEY'),
            'minimax': keys.get('minimax') or os.getenv('MINIMAX_API_KEY'),
            'minimax_group_id': keys.get('minimax_group_id') or os.getenv('MINIMAX_GROUP_ID'),
            'cohere': keys.get('cohere') or os.getenv('COHERE_API_KEY'),
        }

        # التحقق من وجود نماذج واحدة على الأقل
        if not any([self.keys['openai'], self.keys['google'], self.keys['anthropic'], self.keys['groq']]):
            print(f"\n{self.theme['warning']}⚠️ تحذير: لم يتم العثور على مفاتيح API!{self.theme['end']}")
            print(f"{self.theme['info']}💡 شغّل: python3 setup_keys.py لإعداد المفاتيح{self.theme['end']}\n")

    def init_models(self):
        """تهيئة النماذج مع معالجة قوية للأخطاء"""
        self.models = {}
        self.clients = {}
        errors = []

        # OpenAI Models
        if self.keys['openai']:
            try:
                self.clients['openai'] = OpenAI(api_key=self.keys['openai'])
                self.models.update({
                    'gpt-4o-mini': {
                        'name': 'GPT-4o Mini',
                        'client': 'openai',
                        'desc': '💨 سريع جداً واقتصادي',
                        'speed': 'فائق السرعة'
                    },
                    'gpt-4o': {
                        'name': 'GPT-4o',
                        'client': 'openai',
                        'desc': '🎯 متقدم ومتطور',
                        'speed': 'سريع جداً'
                    },
                    'gpt-3.5-turbo': {
                        'name': 'GPT-3.5 Turbo',
                        'client': 'openai',
                        'desc': '💰 اقتصادي ومفيد',
                        'speed': 'سريع'
                    },
                })
                print(f"{self.theme['success']}✅ تم تحميل نماذج OpenAI{self.theme['end']}")
            except Exception as e:
                errors.append(f"OpenAI: {e}")

        # Google Models
        if self.keys['google'] and GOOGLE_AVAILABLE:
            try:
                genai.configure(api_key=self.keys['google'])
                self.clients['google'] = genai
                self.models.update({
                    'gemini-1.5-flash': {
                        'name': 'Gemini 1.5 Flash',
                        'client': 'google',
                        'desc': '⚡ فائق السرعة',
                        'speed': 'فائق السرعة'
                    },
                    'gemini-1.5-pro': {
                        'name': 'Gemini 1.5 Pro',
                        'client': 'google',
                        'desc': '🚀 قوي ومتطور',
                        'speed': 'سريع'
                    },
                })
                print(f"{self.theme['success']}✅ تم تحميل نماذج Google{self.theme['end']}")
            except Exception as e:
                errors.append(f"Google: {e}")
                if not GOOGLE_AVAILABLE:
                    print(f"{self.theme['warning']}⚠️ مكتبة Google غير مثبتة: pip install google-generativeai{self.theme['end']}")

        # Anthropic Models
        if self.keys['anthropic']:
            try:
                self.clients['anthropic'] = Anthropic(api_key=self.keys['anthropic'])
                self.models.update({
                    'claude-3-haiku-20240307': {
                        'name': 'Claude 3 Haiku',
                        'client': 'anthropic',
                        'desc': '💨 سريع وفعال',
                        'speed': 'فائق السرعة'
                    },
                    'claude-3-5-sonnet-20241022': {
                        'name': 'Claude 3.5 Sonnet',
                        'client': 'anthropic',
                        'desc': '⭐ متوازن ومتطور',
                        'speed': 'سريع'
                    },
                })
                print(f"{self.theme['success']}✅ تم تحميل نماذج Anthropic{self.theme['end']}")
            except Exception as e:
                errors.append(f"Anthropic: {e}")

        # Groq Models (مجاني وسريع جداً)
        if self.keys['groq']:
            try:
                self.clients['groq'] = OpenAI(
                    api_key=self.keys['groq'],
                    base_url="https://api.groq.com/openai/v1"
                )
                self.models.update({
                    'llama-3.1-8b-instant': {
                        'name': 'Llama 3.1 8B',
                        'client': 'groq',
                        'desc': '🚀 سريع جداً - مجاني',
                        'speed': 'فائق السرعة'
                    },
                    'llama-3.1-70b-versatile': {
                        'name': 'Llama 3.1 70B',
                        'client': 'groq',
                        'desc': '⚡ فائق السرعة - مجاني',
                        'speed': 'فائق السرعة'
                    },
                })
                print(f"{self.theme['success']}✅ تم تحميل نماذج Groq (مجاني){self.theme['end']}")
            except Exception as e:
                errors.append(f"Groq: {e}")

        # MiniMax Models
        if self.keys['minimax'] and self.keys['minimax_group_id']:
            try:
                self.models.update({
                    'minimax-m2': {
                        'name': 'MiniMax M2',
                        'client': 'minimax',
                        'desc': '🌟 متقدم ومتطور',
                        'speed': 'سريع'
                    },
                })
                print(f"{self.theme['success']}✅ تم تحميل نماذج MiniMax{self.theme['end']}")
            except Exception as e:
                errors.append(f"MiniMax: {e}")

        # Cohere Models
        if self.keys['cohere']:
            try:
                self.clients['cohere'] = OpenAI(
                    api_key=self.keys['cohere'],
                    base_url="https://api.cohere.ai/v1"
                )
                self.models.update({
                    'command-r': {
                        'name': 'Command R',
                        'client': 'cohere',
                        'desc': '💡 متوازن ومفيد',
                        'speed': 'سريع'
                    },
                })
                print(f"{self.theme['success']}✅ تم تحميل نماذج Cohere{self.theme['end']}")
            except Exception as e:
                errors.append(f"Cohere: {e}")

        # عرض الأخطاء إن وجدت
        if errors:
            print(f"\n{self.theme['warning']}⚠️ بعض النماذج لم يتم تحميلها:{self.theme['end']}")
            for error in errors:
                print(f"  • {error}")

        # إحصائيات سريعة
        if self.models:
            print(f"\n{self.theme['bold']}{self.theme['success']}✨ تم تحميل {len(self.models)} نموذج بنجاح!{self.theme['end']}\n")
        else:
            print(f"\n{self.theme['warning']}❌ لم يتم تحميل أي نماذج! تأكد من مفاتيح API{self.theme['end']}\n")

    def load_conversations(self):
        """تحميل المحادثات"""
        if self.conversations_dir.exists():
            for file in self.conversations_dir.glob("*.json"):
                try:
                    with open(file, 'r', encoding='utf-8') as f:
                        chat_data = json.load(f)
                        chat_id = file.stem
                        self.conversations[chat_id] = chat_data
                except Exception as e:
                    print(f"{self.theme['warning']}⚠️ خطأ في تحميل المحادثة {file}: {e}{self.theme['end']}")

    def save_conversation(self, chat_id, conversation):
        """حفظ المحادثة"""
        try:
            filename = self.conversations_dir / f"{chat_id}.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(conversation, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"{self.theme['warning']}⚠️ خطأ في حفظ المحادثة: {e}{self.theme['end']}")
            return False

    def load_usage_stats(self):
        """تحميل إحصائيات الاستخدام"""
        if self.stats_file.exists():
            try:
                with open(self.stats_file, 'r') as f:
                    self.usage_stats = json.load(f)
            except:
                self.usage_stats = {}

    def update_usage_stats(self, model_id):
        """تحديث الإحصائيات"""
        if model_id not in self.usage_stats:
            self.usage_stats[model_id] = {'count': 0, 'last_used': None}

        self.usage_stats[model_id]['count'] += 1
        self.usage_stats[model_id]['last_used'] = datetime.now().isoformat()

    def save_usage_stats(self):
        """حفظ الإحصائيات"""
        try:
            with open(self.stats_file, 'w') as f:
                json.dump(self.usage_stats, f, indent=2)
        except Exception as e:
            print(f"{self.theme['warning']}⚠️ خطأ في حفظ الإحصائيات: {e}{self.theme['end']}")

    def show_models(self):
        """عرض النماذج"""
        if not self.models:
            print(f"\n{self.theme['warning']}⚠️ لا توجد نماذج متاحة{self.theme['end']}\n")
            return None

        print(f"\n{self.theme['bold']}{self.theme['primary']}📋 النماذج المتاحة ({len(self.models)} نموذج):{self.theme['end']}")
        print("="*70)

        model_list = []
        for i, (model_id, info) in enumerate(self.models.items(), 1):
            stats = ""
            if model_id in self.usage_stats:
                count = self.usage_stats[model_id]['count']
                stats = f" (استُخدم {count} مرة)"

            print(f"{i:2d}. {info['name']:<25} - {info['desc']}{stats}")
            print(f"    ⚡ السرعة: {info.get('speed', 'متوسط')}")
            print()
            model_list.append((model_id, info))

        return model_list

    def new_conversation(self):
        """إنشاء محادثة جديدة"""
        self.current_chat_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.conversations[self.current_chat_id] = {
            'title': 'محادثة جديدة',
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'messages': []
        }
        return self.current_chat_id

    def chat_with_model(self, model_id, prompt, save_to_history=True):
        """دردشة مع نموذج محدد - إصدار محسن"""
        if model_id not in self.models:
            raise ValueError(f"النموذج {model_id} غير متوفر")

        model_info = self.models[model_id]
        client_type = model_info['client']

        try:
            # OpenAI
            if client_type == 'openai':
                response = self.clients['openai'].chat.completions.create(
                    model=model_id,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=2000,
                    temperature=0.7
                )
                result = response.choices[0].message.content

            # Google
            elif client_type == 'google':
                if not GOOGLE_AVAILABLE:
                    raise Exception("مكتبة google-generativeai غير مثبتة")
                model = self.clients['google'].GenerativeModel(model_id)
                response = model.generate_content(prompt)
                result = response.text

            # Anthropic
            elif client_type == 'anthropic':
                response = self.clients['anthropic'].messages.create(
                    model=model_id,
                    max_tokens=2000,
                    messages=[{"role": "user", "content": prompt}]
                )
                result = response.content[0].text

            # Groq
            elif client_type == 'groq':
                response = self.clients['groq'].chat.completions.create(
                    model=model_id,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=2000,
                    temperature=0.7
                )
                result = response.choices[0].message.content

            # MiniMax
            elif client_type == 'minimax':
                headers = {
                    'Authorization': f'Bearer {self.keys["minimax"]}',
                    'Content-Type': 'application/json'
                }
                data = {
                    'model': 'minimax-m2',
                    'messages': [{"role": "user", "content": prompt}],
                    'max_tokens': 2000,
                    'temperature': 0.7
                }
                response = requests.post(
                    f"https://api.minimax.io/v1/text/chatcompletion?GroupId={self.keys['minimax_group_id']}",
                    headers=headers,
                    json=data,
                    timeout=30
                )
                result = response.json()['choices'][0]['message']['content']

            # Cohere
            elif client_type == 'cohere':
                response = self.clients['cohere'].chat.completions.create(
                    model=model_id,
                    message=prompt,
                    max_tokens=2000
                )
                result = response.text

            else:
                raise Exception(f"نوع العميل غير مدعوم: {client_type}")

            # تحديث الإحصائيات
            self.update_usage_stats(model_id)

            # حفظ في التاريخ
            if save_to_history and self.current_chat_id:
                self.conversations[self.current_chat_id]['messages'].append({
                    'role': 'user',
                    'content': prompt,
                    'timestamp': datetime.now().isoformat()
                })
                self.conversations[self.current_chat_id]['messages'].append({
                    'role': 'assistant',
                    'content': result,
                    'model': model_id,
                    'timestamp': datetime.now().isoformat()
                })

            return result

        except requests.exceptions.Timeout:
            raise Exception("انتهت مهلة الاتصال، يرجى المحاولة مرة أخرى")
        except requests.exceptions.ConnectionError:
            raise Exception("خطأ في الاتصال، تحقق من الإنترنت")
        except Exception as e:
            raise Exception(f"خطأ في النموذج {model_id}: {str(e)}")

    def generate_image(self, prompt, model='dall-e-3'):
        """توليد صورة - إصدار محسن"""
        if not self.keys['openai']:
            print(f"{self.theme['warning']}⚠️ مطلوب مفتاح OpenAI لتوليد الصور{self.theme['end']}")
            return None

        print(f"\n{self.theme['info']}🎨 جاري توليد الصورة...{self.theme['end']}")
        print(f"{self.theme['info']}الوصف: {prompt}{self.theme['end']}")

        try:
            response = self.clients['openai'].images.generate(
                model=model,
                prompt=prompt,
                size='1024x1024',
                n=1,
                quality='hd' if model == 'dall-e-3' else 'standard'
            )

            image_url = response.data[0].url
            print(f"\n{self.theme['success']}✅ تم توليد الصورة بنجاح!{self.theme['end']}")
            print(f"{self.theme['info']}رابط الصورة: {image_url}{self.theme['end']}")

            # تحميل الصورة
            response_img = requests.get(image_url)
            if response_img.status_code == 200:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = Path.home() / f"ai_image_{timestamp}.png"
                with open(filename, 'wb') as f:
                    f.write(response_img.content)
                print(f"{self.theme['success']}✅ تم حفظ الصورة: {filename}{self.theme['end']}")

            return image_url

        except Exception as e:
            print(f"{self.theme['warning']}⚠️ خطأ في توليد الصورة: {e}{self.theme['end']}")
            return None

    def search_web(self, query, engine='serper'):
        """البحث في الإنترنت - إصدار محسن"""
        if engine == 'serper' and not self.keys['serper']:
            print(f"{self.theme['warning']}⚠️ مفتاح Serper غير متوفر{self.theme['end']}")
            print(f"{self.theme['info']}💡 يمكنك استخدام بحث Google مباشرة عبر المتصفح{self.theme['end']}")
            return

        if engine == 'tavily' and not self.keys['tavily']:
            print(f"{self.theme['warning']}⚠️ مفتاح Tavily غير متوفر{self.theme['end']}")
            print(f"{self.theme['info']}💡 يمكنك استخدام بحث Google مباشرة عبر المتصفح{self.theme['end']}")
            return

        print(f"\n{self.theme['info']}🔍 جاري البحث...{self.theme['end']}")
        print(f"{self.theme['info']}السؤال: {query}{self.theme['end']}")

        try:
            if engine == 'serper':
                url = "https://google.serper.dev/search"
                headers = {
                    'X-API-KEY': self.keys['serper'],
                    'Content-Type': 'application/json'
                }
                payload = {
                    'q': query,
                    'num': 5
                }
                response = requests.post(url, headers=headers, json=payload, timeout=10)
                data = response.json()

                print(f"\n{self.theme['bold']}{self.theme['primary']}🔍 نتائج البحث:{self.theme['end']}")
                print("="*70)

                for i, result in enumerate(data.get('organic', [])[:5], 1):
                    print(f"\n{i}. {self.theme['cyan']}{result.get('title', 'بدون عنوان')}{self.theme['end']}")
                    print(f"   {result.get('link', '')}")
                    print(f"   📝 {result.get('snippet', 'لا يوجد وصف')}")

            elif engine == 'tavily':
                url = "https://api.tavily.com/search"
                payload = {
                    'api_key': self.keys['tavily'],
                    'query': query,
                    'max_results': 5
                }
                response = requests.post(url, json=payload, timeout=10)
                data = response.json()

                print(f"\n{self.theme['bold']}{self.theme['primary']}🔍 نتائج البحث:{self.theme['end']}")
                print("="*70)

                for i, result in enumerate(data.get('results', [])[:5], 1):
                    print(f"\n{i}. {self.theme['cyan']}{result.get('title', 'بدون عنوان')}{self.theme['end']}")
                    print(f"   {result.get('url', '')}")
                    print(f"   📝 {result.get('content', 'لا يوجد وصف')}")

        except requests.exceptions.Timeout:
            print(f"{self.theme['warning']}⚠️ انتهت مهلة البحث، يرجى المحاولة مرة أخرى{self.theme['end']}")
        except requests.exceptions.ConnectionError:
            print(f"{self.theme['warning']}⚠️ خطأ في الاتصال{self.theme['end']}")
        except Exception as e:
            print(f"{self.theme['warning']}⚠️ خطأ في البحث: {e}{self.theme['end']}")

    def analyze_file(self, file_path):
        """تحليل ملف نصي بسيط"""
        file_path = Path(file_path)

        if not file_path.exists():
            print(f"{self.theme['warning']}⚠️ الملف غير موجود{self.theme['end']}")
            return None

        try:
            # قراءة الملفات النصية فقط لتجنب مشاكل التثبيت
            ext = file_path.suffix.lower()

            if ext in ['.txt', '.md', '.json', '.csv', '.py', '.js', '.html', '.css']:
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()

                print(f"\n{self.theme['primary']}📊 تحليل الملف: {file_path.name}{self.theme['end']}")
                print(f"{self.theme['info']}📏 الحجم: {file_path.stat().st_size / 1024:.2f} KB{self.theme['end']}")
                print(f"{self.theme['info']}📝 عدد الأحرف: {len(text):,}{self.theme['end']}")
                print(f"{self.theme['info']}📄 عدد الكلمات: {len(text.split()):,}{self.theme['end']}")
                print()

                return text
            else:
                print(f"{self.theme['warning']}⚠️ نوع الملف غير مدعوم للتقليل. الملفات المدعومة: .txt, .md, .json, .csv, .py, .js, .html, .css{self.theme['end']}")
                return None

        except Exception as e:
            print(f"{self.theme['warning']}⚠️ خطأ في تحليل الملف: {e}{self.theme['end']}")
            return None

    def show_usage_stats(self):
        """عرض إحصائيات الاستخدام"""
        print(f"\n{self.theme['bold']}{self.theme['purple']}📊 إحصائيات الاستخدام:{self.theme['end']}")
        print("="*70)

        if not self.usage_stats:
            print(f"{self.theme['info']}📈 لا توجد إحصائيات بعد{self.theme['end']}")
            return

        # ترتيب حسب الاستخدام
        sorted_stats = sorted(
            self.usage_stats.items(),
            key=lambda x: x[1]['count'],
            reverse=True
        )

        for model_id, stats in sorted_stats:
            model_name = self.models.get(model_id, {}).get('name', model_id)
            count = stats['count']
            last_used = stats.get('last_used', 'لم يُستخدم')
            print(f"{self.theme['cyan']}{model_name:<30}{self.theme['end']} - استخدام: {count} مرة")
            print(f"{self.theme['info']}آخر استخدام: {last_used}{self.theme['end']}")
            print("-"*70)

    def show_help(self):
        """عرض المساعدة"""
        help_text = f"""
{self.theme['bold']}{self.theme['purple']}📖 دليل الاستخدام المحسن:{self.theme['end']}
{"="*70}

{self.theme['cyan']}الأوامر الأساسية:{self.theme['end']}
  exit                 - خروج وحفظ المحادثة
  save                 - حفظ المحادثة الحالية
  help                 - عرض هذه القائمة
  clear                - مسح الشاشة

{self.theme['cyan']}إدارة النماذج:{self.theme['end']}
  models               - عرض النماذج
  change [model]       - تبديل النموذج

{self.theme['cyan']}الميزات المتقدمة:{self.theme['end']}
  search [query]       - البحث في الإنترنت (مطلوب مفتاح)
  generate [prompt]    - توليد صورة (مطلوب OpenAI)
  stats                - عرض إحصائيات الاستخدام

{self.theme['cyan']}أمثلة:{self.theme['end']}
  search أحدث أخبار الذكاء الاصطناعي
  generate منظر طبيعي جميل
  models
  stats

{"="*70}
        """
        print(help_text)

    def run_chat(self):
        """تشغيل الدردشة التفاعلية"""
        if not self.models:
            print(f"{self.theme['warning']}⚠️ لا توجد نماذج متاحة{self.theme['end']}")
            return

        # إنشاء محادثة جديدة
        chat_id = self.new_conversation()
        print(f"\n{self.theme['success']}✅ تم إنشاء محادثة جديدة{self.theme['end']}\n")

        # اختيار النموذج
        model_list = self.show_models()
        if not model_list:
            return

        choice = input(f"\n{self.theme['cyan']}اختر رقم النموذج: {self.theme['end']}").strip()

        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(model_list):
                current_model_id, current_model_info = model_list[idx]
                print(f"\n{self.theme['success']}✅ تم اختيار: {current_model_info['name']}{self.theme['end']}\n")
            else:
                print(f"{self.theme['warning']}⚠️ رقم غير صحيح{self.theme['end']}")
                return
        else:
            print(f"{self.theme['warning']}⚠️ يرجى إدخال رقم صحيح{self.theme['end']}")
            return

        # حلقة الدردشة
        print(f"{self.theme['bold']}{self.theme['primary']}💬 اكتب 'help' للمساعدة أو 'exit' للخروج{self.theme['end']}\n")

        while True:
            try:
                user_input = input(f"{self.theme['bold']}👤 أنت: {self.theme['end']}")

                if user_input.lower() == 'exit':
                    self.save_conversation(chat_id, self.conversations[chat_id])
                    self.save_usage_stats()
                    print(f"\n{self.theme['success']}✅ تم حفظ المحادثة والإحصائيات{self.theme['end']}")
                    print(f"{self.theme['primary']}🎉 شكراً لاستخدام AI Workspace!{self.theme['end']}\n")
                    break

                elif user_input.lower() == 'help':
                    self.show_help()
                    continue

                elif user_input.lower() == 'models':
                    self.show_models()
                    continue

                elif user_input.lower() == 'stats':
                    self.show_usage_stats()
                    continue

                elif user_input.lower() == 'clear':
                    os.system('clear' if os.name == 'posix' else 'cls')
                    self.print_banner()
                    continue

                elif user_input.lower().startswith('change '):
                    new_model_name = user_input.split(' ', 1)[1]
                    # البحث عن النموذج بالاسم
                    found = False
                    for mid, info in self.models.items():
                        if info['name'].lower() == new_model_name.lower():
                            current_model_id = mid
                            current_model_info = info
                            found = True
                            print(f"\n{self.theme['success']}✅ تم التبديل إلى: {current_model_info['name']}{self.theme['end']}\n")
                            break

                    if not found:
                        print(f"{self.theme['warning']}⚠️ نموذج غير موجود{self.theme['end']}")
                    continue

                elif user_input.lower().startswith('search '):
                    query = user_input[7:]
                    self.search_web(query)
                    continue

                elif user_input.lower().startswith('generate '):
                    prompt = user_input[9:]
                    self.generate_image(prompt)
                    continue

                else:
                    # دردشة عادية
                    print(f"\n{self.theme['cyan']}🤖 {current_model_info['name']}:{self.theme['end']}")
                    print(f"{self.theme['info']}⏳ جاري المعالجة...{self.theme['end']}")

                    try:
                        response = self.chat_with_model(current_model_id, user_input)
                        print(f"\n{response}\n")
                    except Exception as e:
                        print(f"\n{self.theme['warning']}⚠️ خطأ: {e}{self.theme['end']}\n")

            except KeyboardInterrupt:
                print(f"\n\n{self.theme['info']}تم المقاطعة بواسطة المستخدم{self.theme['end']}")
                if chat_id:
                    self.save_conversation(chat_id, self.conversations[chat_id])
                break
            except Exception as e:
                print(f"\n{self.theme['warning']}⚠️ خطأ غير متوقع: {e}{self.theme['end']}\n")

    def run(self):
        """تشغيل التطبيق"""
        self.run_chat()


def main():
    """الدالة الرئيسية"""
    try:
        app = AIWorkspaceFixed()
        app.run()
    except KeyboardInterrupt:
        print(f"\n{self.theme['info']}تم إنهاء البرنامج{self.theme['end']}")
    except Exception as e:
        print(f"\n{self.theme['warning']}⚠️ خطأ عام: {e}{self.theme['end']}")


if __name__ == "__main__":
    main()
