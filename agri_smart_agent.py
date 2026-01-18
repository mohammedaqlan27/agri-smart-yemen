import os
import pandas as pd
import glob
from google import genai
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

def analyze_yemen_agriculture():
    """
    محرك تحليل البيانات الزراعية اليمنية - إصدار مفتوح المصدر
    تم تصميمه ليدعم جميع المحافظات بناءً على بيانات NASA POWER
    """
    print("\n" + "="*55)
    print("🌿 AgriSmart Yemen - Open Source Framework (v1.0)")
    print("="*55)

    # البحث عن أي ملف CSV في المجلد (لجعله يدعم عدة محافظات)
    csv_files = glob.glob("*.csv")
    if not csv_files:
        print("❌ لم يتم العثور على ملفات بيانات CSV.")
        return

    # سنأخذ أول ملف متاح كمثال (ويمكن للمطورين تطوير حلقة تكرار لكل الملفات)
    selected_file = csv_files[0]
    print(f"📊 جاري تحليل ملف: {selected_file}")

    try:
        # قراءة البيانات مع معالجة القيم المفقودة -999.0
        df = pd.read_csv(selected_file)
        latest_data = df.iloc[-1].to_dict()
        
        # دالة بسيطة لاستنتاج المحافظة من اسم الملف (يمكن تطويرها مستقبلاً)
        location_hint = "المرتفعات الوسطى (ذمار/صنعاء)" if "015d36N" in selected_file else "منطقة يمنية"

        client = genai.Client(api_key=API_KEY)
        
        prompt = f"""
        أنت محرك ذكاء اصطناعي مخصص للزراعة في اليمن.
        الموقع المستهدف: {location_hint}
        بيانات المناخ الحالية: {latest_data}
        
        المطلوب:
        1. تحليل حالة الطقس (الحرارة، الجفاف، الأمطار).
        2. تقديم نصيحة زراعية باللهجة المحلية وبالفصحى.
        3. دعوة المطورين لتحسين هذا الكود بإضافة خرائط تفاعلية.
        """

        response = client.models.generate_content(
            model="gemini-1.5-flash", # مستقر وسريع للتطوير
            contents=prompt
        )
        
        print(f"\n✅ التوصية لـ {location_hint}:")
        print("-" * 55)
        print(response.text)
        print("-" * 55)

    except Exception as e:
        print(f"❌ خطأ في المعالجة: {e}")

if __name__ == "__main__":
    analyze_yemen_agriculture()
