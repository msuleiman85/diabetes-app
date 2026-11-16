import joblib
import numpy as np
import streamlit as st

# تحميل النموذج المدرب
model = joblib.load('diabetes_model.pkl')

# إعداد عنوان الصفحة
st.set_page_config(page_title='نظام التنبؤ بمرض السكري', page_icon='🩺')
st.title('🩺 نظام التنبؤ الذكي بمرض السكري')
st.write('أدخل البيانات الطبية أدناه للحصول على تقييم مبدئي.')

# تقسيم الواجهة إلى عمودين لتنظيم المدخلات
col1, col2 = st.columns(2)

with col1:
  pregnancies = st.number_input('عدد مرات الحمل', min_value=0, max_value=20, value=0)
  glucose = st.number_input('مستوى الجلوكوز (mg/dL)', min_value=0, max_value=300, value=120)
  blood_pressure = st.number_input('ضغط الدم (mm Hg)', min_value=0, max_value=200, value=70)
  skin_thickness = st.number_input('سمك طية الجلد (mm)', min_value=0, max_value=100, value=20)

with col2:
  insulin = st.number_input('مستوى الأنسولين (mu U/ml)', min_value=0, max_value=900, value=80)
  bmi = st.number_input('مؤشر كتلة الجسم (BMI)', min_value=0.0, max_value=70.0, value=25.0)
  dpf = st.number_input('مؤشر التاريخ الوراثي للسكري', min_value=0.0, max_value=3.0, value=0.5)
  age = st.number_input('العمر (سنوات)', min_value=1, max_value=120, value=30)

# زر التنبؤ
if st.button('تحليل البيانات والتنبؤ', type='primary'):
  # تجميع المدخلات في مصفوفة
  input_data = np.array([[
      pregnancies,
      glucose,
      blood_pressure,
      skin_thickness,
      insulin,
      bmi,
      dpf,
      age,
  ]])

  # إجراء التنبؤ
  prediction = model.predict(input_data)
  probability = model.predict_proba(input_data)[0][1] * 100

  st.divider()
  if prediction[0] == 1:
    st.error(f'⚠️ النتيجة: هناك احتمالية مرتفعة للإصابة بمرض السكري (نسبة الاحتمال: {probability:.1f}%). يُنصح بمراجعة الطبيب.')
  else:
    st.success(f'✅ النتيجة: المؤشرات طبيعية ولا توجد دلالات قوية للإصابة (نسبة الاحتمال: {probability:.1f}%).')