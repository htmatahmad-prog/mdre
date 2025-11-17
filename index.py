#!/usr/bin/env python3
"""
📋 فهرس شامل لجميع ملفات المشروع
Complete Project Index
"""

import os
import sys
from datetime import datetime

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
    print(f"\n{Colors.CYAN}{'='*70}{Colors.END}")
    print(f"{Colors.WHITE}{Colors.BOLD}        📋 فهرس مشروع أدوات الذكاء الاصطناعي           {Colors.END}")
    print(f"{Colors.WHITE}{Colors.BOLD}            AI Tools Project Index                       {Colors.END}")
    print(f"{Colors.CYAN}{'='*70}{Colors.END}\n")

def show_summary():
    print(f"{Colors.BOLD}📊 ملخص المشروع:{Colors.END}\n")

    # عد الملفات
    py_files = [f for f in os.listdir('/data/data/com.termux/files/home') if f.endswith('.py')]
    sh_files = [f for f in os.listdir('/data/data/com.termux/files/home') if f.endswith('.sh')]
    md_files = [f for f in os.listdir('/data/data/com.termux/files/home') if f.endswith('.md')]
    env_exists = os.path.exists('/data/data/com.termux/files/home/.env')
    config_exists = os.path.exists('/data/data/com.termux/files/home/config/.env')

    print(f"{Colors.GREEN}•{Colors.END} ملفات Python: {Colors.CYAN}{len(py_files)}{Colors.END}")
    print(f"{Colors.GREEN}•{Colors.END} ملفات Shell: {Colors.CYAN}{len(sh_files)}{Colors.END}")
    print(f"{Colors.GREEN}•{Colors.END} ملفات Markdown: {Colors.CYAN}{len(md_files)}{Colors.END}")
    print(f"{Colors.GREEN}•{Colors.END} ملف .env: {Colors.GREEN+'✅ موجود' if env_exists else Colors.RED+'❌ مفقود'}{Colors.END}")
    print(f"{Colors.GREEN}•{Colors.END} مجلد config: {Colors.GREEN+'✅ موجود' if config_exists else Colors.RED+'❌ مفقود'}{Colors.END}")

    # تحقق من دليل الأدوات
    prompts_dir = '/data/data/com.termux/files/home/system-prompts-and-models-of-ai-tools'
    if os.path.exists(prompts_dir):
        md_count = len([f for f in os.listdir(prompts_dir) if f.endswith('.md')])
        print(f"{Colors.GREEN}•{Colors.END} دليل الأدوات: {Colors.CYAN}✅ موجود ({md_count} ملف){Colors.END}")
    else:
        print(f"{Colors.GREEN}•{Colors.END} دليل الأدوات: {Colors.RED}❌ مفقود{Colors.END}")

    print()

def show_files():
    print(f"{Colors.BOLD}📁 ملفات Python:{Colors.END}\n")

    py_files = [
        ('start.py', '🚀 التشغيل السريع - نقطة البداية'),
        ('ai_toolkit.py', '💬 مجموعة الأدوات الكاملة'),
        ('comprehensive_api_test.py', '🧪 اختبار شامل للـ APIs'),
        ('test_both_apis.py', '🔍 اختبار سريع OpenAI + Gemini'),
        ('api_test.py', '🔧 اختبار API عام'),
        ('test_openai_quick.py', '⚡ اختبار OpenAI سريع'),
        ('termux_ai_test.py', '📱 اختبار مخصص لـ Termux'),
        ('minimax_api.py', '🤖 اختبار Minimax API'),
        ('simple_ai_client.py', '👤 عميل AI بسيط'),
    ]

    for filename, desc in py_files:
        filepath = f'/data/data/com.termux/files/home/{filename}'
        if os.path.exists(filepath):
            print(f"{Colors.GREEN}✓{Colors.END} {Colors.WHITE}{filename:30}{Colors.END} - {desc}")
        else:
            print(f"{Colors.YELLOW}•{Colors.END} {Colors.WHITE}{filename:30}{Colors.END} - {Colors.YELLOW}{desc}{Colors.END}")

    print()

