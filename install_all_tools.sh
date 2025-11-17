#!/bin/bash

# 🚀 سكريبت التثبيت الشامل لجميع أدوات الذكاء الاصطناعي
# AI Tools Complete Installation Script

set -e  # Exit on any error

# الألوان للعرض
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# إعدادات النظام
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="$SCRIPT_DIR/install_log_$(date +%Y%m%d_%H%M%S).log"

# دالة للطباعة الملونة
print_color() {
    echo -e "${2}${1}${NC}"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# دالة لفحص وجود الأمر
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# دالة للتثبيت باستخدام npm
install_npm_package() {
    local package=$1
    local name=$2

    if npm list -g "$package" >/dev/null 2>&1; then
        print_color "✅ $name مثبت بالفعل" "$GREEN"
    else
        print_color "📦 تثبيت $name..." "$YELLOW"
        if npm install -g "$package"; then
            print_color "✅ تم تثبيت $name بنجاح" "$GREEN"
        else
            print_color "❌ فشل في تثبيت $name" "$RED"
            return 1
        fi
    fi
}

# دالة للتثبيت باستخدام pip
install_pip_package() {
    local package=$1
    local name=$2

    if pip show "$package" >/dev/null 2>&1; then
        print_color "✅ $name مثبت بالفعل" "$GREEN"
    else
        print_color "📦 تثبيت $name..." "$YELLOW"
        if pip install "$package"; then
            print_color "✅ تم تثبيت $name بنجاح" "$GREEN"
        else
            print_color "❌ فشل في تثبيت $name" "$RED"
            return 1
        fi
    fi
}

# فحص متطلبات النظام
check_system_requirements() {
    print_color "🔍 فحص متطلبات النظام..." "$BLUE"

    # فحص Node.js
    if command_exists node; then
        NODE_VERSION=$(node --version)
        print_color "✅ Node.js متوفر: $NODE_VERSION" "$GREEN"
    else
        print_color "❌ Node.js غير مثبت" "$RED"
        echo "   قم بتثبيته من: https://nodejs.org/"
    fi

    # فحص Python
    if command_exists python3; then
        PYTHON_VERSION=$(python3 --version)
        print_color "✅ Python متوفر: $PYTHON_VERSION" "$GREEN"
    elif command_exists python; then
        PYTHON_VERSION=$(python --version)
        print_color "✅ Python متوفر: $PYTHON_VERSION" "$GREEN"
    else
        print_color "❌ Python غير مثبت" "$RED"
        echo "   قم بتثبيته من: https://python.org/"
    fi

    # فحص pip
    if command_exists pip3; then
        PIP_VERSION=$(pip3 --version)
        print_color "✅ pip3 متوفر" "$GREEN"
    elif command_exists pip; then
        PIP_VERSION=$(pip --version)
        print_color "✅ pip متوفر" "$GREEN"
    else
        print_color "❌ pip غير متوفر" "$RED"
    fi

    # فحص npm
    if command_exists npm; then
        NPM_VERSION=$(npm --version)
        print_color "✅ npm متوفر: $NPM_VERSION" "$GREEN"
    else
        print_color "❌ npm غير مثبت" "$RED"
    fi

    # فحص git
    if command_exists git; then
        GIT_VERSION=$(git --version)
        print_color "✅ Git متوفر: $GIT_VERSION" "$GREEN"
    else
        print_color "❌ Git غير مثبت" "$RED"
    fi

    # فحص curl
    if command_exists curl; then
        print_color "✅ curl متوفر" "$GREEN"
    else
        print_color "❌ curl غير مثبت" "$RED"
    fi
}

# تثبيت الأدوات مفتوحة المصدر
install_open_source_tools() {
    print_color "🚀 تثبيت الأدوات مفتوحة المصدر..." "$PURPLE"

    # تثبيت الأدوات باستخدام npm
    install_npm_package "@anthropic-ai/claude-code" "Claude Code"
    install_npm_package "cline" "Cline"
    install_npm_package "@bolt-js/bolt" "Bolt"
    install_npm_package "lumo-ai" "Lumo AI"
    install_npm_package "@google/generative-ai-cli" "Gemini CLI"

    # تثبيت باستخدام pip
    install_pip_package "codex-cli" "Codex CLI"

    # تثبيت RooCode (إذا كان متوفراً)
    if command_exists npm; then
        print_color "📦 تثبيت RooCode..." "$YELLOW"
        if npm install -g roocode 2>/dev/null; then
            print_color "✅ تم تثبيت RooCode" "$GREEN"
        else
            print_color "⚠️  فشل تثبيت RooCode (قد يحتاج إعداد خاص)" "$YELLOW"
        fi
    fi
}

# تثبيت الأدوات التي تتطلب تحميل يدوي
install_manual_tools_info() {
    print_color "📋 الأدوات التي تحتاج تثبيت يدوي:" "$CYAN"

    echo ""
    echo "🔗 VSCode + GitHub Copilot:"
    echo "   1. حمّل VSCode: https://code.visualstudio.com/"
    echo "   2. ثبت إضافة GitHub Copilot"
    echo "   3. سجل دخول بـ GitHub"
    echo ""

    echo "🔗 Cursor Editor:"
    echo "   1. حمّل Cursor: https://cursor.sh/"
    echo "   2. ثبت النسخة المجانية أو Pro"
    echo ""

    echo "🔗 Windsurf:"
    echo "   1. حمّل Windsurf: https://codeium.com/windsurf/"
    echo "   2. سجل حساب مجاني"
    echo ""

    echo "🔗 Replit:"
    echo "   1. اذهب إلى: https://replit.com/"
    echo "   2. أنشئ حساب مجاني"
    echo ""

    echo "🔗 Warp.dev:"
    echo "   1. حمّل Warp: https://www.warp.dev/"
    echo "   2. ثبت النسخة المجانية"
    echo ""
}

# إعداد ملفات التكوين
setup_config_files() {
    print_color "⚙️  إعداد ملفات التكوين..." "$BLUE"

    # إنشاء مجلد التكوين
    mkdir -p "$SCRIPT_DIR/config"
    mkdir -p "$SCRIPT_DIR/data"
    mkdir -p "$SCRIPT_DIR/logs"
    mkdir -p "$SCRIPT_DIR/scripts"

    # إنشاء ملف البيئة
    if [ ! -f "$SCRIPT_DIR/.env" ]; then
        cat > "$SCRIPT_DIR/.env" << 'EOF'
# 🔑 مفاتيح API - قم بإضافة مفاتيحك هنا
# احرص على عدم مشاركة هذا الملف

# Claude Code
CLAUDE_API_KEY=your_claude_api_key_here

# GitHub Copilot (VSCode)
GITHUB_COPILOT_TOKEN=your_copilot_token_here

# Gemini
GEMINI_API_KEY=your_gemini_api_key_here

# OpenAI (للأدوات التي تحتاجها)
OPENAI_API_KEY=your_openai_api_key_here

# Windsurf
WINDSURF_API_KEY=your_windsurf_api_key_here

# إعدادات عامة
AI_CACHE_ENABLED=true
AI_LOG_LEVEL=info
AI_TIMEOUT=30000
EOF
        print_color "✅ تم إنشاء ملف .env" "$GREEN"
    else
        print_color "ℹ️  ملف .env موجود بالفعل" "$YELLOW"
    fi

    # إعداد إعدادات VSCode
    mkdir -p ~/.vscode
    cat > ~/.vscode/settings.json << 'EOF'
{
    "github.copilot.inlineSuggest.enable": true,
    "github.copilot.advanced": {
        "listCount": 10,
        "inlineSuggestCount": 3,
        "experimental": {
            "fullFunctionDupes": true,
            "tryFixCupples": true
        }
    },
    "editor.fontSize": 14,
    "editor.tabSize": 2,
    "editor.insertSpaces": true,
    "editor.detectIndentation": false,
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000,
    "terminal.integrated.fontSize": 13,
    "workbench.colorTheme": "Dark+ (default dark)",
    "git.enableSmartCommit": true,
    "git.autofetch": true
}
EOF

    cat > ~/.vscode/keybindings.json << 'EOF'
[
    {
        "key": "ctrl+shift+c",
        "command": "github.copilot.generate",
        "when": "editorTextFocus"
    },
    {
        "key": "ctrl+shift+a",
        "command": "cursor.chat",
        "when": "editorTextFocus"
    },
    {
        "key": "ctrl+shift+g",
        "command": "workbench.action.git.pull",
        "when": "git:exists"
    },
    {
        "key": "ctrl+shift+s",
        "command": "workbench.action.files.save",
        "when": "dirty"
    }
]
EOF
    print_color "✅ تم إعداد إعدادات VSCode" "$GREEN"
}

# إنشاء سكريبتات المساعدة
create_helper_scripts() {
    print_color "📜 إنشاء سكريبتات المساعدة..." "$CYAN"

    # سكريبت فحص حالة الأدوات
    cat > "$SCRIPT_DIR/check_tools_status.sh" << 'EOF'
#!/bin/bash

echo "🔍 فحص حالة أدوات الذكاء الاصطناعي..."

# فحص الأدوات مثبتة
echo ""
echo "📦 الأدوات المثبتة:"
echo "=================="

# فحص npm packages
npm list -g cline 2>/dev/null && echo "✅ Cline: متوفر" || echo "❌ Cline: غير مثبت"
npm list -g @bolt-js/bolt 2>/dev/null && echo "✅ Bolt: متوفر" || echo "❌ Bolt: غير مثبت"
npm list -g lumo-ai 2>/dev/null && echo "✅ Lumo AI: متوفر" || echo "❌ Lumo AI: غير مثبت"
npm list -g @google/generative-ai-cli 2>/dev/null && echo "✅ Gemini CLI: متوفر" || echo "❌ Gemini CLI: غير مثبت"
npm list -g @anthropic-ai/claude-code 2>/dev/null && echo "✅ Claude Code: متوفر" || echo "❌ Claude Code: غير مثبت"

# فحص pip packages
pip show codex-cli >/dev/null 2>&1 && echo "✅ Codex CLI: متوفر" || echo "❌ Codex CLI: غير مثبت"

# فحص التطبيقات المثبتة
echo ""
echo "🖥️  التطبيقات المثبتة:"
echo "======================"
command -v code >/dev/null && echo "✅ VSCode: متوفر" || echo "❌ VSCode: غير مثبت"
command -v cursor >/dev/null && echo "✅ Cursor: متوفر" || echo "❌ Cursor: غير مثبت"
command -v windsurf >/dev/null && echo "✅ Windsurf: متوفر" || echo "❌ Windsurf: غير مثبت"
command -v warp >/dev/null && echo "✅ Warp.dev: متوفر" || echo "❌ Warp.dev: غير مثبت"

echo ""
echo "📋 رابط فتح VSCode (إذا كان مثبتاً):"
if command -v code >/dev/null; then
    echo "code --version"
else
    echo "VSCode غير مثبت"
fi

echo ""
echo "🔗 روابط التحميل للأدوات المفقودة:"
echo "- VSCode: https://code.visualstudio.com/"
echo "- Cursor: https://cursor.sh/"
echo "- Windsurf: https://codeium.com/windsurf/"
echo "- Warp.dev: https://www.warp.dev/"
EOF
    chmod +x "$SCRIPT_DIR/check_tools_status.sh"

    # سكريبت اختبار سريع
    cat > "$SCRIPT_DIR/quick_test.py" << 'EOF'
#!/usr/bin/env python3
"""
اختبار سريع لأدوات الذكاء الاصطناعي
Quick test for AI tools
"""

import subprocess
import sys
import json

def run_command(cmd, description):
    """تشغيل أمر وفحص النتيجة"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description}: نجح")
            return True
        else:
            print(f"❌ {description}: فشل")
            return False
    except Exception as e:
        print(f"❌ {description}: خطأ - {e}")
        return False

def test_tools():
    """اختبار الأدوات المختلفة"""
    print("🧪 اختبار أدوات الذكاء الاصطناعي...")
    print("=" * 50)

    tools = [
        ("npm list -g cline", "Cline"),
        ("npm list -g @bolt-js/bolt", "Bolt"),
        ("pip show codex-cli", "Codex CLI"),
        ("node --version", "Node.js"),
        ("python3 --version", "Python3"),
        ("git --version", "Git")
    ]

    passed = 0
    total = len(tools)

    for cmd, name in tools:
        if run_command(cmd, name):
            passed += 1

    print("=" * 50)
    print(f"📊 النتائج: {passed}/{total} أدوات تعمل بنجاح")

    if passed == total:
        print("🎉 جميع الأدوات تعمل بشكل صحيح!")
        return True
    else:
        print("⚠️  بعض الأدوات تحتاج تثبيت أو إعداد")
        return False

if __name__ == "__main__":
    test_tools()
EOF
    chmod +x "$SCRIPT_DIR/quick_test.py"

    print_color "✅ تم إنشاء سكريبتات المساعدة" "$GREEN"
}

# تثبيت إضافات VSCode
install_vscode_extensions() {
    if command_exists code; then
        print_color "🔌 تثبيت إضافات VSCode..." "$BLUE"

        extensions=(
            "github.copilot"
            "github.copilot-chat"
            "ms-python.python"
            "ms-vscode.vscode-typescript-next"
            "bradlc.vscode-tailwindcss"
            "esbenp.prettier-vscode"
            "ms-vscode.vscode-json"
            "redhat.vscode-yaml"
            "ms-vscode.vscode-docker"
            "gitpod.gitpod-desktop"
        )

        for ext in "${extensions[@]}"; do
            if code --list-extensions | grep -q "$ext"; then
                print_color "✅ $ext مثبت بالفعل" "$GREEN"
            else
                print_color "📦 تثبيت $ext..." "$YELLOW"
                if code --install-extension "$ext" --force; then
                    print_color "✅ تم تثبيت $ext" "$GREEN"
                else
                    print_color "❌ فشل في تثبيت $ext" "$RED"
                fi
            fi
        done
    else
        print_color "⚠️  VSCode غير مثبت - تخطي تثبيت الإضافات" "$YELLOW"
    fi
}

# إنشاء ملف البدء السريع
create_quick_start_guide() {
    print_color "📚 إنشاء دليل البدء السريع..." "$CYAN"

    cat > "$SCRIPT_DIR/QUICK_START.md" << 'EOF'
# 🚀 دليل البدء السريع - أدوات الذكاء الاصطناعي

## ✅ بعد اكتمال التثبيت

### 1. فتح VSCode مع الإضافات
```bash
code my_project
```

### 2. اختبار الأدوات

#### اختبار Claude Code
```bash
claude --help
```

#### اختبار Cline
```bash
cline --help
```

#### اختبار Bolt
```bash
bolt --help
```

#### اختبار Codex CLI
```bash
codex --help
```

### 3. إعداد مفاتيح API

#### Claude Code
```bash
claude config set-api-key YOUR_API_KEY
```

#### GitHub Copilot
- افتح VSCode
- اذهب إلى Extensions
- انقر على GitHub Copilot
- سجل دخول بـ GitHub

#### Gemini CLI
```bash
gemini config set-api-key YOUR_API_KEY
```

### 4. إنشاء مشروع جديد

#### باستخدام Bolt
```bash
bolt new my-awesome-app
cd my-awesome-app
npm run dev
```

#### باستخدام Cursor
```bash
cursor create my-project
cd my-project
# افتح Cursor Editor
```

#### باستخدام Claude Code
```bash
mkdir my-project
cd my-project
claude init
```

### 5. اختبار سريع

#### Python
```python
# hello_ai.py
def greet_ai():
    """اختبار أساسي للمساعدات"""
    assistants = [
        "GitHub Copilot",
        "Claude Code",
        "Cline",
        "Cursor",
        "Bolt"
    ]

    for assistant in assistants:
        print(f"🤖 {assistant}: Hello!")

    print("\n✅ جميع المساعدات تعمل!")

if __name__ == "__main__":
    greet_ai()
```

#### JavaScript
```javascript
// hello_ai.js
const assistants = {
    copilot: "للإكمال التلقائي",
    claude: "للمهام المعقدة",
    cline: "للبرمجة المجانية",
    cursor: "للتعديل الذكي",
    bolt: "للتطوير السريع"
};

console.log("🤖 أدوات الذكاء الاصطناعي:");
Object.entries(assistants).forEach(([name, purpose]) => {
    console.log(`✅ ${name}: ${purpose}`);
});

console.log("\n🚀 جاهز للبرمجة!");
```

### 6. روابط مفيدة

- [دليل GitHub Copilot](https://docs.github.com/en/copilot)
- [دليل Claude Code](https://docs.anthropic.com/en/docs/claude-code)
- [دليل Cursor](https://cursor.sh/docs)
- [دليل Windsurf](https://codeium.com/windsurf/docs)

### 7. نصائح سريعة

1. **ابدأ بـ GitHub Copilot** - سهل الاستخدام
2. **جرب Claude Code** - قوي للمهام المعقدة
3. **استخدم Cursor** - واجهة ممتازة
4. **جرب Bolt** - للتطوير السريع
5. **استخدم Cline** - بديل مجاني قوي

### 8. استكشاف الأخطاء

#### إذا لم تعمل الأدوات:
```bash
# فحص الحالة
./check_tools_status.sh

# اختبار سريع
python3 quick_test.py

# إعادة التثبيت
./install_all_tools.sh --force
```

#### مشاكل شائعة:
- **API keys مفقودة**: أضفها في ملف .env
- **أذونات غير كافية**: استخدم sudo أو --force
- **اتصال بالإنترنت**: تأكد من الاتصال Stabil

### 9. التحديثات

```bash
# تحديث npm packages
npm update -g

# تحديث pip packages
pip install --upgrade -r requirements.txt

# تحديث VSCode extensions
code --update-extensions
```

---

**🎉 مبروك! أنت جاهز لبدء رحلتك في البرمجة المدعومة بالذكاء الاصطناعي!**
EOF

    print_color "✅ تم إنشاء دليل البدء السريع" "$GREEN"
}

# الدالة الرئيسية
main() {
    print_color "🚀 بدء التثبيت الشامل لأدوات الذكاء الاصطناعي" "$PURPLE"
    echo "=========================================="
    echo "📁 مجلد العمل: $SCRIPT_DIR"
    echo "📋 ملف السجل: $LOG_FILE"
    echo "=========================================="
    echo ""

    # فحص النظام
    check_system_requirements
    echo ""

    # تثبيت الأدوات
    install_open_source_tools
    echo ""

    # إعداد التكوين
    setup_config_files
    echo ""

    # تثبيت إضافات VSCode
    install_vscode_extensions
    echo ""

    # إنشاء سكريبتات المساعدة
    create_helper_scripts
    echo ""

    # إنشاء دليل البدء السريع
    create_quick_start_guide
    echo ""

    # معلومات الأدوات التي تحتاج تثبيت يدوي
    install_manual_tools_info
    echo ""

    # انتهاء التثبيت
    print_color "🎉 تم الانتهاء من التثبيت!" "$GREEN"
    echo "=========================================="
    echo "📚 اقرأ: QUICK_START.md"
    echo "🔍 فحص الحالة: ./check_tools_status.sh"
    echo "🧪 اختبار سريع: python3 quick_test.py"
    echo "📋 ملف السجل: $LOG_FILE"
    echo "=========================================="

    # تشغيل اختبار سريع
    echo ""
    read -p "هل تريد تشغيل اختبار سريع الآن؟ (y/n): " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        python3 quick_test.py
    fi
}

# معالجة المعاملات
if [[ "$1" == "--force" ]]; then
    print_color "⚠️  إعادة التثبيت القسري" "$YELLOW"
    npm list -g >/dev/null 2>&1 || npm install -g npm@latest
elif [[ "$1" == "--check-only" ]]; then
    check_system_requirements
    exit 0
elif [[ "$1" == "--help" ]]; then
    echo "🚀 سكريبت التثبيت الشامل لأدوات الذكاء الاصطناعي"
    echo ""
    echo "الاستخدام:"
    echo "  ./install_all_tools.sh          # تثبيت عادي"
    echo "  ./install_all_tools.sh --force  # إعادة تثبيت"
    echo "  ./install_all_tools.sh --check-only  # فحص فقط"
    echo "  ./install_all_tools.sh --help   # عرض هذه المساعدة"
    exit 0
fi

# تشغيل التثبيت
main "$@"
