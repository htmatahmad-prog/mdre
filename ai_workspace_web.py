#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌐 AI Workspace Web Interface
واجهة ويب شاملة لمساحة عمل الذكاء الاصطناعي
"""

from flask import Flask, render_template_string, request, jsonify, session
from flask_cors import CORS
import os
import secrets
from ai_workspace import AIWorkspace

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
CORS(app)

# HTML Template
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🤖 مساحة عمل الذكاء الاصطناعي</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }

        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }

        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }

        .header p {
            font-size: 1.2em;
            opacity: 0.9;
        }

        .main-content {
            display: grid;
            grid-template-columns: 300px 1fr;
            gap: 0;
            min-height: 600px;
        }

        .sidebar {
            background: #f8f9fa;
            padding: 20px;
            border-left: 1px solid #dee2e6;
        }

        .model-selector {
            margin-bottom: 30px;
        }

        .model-selector h3 {
            margin-bottom: 15px;
            color: #495057;
        }

        .model-btn {
            width: 100%;
            padding: 12px;
            margin: 8px 0;
            border: 2px solid #dee2e6;
            background: white;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s;
            text-align: right;
        }

        .model-btn:hover {
            border-color: #667eea;
            background: #f8f9ff;
        }

        .model-btn.active {
            border-color: #667eea;
            background: #667eea;
            color: white;
        }

        .tools {
            margin-top: 20px;
        }

        .tools h3 {
            margin-bottom: 15px;
            color: #495057;
        }

        .tool-btn {
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            border: none;
            background: #667eea;
            color: white;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s;
        }

        .tool-btn:hover {
            background: #5568d3;
            transform: translateY(-2px);
        }

        .chat-area {
            display: flex;
            flex-direction: column;
            height: 600px;
        }

        .messages {
            flex: 1;
            padding: 20px;
            overflow-y: auto;
            background: #ffffff;
        }

        .message {
            margin: 15px 0;
            padding: 15px;
            border-radius: 15px;
            max-width: 80%;
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
        }

        .input-area {
            padding: 20px;
            background: #f8f9fa;
            border-top: 1px solid #dee2e6;
        }

        .input-group {
            display: flex;
            gap: 10px;
        }

        #userInput {
            flex: 1;
            padding: 15px;
            border: 2px solid #dee2e6;
            border-radius: 10px;
            font-size: 16px;
            font-family: inherit;
        }

        #userInput:focus {
            outline: none;
            border-color: #667eea;
        }

        .send-btn {
            padding: 15px 30px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-size: 16px;
            transition: all 0.3s;
        }

        .send-btn:hover {
            background: #5568d3;
            transform: scale(1.05);
        }

        .send-btn:disabled {
            background: #adb5bd;
            cursor: not-allowed;
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

        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.5);
            z-index: 1000;
            align-items: center;
            justify-content: center;
        }

        .modal.active {
            display: flex;
        }

        .modal-content {
            background: white;
            padding: 30px;
            border-radius: 15px;
            max-width: 500px;
            width: 90%;
        }

        .modal-content h2 {
            margin-bottom: 20px;
            color: #495057;
        }

        .modal-content input,
        .modal-content textarea {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 2px solid #dee2e6;
            border-radius: 8px;
        }

        .modal-content button {
            padding: 10px 20px;
            margin: 5px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }

        .modal-content .btn-primary {
            background: #667eea;
            color: white;
        }

        .modal-content .btn-secondary {
            background: #6c757d;
            color: white;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🤖 مساحة عمل الذكاء الاصطناعي</h1>
            <p>دردشة، بحث، تحليل كود، وأكثر - كل شيء في مكان واحد</p>
        </div>

        <div class="main-content">
            <div class="sidebar">
                <div class="model-selector">
                    <h3>🎯 اختر النموذج</h3>
                    <div id="modelsList"></div>
                </div>

                <div class="tools">
                    <h3>🛠️ الأدوات</h3>
                    <button class="tool-btn" onclick="openSearchModal()">🔍 بحث</button>
                    <button class="tool-btn" onclick="openFileModal()">📄 قراءة ملف</button>
                    <button class="tool-btn" onclick="openAnalyzeModal()">📊 تحليل كود</button>
                    <button class="tool-btn" onclick="clearChat()">🗑️ مسح المحادثة</button>
                </div>
            </div>

            <div class="chat-area">
                <div class="messages" id="messages">
                    <div class="message system">
                        مرحباً! اختر نموذج AI من القائمة وابدأ المحادثة 🚀
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
                            إرسال 📤
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Search Modal -->
    <div class="modal" id="searchModal">
        <div class="modal-content">
            <h2>🔍 البحث في الإنترنت</h2>
            <input type="text" id="searchQuery" placeholder="ما تريد البحث عنه؟">
            <button class="btn-primary" onclick="performSearch()">بحث</button>
            <button class="btn-secondary" onclick="closeModal('searchModal')">إلغاء</button>
        </div>
    </div>

    <!-- File Modal -->
    <div class="modal" id="fileModal">
        <div class="modal-content">
            <h2>📄 قراءة ملف</h2>
            <input type="text" id="filePath" placeholder="مسار الملف">
            <button class="btn-primary" onclick="readFile()">قراءة</button>
            <button class="btn-secondary" onclick="closeModal('fileModal')">إلغاء</button>
        </div>
    </div>

    <!-- Analyze Modal -->
    <div class="modal" id="analyzeModal">
        <div class="modal-content">
            <h2>📊 تحليل كود</h2>
            <input type="text" id="analyzePath" placeholder="مسار ملف الكود">
            <button class="btn-primary" onclick="analyzeCode()">تحليل</button>
            <button class="btn-secondary" onclick="closeModal('analyzeModal')">إلغاء</button>
        </div>
    </div>

    <script>
        let currentModel = null;

        // Load models on page load
        window.onload = function() {
            loadModels();
        };

        function loadModels() {
            fetch('/api/models')
                .then(r => r.json())
                .then(data => {
                    const list = document.getElementById('modelsList');
                    list.innerHTML = '';

                    Object.keys(data.models).forEach(modelId => {
                        const model = data.models[modelId];
                        const btn = document.createElement('button');
                        btn.className = 'model-btn';
                        btn.innerHTML = `
                            <strong>${model.name}</strong><br>
                            <small>${model.desc}</small>
                        `;
                        btn.onclick = () => selectModel(modelId, btn);
                        list.appendChild(btn);
                    });
                });
        }

        function selectModel(modelId, btn) {
            // Remove active class from all
            document.querySelectorAll('.model-btn').forEach(b => {
                b.classList.remove('active');
            });

            // Add active class to selected
            btn.classList.add('active');
            currentModel = modelId;

            addMessage('system', `تم اختيار: ${btn.querySelector('strong').textContent}`);
        }

        function sendMessage() {
            if (!currentModel) {
                alert('اختر نموذج AI أولاً!');
                return;
            }

            const input = document.getElementById('userInput');
            const message = input.value.trim();

            if (!message) return;

            // Add user message
            addMessage('user', message);
            input.value = '';

            // Show loading
            setLoading(true);

            // Send to server
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
                addMessage('system', '❌ حدث خطأ: ' + err);
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

        function clearChat() {
            const messages = document.getElementById('messages');
            messages.innerHTML = '<div class="message system">تم مسح المحادثة ✨</div>';
        }

        function openSearchModal() {
            document.getElementById('searchModal').classList.add('active');
        }

        function openFileModal() {
            document.getElementById('fileModal').classList.add('active');
        }

        function openAnalyzeModal() {
            document.getElementById('analyzeModal').classList.add('active');
        }

        function closeModal(id) {
            document.getElementById(id).classList.remove('active');
        }

        function performSearch() {
            const query = document.getElementById('searchQuery').value;
            if (!query) return;

            closeModal('searchModal');
            setLoading(true);

            fetch('/api/search', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({query: query})
            })
            .then(r => r.json())
            .then(data => {
                setLoading(false);
                addMessage('system', '🔍 نتائج البحث:');
                addMessage('ai', data.results);
            });
        }

        function readFile() {
            const path = document.getElementById('filePath').value;
            if (!path) return;

            closeModal('fileModal');
            setLoading(true);

            fetch('/api/read', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({path: path})
            })
            .then(r => r.json())
            .then(data => {
                setLoading(false);
                addMessage('system', '📄 محتوى الملف:');
                addMessage('ai', data.content);
            });
        }

        function analyzeCode() {
            const path = document.getElementById('analyzePath').value;
            if (!path) return;

            if (!currentModel) {
                alert('اختر نموذج AI أولاً!');
                return;
            }

            closeModal('analyzeModal');
            setLoading(true);

            fetch('/api/analyze', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    model: currentModel,
                    path: path
                })
            })
            .then(r => r.json())
            .then(data => {
                setLoading(false);
                addMessage('system', '📊 تحليل الكود:');
                addMessage('ai', data.analysis);
            });
        }
    </script>
</body>
</html>
'''

# Global workspace instance
workspace = None

@app.before_request
def init_workspace():
    global workspace
    if workspace is None:
        workspace = AIWorkspace()

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/models')
def get_models():
    return jsonify({'models': workspace.models})

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    model = data.get('model')
    message = data.get('message')

    # Set current model
    workspace.current_model = model

    # Get response
    response = workspace.chat(message)

    return jsonify({'response': response})

@app.route('/api/search', methods=['POST'])
def search():
    data = request.json
    query = data.get('query')

    results = workspace.search(query)

    return jsonify({'results': results or 'لم يتم العثور على نتائج'})

@app.route('/api/read', methods=['POST'])
def read_file():
    data = request.json
    path = data.get('path')

    content = workspace.read_file(path)

    return jsonify({'content': content})

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    model = data.get('model')
    path = data.get('path')

    workspace.current_model = model
    analysis = workspace.analyze_code(path)

    return jsonify({'analysis': analysis})

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🌐 واجهة الويب تعمل الآن!")
    print("="*60)
    print("\n🔗 افتح المتصفح على: http://localhost:5000")
    print("\n💡 للإيقاف: اضغط Ctrl+C\n")

    app.run(debug=True, host='0.0.0.0', port=5000)