def show_commands():
    print(f"{Colors.BOLD}⚡ أوامر التشغيل:{Colors.END}\n")

    commands = [
        ('python3 start.py', '🚀 التشغيل السريع - الأفضل للبدء'),
        ('./menu.sh', '📋 القائمة التفاعلية'),
        ('python3 ai_toolkit.py', '💬 مجموعة الأدوات الكاملة'),
        ('python3 comprehensive_api_test.py', '🧪 اختبار شامل للـ APIs'),
        ('python3 test_both_apis.py', '🔍 اختبار سريع OpenAI + Gemini'),
        ('python3 api_test.py', '🔧 اختبار API عام'),
        ('ls -la system-prompts-and-models-of-ai-tools/', '📚 عرض دليل الأدوات'),
        ('cat README.md', '📖 قراءة الدليل الشامل'),
    ]

    for cmd, desc in commands:
        print(f"{Colors.CYAN}▶{Colors.END} {Colors.WHITE}{cmd:45}{Colors.END} - {desc}")

    print()

def show_setup():
    print(f"{Colors.BOLD}⚙️ خطوات الإعداد:{Colors.END}\n")

    print(f"{Colors.YELLOW}1.{Colors.END} تأكد من وجود ملف .env:")
    print(f"   {Colors.CYAN}cat /data/data/com.termux/files/home/.env{Colors.END}")
    print()

    print(f"{Colors.YELLOW}2.{Colors.END} أضف مفاتيح API الحقيقية:")
    print(f"   {Colors.CYAN}nano /data/data/com.termux/files/home/.env{Colors.END}")
    print(f"   {Colors.CYAN}vim /data/data/com.termux/files/home/.env{Colors.END}")
    print()

    print(f"{Colors.YELLOW}3.{Colors.END} احصل على مفاتيح API مجانية:")
    print(f"   {Colors.GREEN}•{Colors.END} OpenAI: https://platform.openai.com/api-keys ($5 مجاني)")
    print(f"   {Colors.GREEN}•{Colors.END} Gemini: https://makersuite.google.com/app/apikey (مجاني)")
    print(f"   {Colors.GREEN}•{Colors.END} Claude: https://console.anthropic.com/ ($5 مجاني)")
    print(f"   {Colors.GREEN}•{Colors.END} Hugging Face: https://huggingface.co/settings/tokens (مجاني)")
    print()

def show_apis():
    print(f"{Colors.BOLD}🔑 APIs المدعومة:{Colors.END}\n")

    apis = [
        ('OpenAI', 'GPT-4, GPT-3.5-turbo', '$5 رصيد مجاني'),
        ('Google Gemini', 'Gemini Pro, Pro Vision', 'مجاني بالكامل'),
        ('Anthropic Claude', 'Claude 3 Haiku, Sonnet, Opus', '$5 رصيد مجاني'),
        ('Hugging Face', '50,000+ نموذج', 'مجاني'),
        ('Serper', 'Google Search API', '2,500 بحث/شهر مجاناً'),
        ('Tavily', 'AI Search', '1,000 بحث/شهر مجاناً'),
        ('ElevenLabs', 'Text to Speech', '10,000 حرف/شهر مجاناً'),
        ('Replicate', 'Stable Diffusion, DALL-E', 'حسب الاستخدام'),
        ('GitHub Copilot', 'IDE Extension', '$10/شهر'),
    ]

    for name, models, limit in apis:
        print(f"{Colors.GREEN}✓{Colors.END} {Colors.WHITE}{name:20}{Colors.END} - {Colors.CYAN}{models:25}{Colors.END} - {Colors.YELLOW}{limit}{Colors.END}")

    print()

def main():
    print_header()
    show_summary()
    show_files()
    show_commands()
    show_setup()
    show_apis()

    print(f"{Colors.BOLD}{Colors.GREEN}✅ جاهز للاستخدام!{Colors.END}\n")
    print(f"{Colors.CYAN}{Colors.BOLD}ابدأ بـ: python3 start.py{Colors.END}\n")

if __name__ == "__main__":
    main()
