# streamlit_app.py
# Streamlit App Sederhana untuk Prediksi Dropout Mahasiswa

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings('ignore')

# Page config
st.set_page_config(
    page_title="Prediksi Dropout Mahasiswa",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .stAlert {
        margin-top: 1rem;
    }
    .risk-high {
        background-color: #ffebee;
        border: 2px solid #f44336;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
    }
    .risk-medium {
        background-color: #fff3e0;
        border: 2px solid #ff9800;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
    }
    .risk-low {
        background-color: #e8f5e8;
        border: 2px solid #4caf50;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Load and prepare data
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv"
    df = pd.read_csv(url, delimiter=';')
    return df

@st.cache_data
def preprocess_data(df):
    df_processed = df.copy()
    label_encoders = {}
    
    # Encode categorical variables
    categorical_cols = df_processed.select_dtypes(include=['object']).columns
    
    for col in categorical_cols:
        if col != 'Status':
            le = LabelEncoder()
            df_processed[col] = le.fit_transform(df_processed[col])
            label_encoders[col] = le
    
    # Encode target
    target_encoder = LabelEncoder()
    df_processed['Status'] = target_encoder.fit_transform(df_processed['Status'])
    
    X = df_processed.drop('Status', axis=1)
    y = df_processed['Status']
    
    return X, y, label_encoders, target_encoder, df_processed

@st.cache_resource
def train_model(X, y):
    model = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10)
    model.fit(X, y)
    return model

def get_risk_level(dropout_prob):
    if dropout_prob >= 0.7:
        return "High Risk", "🔴"
    elif dropout_prob >= 0.4:
        return "Medium Risk", "🟡"
    else:
        return "Low Risk", "🟢"

def main():
    st.markdown('<h1 class="main-header">🎓 Prediksi Dropout Mahasiswa</h1>', unsafe_allow_html=True)
    st.markdown('<center><h3>Jaya Jaya Institut</h3></center>', unsafe_allow_html=True)
    
    # Load data and train model
    with st.spinner('Loading data dan training model...'):
        df = load_data()
        X, y, label_encoders, target_encoder, df_processed = preprocess_data(df)
        model = train_model(X, y)
    
    # Sidebar for navigation
    st.sidebar.title("📊 Menu")
    page = st.sidebar.radio(
        "Pilih Halaman:",
        ["🔮 Prediksi Individual", "📈 Dashboard Overview", "📊 Data Analysis"]
    )
    
    if page == "🔮 Prediksi Individual":
        show_prediction_page(df, model, X.columns, label_encoders, target_encoder)
    elif page == "📈 Dashboard Overview":
        show_dashboard(df)
    elif page == "📊 Data Analysis":
        show_analysis(df, model, X.columns)

def show_prediction_page(df, model, feature_names, label_encoders, target_encoder):
    st.header("🔮 Prediksi Dropout Individual")
    
    st.write("Masukkan data mahasiswa untuk memprediksi risiko dropout:")
    
    # Create two columns for input
    col1, col2 = st.columns(2)
    
    # Input form
    with st.form("prediction_form"):
        
        with col1:
            st.subheader("📋 Data Akademik")
            
            age = st.number_input(
                "Umur saat Pendaftaran",
                min_value=16, max_value=60, value=20,
                help="Umur mahasiswa saat mendaftar"
            )
            
            admission_grade = st.number_input(
                "Nilai Penerimaan",
                min_value=90.0, max_value=200.0, value=140.0,
                help="Nilai yang diperoleh saat penerimaan"
            )
            
            prev_qualification_grade = st.number_input(
                "Nilai Kualifikasi Sebelumnya",
                min_value=90.0, max_value=200.0, value=140.0,
                help="Nilai dari pendidikan sebelumnya"
            )
            
            sem1_grade = st.number_input(
                "Nilai Semester 1",
                min_value=0.0, max_value=20.0, value=12.0,
                help="Rata-rata nilai semester 1"
            )
            
            sem2_grade = st.number_input(
                "Nilai Semester 2", 
                min_value=0.0, max_value=20.0, value=12.0,
                help="Rata-rata nilai semester 2"
            )
            
            sem1_approved = st.number_input(
                "Mata Kuliah Lulus Semester 1",
                min_value=0, max_value=20, value=6,
                help="Jumlah mata kuliah yang lulus di semester 1"
            )
            
            sem2_approved = st.number_input(
                "Mata Kuliah Lulus Semester 2",
                min_value=0, max_value=20, value=6,
                help="Jumlah mata kuliah yang lulus di semester 2"
            )
        
        with col2:
            st.subheader("👤 Data Personal & Sosial")
            
            gender = st.selectbox(
                "Jenis Kelamin",
                options=[0, 1],
                format_func=lambda x: "Perempuan" if x == 0 else "Laki-laki"
            )
            
            marital_status = st.selectbox(
                "Status Pernikahan",
                options=[1, 2, 3, 4, 5, 6],
                format_func=lambda x: f"Status {x}",
                index=0
            )
            
            tuition_up_to_date = st.selectbox(
                "Status Pembayaran SPP",
                options=[0, 1],
                format_func=lambda x: "Tidak Lancar" if x == 0 else "Lancar"
            )
            
            scholarship = st.selectbox(
                "Penerima Beasiswa",
                options=[0, 1],
                format_func=lambda x: "Tidak" if x == 0 else "Ya"
            )
            
            debtor = st.selectbox(
                "Status Hutang",
                options=[0, 1],
                format_func=lambda x: "Tidak Ada Hutang" if x == 0 else "Ada Hutang"
            )
            
            displaced = st.selectbox(
                "Status Pengungsian",
                options=[0, 1],
                format_func=lambda x: "Tidak" if x == 0 else "Ya"
            )
            
            international = st.selectbox(
                "Mahasiswa Internasional",
                options=[0, 1],
                format_func=lambda x: "Tidak" if x == 0 else "Ya"
            )
        
        submitted = st.form_submit_button("🔮 Prediksi Dropout", use_container_width=True)
        
        if submitted:
            # Prepare input data
            input_data = pd.DataFrame({
                'Age_at_enrollment': [age],
                'Admission_grade': [admission_grade],
                'Previous_qualification_grade': [prev_qualification_grade],
                'Curricular_units_1st_sem_grade': [sem1_grade],
                'Curricular_units_2nd_sem_grade': [sem2_grade],
                'Curricular_units_1st_sem_approved': [sem1_approved],
                'Curricular_units_2nd_sem_approved': [sem2_approved],
                'Gender': [gender],
                'Marital_status': [marital_status],
                'Tuition_fees_up_to_date': [tuition_up_to_date],
                'Scholarship_holder': [scholarship],
                'Debtor': [debtor],
                'Displaced': [displaced],
                'International': [international]
            })
            
            # Add missing features with default values
            for feature in feature_names:
                if feature not in input_data.columns:
                    input_data[feature] = 0
            
            # Reorder columns to match training data
            input_data = input_data[feature_names]
            
            # Make prediction
            prediction = model.predict(input_data)[0]
            probabilities = model.predict_proba(input_data)[0]
            
            # Convert back to original labels
            predicted_status = target_encoder.inverse_transform([prediction])[0]
            
            # Get dropout probability
            class_names = target_encoder.classes_
            prob_dict = dict(zip(class_names, probabilities))
            dropout_prob = prob_dict.get('Dropout', 0)
            
            risk_level, risk_icon = get_risk_level(dropout_prob)
            
            # Display results
            st.success("✅ Prediksi Berhasil!")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Prediksi Status", predicted_status)
            
            with col2:
                st.metric("Probabilitas Dropout", f"{dropout_prob:.1%}")
            
            with col3:
                st.metric("Level Risiko", f"{risk_icon} {risk_level}")
            
            # Risk level explanation
            if risk_level == "High Risk":
                st.markdown("""
                <div class="risk-high">
                    <h4>🔴 Risiko Tinggi</h4>
                    <p><strong>Rekomendasi:</strong></p>
                    <ul>
                        <li>Segera lakukan konseling akademik intensif</li>
                        <li>Berikan bimbingan khusus dan mentoring</li>
                        <li>Evaluasi masalah finansial dan akademik</li>
                        <li>Pertimbangkan program remedial</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            elif risk_level == "Medium Risk":
                st.markdown("""
                <div class="risk-medium">
                    <h4>🟡 Risiko Sedang</h4>
                    <p><strong>Rekomendasi:</strong></p>
                    <ul>
                        <li>Monitor progress akademik secara berkala</li>
                        <li>Berikan dukungan akademik tambahan</li>
                        <li>Lakukan konseling ringan</li>
                        <li>Pantau kehadiran dan partisipasi</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="risk-low">
                    <h4>🟢 Risiko Rendah</h4>
                    <p><strong>Rekomendasi:</strong></p>
                    <ul>
                        <li>Pertahankan performa akademik</li>
                        <li>Berikan apresiasi dan motivasi</li>
                        <li>Libatkan dalam kegiatan leadership</li>
                        <li>Monitor secara rutin</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            # Probability breakdown
            st.subheader("📊 Detail Probabilitas")
            
            # Create probability chart
            prob_df = pd.DataFrame({
                'Status': list(prob_dict.keys()),
                'Probabilitas': list(prob_dict.values())
            })
            
            fig = px.bar(
                prob_df, 
                x='Status', 
                y='Probabilitas',
                title="Probabilitas untuk Setiap Status",
                color='Status',
                color_discrete_map={'Graduate': '#4CAF50', 'Dropout': '#F44336', 'Enrolled': '#2196F3'}
            )
            
            fig.update_layout(
                yaxis_tickformat='.1%',
                xaxis_title="Status Mahasiswa",
                yaxis_title="Probabilitas"
            )
            
            st.plotly_chart(fig, use_container_width=True)

def show_dashboard(df):
    st.header("📈 Dashboard Overview")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    total_students = len(df)
    dropout_count = len(df[df['Status'] == 'Dropout'])
    graduate_count = len(df[df['Status'] == 'Graduate'])
    dropout_rate = (dropout_count / total_students) * 100
    
    with col1:
        st.metric("👥 Total Mahasiswa", f"{total_students:,}")
    with col2:
        st.metric("🎓 Lulusan", f"{graduate_count:,}")
    with col3:
        st.metric("❌ Dropout", f"{dropout_count:,}")
    with col4:
        st.metric("📉 Tingkat Dropout", f"{dropout_rate:.1f}%")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Status distribution
        status_counts = df['Status'].value_counts()
        fig = px.pie(
            values=status_counts.values,
            names=status_counts.index,
            title="Distribusi Status Mahasiswa"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Gender vs Status
        gender_status = pd.crosstab(df['Gender'], df['Status'])
        fig = px.bar(
            gender_status,
            title="Status berdasarkan Gender",
            barmode='group'
        )
        st.plotly_chart(fig, use_container_width=True)

def show_analysis(df, model, feature_names):
    st.header("📊 Analisis Data")
    
    # Feature importance
    if hasattr(model, 'feature_importances_'):
        st.subheader("🎯 Feature Importance")
        
        feature_importance = pd.DataFrame({
            'Feature': feature_names,
            'Importance': model.feature_importances_
        }).sort_values('Importance', ascending=False).head(15)
        
        fig = px.bar(
            feature_importance,
            x='Importance',
            y='Feature',
            orientation='h',
            title="Top 15 Feature Importance"
        )
        fig.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)
    
    # Data distribution
    st.subheader("📊 Distribusi Data")
    
    selected_feature = st.selectbox(
        "Pilih feature untuk dianalisis:",
        options=['Age_at_enrollment', 'Admission_grade', 'Curricular_units_1st_sem_grade', 
                'Curricular_units_2nd_sem_grade', 'Tuition_fees_up_to_date']
    )
    
    if selected_feature in df.columns:
        fig = px.histogram(
            df,
            x=selected_feature,
            color='Status',
            title=f"Distribusi {selected_feature} berdasarkan Status",
            nbins=20
        )
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()