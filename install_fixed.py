#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 المثبت المحسن - تثبيت سريع ومضمون
تثبيت جميع المتطلبات بدون أخطاء
"""

import os
import sys
import subprocess
from pathlib import Path

def print_header():
    """عرض رأس جميل"""
    print("\n" + "="*70)
    print("🚀 المثبت المحسن لـ AI Workspace - تثبيت سريع ومضمون")
    print("="*70)
    print()

def print_step(step, message):
    """طباعة خطوة"""
    print(f"\n{step}. {message}")
    print("-" * 70)

def run_command(command, description):
    """تشغيل أمر مع عرض النتيجة"""
    print(f"   جاري تشغيل: {description}")
    print(f"   الأمر: {command}")

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=180
        )

        if result.returncode == 0:
            print(f"   ✅ نجح")
            return True
        else:
            print(f"   ⚠️ تحذير:")
            if result.stderr:
                print(f"      {result.stderr[:200]}")
            return False
    except subprocess.TimeoutExpired:
        print(f"   ❌ انتهت المهلة")
        return False
    except Exception as e:
        print(f"   ❌ خطأ: {e}")
        return False

def install_package(package, upgrade=True):
    """تثبيت مكتبة واحدة"""
    cmd = f"pip install {package}"
    if upgrade:
        cmd += " --upgrade"
    cmd += " --quiet --no-warn-script-location"

    return run_command(cmd, f"تثبيت {package}")

def check_python():
    """فحص إصدار Python"""
    print_step("فحص Python", "فحص إصدار Python")

    version = sys.version_info
    print(f"   الإصدار: {version.major}.{version.minor}.{version.micro}")

    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("   ❌ مطلوب Python 3.8 أو أحدث")
        return False

    print("   ✅ Python متوافق")
    return True

def install_basic_packages():
    """تثبيت المكتبات الأساسية"""
    print_step("المكتبات الأساسية", "تثبيت المكتبات الضرورية")

    # قائمة المكتبات الأساسية (بدون مكتبات ثقيلة)
    basic_packages = [
        "openai",
        "anthropic",
        "requests",
        "rich",
    ]

    success_count = 0
    for package in basic_packages:
        if install_package(package):
            success_count += 1

    print(f"\n   تم تثبيت {success_count}/{len(basic_packages)} مكتبة بنجاح")

    return success_count == len(basic_packages)

def install_optional_packages():
    """تثبيت المكتبات الاختيارية"""
    print_step("المكتبات الاختيارية", "تثبيت مكتبات اختيارية (Google, Flask)")

    # محاولة تثبيت Google (قد تفشل في Termux)
    print("\n   محاولة تثبيت google-generativeai...")
    if install_package("google-generativeai", upgrade=False):
        print("   ✅ تم تثبيت Google بنجاح")
    else:
        print("   ⚠️ لم يتم تثبيت Google (يمكن تثبيتها لاحقاً)")

    # محاولة تثبيت Flask
    print("\n   محاولة تثبيت Flask...")
    if install_package("flask", upgrade=False):
        print("   ✅ تم تثبيت Flask بنجاح")
    else:
        print("   ⚠️ لم يتم تثبيت Flask (يمكن تثبيتها لاحقاً)")

def create_shortcuts():
    """إنشاء اختصارات"""
    print_step("الاختصارات", "إنشاء اختصارات سهلة الاستخدام")

    shortcuts_dir = Path.home() / "ai_workspace_shortcuts"
    shortcuts_dir.mkdir(exist_ok=True)

    # إنشاء script للتطبيق المحسن
    phone_script = shortcuts_dir / "run_phone_fixed.sh"
    with open(phone_script, 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("# AI Phone Fixed - تشغيل التطبيق المحسن\n")
        f.write("cd /data/data/com.termux/files/home\n")
        f.write("python3 ai_phone_fixed.py\n")
    os.chmod(phone_script, 0o755)
    print(f"   ✅ تم إنشاء: {phone_script}")

    # إنشاء script للنسخة العادية
    normal_script = shortcuts_dir / "run_normal.sh"
    with open(normal_script, 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("# AI Workspace Fixed - تشغيل النسخة العادية\n")
        f.write("cd /data/data/com.termux/files/home\n")
        f.write("python3 ai_workspace_fixed.py\n")
    os.chmod(normal_script, 0o755)
    print(f"   ✅ تم إنشاء: {normal_script}")

    # إنشاء script لإعداد API Keys
    keys_script = shortcuts_dir / "setup_keys.sh"
    with open(keys_script, 'w') as f:
        f.write("#!/bin/bash\n")
        f.write("# Setup API Keys - إعداد مفاتيح API\n")
        f.write("cd /data/data/com.termux/files/home\n")
        f.write("python3 setup_keys.py\n")
    os.chmod(keys_script, 0o755)
    print(f"   ✅ تم إنشاء: {keys_script}")

    print(f"\n   📁 جميع الاختصارات في: {shortcuts_dir}")
    print(f"   يمكنك تشغيلها من Termux:")
    print(f"     bash ~/ai_workspace_shortcuts/run_phone_fixed.sh")
    print(f"     bash ~/ai_workspace_shortcuts/run_normal.sh")
    print(f"     bash ~/ai_workspace_shortcuts/setup_keys.sh")

def show_final_instructions():
    """عرض التعليمات النهائية"""
    print("\n" + "="*70)
    print("🎉 تم التثبيت بنجاح!")
    print("="*70)

    print("\n✨ الخطوات التالية:")
    print()
    print("1️⃣ إعداد مفاتيح API:")
    print("   python3 setup_keys.py")
    print()
    print("   المفاتيح الموصى بها:")
    print("   • Groq (مجاني وسريع): https://console.groq.com")
    print("   • Anthropic (مجاني): https://console.anthropic.com")
    print("   • OpenAI (مدفوع): https://platform.openai.com/api-keys")
    print()

    print("2️⃣ تشغيل التطبيق:")
    print("   python3 ai_phone_fixed.py      # تطبيق الهاتف المحسن")
    print("   python3 ai_workspace_fixed.py  # النسخة العادية")
    print()

    print("3️⃣ أو استخدام الاختصارات:")
    print("   bash ~/ai_workspace_shortcuts/run_phone_fixed.sh")
    print()

    print("="*70)

def main():
    """الدالة الرئيسية"""
    print_header()

    # فحص Python
    if not check_python():
        print("\n❌ يرجى تحديث Python إلى إصدار أحدث")
        return False

    # تثبيت المكتبات الأساسية
    if not install_basic_packages():
        print("\n⚠️ تحذير: لم يتم تثبيت جميع المكتبات الأساسية")
        print("   لكن يمكن للمشروع أن يعمل")
    else:
        print("\n✅ تم تثبيت جميع المكتبات الأساسية بنجاح")

    # تثبيت المكتبات الاختيارية
    install_optional_packages()

    # إنشاء اختصارات
    create_shortcuts()

    # عرض التعليمات النهائية
    show_final_instructions()

    return True

if __name__ == "__main__":
    try:
        success = main()
        if success:
            sys.exit(0)
        else:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n⚠️ تم إيقاف التثبيت بواسطة المستخدم")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ خطأ عام: {e}")
        sys.exit(1)
