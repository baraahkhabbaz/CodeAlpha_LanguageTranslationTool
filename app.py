import streamlit as st
from deep_translator import GoogleTranslator

# عنوان التطبيق
st.title("🌐 أداة الترجمة الفورية - Language Translation Tool")

# قائمة اللغات المتاحة مع رموزها
languages = {
    "العربية": "ar",
    "الإنكليزية": "en",
    "الفرنسية": "fr",
    "التركية": "tr",
    "الألمانية": "de",
    "الإسبانية": "es",
    "الإيطالية": "it",
    "الروسية": "ru"
}

# تقسيم الواجهة إلى عمودين
col1, col2 = st.columns(2)

with col1:
    src_lang = st.selectbox("لغة النص الأصلي:", ["تلقائي (Auto)"] + list(languages.keys()))

with col2:
    target_lang = st.selectbox("اللغة المراد الترجمة إليها:", list(languages.keys()), index=0)

# صندوق إدخال النص
user_text = st.text_area("أدخل النص المراد ترجمته هنا:", height=150)

# زر الترجمة
if st.button("ترجمة"):
    if user_text.strip():
        try:
            target_code = languages[target_lang]

            # تنفيذ الترجمة
            translated_text = GoogleTranslator(source='auto', target=target_code).translate(user_text)

            # عرض النتيجة
            st.success("الترجمة:")
            st.write(translated_text)
        except Exception as e:
            st.error(f"حدث خطأ أثناء الترجمة: {e}")
    else:
        st.warning("يرجى إدخال نص أولاً.")