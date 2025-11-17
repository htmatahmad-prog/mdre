#!/usr/bin/env python3
"""
🧪 اختبار شامل لجميع APIs المطلوبة لأدوات الذكاء الاصطناعي
Comprehensive API Testing Suite for AI Tools
"""

import os
import sys
import json
import time
import urllib.request
from datetime import datetime
from typing import Dict, List, Tuple

# ألوان للنص
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_header(text: str):
    """طباعة عنوان ملون"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'=' * 60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{text.center(60)}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'=' * 60}{Colors.END}\n")

def print_status(name: str, status: str, message: str = ""):
    """طباعة حالة اختبار"""
    icons = {
        'success': f"{Colors.GREEN}✅",
        'error': f"{Colors.RED}❌",
        'warning': f"{Colors.YELLOW}⚠️",
        'info': f"{Colors.BLUE}ℹ️"
    }
    icons_end = Colors.END
    print(f"{icons[status]} {Colors.BOLD}{name:25}{Colors.END} {message} {icons_end}")

def test_api_connection(url: str, headers: Dict, method: str = "GET", data: Dict = None, timeout: int = 10) -> Tuple[bool, str]:
    """اختبار اتصال API عام"""
    try:
        if method.upper() == "GET":
            req = urllib.request.Request(url, headers=headers)
        else:
            req = urllib.request.Request(
                url,
                data=json.dumps(data).encode('utf-8') if data else None,
                headers=headers,
                method=method
            )

        with urllib.request.urlopen(req, timeout=timeout) as response:
            result = {
                'status_code': response.getcode(),
                'response': response.read().decode('utf-8')
            }
            return True, result
    except Exception as e:
        return False, str(e)

class APITester:
    def __init__(self):
        self.results = []
        self.load_env_vars()

    def load_env_vars(self):
        """تحميل متغيرات البيئة"""
        self.env_vars = {
            # APIs متوفرة
            'OPENAI_API_KEY': os.getenv('OPENAI_API_KEY'),
            'GEMINI_API_KEY': os.getenv('GEMINI_API_KEY'),

            # APIs مطلوبة
            'ANTHROPIC_API_KEY': os.getenv('ANTHROPIC_API_KEY'),
            'HUGGINGFACE_API_KEY': os.getenv('HUGGINGFACE_API_KEY'),
            'GITHUB_COPILOT_TOKEN': os.getenv('GITHUB_COPILOT_TOKEN'),

            # Search APIs
            'SERPER_API_KEY': os.getenv('SERPER_API_KEY'),
            'TAVILY_API_KEY': os.getenv('TAVILY_API_KEY'),

            # Speech APIs
            'ELEVENLABS_API_KEY': os.getenv('ELEVENLABS_API_KEY'),
            'ASSEMBLYAI_API_KEY': os.getenv('ASSEMBLYAI_API_KEY'),

            # Image APIs
            'REPLICATE_API_TOKEN': os.getenv('REPLICATE_API_TOKEN'),
            'STABILITY_API_KEY': os.getenv('STABILITY_API_KEY'),

            # Vector DBs
            'PINECONE_API_KEY': os.getenv('PINECONE_API_KEY'),
            'WEAVIATE_API_KEY': os.getenv('WEAVIATE_API_KEY'),

            # Communication
            'TWILIO_ACCOUNT_SID': os.getenv('TWILIO_ACCOUNT_SID'),
            'TWILIO_AUTH_TOKEN': os.getenv('TWILIO_AUTH_TOKEN'),
            'SENDGRID_API_KEY': os.getenv('SENDGRID_API_KEY'),

            # Alternative LLMs
            'CODEIUM_API_KEY': os.getenv('CODEIUM_API_KEY'),
            'MISTRAL_API_KEY': os.getenv('MISTRAL_API_KEY'),
            'COHERE_API_KEY': os.getenv('COHERE_API_KEY'),

            # Other
            'DEEPL_API_KEY': os.getenv('DEEPL_API_KEY'),
            'OPENWEATHER_API_KEY': os.getenv('OPENWEATHER_API_KEY'),
            'NEWS_API_KEY': os.getenv('NEWS_API_KEY'),
        }

    def check_env_vars(self):
        """فحص متغيرات البيئة"""
        print_header("🔍 فحص متغيرات البيئة")

        available = 0
        missing = 0
        total = len(self.env_vars)

        for var, value in self.env_vars.items():
            if value and value != "your_" + var.lower() + "_here":
                print_status(var, 'success', f"{Colors.GREEN}متوفر{Colors.END}")
                available += 1
            else:
                print_status(var, 'warning', f"{Colors.YELLOW}غير محدد{Colors.END}")
                missing += 1

        print(f"\n{Colors.CYAN}المجموع: {Colors.BOLD}{total}{Colors.END}")
        print(f"{Colors.GREEN}متوفرة: {Colors.BOLD}{available}{Colors.END}")
        print(f"{Colors.YELLOW}مفقودة: {Colors.BOLD}{missing}{Colors.END}")

        return available, missing

    def test_openai_api(self):
        """اختبار OpenAI API"""
        print_header("🤖 اختبار OpenAI API")
        api_key = self.env_vars.get('OPENAI_API_KEY')

        if not api_key:
            print_status("OpenAI", 'error', "API key غير محدد")
            return False

        url = "https://api.openai.com/v1/models"
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

        success, result = test_api_connection(url, headers)

        if success:
            try:
                models = json.loads(result['response'])
                model_count = len(models.get('data', []))
                print_status("OpenAI", 'success', f"متصل - {model_count} نموذج متاح")
                return True
            except:
                print_status("OpenAI", 'warning', "متصل لكن لا يمكن قراءة الاستجابة")
                return True
        else:
            print_status("OpenAI", 'error', f"فشل الاتصال: {result[:100]}")
            return False

    def test_gemini_api(self):
        """اختبار Gemini API"""
        print_header("🌟 اختبار Gemini API")
        api_key = self.env_vars.get('GEMINI_API_KEY')

        if not api_key:
            print_status("Gemini", 'error', "API key غير محدد")
            return False

        url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
        headers = {'Content-Type': 'application/json'}

        success, result = test_api_connection(url, headers)

        if success:
            try:
                models = json.loads(result['response'])
                model_count = len(models.get('models', []))
                print_status("Gemini", 'success', f"متصل - {model_count} نموذج متاح")
                return True
            except:
                print_status("Gemini", 'warning', "متصل لكن لا يمكن قراءة الاستجابة")
                return True
        else:
            print_status("Gemini", 'error', f"فشل الاتصال: {result[:100]}")
            return False

    def test_anthropic_api(self):
        """اختبار Anthropic API"""
        print_header("🧠 اختبار Anthropic API")
        api_key = self.env_vars.get('ANTHROPIC_API_KEY')

        if not api_key or api_key == "your_anthropic_api_key_here":
            print_status("Anthropic", 'warning', "API key غير محدد - مطلوب لـ Claude")
            return False

        url = "https://api.anthropic.com/v1/messages"
        headers = {
            'x-api-key': api_key,
            'Content-Type': 'application/json',
            'anthropic-version': '2023-06-01'
        }
        data = {
            'model': 'claude-3-haiku-20240307',
            'max_tokens': 10,
            'messages': [{'role': 'user', 'content': 'hi'}]
        }

        success, result = test_api_connection(url, headers, "POST", data)

        if success:
            print_status("Anthropic", 'success', "متصل - يعمل بشكل صحيح")
            return True
        else:
            print_status("Anthropic", 'error', f"فشل الاتصال: {result[:100]}")
            return False

    def test_huggingface_api(self):
        """اختبار Hugging Face API"""
        print_header("🤗 اختبار Hugging Face API")
        api_key = self.env_vars.get('HUGGINGFACE_API_KEY')

        if not api_key or api_key == "your_huggingface_token_here":
            print_status("Hugging Face", 'warning', "API key غير محدد - +50,000 نموذج مجاني")
            return False

        url = "https://huggingface.co/api/models"
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

        success, result = test_api_connection(url, headers)

        if success:
            try:
                models = json.loads(result['response'])
                model_count = len(models) if isinstance(models, list) else 0
                print_status("Hugging Face", 'success', f"متصل - {model_count} نموذج")
                return True
            except:
                print_status("Hugging Face", 'success', "متصل")
                return True
        else:
            print_status("Hugging Face", 'error', f"فشل الاتصال: {result[:100]}")
            return False

    def test_serper_api(self):
        """اختبار Serper API (Google Search)"""
        print_header("🔍 اختبار Serper Search API")
        api_key = self.env_vars.get('SERPER_API_KEY')

        if not api_key or api_key == "your_serper_key_here":
            print_status("Serper", 'warning', "API key غير محدد - 2,500 بحث مجاني/شهر")
            return False

        url = "https://google.serper.dev/search"
        headers = {
            'X-API-KEY': api_key,
            'Content-Type': 'application/json'
        }
        data = {'q': 'test', 'num': 1}

        success, result = test_api_connection(url, headers, "POST", data)

        if success:
            print_status("Serper", 'success', "متصل - يعمل بشكل صحيح")
            return True
        else:
            print_status("Serper", 'error', f"فشل الاتصال: {result[:100]}")
            return False

    def test_tavily_api(self):
        """اختبار Tavily API (AI Search)"""
        print_header("🌐 اختبار Tavily AI Search")
        api_key = self.env_vars.get('TAVILY_API_KEY')

        if not api_key or api_key == "your_tavily_api_key_here":
            print_status("Tavily", 'warning', "API key غير محدد - 1,000 بحث مجاني/شهر")
            return False

        url = "https://api.tavily.com/search"
        headers = {'Content-Type': 'application/json'}
        data = {
            'api_key': api_key,
            'query': 'test',
            'search_depth': 'basic'
        }

        success, result = test_api_connection(url, headers, "POST", data)

        if success:
            print_status("Tavily", 'success', "متصل - يعمل بشكل صحيح")
            return True
        else:
            print_status("Tavily", 'error', f"فشل الاتصال: {result[:100]}")
            return False

    def test_elevenlabs_api(self):
        """اختبار ElevenLabs API"""
        print_header("🔊 اختبار ElevenLabs TTS")
        api_key = self.env_vars.get('ELEVENLABS_API_KEY')

        if not api_key or api_key == "your_elevenlabs_key_here":
            print_status("ElevenLabs", 'warning', "API key غير محدد - 10,000 حرف مجاني/شهر")
            return False

        url = "https://api.elevenlabs.io/v1/voices"
        headers = {
            'xi-api-key': api_key,
            'Content-Type': 'application/json'
        }

        success, result = test_api_connection(url, headers)

        if success:
            try:
                voices = json.loads(result['response'])
                voice_count = len(voices.get('voices', []))
                print_status("ElevenLabs", 'success', f"متصل - {voice_count} صوت متاح")
                return True
            except:
                print_status("ElevenLabs", 'success', "متصل")
                return True
        else:
            print_status("ElevenLabs", 'error', f"فشل الاتصال: {result[:100]}")
            return False

    def test_replicate_api(self):
        """اختبار Replicate API"""
        print_header("🎨 اختبار Replicate API")
        api_token = self.env_vars.get('REPLICATE_API_TOKEN')

        if not api_token or api_token == "your_replicate_token_here":
            print_status("Replicate", 'warning', "API token غير محدد - Stable Diffusion, DALL-E")
            return False

        url = "https://api.replicate.com/v1/models"
        headers = {
            'Authorization': f'Token {api_token}',
            'Content-Type': 'application/json'
        }

        success, result = test_api_connection(url, headers)

        if success:
            print_status("Replicate", 'success', "متصل - يعمل بشكل صحيح")
            return True
        else:
            print_status("Replicate", 'error', f"فشل الاتصال: {result[:100]}")
            return False

    def test_pinecone_api(self):
        """اختبار Pinecone API"""
        print_header("🗄️ اختبار Pinecone Vector DB")
        api_key = self.env_vars.get('PINECONE_API_KEY')
        env = self.env_vars.get('PINECONE_ENV')

        if not api_key or api_key == "your_pinecone_key_here":
            print_status("Pinecone", 'warning', "API key غير محدد - Vector Search")
            return False

        url = f"https://{env}.pinecone.io/indexes"
        headers = {
            'Api-Key': api_key,
            'Content-Type': 'application/json'
        }

        success, result = test_api_connection(url, headers)

        if success:
            print_status("Pinecone", 'success', "متصل - يعمل بشكل صحيح")
            return True
        else:
            print_status("Pinecone", 'error', f"فشل الاتصال: {result[:100]}")
            return False

    def test_github_copilot_status(self):
        """فحص حالة GitHub Copilot"""
        print_header("💻 فحص GitHub Copilot")

        token = self.env_vars.get('GITHUB_COPILOT_TOKEN')

        if not token or token == "your_copilot_token_here":
            print_status("GitHub Copilot", 'warning', "Token غير محدد - VSCode Extension ($10/شهر)")
            print(f"\n{Colors.YELLOW}💡 طريقة الحصول عليه:{Colors.END}")
            print(f"   1. ثبت VSCode")
            print(f"   2. ثبت إضافة GitHub Copilot")
            print(f"   3. سجل دخول بـ GitHub")
            print(f"   4. اشترك في Copilot ($10/شهر)")
            return False

        print_status("GitHub Copilot", 'success', "Token متوفر")
        print(f"\n{Colors.GREEN}💡 كيفية الاستخدام:{Colors.END}")
        print(f"   1. افتح VSCode")
        print(f"   2. اضغط Ctrl+I لبدء المحادثة")
        print(f"   3. اضغط Tab لقبول الاقتراحات")
        return True

    def print_summary(self):
        """طباعة ملخص النتائج"""
        print_header("📊 ملخص النتائج")

        # قائمة APIs مع حالتها
        apis = [
            ("OpenAI", self.env_vars.get('OPENAI_API_KEY') and self.env_vars.get('OPENAI_API_KEY') != "your_openai_api_key_here"),
            ("Gemini", self.env_vars.get('GEMINI_API_KEY') and self.env_vars.get('GEMINI_API_KEY') != "your_gemini_api_key_here"),
            ("Anthropic (Claude)", self.env_vars.get('ANTHROPIC_API_KEY') and self.env_vars.get('ANTHROPIC_API_KEY') != "your_anthropic_api_key_here"),
            ("Hugging Face", self.env_vars.get('HUGGINGFACE_API_KEY') and self.env_vars.get('HUGGINGFACE_API_KEY') != "your_huggingface_token_here"),
            ("GitHub Copilot", self.env_vars.get('GITHUB_COPILOT_TOKEN') and self.env_vars.get('GITHUB_COPILOT_TOKEN') != "your_copilot_token_here"),
            ("Serper Search", self.env_vars.get('SERPER_API_KEY') and self.env_vars.get('SERPER_API_KEY') != "your_serper_key_here"),
            ("Tavily Search", self.env_vars.get('TAVILY_API_KEY') and self.env_vars.get('TAVILY_API_KEY') != "your_tavily_api_key_here"),
            ("ElevenLabs TTS", self.env_vars.get('ELEVENLABS_API_KEY') and self.env_vars.get('ELEVENLABS_API_KEY') != "your_elevenlabs_key_here"),
            ("Replicate", self.env_vars.get('REPLICATE_API_TOKEN') and self.env_vars.get('REPLICATE_API_TOKEN') != "your_replicate_token_here"),
            ("Pinecone", self.env_vars.get('PINECONE_API_KEY') and self.env_vars.get('PINECONE_API_KEY') != "your_pinecone_key_here"),
        ]

        available = 0
        for name, is_available in apis:
            if is_available:
                print_status(name, 'success', f"{Colors.GREEN}متوفر✅{Colors.END}")
                available += 1
            else:
                print_status(name, 'warning', f"{Colors.YELLOW}مفقود❌{Colors.END}")

        print(f"\n{Colors.CYAN}{'=' * 60}{Colors.END}")
        print(f"{Colors.BOLD}الإجمالي: {len(apis)} APIs{Colors.END}")
        print(f"{Colors.GREEN}متوفرة: {Colors.BOLD}{available}{Colors.END}")
        print(f"{Colors.YELLOW}مفقودة: {Colors.BOLD}{len(apis) - available}{Colors.END}")
        print(f"{Colors.CYAN}{'=' * 60}{Colors.END}")

        print(f"\n{Colors.BOLD}الخطوات التالية:{Colors.END}")
        print(f"{Colors.CYAN}1.{Colors.END} احصل على المفاتيح المفقودة من: {Colors.BLUE}MISSING_APIs.md{Colors.END}")
        print(f"{Colors.CYAN}2.{Colors.END} أضفها في ملف: {Colors.BLUE}config/.env{Colors.END}")
        print(f"{Colors.CYAN}3.{Colors.END} شغّل الاختبار مرة أخرى")

        if available >= 2:
            print(f"\n{Colors.GREEN}🎉 لديك مفاتيح أساسية كافية لبدء العمل!{Colors.END}")
        else:
            print(f"\n{Colors.YELLOW}⚠️  تحتاج على الأقل OpenAI أو Gemini + مفاتيح أخرى{Colors.END}")

    def run_all_tests(self):
        """تشغيل جميع الاختبارات"""
        print(f"{Colors.BOLD}{Colors.PURPLE}")
        print("╔══════════════════════════════════════════════════════════╗")
        print("║         🧪 اختبار شامل لجميع APIs الذكاء الاصطناعي          ║")
        print("║          Comprehensive AI APIs Testing Suite             ║")
        print("╚══════════════════════════════════════════════════════════╝")
        print(f"{Colors.END}")
        print(f"{Colors.WHITE}التاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.END}")

        # فحص متغيرات البيئة
        self.check_env_vars()

        # اختبار APIs
        tests = [
            ("OpenAI", self.test_openai_api),
            ("Gemini", self.test_gemini_api),
            ("Anthropic", self.test_anthropic_api),
            ("Hugging Face", self.test_huggingface_api),
            ("GitHub Copilot", self.test_github_copilot_status),
            ("Serper", self.test_serper_api),
            ("Tavily", self.test_tavily_api),
            ("ElevenLabs", self.test_elevenlabs_api),
            ("Replicate", self.test_replicate_api),
            ("Pinecone", self.test_pinecone_api),
        ]

        for name, test_func in tests:
            try:
                test_func()
                time.sleep(0.5)  # تأخير بين الاختبارات
            except KeyboardInterrupt:
                print(f"\n{Colors.YELLOW}تم إيقاف الاختبار بواسطة المستخدم{Colors.END}")
                break
            except Exception as e:
                print_status(name, 'error', f"خطأ غير متوقع: {str(e)[:50]}")

        # طباعة الملخص
        self.print_summary()

def main():
    """الدالة الرئيسية"""
    # تحميل ملف .env إذا وجد
    env_file = os.path.join(os.path.dirname(__file__), 'config', '.env')
    if os.path.exists(env_file):
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    if value and value != "your_" + key.lower() + "_here":
                        os.environ[key] = value

    # تشغيل الاختبارات
    tester = APITester()
    tester.run_all_tests()

if __name__ == "__main__":
    main()
