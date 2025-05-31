# model_inference.py
# Kode untuk inferensi model prediksi dropout

import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings('ignore')

class DropoutPredictor:
    def __init__(self):
        self.model = None
        self.scaler = None
        self.label_encoders = {}
        self.target_encoder = None
        self.feature_names = None
        self.is_trained = False
    
    def load_and_prepare_data(self, url="https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv"):
        """Load dan persiapkan data untuk training"""
        print("📥 Loading data...")
        df = pd.read_csv(url, delimiter=';')
        
        # Preprocessing
        df_processed = df.copy()
        
        # Encode categorical variables
        categorical_cols = df_processed.select_dtypes(include=['object']).columns
        
        for col in categorical_cols:
            if col != 'Status':
                le = LabelEncoder()
                df_processed[col] = le.fit_transform(df_processed[col])
                self.label_encoders[col] = le
        
        # Encode target variable
        self.target_encoder = LabelEncoder()
        df_processed['Status'] = self.target_encoder.fit_transform(df_processed['Status'])
        
        # Separate features and target
        X = df_processed.drop('Status', axis=1)
        y = df_processed['Status']
        
        self.feature_names = X.columns.tolist()
        
        return X, y, df
    
    def train_model(self, X, y):
        """Training model"""
        print("🤖 Training model...")
        
        # Initialize and train model
        self.model = RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            max_depth=10,
            min_samples_split=5,
            min_samples_leaf=2
        )
        
        self.model.fit(X, y)
        
        # Initialize scaler (optional for RandomForest, but good to have)
        self.scaler = StandardScaler()
        self.scaler.fit(X)
        
        self.is_trained = True
        
        print("✅ Model training completed!")
        
        # Print feature importance
        feature_importance = pd.DataFrame({
            'feature': self.feature_names,
            'importance': self.model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        print("\n🎯 Top 10 Most Important Features:")
        print(feature_importance.head(10))
        
        return self.model
    
    def predict_single(self, student_data):
        """Prediksi untuk satu mahasiswa"""
        if not self.is_trained:
            raise ValueError("Model belum ditraining! Jalankan train_model() terlebih dahulu.")
        
        # Convert to DataFrame if it's a dictionary
        if isinstance(student_data, dict):
            df_input = pd.DataFrame([student_data])
        else:
            df_input = student_data.copy()
        
        # Encode categorical variables
        for col in self.label_encoders:
            if col in df_input.columns:
                # Handle unseen categories
                try:
                    df_input[col] = self.label_encoders[col].transform(df_input[col])
                except ValueError:
                    # If category not seen before, use the most frequent category
                    df_input[col] = 0
        
        # Ensure all required features are present
        for feature in self.feature_names:
            if feature not in df_input.columns:
                df_input[feature] = 0  # Default value
        
        # Reorder columns to match training data
        df_input = df_input[self.feature_names]
        
        # Make prediction
        prediction = self.model.predict(df_input)[0]
        probability = self.model.predict_proba(df_input)[0]
        
        # Convert prediction back to original labels
        predicted_status = self.target_encoder.inverse_transform([prediction])[0]
        
        # Get probabilities for each class
        prob_dict = {}
        for i, class_name in enumerate(self.target_encoder.classes_):
            prob_dict[class_name] = probability[i]
        
        return {
            'predicted_status': predicted_status,
            'probabilities': prob_dict,
            'dropout_probability': prob_dict.get('Dropout', 0),
            'risk_level': self._get_risk_level(prob_dict.get('Dropout', 0))
        }
    
    def predict_batch(self, students_data):
        """Prediksi untuk multiple mahasiswa"""
        results = []
        for idx, student in students_data.iterrows():
            try:
                result = self.predict_single(student.to_dict())
                result['student_id'] = idx
                results.append(result)
            except Exception as e:
                print(f"Error predicting for student {idx}: {e}")
                results.append({
                    'student_id': idx,
                    'predicted_status': 'Error',
                    'probabilities': {},
                    'dropout_probability': 0,
                    'risk_level': 'Unknown'
                })
        
        return results
    
    def _get_risk_level(self, dropout_prob):
        """Tentukan level risiko berdasarkan probabilitas dropout"""
        if dropout_prob >= 0.7:
            return 'High Risk'
        elif dropout_prob >= 0.4:
            return 'Medium Risk'
        else:
            return 'Low Risk'
    
    def save_model(self, filepath='dropout_model.pkl'):
        """Simpan model dan preprocessors"""
        model_data = {
            'model': self.model,
            'scaler': self.scaler,
            'label_encoders': self.label_encoders,
            'target_encoder': self.target_encoder,
            'feature_names': self.feature_names,
            'is_trained': self.is_trained
        }
        
        joblib.dump(model_data, filepath)
        print(f"✅ Model saved to {filepath}")
    
    def load_model(self, filepath='dropout_model.pkl'):
        """Load model dan preprocessors"""
        model_data = joblib.load(filepath)
        
        self.model = model_data['model']
        self.scaler = model_data['scaler']
        self.label_encoders = model_data['label_encoders']
        self.target_encoder = model_data['target_encoder']
        self.feature_names = model_data['feature_names']
        self.is_trained = model_data['is_trained']
        
        print(f"✅ Model loaded from {filepath}")

# Contoh penggunaan
if __name__ == "__main__":
    # Initialize predictor
    predictor = DropoutPredictor()
    
    # Load and prepare data
    X, y, original_df = predictor.load_and_prepare_data()
    
    # Train model
    model = predictor.train_model(X, y)
    
    # Save model
    predictor.save_model('dropout_model.pkl')
    
    # Example prediction for a single student
    print("\n🔮 Example Prediction:")
    
    # Sample student data (sesuaikan dengan kolom yang tersedia)
    sample_student = {
        'Marital_status': 1,
        'Application_mode': 17,
        'Application_order': 5,
        'Course': 171,
        'Daytime_evening_attendance': 1,
        'Previous_qualification': 1,
        'Previous_qualification_grade': 122.0,
        'Nacionality': 1,
        'Mothers_qualification': 19,
        'Fathers_qualification': 12,
        'Mothers_occupation': 5,
        'Fathers_occupation': 9,
        'Admission_grade': 127.3,
        'Displaced': 1,
        'Educational_special_needs': 0,
        'Debtor': 0,
        'Tuition_fees_up_to_date': 1,
        'Gender': 1,
        'Scholarship_holder': 0,
        'Age_at_enrollment': 20,
        'International': 0,
        'Curricular_units_1st_sem_credited': 0,
        'Curricular_units_1st_sem_enrolled': 0,
        'Curricular_units_1st_sem_evaluations': 0,
        'Curricular_units_1st_sem_approved': 0,
        'Curricular_units_1st_sem_grade': 0.0,
        'Curricular_units_1st_sem_without_evaluations': 0,
        'Curricular_units_2nd_sem_credited': 0,
        'Curricular_units_2nd_sem_enrolled': 0,
        'Curricular_units_2nd_sem_evaluations': 0,
        'Curricular_units_2nd_sem_approved': 0,
        'Curricular_units_2nd_sem_grade': 0.0,
        'Curricular_units_2nd_sem_without_evaluations': 0,
        'Unemployment_rate': 10.8,
        'Inflation_rate': 1.4,
        'GDP': 1.74
    }
    
    # Make prediction
    result = predictor.predict_single(sample_student)
    
    print(f"Predicted Status: {result['predicted_status']}")
    print(f"Dropout Probability: {result['dropout_probability']:.3f}")
    print(f"Risk Level: {result['risk_level']}")
    print("All Probabilities:")
    for status, prob in result['probabilities'].items():
        print(f"  {status}: {prob:.3f}")
    
    print("\n✅ Inference code ready!")
    print("Gunakan class DropoutPredictor untuk prediksi di aplikasi Streamlit.")