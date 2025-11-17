#!/bin/bash

# 🔄 سكريبت تحديث أدوات الذكاء الاصطناعي
# AI Tools Update Script

set -e

# الألوان
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# إعدادات
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
UPDATE_LOG="$SCRIPT_DIR/update_log_$(date +%Y%m%d_%H%M%S).log"

# دالة الطباعة الملونة
print_color() {
    echo -e "${2}${1}${NC}"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$UPDATE_LOG"
}

# دالة للتحقق من وجود الأمر
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# تحديث npm packages
update_npm_packages() {
    print_color "📦 تحديث npm packages..." "$BLUE"

    if command_exists npm; then
        print_color "🔍 فحص npm packages المحدثة..." "$YELLOW"

        # قائمة الأدوات للتحديث
        local packages=(
            "@anthropic-ai/claude-code"
            "cline"
            "@bolt-js/bolt"
            "lumo-ai"
            "@google/generative-ai-cli"
            "roocode"
        )

        for package in "${packages[@]}"; do
            if npm list -g "$package" >/dev/null 2>&1; then
                print_color "🔄 تحديث $package..." "$CYAN"
                if npm install -g "$package" --force; then
                    print_color "✅ تم تحديث $package" "$GREEN"
                else
                    print_color "❌ فشل في تحديث $package" "$RED"
                fi
            else
                print_color "⚠️  $package غير مثبت - سيتم تثبيته" "$YELLOW"
                if npm install -g "$package"; then
                    print_color "✅ تم تثبيت $package" "$GREEN"
                else
                    print_color "❌ فشل في تثبيت $package" "$RED"
                fi
            fi
        done
    else
        print_color "❌ npm غير متوفر - تخطي تحديث npm packages" "$RED"
    fi
}

# تحديث pip packages
update_pip_packages() {
    print_color "🐍 تحديث pip packages..." "$BLUE"

    if command_exists pip3; then
        print_color "🔍 تحديث pip packages..." "$YELLOW"

        # قائمة الأدوات للتحديث
        local packages=("codex-cli")

        for package in "${packages[@]}"; do
            if pip3 show "$package" >/dev/null 2>&1; then
                print_color "🔄 تحديث $package..." "$CYAN"
                if pip3 install --upgrade "$package"; then
                    print_color "✅ تم تحديث $package" "$GREEN"
                else
                    print_color "❌ فشل في تحديث $package" "$RED"
                fi
            else
                print_color "⚠️  $package غير مثبت - سيتم تثبيته" "$YELLOW"
                if pip3 install "$package"; then
                    print_color "✅ تم تثبيت $package" "$GREEN"
                else
                    print_color "❌ فشل في تثبيت $package" "$RED"
                fi
            fi
        done
    elif command_exists pip; then
        print_color "🔍 تحديث pip packages (باستخدام pip)..." "$YELLOW"

        for package in "codex-cli"; do
            if pip show "$package" >/dev/null 2>&1; then
                print_color "🔄 تحديث $package..." "$CYAN"
                if pip install --upgrade "$package"; then
                    print_color "✅ تم تحديث $package" "$GREEN"
                else
                    print_color "❌ فشل في تحديث $package" "$RED"
                fi
            else
                print_color "⚠️  $package غير مثبت - سيتم تثبيته" "$YELLOW"
                if pip install "$package"; then
                    print_color "✅ تم تثبيت $package" "$GREEN"
                else
                    print_color "❌ فشل في تثبيت $package" "$RED"
                fi
            fi
        done
    else
        print_color "❌ pip غير متوفر - تخطي تحديث pip packages" "$RED"
    fi
}

# تحديث npm نفسه
update_npm() {
    print_color "🔄 تحديث npm..." "$BLUE"

    if command_exists npm; then
        local npm_version=$(npm --version)
        print_color "📋 إصدار npm الحالي: v$npm_version" "$CYAN"

        if npm install -g npm@latest; then
            local new_version=$(npm --version)
            print_color "✅ تم تحديث npm إلى v$new_version" "$GREEN"
        else
            print_color "❌ فشل في تحديث npm" "$RED"
        fi
    else
        print_color "❌ npm غير متوفر" "$RED"
    fi
}

# تحديث Python pip
update_pip() {
    print_color "🔄 تحديث pip..." "$BLUE"

    if command_exists pip3; then
        local pip_version=$(pip3 --version | cut -d' ' -f2)
        print_color "📋 إصدار pip3 الحالي: v$pip_version" "$CYAN"

        if pip3 install --upgrade pip; then
            local new_version=$(pip3 --version | cut -d' ' -f2)
            print_color "✅ تم تحديث pip3 إلى v$new_version" "$GREEN"
        else
            print_color "❌ فشل في تحديث pip3" "$RED"
        fi
    elif command_exists pip; then
        local pip_version=$(pip --version | cut -d' ' -f2)
        print_color "📋 إصدار pip الحالي: v$pip_version" "$CYAN"

        if pip install --upgrade pip; then
            local new_version=$(pip --version | cut -d' ' -f2)
            print_color "✅ تم تحديث pip إلى v$new_version" "$GREEN"
        else
            print_color "❌ فشل في تحديث pip" "$RED"
        fi
    else
        print_color "❌ pip غير متوفر" "$RED"
    fi
}

