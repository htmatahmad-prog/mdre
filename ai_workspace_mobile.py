#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌐 AI Workspace Mobile Web App
تطبيق ويب يعمل على الهاتف - PWA
"""

from flask import Flask, render_template_string, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import json
from pathlib import Path
from ai_workspace_pro import AIWorkspacePro
import threading
import socket

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)

# Global workspace
workspace = None
workspace_lock = threading.Lock()

def load_saved_keys():
    """تحميل المفاتيح المحفوظة"""
    config_file = Path.home() / "config_keys.json"
    if config_file.exists():
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except:
            pass
    return {}

def get_local_ip():
    """الحصول على IP المحلي"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "localhost"

# HTML Template - PWA Ready
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="theme-color" content="#667eea">
    <title>🤖 AI Workspace Pro</title>

    <!-- PWA Manifest -->
    <link rel="manifest" href="/manifest.json">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🤖</text></svg>">

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 0;
            overflow-x: hidden;
        }

        .app-container {
            max-width: 100vw;
            margin: 0 auto;
            background: white;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }

        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .header h1 {
            font-size: 1.5em;
            margin-bottom: 5px;
        }

        .header p {
            font-size: 0.9em;
            opacity: 0.9;
        }

        .model-selector {
            background: #f8f9fa;
            padding: 10px;
            overflow-x: auto;
            white-space: nowrap;
            -webkit-overflow-scrolling: touch;
        }

        .model-btn {
            display: inline-block;
            padding: 8px 15px;
            margin: 5px;
            border: 2px solid #dee2e6;
            background: white;
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.3s;
            font-size: 0.9em;
        }

        .model-btn.active {
            border-color: #667eea;
            background: #667eea;
            color: white;
        }

        .messages {
            flex: 1;
            padding: 15px;
            overflow-y: auto;
            background: #ffffff;
            -webkit-overflow-scrolling: touch;
        }

        .message {
            margin: 10px 0;
            padding: 12px 15px;
            border-radius: 15px;
            max-width: 85%;
            word-wrap: break-word;
            animation: slideIn 0.3s;
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .message.user {
            background: #667eea;
            color: white;
            margin-right: auto;
            border-bottom-right-radius: 5px;
        }

        .message.ai {
            background: #f1f3f5;
            color: #212529;
            margin-left: auto;
            border-bottom-left-radius: 5px;
        }

        .message.system {
            background: #fff3cd;
            color: #856404;
            text-align: center;
            margin: 10px auto;
            font-size: 0.9em;
        }

        .input-area {
            padding: 10px;
            background: #f8f9fa;
            border-top: 1px solid #dee2e6;
            position: sticky;
            bottom: 0;
        }

        .input-group {
            display: flex;
            gap: 8px;
        }

        #userInput {
            flex: 1;
            padding: 12px;
            border: 2px solid #dee2e6;
            border-radius: 25px;
            font-size: 16px;
            font-family: inherit;
        }

        #userInput:focus {
            outline: none;
            border-color: #667eea;
        }

        .send-btn {
            width: 50px;
            height: 50px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 50%;
            cursor: pointer;
            font-size: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s;
        }

        .send-btn:active {
            transform: scale(0.95);
        }

        .send-btn:disabled {
            background: #adb5bd;
        }

        .loading {
            display: none;
            text-align: center;
            padding: 10px;
            color: #667eea;
        }

        .loading.active {
            display: block;
        }

        .tools-btn {
            position: fixed;
            bottom: 80px;
            left: 20px;
            width: 60px;
            height: 60px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 50%;
            font-size: 24px;
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
            cursor: pointer;
            z-index: 50;
            transition: all 0.3s;
        }

        .tools-btn:active {
            transform: scale(0.9);
        }

        .tools-menu {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: white;
            border-radius: 20px 20px 0 0;
            box-shadow: 0 -4px 20px rgba(0,0,0,0.1);
            transform: translateY(100%);
            transition: transform 0.3s;
            z-index: 60;
            max-height: 60vh;
            overflow-y: auto;
        }

        .tools-menu.active {
            transform: translateY(0);
        }

        .tools-menu h3 {
            padding: 20px;
            background: #f8f9fa;
            border-radius: 20px 20px 0 0;
            margin: 0;
        }

        .tool-item {
            padding: 15px 20px;
            border-bottom: 1px solid #f1f3f5;
            cursor: pointer;
            transition: background 0.2s;
        }

        .tool-item:active {
            background: #f8f9fa;
        }

        @media (min-width: 768px) {
            .app-container {
                max-width: 768px;
                border-radius: 20px;
                margin: 20px auto;
                min-height: calc(100vh - 40px);
            }

            .header {
                border-radius: 20px 20px 0 0;
            }
        }

        .install-prompt {
            display: none;
            position: fixed;
            bottom: 80px;
            left: 50%;
            transform: translateX(-50%);
            background: white;
            padding: 15px 20px;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            z-index: 70;
            max-width: 90%;
        }

        .install-prompt.active {
            display: block;
        }

        .install-btn {
            background: #667eea;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            margin: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="app-container">
        <div class="header">
            <h1>🤖 AI Workspace Pro</h1>
            <p>مساحة عمل ذكية متقدمة</p>
        </div>

        <div class="model-selector" id="modelSelector">
            <!-- Models will be loaded here -->
        </div>

        <div class="messages" id="messages">
            <div class="message system">
                مرحباً! اختر نموذج AI وابدأ المحادثة 🚀
            </div>
        </div>

        <div class="loading" id="loading">
            ⏳ جاري المعالجة...
        </div>

        <div class="input-area">
            <div class="input-group">
                <input
                    type="text"
                    id="userInput"
                    placeholder="اكتب رسالتك هنا..."
                    onkeypress="if(event.key==='Enter') sendMessage()"
                >
                <button class="send-btn" onclick="sendMessage()" id="sendBtn">
                    ➤
                </button>
            </div>
        </div>
    </div>

    <button class="tools-btn" onclick="toggleTools()">🛠️</button>

    <div class="tools-menu" id="toolsMenu">
        <h3>🛠️ الأدوات</h3>
        <div class="tool-item" onclick="toolAction('search')">🔍 بحث في الإنترنت</div>
        <div class="tool-item" onclick="toolAction('image')">🎨 توليد صورة</div>
        <div class="tool-item" onclick="toolAction('voice')">🔊 تحويل لصوت</div>
        <div class="tool-item" onclick="toolAction('compare')">📊 مقارنة نماذج</div>
        <div class="tool-item" onclick="clearChat()">🗑️ مسح المحادثة</div>
        <div class="tool-item" onclick="toggleTools()">❌ إغلاق</div>
    </div>

    <div class="install-prompt" id="installPrompt">
        <p>📱 أضف التطبيق للشاشة الرئيسية؟</p>
        <button class="install-btn" onclick="installApp()">تثبيت</button>
        <button class="install-btn" style="background:#6c757d" onclick="hideInstallPrompt()">لاحقاً</button>
    </div>

    <script>
        let currentModel = null;
        let deferredPrompt = null;

        // PWA Install
        window.addEventListener('beforeinstallprompt', (e) => {
            e.preventDefault();
            deferredPrompt = e;
            document.getElementById('installPrompt').classList.add('active');
        });

        function installApp() {
            if (deferredPrompt) {
                deferredPrompt.prompt();
                deferredPrompt.userChoice.then((choiceResult) => {
                    deferredPrompt = null;
                    hideInstallPrompt();
                });
            }
        }

        function hideInstallPrompt() {
            document.getElementById('installPrompt').classList.remove('active');
        }

        // Load models on start
        window.onload = function() {
            loadModels();
        };

        function loadModels() {
            fetch('/api/models')
                .then(r => r.json())
                .then(data => {
                    const selector = document.getElementById('modelSelector');
                    selector.innerHTML = '';

                    Object.keys(data.models).forEach(modelId => {
                        const model = data.models[modelId];
                        const btn = document.createElement('button');
                        btn.className = 'model-btn';
                        btn.textContent = model.name;
                        btn.onclick = () => selectModel(modelId, btn);
                        selector.appendChild(btn);
                    });
                });
        }

        function selectModel(modelId, btn) {
            document.querySelectorAll('.model-btn').forEach(b => {
                b.classList.remove('active');
            });

            btn.classList.add('active');
            currentModel = modelId;

            addMessage('system', `تم اختيار: ${btn.textContent}`);
        }

        function sendMessage() {
            if (!currentModel) {
                alert('اختر نموذج AI أولاً!');
                return;
            }

            const input = document.getElementById('userInput');
            const message = input.value.trim();

            if (!message) return;

            addMessage('user', message);
            input.value = '';
            setLoading(true);

            fetch('/api/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    model: currentModel,
                    message: message
                })
            })
            .then(r => r.json())
            .then(data => {
                setLoading(false);
                addMessage('ai', data.response);
            })
            .catch(err => {
                setLoading(false);
                addMessage('system', '❌ حدث خطأ');
            });
        }

        function addMessage(type, text) {
            const messages = document.getElementById('messages');
            const div = document.createElement('div');
            div.className = `message ${type}`;
            div.textContent = text;
            messages.appendChild(div);
            messages.scrollTop = messages.scrollHeight;
        }

        function setLoading(show) {
            document.getElementById('loading').classList.toggle('active', show);
            document.getElementById('sendBtn').disabled = show;
        }

        function toggleTools() {
            document.getElementById('toolsMenu').classList.toggle('active');
        }

        function clearChat() {
            document.getElementById('messages').innerHTML = '<div class="message system">تم مسح المحادثة ✨</div>';
            toggleTools();
        }

        function toolAction(action) {
            toggleTools();

            if (action === 'search') {
                const query = prompt('🔍 ما تريد البحث عنه؟');
                if (query) {
                    addMessage('user', `/search ${query}`);
                    // Handle search...
                }
            } else if (action === 'image') {
                const prompt = prompt('🎨 صف الصورة التي تريدها:');
                if (prompt) {
                    addMessage('user', `/image ${prompt}`);
                    // Handle image generation...
                }
            } else if (action === 'voice') {
                const text = prompt('📝 النص المراد تحويله لصوت:');
                if (text) {
                    addMessage('user', `/voice ${text}`);
                    // Handle TTS...
                }
            } else if (action === 'compare') {
                const question = prompt('❓ السؤال للمقارنة:');
                if (question) {
                    addMessage('user', `/compare ${question}`);
                    // Handle comparison...
                }
            }
        }

        // Service Worker Registration
        if ('serviceWorker' in navigator) {
            navigator.serviceWorker.register('/sw.js');
        }
    </script>
