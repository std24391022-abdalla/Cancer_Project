from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

print("System Architect: Abdalla Adil Abas - Initializing AI Training...")

# 1. تحميل قاعدة بيانات سرطان الثدي الحقيقية من مكتبة scikit-learn
data = load_breast_cancer()

# ملاحظة هندسية: قاعدة البيانات تحتوي على 30 ميزة، لكننا في برنامجنا نستخدم أول 9 ميزات فقط
# وهي بالترتيب: Radius, Texture, Perimeter, Area, Smoothness, Compactness, Concavity, Concave points, Symmetry
X = data.data[:, :9]

# النتيجة: 0 تعني خبيث (Malignant)، و 1 تعني حميد (Benign)
y = data.target

# 2. تقسيم البيانات إلى قسمين: 80% للتدريب و 20% للاختبار
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. توحيد مقاييس البيانات (Scaling) - خطوة حرجة جداً في البيانات الطبية
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# 4. بناء وتدريب نموذج الغابات العشوائية (Random Forest)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# 5. حفظ "العقل الذكي" (النموذج) و"المقياس" (Scaler) في ملفات جاهزة للربط
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(model, 'model.pkl')

print("Success! 'model.pkl' and 'scaler.pkl' have been generated and saved.")
print("The AI brain is ready to be linked to your GUI.")