# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini, institusi ini telah mencetak banyak lulusan dengan reputasi yang sangat baik. Namun, terdapat permasalahan yang cukup besar, yaitu tingginya jumlah siswa yang tidak menyelesaikan pendidikannya atau dropout.

Masalah dropout yang tinggi ini sangat merugikan institusi karena berpengaruh pada kualitas pendidikan dan reputasi. Oleh karena itu, Jaya Jaya Institut ingin dapat mendeteksi secara dini siswa yang berpotensi dropout agar dapat diberikan bimbingan dan intervensi khusus.

Sebagai calon data scientist masa depan, Anda diminta untuk membantu Jaya Jaya Institut menyelesaikan permasalahan ini dengan memanfaatkan dataset yang telah disediakan. Selain itu, Anda juga diminta membuat dashboard agar pihak institusi mudah dalam memahami data dan memonitor performa siswa secara efektif.

### Permasalahan Bisnis

- Tingginya angka siswa yang melakukan dropout di Jaya Jaya Institut.
- Kesulitan institusi dalam mendeteksi siswa yang berpotensi dropout secara dini.
- Kurangnya sistem yang dapat membantu institusi memberikan bimbingan atau intervensi tepat waktu bagi siswa yang berisiko dropout.
- Kebutuhan untuk menyediakan dashboard yang memudahkan pemantauan performa siswa dan pengambilan keputusan berdasarkan data.
  
### Cakupan Proyek

Proyek ini mencakup beberapa tahapan utama, yaitu eksplorasi dan pemrosesan data untuk memahami karakteristik siswa, pengembangan model prediksi untuk mendeteksi risiko dropout, serta deployment model menggunakan Streamlit agar mudah diakses dan digunakan oleh pihak institusi. Selain itu, saya juga membuat dashboard interaktif menggunakan Metabase yang memudahkan monitoring performa siswa secara real-time. Semua proses ini dijalankan secara menyeluruh dalam siklus proyek data science, mulai dari eksplorasi data, pemodelan, evaluasi, hingga deployment dan visualisasi.

### Persiapan

**Sumber Data:**  
Dataset yang digunakan dalam proyek ini dapat diunduh dari repositori GitHub Dicoding pada tautan berikut:  
[https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv).

**Setup Environment:**  
Untuk menjalankan proyek ini, disarankan menggunakan virtual environment (venv) Python agar lingkungan pengembangan terisolasi dan mudah dikelola. Berikut langkah setup environment:

```bash
# Membuat virtual environment
python -m venv venv
```

# Mengaktifkan virtual environment
# Windows
```
venv\Scripts\activate
```
```
# macOS/Linux
source venv/bin/activate
```
# Menginstall dependencies dari file requirements.txt
```
pip install -r requirements.txt
```

File requirements.txt sudah tersedia di dalam proyek dan berisi semua library yang dibutuhkan untuk preprocessing data, pemodelan, deployment aplikasi dengan Streamlit, serta integrasi dengan Metabase.

Dashboard Interaktif Metabase:
Proyek ini juga dilengkapi dengan dashboard interaktif menggunakan Metabase, yang menyimpan konfigurasinya dalam file **metabase.db.mv.db**. Untuk mengakses dashboard Metabase, gunakan kredensial berikut:
> Email: mrizki135790@gmail.com

> Password: dG8M@BWcewxUtxc

### Menjalankan Aplikasi dan Model Prediksi:
Untuk mencoba prototipe model prediksi dan aplikasi dashboard, dapat mengakses link berikut yang sudah dideploy di Streamlit Community Cloud:
> https://mhd-rizki-bpds-edutech.streamlit.app/

---

## 📊 Dashboard Analisis Mahasiswa – Jaya Jaya Institute (JJI)
<p align="center">
  <img src="https://github.com/user-attachments/assets/850642fb-afbd-40bd-9e85-2c1d3b0ea25b" width="45%"/>
  <img src="https://github.com/user-attachments/assets/86383157-119c-4243-93d6-fc0e316beddd" width="45%"/>
</p>


### 🎯 Highlight

#### 1. International vs Local Students
- Mahasiswa **lokal mendominasi** dengan jumlah sekitar **4.000 orang**.
- Mahasiswa **internasional sangat sedikit**, menunjukkan bahwa populasi mahasiswa mayoritas berasal dari dalam negeri.

#### 2. Tuition Payment Status
- Sebagian besar mahasiswa memiliki status pembayaran **"Up-to-date"**.
- Namun masih ada mahasiswa dengan status **"Not up-to-date"**, yang perlu mendapat perhatian khusus terkait dukungan finansial.

#### 3. Age Distribution at Enrollment
- Puncak pendaftaran terjadi pada usia **18–20 tahun**, sesuai dengan lulusan sekolah menengah atas.
- Terdapat distribusi usia yang lebih tua hingga usia **60 tahun ke atas**, menunjukkan keberadaan **mahasiswa dewasa** atau **lifelong learners**.

#### 4. Student Count by Marital Status
- Sebanyak **88.58%** mahasiswa berstatus **lajang**.
- **8.57% menikah**, dan **2.85% lainnya** berstatus "Other", menunjukkan keberagaman kondisi sosial mahasiswa.

