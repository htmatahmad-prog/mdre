#!/usr/bin/env python3
"""
🚀 تشغيل سريع لأدوات الذكاء الاصطناعي
Quick Start - AI Tools Launcher
"""

import os
import sys

# تحميل متغيرات البيئة
def load_env():
    """تحميل ملف .env"""
    env_file = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(env_file):
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    if value and value != "your_" + key.lower() + "_here":
                        os.environ[key] = value

# ألوان
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    WHITE = '\033[1;37m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_header():
    print(f"\n{Colors.CYAN}{'='*60}{Colors.END}")
    print(f"{Colors.WHITE}{Colors.BOLD}    🤖 أدوات الذكاء الاصطناعي - التشغيل السريع    {Colors.END}")
    print(f"{Colors.CYAN}{'='*60}{Colors.END}\n")

def show_menu():
    print(f"{Colors.BOLD}الخيارات المتاحة:{Colors.END}\n")
    print(f"{Colors.GREEN}1.{Colors.END} 🧪 اختبار APIs سريع")
    print(f"{Colors.GREEN}2.{Colors.END} 💬 تشغيل مجموعة الأدوات الكاملة")
    print(f"{Colors.GREEN}3.{Colors.END} 🔍 مقارنة OpenAI و Gemini")
    print(f"{Colors.GREEN}4.{Colors.END} 📚 عرض دليل الأدوات (30k+ سطر)")
    print(f"{Colors.GREEN}5.{Colors.END} ⚙️ فحص حالة APIs")
    print(f"{Colors.GREEN}6.{Colors.END} 🚀 تشغيل setup.sh (إعداد أولي)")
    print(f"{Colors.GREEN}0.{Colors.END} 🚪 خروج\n")

def main():
    load_env()
    print_header()
    show_menu()

    choice = input(f"{Colors.BOLD}{Colors.CYAN}اختر رقماً (0-6): {Colors.END}").strip()

    if choice == "1":
        print(f"\n{Colors.YELLOW}جاري تشغيل الاختبار السريع...{Colors.END}")
        os.system("python3 /data/data/com.termux/files/home/api_test.py")

    elif choice == "2":
        print(f"\n{Colors.YELLOW}جاري تشغيل مجموعة الأدوات...{Colors.END}")
        os.system("python3 /data/data/com.termux/files/home/ai_toolkit.py")

    elif choice == "3":
        print(f"\n{Colors.YELLOW}جاري تشغيل مقارنة APIs...{Colors.END}")
        os.system("python3 /data/data/com.termux/files/home/test_both_apis.py")

    elif choice == "4":
        print(f"\n{Colors.GREEN}📚 دليل الأدوات متوفر في:{Colors.END}")
        print(f"   {Colors.CYAN}/data/data/com.termux/files/home/system-prompts-and-models-of-ai-tools/{Colors.END}")
        print(f"\n{Colors.YELLOW}جرب الأوامر التالية:{Colors.END}")
        print(f"   ls -la /data/data/com.termux/files/home/system-prompts-and-models-of-ai-tools/")
        print(f"   cat /data/data/com.termux/files/home/system-prompts-and-models-of-ai-tools/README.md")

    elif choice == "5":
        print(f"\n{Colors.YELLOW}جاري تشغيل الفحص الشامل...{Colors.END}")
        os.system("python3 /data/data/com.termux/files/home/comprehensive_api_test.py")

    elif choice == "6":
        print(f"\n{Colors.YELLOW}جاري تشغيل الإعداد...{Colors.END}")
        os.system("bash /data/data/com.termux/files/home/setup.sh")

    elif choice == "0":
        print(f"\n{Colors.GREEN}👋 وداعاً!{Colors.END}\n")
        return

    else:
        print(f"\n{Colors.RED}❌ اختيار غير صحيح!{Colors.END}")

    input(f"\n{Colors.CYAN}اضغط Enter للعودة للقائمة الرئيسية...{Colors.END}")
    main()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.GREEN}👋 وداعاً!{Colors.END}\n")