</body>
</html>
'''

# Manifest JSON
MANIFEST = '''{
  "name": "AI Workspace Pro",
  "short_name": "AI Workspace",
  "description": "مساحة عمل ذكية متقدمة",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#667eea",
  "theme_color": "#667eea",
  "orientation": "portrait",
  "icons": [
    {
      "src": "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🤖</text></svg>",
      "sizes": "512x512",
      "type": "image/svg+xml"
    }
  ]
}'''

# Service Worker
SERVICE_WORKER = '''
self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open('ai-workspace-v1').then((cache) => {
      return cache.addAll(['/']);
    })
  );
});

self.addEventListener('fetch', (e) => {
  e.respondWith(
    caches.match(e.request).then((response) => {
      return response || fetch(e.request);
    })
  );
});
'''

@app.before_request
def init_workspace():
    global workspace
    if workspace is None:
        with workspace_lock:
            if workspace is None:
                workspace = AIWorkspacePro()

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/manifest.json')
def manifest():
    return MANIFEST, 200, {'Content-Type': 'application/json'}

@app.route('/sw.js')
def service_worker():
    return SERVICE_WORKER, 200, {'Content-Type': 'application/javascript'}

@app.route('/api/models')
def get_models():
    return jsonify({'models': workspace.models})

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    model = data.get('model')
    message = data.get('message')

    workspace.current_model = model
    response = workspace.chat(message)

    return jsonify({'response': response})

if __name__ == '__main__':
    local_ip = get_local_ip()
    port = 5000

    # فحص المفاتيح المحفوظة
    saved_keys = load_saved_keys()
    has_keys = any(saved_keys.values()) if saved_keys else False

    print("\n" + "="*70)
    print("🌐 AI Workspace Pro - تطبيق الويب")
    print("="*70)

    if not has_keys:
        print("\n⚠️  تحذير: لم يتم العثور على مفاتيح API محفوظة!")
        print("   شغّل: python3 setup_keys.py  لإعداد المفاتيح\n")

    print(f"\n📱 على الهاتف/الكمبيوتر في نفس الشبكة:")
    print(f"   http://{local_ip}:{port}")
    print(f"\n💻 على هذا الجهاز:")
    print(f"   http://localhost:{port}")
    print(f"\n💡 لتثبيت كتطبيق:")
    print(f"   1. افتح الرابط في المتصفح")
    print(f"   2. اضغط 'إضافة للشاشة الرئيسية'")
    print(f"\n⏹️  للإيقاف: Ctrl+C\n")

    app.run(host='0.0.0.0', port=port, debug=False)
