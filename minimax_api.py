import requests
import json

# =========================================================
# === إعدادات MiniMax (معدلة لضمان عملها) ===
# =========================================================

# مفتاح API السري الخاص بك (يجب أن يكون صالحًا وغير منتهي الصلاحية)
API_KEY = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJHcm91cE5hbWUiOiJZYXNzZW4gSmpqIiwiVXNlck5hbWUiOiLZhNmK2LMg2YTYr9mKINit2KrZiSDYp9mE2KfZhiIsIkFjY291bnQiOiIiLCJTdWJqZWN0SUQiOiIxOTg4NzI5MTI1NzExMzg1MTkzIiwiUGhvbmUiOiIiLCJHcm91cElEIjoiMTk4ODcyOTEyNTcwNzE5NDk4NSIsIlBhZ2VOYW1lIjoiIiwiTWFpbCI6Inlhc3NlbmpqajJAZ21haWwuY29tIiwiQ3JlYXRlVGltZSI6IjIwMjUtMTEtMTMgMDY6NTc6NDUiLCJUb2tlblR5cGUiOjEsImlzcyI6Im1pbmltYXgifQ.LfLlqrIZbR393tw3XjHdAqQUBAgvz3ddrBLghqI_Xzeiszt6O36O91I9Z_gtdW97VANQJgIPAHMsCjSlZ2i0jQmTwtZdTnaeASt9Aj7pqtE7j6HGhGqPo-XEyZQKhd91hWFvwCwYJ278rUzdrzQ0fGp2az25PVe6-qTcmY-8mjXzrcq_kHJ0O5w9JVgwYdtSiUe1uuEBCnWO_XOzqSrbeDicZCHrOdwCGooNyPvRgy8IIgaeZOiQ_nXFZKYx7Ou_7KuURXJ5vE8ETU5Q_j6zwMmcZuujktzkc9T7pTH3RxX2K_pFxeS7ZDRooXRGHw0ZMtJxQRayC-VG8hNBEyp29dg"

# Group ID الخاص بك (مستخرج من مفتاح API ومطلوب للتفويض في العنوان)
GROUP_ID = "1988729125707194985" 

# نقطة النهاية المحدثة للـ LLM، مع إضافة Group ID كباراميتر (Query Parameter)
BASE_URL = f"https://api.minimax.io/v1/text/chatcompletion?GroupId={GROUP_ID}" 

# =========================================================

HEADERS = {
    # نرسل المفتاح السري باستخدام تنسيق Bearer
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# البيانات التي سيتم إرسالها (Body)
DATA = {
    "model": "MiniMax-M2",
    "max_tokens": 1000,
    "system": "You are a helpful assistant.",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Hi, how are you? Please respond in Arabic." # تم تعديل السؤال لطلب الرد بالعربية
                }
            ]
        }
    ]
}

try:
    # إرسال طلب POST
    response = requests.post(BASE_URL, headers=HEADERS, data=json.dumps(DATA))
    response.raise_for_status() # إلقاء استثناء إذا كان الكود غير 200 (مثل 4xx أو 5xx)
    
    # تحويل الاستجابة إلى JSON
    message = response.json()
    
    print("--- الاستجابة من MiniMax ---")
    
    # معالجة الاستجابة (بافتراض أن التنسيق قد تغير قليلاً مع نقطة النهاية الجديدة)
    if "choices" in message and message["choices"]:
        # الردود غالباً ما تكون داخل "choices" ثم "messages"
        for choice in message["choices"]:
            if "messages" in choice:
                for msg in choice["messages"]:
                    if msg.get("role") == "assistant" and "content" in msg:
                        print(f"Text:\n{msg.get('content')}\n")
                        break # نكتفي بالرد الأول
            elif "content" in choice: # تنسيق بديل
                print(f"Text:\n{choice.get('content')}\n")
    else:
        # إذا كان هناك خطأ في الطلب، سيتم طباعة الرسالة كاملة
        print("تنسيق الاستجابة غير متوقع أو حدث خطأ:")
        print(message)

except requests.exceptions.RequestException as e:
    print(f"حدث خطأ في طلب HTTP: {e}")
except Exception as e:
    print(f"حدث خطأ غير متوقع: {e}")


# =========================================================

HEADERS = {
    # تم تغيير تنسيق التفويض (Authorization) لإرسال المفتاح مباشرة 
    "Authorization": API_KEY,  # لاحظ حذف الـ f"Bearer { ... }"
    "Content-Type": "application/json"
}

# البيانات التي سيتم إرسالها (Body)
# ... بقية الكود

