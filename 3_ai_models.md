# النماذج الذكية (AI Models)

## 1. Anthropic

### معلومات أساسية:
- **النوع**: شركة نماذج AI متقدمة
- **الملفات**:
  - `Anthropic/Claude Code 2.0.txt`
  - `Anthropic/Sonnet 4.5 Prompt.txt`

### نماذج Claude:

#### Claude Code 2.0
```markdown
You are an interactive CLI tool that helps users with software engineering tasks.

IMPORTANT: Assist with defensive security tasks only. Refuse to create, modify, or improve code that may be used maliciously.

# Tone and style
You should be concise, direct, and to the point.
You MUST answer concisely with fewer than 4 lines (not including tool use or code generation), unless user asks for detail.

IMPORTANT: You should minimize output tokens as much as possible while maintaining helpfulness, quality, and accuracy.

# Following conventions
When making changes to files, first understand the file's code conventions.
- Mimic code style, use existing libraries and utilities, and follow existing patterns
- NEVER assume a given library is available, even if it is well known
- Always follow security best practices

# Task Management
You have access to the TodoWrite tools to help you with task management.
Use TodoWrite VERY frequently to ensure that you are tracking progress.

You are powered by the model named Sonnet 4. The exact model ID is claude-sonnet-4-20250514.
```

#### Claude Code Tools (JSON Schema)
```json
{
  "tools": [
    {
      "name": "Bash",
      "description": "Executes a given bash command in a persistent shell session"
    },
    {
      "name": "Glob",
      "description": "Fast file pattern matching tool that works with any codebase size"
    },
    {
      "name": "Grep",
      "description": "A powerful search tool built on ripgrep"
    },
    {
      "name": "Read",
      "description": "Reads a file from the local filesystem"
    },
    {
      "name": "Edit",
      "description": "Performs exact string replacements in files"
    },
    {
      "name": "Write",
      "description": "Writes a file to the local filesystem"
    },
    {
      "name": "TodoWrite",
      "description": "Use this tool to create and manage a structured task list"
    },
    {
      "name": "WebFetch",
      "description": "Fetches content from a specified URL and processes it"
    },
    {
      "name": "WebSearch",
      "description": "Allows Claude to search the web and use the results"
    }
  ]
}
```

---

## 2. Gemini

### معلومات أساسية:
- **النوع**: نموذج AI من Google
- **الملف**: `Gemini/`

### المميزات:
- **نموذج متقدم**: Gemini Pro 2.5
- **قدرات متطورة**: فهم النصوص والأكواد
- **تكامل مع VSCode**: نماذج مخصصة
- **أداء عالي**: معالجة سريعة وذكية

### الاستخدام في البرمجة:
- كتابة كود عالي الجودة
- مراجعة وتحسين الأكواد
- حل المشاكل البرمجية المعقدة
- إنشاء الوثائق التقنية

---

## 3. Emergent

### معلومات أساسية:
- **النوع**: منصة AI ناشئة
- **الملف**: `Emergent/`

### الميزات:
- **تقنيات حديثة**: أحدث نماذج AI
- **واجهات مبتكرة**: تجربة مستخدم فريدة
- **مرونة في الاستخدام**: دعم متعدد اللغات
- **تحديثات مستمرة**: تطوير مستمر

---

## مميزات النماذج الذكية:

### 1. القوة الحاسوبية
- **سرعة المعالجة**: ردود فورية
- **دقة النتائج**: جودة عالية في الإجابات
- **قدرة على التحليل**: فهم عميق للسياق

### 2. المرونة
- **دعم متعدد اللغات**: JavaScript, Python, Go, Rust, إلخ
- **تكامل مع IDEs**: VSCode, Cursor, Windsurf
- **أدوات متنوعة**: بحث، تحرير، كتابة

### 3. الأمان
- **الالتزام بالسياسات**: عدم إنشاء محتوى ضار
- **حماية البيانات**: خصوصية المعلومات
- **مراجعة الكود**: فحص الأخطاء والثغرات

### 4. التخصص
- **Claude**: CLI tool متطور للبرمجة
- **Gemini**: نموذج متكامل من Google
- **Emergent**: منصة ناشئة مبتكرة

---

## مقارنة النماذج:

| النموذج | القوة | الاستخدام الأمثل | التكامل |
|---------|-------|------------------|----------|
| **Claude** | دقة متقدمة + أدوات CLI | برمجة متقدمة + تحليل | CLI, IDEs |
| **Gemini** | سرعة + تكامل Google | برمجة عامة + بحث | VSCode, IDEs |
| **Emergent** | ابتكار + مرونة | مشاريع تجريبية | متعدد |

---

## كيفية الاستخدام:

### 1. الاختيار
- **Claude**: للمشاريع المعقدة التي تتطلب دقة
- **Gemini**: للبرمجة العامة والتطوير السريع
- **Emergent**: للتجارب والمشاريع الجديدة

### 2. التكامل
```bash
# تثبيت Claude Code
npm install -g @anthropic-ai/claude-code

# إعداد Gemini في VSCode
# تثبيت إضافة Gemini AI

# استخدام Emergent
# التسجيل في المنصة والحصول على API key
```

### 3. أفضل الممارسات
- **ابدأ بنموذج واحد** وتعلم استخدامه جيداً
- **اختبر النماذج المختلفة** على نفس المشروع
- **استخدم الأدوات المناسبة** لكل مهمة
- **احفظ النتائج المهمة** للمراجعة لاحقاً

---

## التحديثات والتطوير:

### Claude:
- **الإصدار الحالي**: Sonnet 4.5
- **المميزات الجديدة**: أدوات CLI محسنة
- **الخطط المستقبلية**: تحسين الأداء

### Gemini:
- **الإصدار الحالي**: Gemini 2.5 Pro
- **التحديثات**: تكامل أعمق مع أدوات Google
- **الابتكارات**: نماذج متخصصة

### Emergent:
- **الحالة**: منصة ناشئة
- **التطوير**: المستمر للنماذج والواجهات
- **الرؤية**: مستقبل مبتكر في AI

---

## ملاحظات مهمة:
- **النماذج تتطور بسرعة**: تحديثات دورية
- **جودة النتائج تختلف**: حسب نوع المشروع
- **الكلفة**: بعضها مجاني وبعضها مدفوع
- **الخصوصية**: تأكد من سياسة الخصوصية
- **الاختبار**: جرب النماذج قبل الاعتماد الكامل
