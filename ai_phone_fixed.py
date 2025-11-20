#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📱 AI Phone Fixed - تطبيق الهاتف المحسن
واجهة محسنة وسهلة الاستخدام على الهاتف
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path
import time
import shutil

# استيراد المشروع المحسن
from ai_workspace_fixed import AIWorkspaceFixed

class AIPhoneFixed(AIWorkspaceFixed):
    """📱 تطبيق الهاتف المحسن"""

    def __init__(self):
        """تهيئة تطبيق الهاتف المحسن"""
        super().__init__()
        self.screen_width = shutil.get_terminal_size().columns
        self.screen_height = shutil.get_terminal_size().lines
        self.setup_phone_theme()

    def setup_phone_theme(self):
        """إعداد ثيم الهاتف المحسن"""
        # ألوان محسنة
        self.colors = {
            'primary': '\033[96m',      # أزرق فاتح
            'secondary': '\033[95m',    # بنفسجي
            'success': '\033[92m',      # أخضر
            'warning': '\033[93m',      # أصفر
            'danger': '\033[91m',       # أحمر
            'info': '\033[94m',         # أزرق
            'light': '\033[97m',        # أبيض
            'dark': '\033[90m',         # رمادي
            'bold': '\033[1m',
            'end': '\033[0m',
            'cyan': '\033[36m',         # تركوازي
            'purple': '\033[95m',       # بنفسجي
        }

        # أيقونات جميلة
        self.icons = {
            'home': '🏠',
            'chat': '💬',
            'image': '🎨',
            'search': '🔍',
            'translate': '🌐',
            'settings': '⚙️',
            'stats': '📊',
            'files': '📁',
            'model': '🤖',
            'star': '⭐',
            'fire': '🔥',
            'rocket': '🚀',
            'check': '✅',
            'cross': '❌',
        }

    def clear_screen(self):
        """مسح الشاشة"""
        os.system('clear' if os.name == 'posix' else 'cls')

    def print_header(self, title, icon=None):
        """طباعة رأس الصفحة"""
        icon = icon or self.icons['home']
        width = min(self.screen_width, 60)

        print(f"\n{self.colors['primary']}{self.colors['bold']}")
        print("╔" + "═" * (width - 2) + "╗")
        print(f"║ {icon} {title:<{width - 7}} ║")
        print("╚" + "═" * (width - 2) + "╝")
        print(f"{self.colors['end']}\n")

    def get_user_choice(self, max_choice):
        """الحصول على اختيار المستخدم مع التحقق المحسن"""
        while True:
            try:
                choice = input(f"{self.colors['bold']}{self.colors['primary']}➤{self.colors['end']} ")
                if choice == '0':
                    return 0
                choice_num = int(choice)
                if 1 <= choice_num <= max_choice:
                    return choice_num
                else:
                    print(f"{self.colors['warning']}⚠️ اختر رقم من 1 إلى {max_choice} أو 0 للعودة{self.colors['end']}")
            except (ValueError, EOFError):
                print(f"{self.colors['warning']}⚠️ أدخل رقماً صحيحاً{self.colors['end']}")
                time.sleep(0.5)

    def show_home_screen(self):
        """الشاشة الرئيسية المحسنة"""
        self.clear_screen()

        # ترحيب جميل
        print(f"\n{self.colors['primary']}{self.colors['bold']}")
        print("╔════════════════════════════════════════════════════════════╗")
        print("║            📱 AI Phone Fixed - التطبيق المحسن              ║")
        print("║                    🚀 سريع ومستقر 🚀                      ║")
        print("╚════════════════════════════════════════════════════════════╝")
        print(f"{self.colors['end']}\n")

        # معلومات سريعة
        print(f"{self.colors['bold']}{self.colors['success']}✨ المميزات:{self.colors['end']}")
        print(f"  {self.icons['chat']} 15+ نموذج ذكاء اصطناعي")
        print(f"  {self.icons['image']} توليد صور (DALL-E)")
        print(f"  {self.icons['search']} بحث ذكي")
        print(f"  {self.icons['stats']} إحصائيات مفصلة")

        # عدد النماذج
        if self.models:
            print(f"\n{self.colors['bold']}{self.colors['success']}🎯 النماذج المتاحة: {len(self.models)} نموذج{self.colors['end']}")
        else:
            print(f"\n{self.colors['warning']}⚠️ لا توجد نماذج متاحة - قم بإعداد API Keys{self.colors['end']}")

        print(f"\n{self.colors['bold']}{self.colors['cyan']}─" * 50 + f"{self.colors['end']}\n")

        # قائمة محسنة
        print(f"{self.colors['bold']}{self.colors['cyan']}📋 الخيارات:{self.colors['end']}\n")
        print(f"  1️⃣ {self.icons['chat']} بدء دردشة")
        print(f"  2️⃣ {self.icons['model']} عرض النماذج")
        print(f"  3️⃣ {self.icons['image']} توليد صور")
        print(f"  4️⃣ {self.icons['search']} البحث")
        print(f"  5️⃣ {self.icons['stats']} الإحصائيات")
        print(f"  6️⃣ {self.icons['files']} تحليل الملفات")
        print(f"  7️⃣ {self.icons['settings']} الإعدادات")

        print(f"\n{self.colors['dark']}0. خروج{self.colors['end']}")

    def show_models_screen(self):
        """شاشة عرض النماذج"""
        self.clear_screen()
        self.print_header("النماذج المتاحة", self.icons['model'])

        if not self.models:
            print(f"{self.colors['warning']}⚠️ لا توجد نماذج متاحة{self.colors['end']}")
            print(f"{self.colors['info']}💡 قم بإعداد API Keys أولاً{self.colors['end']}")
            input("\nاضغط Enter للعودة...")
            return

        # عرض النماذج مع الإحصائيات
        model_list = []
        for model_id, info in self.models.items():
            stats = ""
            if model_id in self.usage_stats:
                count = self.usage_stats[model_id]['count']
                stats = f" (استُخدم {count} مرة)"

            print(f"{self.colors['cyan']}• {info['name']}{stats}{self.colors['end']}")
            print(f"  {info['desc']}")
            print(f"  ⚡ {info.get('speed', 'متوسط')}\n")
            model_list.append((model_id, info))

        input("\nاضغط Enter للعودة...")

    def chat_screen(self):
        """شاشة الدردشة المحسنة"""
        self.clear_screen()
        self.print_header("بدء الدردشة", self.icons['chat'])

        if not self.models:
            print(f"{self.colors['warning']}⚠️ لا توجد نماذج متاحة{self.colors['end']}")
            input("اضغط Enter للعودة...")
            return

        # عرض النماذج للاختيار
        model_list = []
        for i, (model_id, info) in enumerate(self.models.items(), 1):
            print(f"{i}. {info['name']} - {info['desc']}")
            model_list.append((model_id, info))

        print("\n0. عودة")
        choice = self.get_user_choice(len(model_list))

        if choice == 0:
            return

        selected_model_id, selected_model_info = model_list[choice - 1]

        # بدء الدردشة
        self.clear_screen()
        self.print_header(f"دردشة: {selected_model_info['name']}", self.icons['chat'])

        # إنشاء محادثة جديدة
        chat_id = self.new_conversation()
        print(f"{self.colors['success']}✅ تم إنشاء محادثة جديدة{self.colors['end']}\n")
        print(f"{self.colors['info']}💡 اكتب 'exit' للخروج أو 'help' للمساعدة{self.colors['end']}\n")

        # حلقة الدردشة
        while True:
            try:
                user_input = input(f"{self.colors['bold']}👤 {self.colors['end']}")

                if user_input.lower() == 'exit':
                    self.save_conversation(chat_id, self.conversations[chat_id])
                    self.save_usage_stats()
                    print(f"\n{self.colors['success']}✅ تم حفظ المحادثة!{self.colors['end']}")
                    input("اضغط Enter للعودة...")
                    break

                elif user_input.lower() == 'help':
                    self.show_mobile_help()
                    continue

                elif user_input.lower() == 'clear':
                    self.clear_screen()
                    self.print_header(f"دردشة: {selected_model_info['name']}", self.icons['chat'])
                    continue

                else:
                    print(f"\n{self.colors['cyan']}🤖 {selected_model_info['name']}:{self.colors['end']}")
                    print(f"{self.colors['info']}⏳ جاري الكتابة...{self.colors['end']}")

                    try:
                        response = self.chat_with_model(selected_model_id, user_input)
                        print(f"\n{response}\n")
                    except Exception as e:
                        print(f"\n{self.colors['danger']}❌ خطأ: {e}{self.colors['end']}\n")

            except KeyboardInterrupt:
                print("\n")
                self.save_conversation(chat_id, self.conversations[chat_id])
                break
            except EOFError:
                print(f"\n{self.colors['warning']}⚠️ تم المقاطعة{self.colors['end']}")
                self.save_conversation(chat_id, self.conversations[chat_id])
                break
            except Exception as e:
                print(f"\n{self.colors['danger']}❌ خطأ: {e}{self.colors['end']}\n")
                time.sleep(1)

    def generate_image_screen(self):
        """شاشة توليد الصور المحسنة"""
        self.clear_screen()
        self.print_header("توليد الصور", self.icons['image'])

        if not self.keys['openai']:
            print(f"{self.colors['warning']}⚠️ مطلوب مفتاح OpenAI لتوليد الصور{self.colors['end']}")
            print(f"{self.colors['info']}💡 قم بإعداده في python3 setup_keys.py{self.colors['end']}")
            input("\nاضغط Enter للعودة...")
            return

        print(f"{self.colors['info']}أمثلة: قطة جميلة، منظر طبيعي، شعار شركة{self.colors['end']}\n")

        try:
            prompt = input(f"{self.colors['bold']}🎨 اكتب وصف الصورة: {self.colors['end']}").strip()

            if not prompt:
                return

            print(f"\n{self.colors['info']}اختر النموذج:{self.colors['end']}")
            print(f"1. DALL-E 3 (عالية الجودة)")
            print(f"2. DALL-E 2 (سريع)")
            choice = self.get_user_choice(2)

            model = 'dall-e-3' if choice == 1 else 'dall-e-2'

            self.generate_image(prompt, model)
            input("\nاضغط Enter للعودة...")

        except (EOFError, KeyboardInterrupt):
            print("\n")

    def search_screen(self):
        """شاشة البحث المحسنة"""
        self.clear_screen()
        self.print_header("البحث في الإنترنت", self.icons['search'])

        if not (self.keys['serper'] or self.keys['tavily']):
            print(f"{self.colors['warning']}⚠️ مطلوب مفتاح بحث (Serper أو Tavily){self.colors['end']}")
            print(f"{self.colors['info']}💡 أو استخدم Google مباشرة عبر المتصفح{self.colors['end']}")
            print(f"\n{self.colors['cyan']}للحصول على مفتاح Serper (مجاني):{self.colors['end']}")
            print(f"  https://console.groq.com")
            input("\nاضغط Enter للعودة...")
            return

        try:
            query = input(f"{self.colors['bold']}🔍 اكتب سؤالك: {self.colors['end']}").strip()

            if not query:
                return

            # اختيار محرك البحث
            engines = []
            if self.keys['serper']:
                engines.append('Serper')
            if self.keys['tavily']:
                engines.append('Tavily')

            print(f"\n{self.colors['info']}اختر محرك البحث:{self.colors['end']}")
            for i, eng in enumerate(engines, 1):
                print(f"{i}. {eng}")

            choice = self.get_user_choice(len(engines))
            engine = engines[choice - 1].lower()

            self.search_web(query, engine)
            input("\nاضغط Enter للعودة...")

        except (EOFError, KeyboardInterrupt):
            print("\n")

    def stats_screen(self):
        """شاشة الإحصائيات المحسنة"""
        self.clear_screen()
        self.print_header("الإحصائيات", self.icons['stats'])

        self.show_usage_stats()

        # إحصائيات إضافية
        total_messages = sum(len(chat.get('messages', [])) for chat in self.conversations.values())

        print(f"\n{self.colors['bold']}{self.colors['primary']}📊 إحصائيات إضافية:{self.colors['end']}")
        print(f"  💬 إجمالي المحادثات: {len(self.conversations)}")
        print(f"  📝 إجمالي الرسائل: {total_messages}")
        print(f"  🤖 النماذج المتاحة: {len(self.models)}")

        input("\nاضغط Enter للعودة...")

    def files_screen(self):
        """شاشة تحليل الملفات المحسنة"""
        self.clear_screen()
        self.print_header("تحليل الملفات", self.icons['files'])

        print(f"{self.colors['info']}الملفات المدعومة: .txt, .md, .json, .csv, .py, .js, .html, .css{self.colors['end']}\n")

        try:
            file_path = input(f"{self.colors['bold']}📁 مسار الملف: {self.colors['end']}").strip()

            if not file_path:
                return

            text = self.analyze_file(file_path)

            if text and self.models:
                print(f"\n{self.colors['info']}جاري إرسال الملف لـ AI للتحليل...{self.colors['end']}")
                first_model_id = list(self.models.keys())[0]
                first_model_name = self.models[first_model_id]['name']

                print(f"{self.colors['info']}الاستخدام: {first_model_name}{self.colors['end']}")

                try:
                    analysis = self.chat_with_model(
                        first_model_id,
                        f"حلل هذا النص وقدم ملخصاً مفيداً:\n\n{text[:1500]}"
                    )
                    print(f"\n{self.colors['success']}✅ التحليل:{self.colors['end']}")
                    print(analysis)
                except Exception as e:
                    print(f"{self.colors['danger']}❌ خطأ في التحليل: {e}{self.colors['end']}")

            input("\nاضغط Enter للعودة...")

        except (EOFError, KeyboardInterrupt):
            print("\n")

    def settings_screen(self):
        """شاشة الإعدادات المحسنة"""
        self.clear_screen()
        self.print_header("الإعدادات", self.icons['settings'])

        print("1. عرض مفاتيح API")
        print("2. معلومات التطبيق")
        print("3. المساعدة")
        print("0. عودة")

        choice = self.get_user_choice(3)

        if choice == 1:
            self.clear_screen()
            print(f"\n{self.colors['bold']}{self.colors['primary']}مفاتيح API:{self.colors['end']}\n")
            for key, value in self.keys.items():
                status = "✅ موجود" if value else "❌ غير موجود"
                masked_value = value[:10] + "..." if value and len(value) > 10 else value
                print(f"  {key:<20} - {status} {masked_value or ''}")
            input("\nاضغط Enter للعودة...")

        elif choice == 2:
            self.clear_screen()
            print(f"\n{self.colors['bold']}{self.colors['purple']}ℹ️ معلومات التطبيق:{self.colors['end']}\n")
            print(f"  📱 الاسم: AI Phone Fixed")
            print(f"  🚀 النسخة: 2.0 - محسن")
            print(f"  📅 التاريخ: {datetime.now().strftime('%Y-%m-%d')}")
            print(f"  🐍 Python: {sys.version.split()[0]}")
            print(f"  💻 النظام: {os.name}")
            print(f"  🔧 المكتبات: {'✓' if self.models else '⚠️'}")
            input("\nاضغط Enter للعودة...")

        elif choice == 3:
            self.show_mobile_help()

    def show_mobile_help(self):
        """عرض المساعدة للهاتف المحسن"""
        help_text = f"""
{self.colors['bold']}{self.colors['purple']}📖 دليل الاستخدام:{self.colors['end']}
{self.colors['dark']}{'═' * 60}{self.colors['end']}

{self.colors['cyan']}💬 الدردشة:{self.colors['end']}
  - اختر نموذج من القائمة
  - اكتب سؤالك وانتظر الرد
  - 'exit' للخروج
  - 'clear' لمسح الشاشة

{self.colors['cyan']}🎨 توليد الصور:{self.colors['end']}
  - اكتب وصفاً واضحاً
  - DALL-E 3: جودة عالية
  - DALL-E 2: سريع
  - مطلوب OpenAI API Key

{self.colors['cyan']}🔍 البحث:{self.colors['end']}
  - مطلوب مفتاح Serper أو Tavily
  - أو استخدم Google مباشرة

{self.colors['cyan']}📁 تحليل الملفات:{self.colors['end']}
  - يدعم الملفات النصية
  - سيرسل الملف لـ AI للتحليل

{self.colors['dark']}{'═' * 60}{self.colors['end']}
        """
        print(help_text)
        input("اضغط Enter للعودة...")

    def run(self):
        """تشغيل تطبيق الهاتف المحسن"""
        self.clear_screen()

        # شاشة الترحيب
        print(f"\n{self.colors['primary']}{self.colors['bold']}")
        print("╔════════════════════════════════════════════════════════════╗")
        print("║           📱 AI Phone Fixed - التطبيق المحسن              ║")
        print("║                    🚀 مرحباً بك! 🚀                      ║")
        print("╚════════════════════════════════════════════════════════════╝")
        print(f"{self.colors['end']}\n")

        if not self.models:
            print(f"{self.colors['warning']}⚠️ لا توجد نماذج متاحة{self.colors['end']}")
            print(f"{self.colors['info']}💡 قم بإعداد API Keys: python3 setup_keys.py{self.colors['end']}")
            print(f"\n{self.colors['success']}الأساسيات المطلوبة:{self.colors['end']}")
            print(f"  • Groq (مجاني): https://console.groq.com")
            print(f"  • Anthropic (مجاني): https://console.anthropic.com")
            input("\nاضغط Enter للخروج...")
            return

        try:
            input(f"{self.colors['success']}✅ اضغط Enter للدخول...{self.colors['end']}")

            # حلقة التطبيق الرئيسية
            while True:
                self.show_home_screen()
                choice = input(f"\n{self.colors['bold']}{self.colors['primary']}➤{self.colors['end']} ")

                if choice == '0':
                    print(f"\n{self.colors['success']}🎉 شكراً لاستخدام AI Phone Fixed!{self.colors['end']}\n")
                    break

                elif choice == '1':
                    self.chat_screen()

                elif choice == '2':
                    self.show_models_screen()

                elif choice == '3':
                    self.generate_image_screen()

                elif choice == '4':
                    self.search_screen()

                elif choice == '5':
                    self.stats_screen()

                elif choice == '6':
                    self.files_screen()

                elif choice == '7':
                    self.settings_screen()

                else:
                    print(f"\n{self.colors['warning']}⚠️ خيار غير صحيح{self.colors['end']}")
                    time.sleep(1)

        except KeyboardInterrupt:
            print(f"\n\n{self.colors['info']}تم المقاطعة{self.colors['end']}")
        except EOFError:
            print(f"\n\n{self.colors['info']}تم الخروج{self.colors['end']}")
        except Exception as e:
            print(f"\n{self.colors['danger']}❌ خطأ: {e}{self.colors['end']}")


def main():
    """الدالة الرئيسية"""
    try:
        app = AIPhoneFixed()
        app.run()
    except Exception as e:
        print(f"\n❌ خطأ عام: {e}")


if __name__ == "__main__":
    main()