# تحديث VSCode extensions
update_vscode_extensions() {
    print_color "🔌 تحديث إضافات VSCode..." "$BLUE"

    if command_exists code; then
        # قائمة الإضافات المطلوب التأكد من تثبيتها
        local extensions=(
            "github.copilot"
            "github.copilot-chat"
            "ms-python.python"
            "ms-vscode.vscode-typescript-next"
            "bradlc.vscode-tailwindcss"
            "esbenp.prettier-vscode"
            "ms-vscode.vscode-json"
            "redhat.vscode-yaml"
            "ms-vscode.vscode-docker"
        )

        for ext in "${extensions[@]}"; do
            if code --list-extensions | grep -q "$ext"; then
                print_color "🔄 تحديث $ext..." "$CYAN"
                if code --install-extension "$ext" --force; then
                    print_color "✅ تم تحديث $ext" "$GREEN"
                else
                    print_color "❌ فشل في تحديث $ext" "$RED"
                fi
            else
                print_color "🔄 تثبيت $ext..." "$CYAN"
                if code --install-extension "$ext"; then
                    print_color "✅ تم تثبيت $ext" "$GREEN"
                else
                    print_color "❌ فشل في تثبيت $ext" "$RED"
                fi
            fi
        done
    else
        print_color "❌ VSCode غير مثبت - تخطي تحديث الإضافات" "$RED"
    fi
}

# تنظيف ملفات npm المخزنة مؤقتاً
clean_npm_cache() {
    print_color "🧹 تنظيف npm cache..." "$BLUE"

    if command_exists npm; then
        if npm cache clean --force; then
            print_color "✅ تم تنظيف npm cache" "$GREEN"
        else
            print_color "❌ فشل في تنظيف npm cache" "$RED"
        fi
    else
        print_color "❌ npm غير متوفر" "$RED"
    fi
}

# تنظيف ملفات pip المخزنة مؤقتاً
clean_pip_cache() {
    print_color "🧹 تنظيف pip cache..." "$BLUE"

    if command_exists pip3; then
        if pip3 cache purge; then
            print_color "✅ تم تنظيف pip cache" "$GREEN"
        else
            print_color "❌ فشل في تنظيف pip cache" "$RED"
        fi
    elif command_exists pip; then
        if pip cache purge; then
            print_color "✅ تم تنظيف pip cache" "$GREEN"
        else
            print_color "❌ فشل في تنظيف pip cache" "$RED"
        fi
    else
        print_color "❌ pip غير متوفر" "$RED"
    fi
}

# فحص التحديثات المتوفرة
check_for_updates() {
    print_color "🔍 فحص التحديثات المتوفرة..." "$BLUE"

    # فحص npm packages
    if command_exists npm; then
        print_color "📦 فحص npm packages..." "$CYAN"
        npm outdated -g 2>/dev/null || echo "جميع npm packages محدثة"
    fi

    # فحص Python packages
    if command_exists pip3; then
        print_color "🐍 فحص Python packages..." "$CYAN"
        pip3 list --outdated 2>/dev/null || echo "جميع Python packages محدثة"
    fi

    # فحص VSCode
    if command_exists code; then
        print_color "📝 فحص تحديثات VSCode..." "$CYAN"
        code --update-extensions 2>/dev/null || echo "VSCode محدث"
    fi
}

# إنشاء نسخة احتياطية من الإعدادات
backup_config() {
    print_color "💾 إنشاء نسخة احتياطية..." "$BLUE"

    local backup_dir="$SCRIPT_DIR/backup_$(date +%Y%m%d_%H%M%S)"
    mkdir -p "$backup_dir"

    # نسخ إعدادات VSCode
    if [ -d "$HOME/.vscode" ]; then
        cp -r "$HOME/.vscode" "$backup_dir/" 2>/dev/null || true
        print_color "✅ تم نسخ إعدادات VSCode" "$GREEN"
    fi

    # نسخ ملف .env إذا كان موجوداً
    if [ -f ".env" ]; then
        cp ".env" "$backup_dir/" 2>/dev/null || true
        print_color "✅ تم نسخ ملف .env" "$GREEN"
    fi

    # نسخ npm global packages list
    if command_exists npm; then
        npm list -g --depth=0 > "$backup_dir/npm_packages.txt" 2>/dev/null || true
        print_color "✅ تم نسخ قائمة npm packages" "$GREEN"
    fi

    # نسخ pip packages list
    if command_exists pip3; then
        pip3 list > "$backup_dir/pip_packages.txt" 2>/dev/null || true
        print_color "✅ تم نسخ قائمة pip packages" "$GREEN"
    fi

    print_color "📦 النسخة الاحتياطية محفوظة في: $backup_dir" "$CYAN"
}