#### 5. Average Grade for 1st and 2nd Semester
- **Nilai rata-rata cukup tinggi dan konsisten** antara semester 1 dan semester 2.
- Ini mengindikasikan performa akademik awal mahasiswa cenderung stabil dan positif.

---

### 💡 Insight Strategis

#### 🔹 Potensi Intervensi Finansial
Mahasiswa dengan status pembayaran yang belum up-to-date dapat menjadi target program:
- **Beasiswa atau keringanan biaya kuliah**
- **Program pengingat dan konseling finansial**
- **Upaya pencegahan dropout akibat masalah ekonomi**

#### 🔹 Peluang Ekspansi Internasional
Jumlah mahasiswa internasional yang rendah menunjukkan:
- Peluang besar untuk meningkatkan **promosi internasional**
- Potensi pengembangan **kelas berbahasa Inggris atau program pertukaran pelajar**

#### 🔹 Dukungan untuk Mahasiswa Dewasa
Mahasiswa dengan usia >30 tahun membutuhkan:
- **Program pembelajaran fleksibel** (kelas malam, daring)
- **Kurikulum yang relevan dengan dunia kerja atau re-skilling**

#### 🔹 Kebutuhan Pendampingan Sosial
Mahasiswa menikah mungkin menghadapi beban ganda:
- Perlu adanya **support group atau konseling keluarga**
- Penyesuaian dalam **beban studi atau jadwal kuliah**

#### 🔹 Stabilitas Akademik Awal
Nilai rata-rata yang stabil antar semester menunjukkan:
- Kurikulum awal cukup efektif
- Perlu **pemantauan berkelanjutan** agar performa tetap baik di semester lanjutan

---

## 🚀 Menjalankan Sistem Machine Learning

Model dapat dijalankan secara lokal menggunakan `model_inference.py`, atau langsung diuji melalui prototipe Streamlit berikut:

🌐 **[Coba Prototipe di Streamlit](https://mhd-rizki-bpds-edutech.streamlit.app/)**
![image](https://github.com/user-attachments/assets/eaa2391a-f6f5-4a12-a86f-16065989d317)

### ✨ Fitur Utama Prototipe:
- 🔮 **Prediksi Individual**  
  Form input untuk memprediksi status siswa (Dropout, Enrolled, Graduate), probabilitas, risiko, dan rekomendasi tindakan.

- 📈 **Dashboard Overview**  
  Visualisasi performa dan statistik penting siswa secara ringkas.

- 📊 **Data Analysis**  
  Eksplorasi data menyeluruh untuk analisis lanjutan.

---

## 🤖 Ringkasan Model & Evaluasi

Model terbaik: **Random Forest**  
- **Accuracy:** `0.7672`  
- **Cross Validation (CV Mean):** `0.7782 ± 0.0124`

### 📋 Hasil Klasifikasi (Random Forest)
- **Dropout**: F1-score `0.78`, Precision `0.81`, Recall `0.75`
- **Enrolled**: F1-score `0.45`, Precision `0.57`, Recall `0.37`
- **Graduate**: F1-score `0.85`, Precision `0.78`, Recall `0.92`
- **Overall Accuracy**: `0.77`

### 🔝 Top 5 Fitur Terpenting:
1. `Curricular_units_2nd_sem_approved` – 14.2%
2. `Curricular_units_2nd_sem_grade` – 10.9%
3. `Curricular_units_1st_sem_approved` – 9.2%


4. `Curricular_units_1st_sem_grade` – 6.0%
5. `Admission_grade` – 4.4%

---

## ✅ Conclusion

Proyek ini berhasil membangun sistem prediksi mahasiswa dropout dengan akurasi mencapai **76.7%**, menggunakan model terbaik **Random Forest**. Sistem ini dapat digunakan untuk **identifikasi dini**, **intervensi risiko**, dan **pengambilan keputusan berbasis data** oleh institusi pendidikan.

Analisis data juga mengungkap insight penting terkait profil mahasiswa, risiko dropout, dan peluang pengembangan program.

---

### 📌 Rekomendasi Action Items

1. **Implementasi Early Warning System**
   - Monitor mahasiswa dengan risiko dropout tinggi (>70%)
   - Lakukan intervensi akademik dan finansial secara dini

2. **Program Intervensi Mahasiswa**
   - Bimbingan akademik & mentoring untuk mahasiswa berisiko
   - Program fleksibilitas pembayaran atau beasiswa

3. **Evaluasi & Update Berkala**
   - Perbarui model secara periodik dengan data terbaru
   - Pantau efektivitas intervensi dan identifikasi faktor baru

4. **Pendekatan Khusus Berdasarkan Insight**
   - 🎯 Fokus akademik: unit semester 1 & 2 yang berpengaruh besar
   - 💰 Finansial: bantu mahasiswa dengan status "Not up-to-date"
   - 🌍 Promosi internasional: peluang perluasan mahasiswa asing
   - 👨‍👩‍👧 Mahasiswa dewasa & menikah: butuh program fleksibel & support sosial

---
