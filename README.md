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
>Password: dG8M@BWcewxUtxc

### Menjalankan Aplikasi dan Model Prediksi:
Untuk mencoba prototipe model prediksi dan aplikasi dashboard, dapat mengakses link berikut yang sudah dideploy di Streamlit Community Cloud:
> https://mhd-rizki-bpds-edutech.streamlit.app/