# اختبار الأدوات بعد التحديث
test_after_update() {
    print_color "🧪 اختبار الأدوات بعد التحديث..." "$BLUE"

    # اختبار الأدوات الأساسية
    local tools=("node" "npm" "python3" "git")
    for tool in "${tools[@]}"; do
        if command_exists "$tool"; then
            print_color "✅ $tool: يعمل" "$GREEN"
        else
            print_color "❌ $tool: لا يعمل" "$RED"
        fi
    done

    # اختبار أدوات AI
    local ai_tools=("claude" "cline" "bolt" "lumo" "gemini" "codex")
    for tool in "${ai_tools[@]}"; do
        if command_exists "$tool"; then
            version=$($tool --version 2>/dev/null || echo "unknown")
            print_color "✅ $tool: v$version" "$GREEN"
        else
            print_color "❌ $tool: غير مثبت" "$RED"
        fi
    done

    # تشغيل اختبار سريع
    if [ -f "$SCRIPT_DIR/scripts/quick_test.py" ]; then
        print_color "🧪 تشغيل اختبار سريع..." "$CYAN"
        python3 "$SCRIPT_DIR/scripts/quick_test.py" --quick 2>/dev/null || print_color "⚠️  اختبار سريع فشل" "$YELLOW"
    fi
}

# عرض ملخص التحديث
show_update_summary() {
    print_color "\n📊 ملخص التحديث" "$PURPLE"
    echo "================"

    # إحصائيات التحديث
    local update_count=0
    local install_count=0
    local error_count=0

    # عد النتائج من ملف السجل
    update_count=$(grep -c "تم تحديث" "$UPDATE_LOG" 2>/dev/null || echo "0")
    install_count=$(grep -c "تم تثبيت" "$UPDATE_LOG" 2>/dev/null || echo "0")
    error_count=$(grep -c "فشل في" "$UPDATE_LOG" 2>/dev/null || echo "0")

    print_color "🔄 حزم محدثة: $update_count" "$GREEN"
    print_color "📦 حزم مثبتة: $install_count" "$GREEN"
    print_color "❌ أخطاء: $error_count" "$RED"

    if [ "$error_count" -eq 0 ]; then
        print_color "\n🎉 تم التحديث بنجاح!" "$GREEN"
        print_color "✅ جميع الأدوات جاهزة للاستخدام" "$GREEN"
    else
        print_color "\n⚠️  حدثت بعض الأخطاء أثناء التحديث" "$YELLOW"
        print_color "🔍 راجع ملف السجل: $UPDATE_LOG" "$BLUE"
    fi

    echo ""
    print_color "💡 خطوات تالية مقترحة:" "$CYAN"
    echo "1. تشغيل: ./scripts/check_system_health.sh"
    echo "2. اختبار سريع: ./scripts/quick_test.py"
    echo "3. إعداد مفاتيح API: ./api_keys_setup.md"
    echo "4. قراءة: ./QUICK_START.md"
}

# الدالة الرئيسية
main() {
    print_color "🔄 بدء تحديث أدوات الذكاء الاصطناعي" "$PURPLE"
    echo "=========================================="
    echo "📁 مجلد العمل: $SCRIPT_DIR"
    echo "📋 ملف السجل: $UPDATE_LOG"
    echo "=========================================="
    echo ""

    # إنشاء نسخة احتياطية
    backup_config
    echo ""

    # تحديث الأساسيات أولاً
    print_color "🔧 تحديث الأدوات الأساسية..." "$BLUE"
    update_npm
    update_pip
    echo ""

    # تحديث الأدوات
    update_npm_packages
    echo ""
    update_pip_packages
    echo ""
    update_vscode_extensions
    echo ""

    # تنظيف
    clean_npm_cache
    clean_pip_cache
    echo ""

    # فحص التحديثات
    check_for_updates
    echo ""

    # اختبار بعد التحديث
    test_after_update
    echo ""

    # عرض الملخص
    show_update_summary

    print_color "\n🎯 التحديث مكتمل!" "$GREEN"
    echo "=========================================="
    echo "📋 ملف السجل: $UPDATE_LOG"
    echo "💾 النسخة الاحتياطية: متوفرة"
    echo "🔍 للفحص: ./scripts/check_system_health.sh"
    echo "=========================================="
}

# معالجة المعاملات
if [[ "$1" == "--force" ]]; then
    print_color "⚠️  إعادة تحديث قسري" "$YELLOW"
    clean_npm_cache
    clean_pip_cache
elif [[ "$1" == "--check-only" ]]; then
    check_for_updates
    exit 0
elif [[ "$1" == "--backup-only" ]]; then
    backup_config
    exit 0
elif [[ "$1" == "--test-only" ]]; then
    test_after_update
    exit 0
elif [[ "$1" == "--help" ]]; then
    echo "🔄 سكريبت تحديث أدوات الذكاء الاصطناعي"
    echo ""
    echo "الاستخدام:"
    echo "  $0                # تحديث شامل"
    echo "  $0 --force        # تحديث قسري مع تنظيف cache"
    echo "  $0 --check-only   # فحص التحديثات فقط"
    echo "  $0 --backup-only  # إنشاء نسخة احتياطية فقط"
    echo "  $0 --test-only    # اختبار فقط"
    echo "  $0 --help         # عرض هذه المساعدة"
    exit 0
fi

# تشغيل التحديث
main "$@"
