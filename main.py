import customtkinter as ctk
import numpy as np
import joblib
import os

# إعدادات المظهر العام
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class AdvancedDiagnosticApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # إعدادات النافذة الرئيسية
        self.title("Breast Cancer AI Diagnostic System - By ABDALLA ADIL ABAS")
        self.geometry("1000x700")
        self.resizable(False, False)

        # قاموس لتخزين بيانات المريض والميزات الطبية
        self.patient_data = {}

        # الحاوية الرئيسية التي ستتبدل بداخلها الواجهات
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True)

        # تذييل ثابت لحقوق الملكية باسمك
        self.draw_footer()

        # تشغيل الواجهة 0 (بيانات المريض)
        self.show_screen_0()

    def clear_screen(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()

    def draw_header(self, step_title, progress_text):
        header_frame = ctk.CTkFrame(self.main_container, fg_color="#1a1a2e", corner_radius=10, border_width=1,
                                    border_color="#0f3460")
        header_frame.pack(fill="x", padx=20, pady=15)

        brand = ctk.CTkLabel(header_frame, text="System Architect: ABDALLA ADIL ABAS",
                             font=ctk.CTkFont(size=15, weight="bold"), text_color="#00d2ff")
        brand.pack(side="left", padx=20, pady=15)

        title = ctk.CTkLabel(header_frame, text=step_title,
                             font=ctk.CTkFont(size=20, weight="bold"), text_color="#ffffff")
        title.pack(side="left", expand=True)

        progress = ctk.CTkLabel(header_frame, text=progress_text,
                                font=ctk.CTkFont(size=14, slant="italic"), text_color="#e94560")
        progress.pack(side="right", padx=20)

    def draw_footer(self):
        footer_frame = ctk.CTkFrame(self, height=30, fg_color="#0f3460", corner_radius=0)
        footer_frame.pack(side="bottom", fill="x")

        copyright_lbl = ctk.CTkLabel(footer_frame,
                                     text="© 2026 Developed exclusively by Eng. Abdalla Adil Abas. All Rights Reserved.",
                                     font=ctk.CTkFont(size=12), text_color="#a2a2bd")
        copyright_lbl.pack(pady=5)

    def show_error_report(self, msg="Data Error"):
        self.clear_screen()
        self.draw_header("System Error", "Action Required")
        err_frame = ctk.CTkFrame(self.main_container, corner_radius=10, border_color="#ff4d4d", border_width=2)
        err_frame.pack(pady=50, padx=50, fill="both", expand=True)

        ctk.CTkLabel(err_frame, text="⚠️ Error Detected", font=ctk.CTkFont(size=30, weight="bold"),
                     text_color="#ff4d4d").pack(pady=30)
        ctk.CTkLabel(err_frame, text=msg, font=ctk.CTkFont(size=18)).pack(pady=20)

        ctk.CTkButton(err_frame, text="Go Back ↺", command=self.show_screen_0,
                      font=ctk.CTkFont(size=16, weight="bold")).pack(pady=30)

    # ==========================================
    # دالة تصميم اللوحات الطبية (البديل للصور)
    # ==========================================
    def draw_medical_panel(self, parent, title, desc, point1, point2, point3):
        """تصميم احترافي يعرض معلومات طبية بدلاً من الصور"""
        panel_frame = ctk.CTkFrame(parent, fg_color="#10101a", corner_radius=15, border_width=1, border_color="#00d2ff")
        panel_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # أيقونة/عنوان اللوحة
        ctk.CTkLabel(panel_frame, text="⚕", font=ctk.CTkFont(size=40), text_color="#00d2ff").pack(pady=(20, 0))
        ctk.CTkLabel(panel_frame, text=title, font=ctk.CTkFont(size=22, weight="bold"), text_color="#ffffff").pack(
            pady=5)

        # الوصف الطبي
        ctk.CTkLabel(panel_frame, text=desc, font=ctk.CTkFont(size=14), text_color="#a2a2bd", wraplength=350,
                     justify="center").pack(pady=10, padx=20)

        # النقاط التفصيلية
        points_frame = ctk.CTkFrame(panel_frame, fg_color="transparent")
        points_frame.pack(fill="x", padx=30, pady=10)

        ctk.CTkLabel(points_frame, text=f"➤ {point1}", font=ctk.CTkFont(size=14, weight="bold"), text_color="#28a745",
                     anchor="w").pack(fill="x", pady=5)
        ctk.CTkLabel(points_frame, text=f"➤ {point2}", font=ctk.CTkFont(size=14, weight="bold"), text_color="#ffc107",
                     anchor="w").pack(fill="x", pady=5)
        ctk.CTkLabel(points_frame, text=f"➤ {point3}", font=ctk.CTkFont(size=14, weight="bold"), text_color="#e94560",
                     anchor="w").pack(fill="x", pady=5)

    def create_input(self, parent, label_text, default_val=""):
        ctk.CTkLabel(parent, text=label_text, font=ctk.CTkFont(size=15)).pack(anchor="w", padx=30, pady=(15, 0))
        entry = ctk.CTkEntry(parent, width=350, height=40, border_color="#00d2ff", border_width=1)
        entry.pack(padx=30, pady=(5, 5))
        if default_val:
            entry.insert(0, str(default_val))
        return entry

    # ==========================================
    # الواجهة 0: بيانات المريض
    # ==========================================
    def show_screen_0(self):
        self.clear_screen()
        self.draw_header("Phase 0: Patient Demographics", "Step 0 of 5")

        content_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, padx=20, pady=10)

        inputs_frame = ctk.CTkFrame(content_frame, width=500)
        inputs_frame.pack(side="left", fill="y", padx=10, pady=10)
        inputs_frame.pack_propagate(False)

        info_frame = ctk.CTkFrame(content_frame, width=400, fg_color="transparent")
        info_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(inputs_frame, text="Patient General Info", font=ctk.CTkFont(size=20, weight="bold"),
                     text_color="#00d2ff").pack(pady=20)

        self.entry_name = self.create_input(inputs_frame, "Patient Full Name:", self.patient_data.get('Name', ''))
        self.entry_age = self.create_input(inputs_frame, "Age (Years):", self.patient_data.get('Age', ''))
        self.entry_height = self.create_input(inputs_frame, "Height (cm):", self.patient_data.get('Height', ''))
        self.entry_weight = self.create_input(inputs_frame, "Weight (kg):", self.patient_data.get('Weight', ''))

        next_btn = ctk.CTkButton(inputs_frame, text="START DIAGNOSIS ➔", command=self.go_to_screen_1,
                                 font=ctk.CTkFont(size=16, weight="bold"), height=45, fg_color="#007bff",
                                 hover_color="#0056b3")
        next_btn.pack(pady=30, padx=30, fill="x", side="bottom")

        self.draw_medical_panel(info_frame,
                                "Admission Protocol",
                                "Accurate demographic data ensures proper medical record keeping and cross-referencing for future AI predictive analytics.",
                                "Name ensures record accuracy.",
                                "Age influences risk factors.",
                                "BMI (Height/Weight) context.")

    def go_to_screen_1(self):
        self.patient_data['Name'] = self.entry_name.get() or "Unknown Patient"
        self.patient_data['Age'] = self.entry_age.get() or "N/A"
        self.patient_data['Height'] = self.entry_height.get() or "N/A"
        self.patient_data['Weight'] = self.entry_weight.get() or "N/A"
        self.show_screen_1()

    # ==========================================
    # الواجهة 1: الأبعاد
    # ==========================================
    def show_screen_1(self):
        self.clear_screen()
        self.draw_header("Phase 1: Cell Size & Dimensions", "Step 1 of 5")

        content_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, padx=20, pady=10)

        inputs_frame = ctk.CTkFrame(content_frame, width=450)
        inputs_frame.pack(side="left", fill="y", padx=10, pady=10)
        inputs_frame.pack_propagate(False)

        info_frame = ctk.CTkFrame(content_frame, width=450, fg_color="transparent")
        info_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(inputs_frame, text="Primary Measurements", font=ctk.CTkFont(size=20, weight="bold"),
                     text_color="#00d2ff").pack(pady=20)

        self.entry_radius = self.create_input(inputs_frame, "1. Mean Radius (μm):",
                                              self.patient_data.get('Mean Radius', ''))
        self.entry_perimeter = self.create_input(inputs_frame, "2. Mean Perimeter (μm):",
                                                 self.patient_data.get('Mean Perimeter', ''))
        self.entry_area = self.create_input(inputs_frame, "3. Mean Area (μm²):", self.patient_data.get('Mean Area', ''))

        next_btn = ctk.CTkButton(inputs_frame, text="NEXT ➔", command=self.go_to_screen_2,
                                 font=ctk.CTkFont(size=16, weight="bold"), height=45, fg_color="#007bff",
                                 hover_color="#0056b3")
        next_btn.pack(pady=30, padx=30, fill="x", side="bottom")

        self.draw_medical_panel(info_frame,
                                "Dimensional Analysis",
                                "Malignant cancer cells often exhibit abnormal enlargement. The AI algorithm checks these boundaries against normal historical metrics.",
                                "Radius: Distance from center to edge.",
                                "Perimeter: Total boundary length.",
                                "Area: Overall cellular footprint.")

    def go_to_screen_2(self):
        self.patient_data['Mean Radius'] = self.entry_radius.get()
        self.patient_data['Mean Perimeter'] = self.entry_perimeter.get()
        self.patient_data['Mean Area'] = self.entry_area.get()
        self.show_screen_2()

    # ==========================================
    # الواجهة 2: السطح
    # ==========================================
    def show_screen_2(self):
        self.clear_screen()
        self.draw_header("Phase 2: Cell Surface & Density", "Step 2 of 5")

        content_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, padx=20, pady=10)

        inputs_frame = ctk.CTkFrame(content_frame, width=450)
        inputs_frame.pack(side="left", fill="y", padx=10, pady=10)
        inputs_frame.pack_propagate(False)

        info_frame = ctk.CTkFrame(content_frame, width=450, fg_color="transparent")
        info_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(inputs_frame, text="Surface Measurements", font=ctk.CTkFont(size=20, weight="bold"),
                     text_color="#00d2ff").pack(pady=20)

        self.entry_texture = self.create_input(inputs_frame, "4. Mean Texture:",
                                               self.patient_data.get('Mean Texture', ''))
        self.entry_smoothness = self.create_input(inputs_frame, "5. Mean Smoothness:",
                                                  self.patient_data.get('Mean Smoothness', ''))
        self.entry_compactness = self.create_input(inputs_frame, "6. Mean Compactness:",
                                                   self.patient_data.get('Mean Compactness', ''))

        next_btn = ctk.CTkButton(inputs_frame, text="NEXT ➔", command=self.go_to_screen_3,
                                 font=ctk.CTkFont(size=16, weight="bold"), height=45, fg_color="#007bff",
                                 hover_color="#0056b3")
        next_btn.pack(pady=30, padx=30, fill="x", side="bottom")

        self.draw_medical_panel(info_frame,
                                "Texture & Density",
                                "Cancerous cells frequently lose their smooth exterior. The AI evaluates the variance in gray-scale values and structural density.",
                                "Texture: Gray-scale variance.",
                                "Smoothness: Local length variations.",
                                "Compactness: Perimeter² / Area - 1.0.")

    def go_to_screen_3(self):
        self.patient_data['Mean Texture'] = self.entry_texture.get()
        self.patient_data['Mean Smoothness'] = self.entry_smoothness.get()
        self.patient_data['Mean Compactness'] = self.entry_compactness.get()
        self.show_screen_3()

    # ==========================================
    # الواجهة 3: التشوه
    # ==========================================
    def show_screen_3(self):
        self.clear_screen()
        self.draw_header("Phase 3: Structural Deformity", "Step 3 of 5")

        content_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        content_frame.pack(fill="both", expand=True, padx=20, pady=10)

        inputs_frame = ctk.CTkFrame(content_frame, width=450)
        inputs_frame.pack(side="left", fill="y", padx=10, pady=10)
        inputs_frame.pack_propagate(False)

        info_frame = ctk.CTkFrame(content_frame, width=450, fg_color="transparent")
        info_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(inputs_frame, text="Deformity Measurements", font=ctk.CTkFont(size=20, weight="bold"),
                     text_color="#00d2ff").pack(pady=20)

        self.entry_concavity = self.create_input(inputs_frame, "7. Mean Concavity:",
                                                 self.patient_data.get('Mean Concavity', ''))
        self.entry_concave_pts = self.create_input(inputs_frame, "8. Mean Concave Points:",
                                                   self.patient_data.get('Mean Concave Points', ''))
        self.entry_symmetry = self.create_input(inputs_frame, "9. Mean Symmetry:",
                                                self.patient_data.get('Mean Symmetry', ''))

        done_btn = ctk.CTkButton(inputs_frame, text="DONE ✔", command=self.go_to_review,
                                 font=ctk.CTkFont(size=16, weight="bold"), height=45, fg_color="#28a745",
                                 hover_color="#218838")
        done_btn.pack(pady=30, padx=30, fill="x", side="bottom")

        self.draw_medical_panel(info_frame,
                                "Structural Deformity",
                                "Malignancy often disrupts cellular symmetry and causes concave indentations along the cellular membrane.",
                                "Concavity: Severity of indentations.",
                                "Concave Points: Number of contour dips.",
                                "Symmetry: Structural balance.")

    def go_to_review(self):
        self.patient_data['Mean Concavity'] = self.entry_concavity.get()
        self.patient_data['Mean Concave Points'] = self.entry_concave_pts.get()
        self.patient_data['Mean Symmetry'] = self.entry_symmetry.get()
        self.show_review_screen()

    # ==========================================
    # الواجهة 4: المراجعة
    # ==========================================
    def show_review_screen(self):
        self.clear_screen()
        self.draw_header("Phase 4: Data Verification", "Step 4 of 5")

        main_frame = ctk.CTkFrame(self.main_container)
        main_frame.pack(fill="both", expand=True, padx=40, pady=20)

        ctk.CTkLabel(main_frame, text=f"Patient: {self.patient_data.get('Name', '')} | Verify Clinical Features",
                     font=ctk.CTkFont(size=18, weight="bold"), text_color="#ffc107").pack(pady=20)

        grid_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        grid_frame.pack(pady=10)

        # استبعاد البيانات الأساسية من العرض الشبكي للميزات الطبية
        medical_features = {k: v for k, v in self.patient_data.items() if k not in ['Name', 'Age', 'Height', 'Weight']}

        row, col = 0, 0
        for i, (key, value) in enumerate(medical_features.items()):
            bg_color = "#2a2a3b" if i % 2 == 0 else "#1a1a2e"
            item_frame = ctk.CTkFrame(grid_frame, fg_color=bg_color, corner_radius=5)
            item_frame.grid(row=row, column=col, padx=10, pady=5, sticky="ew")

            ctk.CTkLabel(item_frame, text=f"{key}:", font=ctk.CTkFont(size=14, weight="bold")).pack(side="left",
                                                                                                    padx=10, pady=5)
            ctk.CTkLabel(item_frame, text=f"{value}", font=ctk.CTkFont(size=14), text_color="#00d2ff").pack(
                side="right", padx=10, pady=5)

            col += 1
            if col > 2:
                col = 0
                row += 1

        btn_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        btn_frame.pack(pady=40)

        edit_btn = ctk.CTkButton(btn_frame, text="Edit Data ✎", command=self.show_screen_1,
                                 font=ctk.CTkFont(size=16), height=45, fg_color="#6c757d", hover_color="#5a6268")
        edit_btn.pack(side="left", padx=20)

        analyze_btn = ctk.CTkButton(btn_frame, text="RUN AI ANALYSIS ⚙", command=self.run_ai_and_show_report,
                                    font=ctk.CTkFont(size=16, weight="bold"), height=45, fg_color="#e94560",
                                    hover_color="#d63447")
        analyze_btn.pack(side="right", padx=20)

    # ==========================================
    # الواجهة 5: التقرير النهائي (AI)
    # ==========================================
    def run_ai_and_show_report(self):
        self.clear_screen()
        self.draw_header("Phase 5: Real AI Diagnostic Report", "Final Step")

        try:
            if not os.path.exists('model.pkl') or not os.path.exists('scaler.pkl'):
                self.show_error_report("AI Model files missing! Please run 'train_model.py' first.")
                return

            scaler = joblib.load('scaler.pkl')
            model = joblib.load('model.pkl')

            features = [
                float(self.patient_data.get('Mean Radius', 0)),
                float(self.patient_data.get('Mean Texture', 0)),
                float(self.patient_data.get('Mean Perimeter', 0)),
                float(self.patient_data.get('Mean Area', 0)),
                float(self.patient_data.get('Mean Smoothness', 0)),
                float(self.patient_data.get('Mean Compactness', 0)),
                float(self.patient_data.get('Mean Concavity', 0)),
                float(self.patient_data.get('Mean Concave Points', 0)),
                float(self.patient_data.get('Mean Symmetry', 0))
            ]

            input_data = np.array([features])
            scaled_data = scaler.transform(input_data)

            prediction = model.predict(scaled_data)[0]
            probabilities = model.predict_proba(scaled_data)[0]

            is_malignant = (prediction == 0)
            confidence = round(max(probabilities) * 100, 2)

        except ValueError:
            self.show_error_report("Invalid Data Entry. Ensure all 9 features are numbers.")
            return
        except Exception as e:
            self.show_error_report(f"An unexpected error occurred: {e}")
            return

        result_color = "#ff4d4d" if is_malignant else "#00cc66"
        result_text = "MALIGNANT (خبيث)" if is_malignant else "BENIGN (حميد)"

        analysis_summary = "Based on the integration of the 9 clinical features processed through the Random Forest Machine Learning Model. "
        if is_malignant:
            analysis_summary += "The neural/ensemble analysis strongly correlates the cell morphology with malignant patterns."
            advice_text = "CRITICAL: Urgent specialist consultation and biopsy recommended. Do not delay."
        else:
            analysis_summary += "The cellular structures align closely with benign historical data."
            advice_text = "Routine annual screening and self-examination recommended."

        report_frame = ctk.CTkFrame(self.main_container, corner_radius=15, border_width=2, border_color="#0f3460")
        report_frame.pack(fill="both", expand=True, padx=50, pady=30)

        ctk.CTkLabel(report_frame, text="Official Medical AI Analysis Report",
                     font=ctk.CTkFont(size=26, weight="bold", underline=True), text_color="#ffffff").pack(pady=15)

        # عرض بيانات المريض
        p_row_frame = ctk.CTkFrame(report_frame, fg_color="#10101a", corner_radius=5)
        p_row_frame.pack(fill="x", padx=50, pady=10)
        ctk.CTkLabel(p_row_frame, text=f"Patient: {self.patient_data.get('Name', 'Unknown')}",
                     font=ctk.CTkFont(size=16, weight="bold")).pack(side="left", padx=15, pady=5)
        ctk.CTkLabel(p_row_frame,
                     text=f"Age: {self.patient_data.get('Age', '-')} | H: {self.patient_data.get('Height', '-')}cm | W: {self.patient_data.get('Weight', '-')}kg",
                     font=ctk.CTkFont(size=16)).pack(side="right", padx=15, pady=5)

        ctk.CTkLabel(report_frame, text="Diagnosis Result:", font=ctk.CTkFont(size=18)).pack(pady=(15, 5))
        ctk.CTkLabel(report_frame, text=result_text, font=ctk.CTkFont(size=40, weight="bold"),
                     text_color=result_color).pack(pady=5)

        ctk.CTkLabel(report_frame, text=f"AI System Confidence Score: {confidence}%",
                     font=ctk.CTkFont(size=17, weight="bold"), text_color="#00d2ff").pack(pady=5)

        analysis_frame = ctk.CTkFrame(report_frame, fg_color="#10101a", corner_radius=10)
        analysis_frame.pack(fill="x", padx=50, pady=10)
        ctk.CTkLabel(analysis_frame, text="Technical Analysis (ML Output):",
                     font=ctk.CTkFont(size=15, weight="bold")).pack(anchor="w", padx=15, pady=(10, 0))
        ctk.CTkLabel(analysis_frame, text=analysis_summary, font=ctk.CTkFont(size=14), text_color="#a2a2bd",
                     wraplength=800, justify="left").pack(pady=(5, 10), padx=15)

        advice_frame = ctk.CTkFrame(report_frame, fg_color="#1a1a2e", corner_radius=10, border_width=1,
                                    border_color=result_color)
        advice_frame.pack(fill="x", padx=50, pady=10)
        ctk.CTkLabel(advice_frame, text="Medical Recommendation:", font=ctk.CTkFont(size=16, weight="bold"),
                     text_color="#f39c12").pack(pady=(10, 0))
        ctk.CTkLabel(advice_frame, text=advice_text, font=ctk.CTkFont(size=16), text_color="#ffffff",
                     wraplength=800).pack(pady=(5, 15), padx=20)

        restart_btn = ctk.CTkButton(report_frame, text="New Patient Admission ↺", command=self.reset_app,
                                    font=ctk.CTkFont(size=16, weight="bold"), height=45, fg_color="#6c757d",
                                    hover_color="#5a6268")
        restart_btn.pack(pady=15)

    def reset_app(self):
        self.patient_data.clear()
        self.show_screen_0()


if __name__ == "__main__":
    app = AdvancedDiagnosticApp()
    app.mainloop()