Readme ini memberikan gambaran umum tentang proyek analisis teks menggunakan dataset BBC News. Proyek ini mencakup tahapan dari pengambilan data hingga analisis eksplorasi data (EDA).

---

# Proyek Analisis Teks: BBC News Dataset

Proyek ini bertujuan untuk melakukan analisis data eksploratif (EDA) pada kumpulan artikel berita dari BBC. Notebook ini dirancang sebagai template eksperimen untuk alur kerja Machine Learning, khususnya untuk tugas Natural Language Processing (NLP).

## 1. Daftar Isi

* [Deskripsi Proyek](https://www.google.com/search?q=%23deskripsi-proyek)
* [Struktur Dataset](https://www.google.com/search?q=%23struktur-dataset)
* [Prasyarat & Library](https://www.google.com/search?q=%23prasyarat--library)
* [Tahapan Proyek](https://www.google.com/search?q=%23tahapan-proyek)
* [Cara Penggunaan](https://www.google.com/search?q=%23cara-penggunaan)

## 2. Deskripsi Proyek

Eksperimen ini menggunakan dataset artikel berita BBC yang dikategorikan ke dalam beberapa topik. Fokus utama saat ini adalah memuat data dari Kaggle, melakukan pembersihan awal, dan memahami distribusi serta karakteristik teks melalui skor keterbacaan (*Readability Scores*).

## 3. Struktur Dataset

Dataset yang digunakan berasal dari dataset publik BBC News. Kolom-kolom utama meliputi:

* `text`: Isi lengkap artikel berita.
* `labels`: Kategori berita (Business, Entertainment, Politics, Sport, Tech).
* `no_sentences`: Jumlah kalimat dalam artikel.
* `Flesch Reading Ease Score`: Metrik tingkat kemudahan baca teks.
* `Dale-Chall Readability Score`: Metrik kompleksitas kosakata teks.
* `text_rank_summary` & `lsa_summary`: Ringkasan teks hasil ekstraksi.

## 4. Prasyarat & Library

Proyek ini dikembangkan menggunakan Python 3. Library utama yang digunakan meliputi:

* `pandas` & `os`: Manipulasi data dan manajemen file.
* `kagglehub`: Mengunduh dataset langsung dari Kaggle.
* `matplotlib` & `seaborn`: Visualisasi data.
* `nltk`: Pemrosesan bahasa alami (Stopwords).
* `scikit-learn`: Preprocessing data (LabelEncoder).

## 5. Tahapan Proyek

1. **Perkenalan & Sumber Dataset**: Mendefinisikan sumber data dari repositori publik.
2. **Import Library**: Menyiapkan lingkungan kerja.
3. **Memuat Dataset**: Mengunduh dataset menggunakan `kagglehub` dan menyimpannya ke direktori lokal (`../bbc_news_raw/`).
4. **Exploratory Data Analysis (EDA)**:
* Pengecekan nilai kosong (*missing values*).
* Analisis distribusi label (Kategori berita).
* Identifikasi *outlier* pada panjang teks menggunakan metode IQR.



## 6. Cara Penggunaan

1. Pastikan Anda memiliki kredensial Kaggle jika diperlukan oleh library.
2. Jalankan notebook `Template_Eksperimen_MSML.ipynb` secara berurutan.
3. Dataset akan otomatis terunduh dan disimpan di folder kerja Anda.

---

*Dokumentasi ini dibuat berdasarkan struktur file `Template_Eksperimen_MSML.ipynb`.*