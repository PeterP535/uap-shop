Nama : Peter Putra Lesmana
NPM : 2306152361
Kelas: PBP B

[Tugas 2](#tugas-2)
[Tugas 3](#tugas-3)

# Tugas 2
## Membuat sebuah proyek Django baru
1. Membuat direktori baru untuk proyek Django baru.
2. Buka command prompt di direktori tersebut dan jalankan perintah `python -m venv env` untuk membuat virtual environment untuk Python. Environment akan mengisolasi package dan *dependencies* dari aplikasi sehingga tidak konflik dengan versi lain.
3. Mengaktifkan virtual environment dengan menjalankan perintah `env\Scripts\activate.bat` (windows).
4. Buat file dengn nama `requirements.txt` di direktori yang sama dan isi dengan *dependencies* berikut:
`django`
`gunicorn`
`whitenoise`
`psycopg2-binary`
`requests`
`urllib3`
5. Install *dependencies* dengan perintah `pip install -r requirements.txt` dengan virtual environment menyala.
6. Membuat proyek Django dengan nama yang diinginkan melalui perintah `django-admin startproject uap_shop .`
7. Buka file settings.py yang ada di dalam folder yang telah dibuat dan tambahkan '*' pada `ALLOWED_HOSTS` untuk mengizinkan akses dari semua *host*.
8. Buka kembali command prompt dan jalankan perintah `python manage.py runserver` (windows) dan buka http://localhost:8000 untuk melihat apakah aplikasi Django berhasil dibuat.
9. Hentikan server dengan menekan `Ctrl+C` di command prompt dan jalankan perintah `deactivate` untuk mematikan virtual environment. Push hasil perubahan ke GitHub.

## Membuat aplikasi dengan nama main pada proyek tersebut.
1. Mengaktifkan virtual environment dengan perintah `env\Scripts\activate.bat` (windows).
2. Jalankan perintah `python manage.py startapp main` untuk membuat aplikasi baru dengan nama main.
3. Buka berkas settings.py di dalam proyek Django yang dibuat dan tambahkan `'main'` di variabel `INSTALLED_APPS`. 

## Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
1. Membuat berkas dengan nama `urls.py` di dalam direktori `main` dan isi dengan kode berikut untuk mengatur rute URL:
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
show_main digunakan sebagai tampilan ketika URL yang terkait diakses dan app_name sebagai nama unik pada pola URL aplikasi.
2. Buka berkas `urls.py` di direktori proyek Django dan bukan `urls.py` di direktori `main` dan tambahkan rute URL seperti berikut:
```python
urlpatterns = [
    ...
    path('main/', include('main.urls')),
    ...
]
```
*Path* `main/` akan diarahkan ke rute yang didefinisikan dalam berkas `urls.py` pada aplikasi `main`.

## Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
1. Buka file `models.py` dan isi file dengan nama dan atribut yang diminta.
2. Berdasarkan ketentuan soal, file minimal harus memiliki isi sebagai berikut:
```python
from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    description = models.TextField(null=True)
```
3. Jalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk mengaplikasikan perubahan model.

## Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
1. Buka file `views.py` di dalam direktori `main`.
2. Tambahkan kode berikut ke dalam file.
```python 
from django.shortcuts import render
``` 
3. Tambahkan fungsi berikut ke dalam file.
```python
def show_main(request):
    context = {
        'npm' : 'npm'
        'name': 'nama',
        'class': 'kelas'
    }

    return render(request, "main.html", context)
```
4. Buat direktori dengan nama `templates` di dalam direktori main dan buat file dengan nama `main.html` kemudian isi dengan kode html untuk menampilkan data yang ada di file sebelumnya.
```html
<h1>UAP SHOP</h1>

<h5>NPM: </h5>
<p>{{ npm }}<p>
<h5>Name: </h5>
<p>{{ name }}<p>
<h5>Class: </h5>
<p>{{ class }}<p>

```

## Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
1. Membuat berkas dengan nama `urls.py` di dalam direktori `main` dan isi dengan kode berikut untuk mengatur rute URL:
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
## Melakukan deployment ke PWS sehingga nantinya dapat diakses oleh teman-teman melalui Internet.
1. Akses halaman PWS pada https://pbp.cs.ui.ac.id. dan melakukan login/register
2. Buat proyek baru dengan menekan tombol Create New Project dan masukkan nama project untuk membuat projectnya
3. Akan muncul dua informasi baru, yaitu mengenai Project Credentials dan Project Command. Simpan credentials yang kamu peroleh di tempat yang aman, karena seterusnya credentials ini tidak akan bisa kamu lihat lagi. Jangan jalankan dulu instruksi Project Command.
4. Pada settings.py di proyek Django yang sudah kamu buat tadi, tambahkan URL deployment PWS pada ALLOWED_HOSTS.
```python
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "<URL deployment PWS kamu>"]
```
5. Jalankan perintah yang terdapat pada informasi Project Command pada halaman PWS. Ketika kamu melakukan push ke PWS, akan ada window yang meminta username dan password. Gunakan credentials yang kamu terima dari PWS, bukan credentials SSO.

6. Setelah menjalankan perintah sebelumnya, jalankan perintah ini untuk kembali mengubah nama branch utama kamu menjadi main.
```
git branch -M main
```
7. Pada side bar situs PWS, klik proyek yang telah kamu buat. Kamu dapat melihat status deployment kamu saat ini. Apabila statusnya Building, artinya proyek kamu masih dalam proses deployment. Apabila statusnya Running, maka proyek kamu sudah bisa diakses pada URL deployment. Kamu bisa menekan tombol View Project yang terdapat pada halaman proyek kamu.

## *Request client* ke web aplikasi berbasis Django beserta responnya

![DJango Framework](https://github.com/PeterP535/uap-shop/blob/main/images/bagan1.png)
Pertama, pengguna atau klien akan meminta akses atau resource. Django kemudian akan memproses URL dari klien dan mencocokkannya dengan pola yang ada di file urls.py (pemetaan URL). Selanjutnya, Django akan merujuk ke file views.py untuk mengakses tampilan yang sesuai. File models.py akan mengelola data yang diperlukan berdasarkan permintaan pengguna, sedangkan folder template menyimpan file-file dengan ekstensi html. File-file tersebut berisi kode HTML yang mengatur elemen seperti teks, tabel, ukuran, dan lainnya. Setelah semuanya diproses, hasil tampilan akan dikirim kembali ke pengguna atau klien. 
Source: https://intellipaat.com/blog/tutorial/python-django-tutorial/

## Fungsi dari git dalam pengembangan perangkat lunak
Git adalah sistem kontrol versi yang penting dalam pengembangan perangkat lunak, memungkinkan pengembang melacak perubahan kode, bekerja secara kolaboratif, dan mengelola versi proyek secara efisien. Dengan fitur branching dan merging, tim dapat mengembangkan fitur atau memperbaiki bug tanpa mengganggu kode utama. Setiap perubahan dicatat melalui commit, memudahkan tinjauan dan pemulihan versi jika terjadi kesalahan. Git juga memungkinkan kolaborasi tim secara terdistribusi, memberikan setiap anggota salinan penuh dari proyek, serta mendukung kerja offline yang bisa disinkronkan dengan repositori pusat saat online. Fungsionalitas ini menjadikan Git alat penting untuk pengembangan perangkat lunak yang terstruktur dan kolaboratif.
Source: https://www.simplilearn.com/tutorials/git-tutorial/what-is-git

## Framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak
Django sering dijadikan pilihan awal dalam pembelajaran pengembangan perangkat lunak karena beberapa alasan kuat. Pertama, Django adalah framework berbasis Python, bahasa pemrograman yang terkenal dengan sintaks yang mudah dipahami dan digunakan oleh pemula. Django juga menyediakan struktur "batteries-included," yang berarti sudah dilengkapi dengan banyak fitur bawaan seperti autentikasi, ORM (Object-Relational Mapping), dan admin panel, sehingga pengembang pemula tidak perlu membangun dari nol. Selain itu, Django mendorong praktik terbaik seperti DRY (Don't Repeat Yourself) dan pembagian kode yang jelas melalui konsep Model-View-Template (MVT), yang membantu pemula memahami arsitektur perangkat lunak yang terorganisir.
Source: https://sunscrapers.com/blog/pros-and-cons-of-using-django-for-web-development/

## Mengapa model pada Django disebut sebagai ORM?
Pada Django, model disebut sebagai ORM (Object-Relational Mapping) karena perannya dalam memetakan objek Python ke tabel pada database relasional. Dengan menggunakan ORM, pengembang dapat mengelola database menggunakan kode objek alih-alih menulis kueri SQL secara langsung. Setiap kelas model di Django merepresentasikan tabel dalam database, dan setiap atributnya adalah kolom dari tabel tersebut. ORM di Django memungkinkan pengembang melakukan operasi database seperti Create, Read, Update, dan Delete (CRUD) dengan lebih mudah, efisien, dan aman, sekaligus mencegah kesalahan umum seperti injeksi SQL.
Source: https://www.scaler.com/topics/django/django-orm/


# Tugas 3
# Data Delivery dalam Pengimplementasian Sebuah Platform

Data delivery merupakan elemen penting dalam pengimplementasian sebuah platform. Berikut adalah alasan mengapa data delivery dibutuhkan:

## 1. Penyampaian Informasi
Data delivery memastikan bahwa informasi dapat disampaikan kepada pengguna akhir atau sistem tujuan dengan **cepat**, **akurat**, dan **aman**. Dalam sebuah platform, data harus ditransfer dari sumber ke pengguna agar platform dapat berfungsi sebagaimana mestinya.

## 2. Konektivitas dan Komunikasi
Dalam sistem terdistribusi atau platform berbasis cloud, berbagai komponen sering kali berada di lokasi yang berbeda. Data delivery memungkinkan **komunikasi** antara komponen-komponen tersebut (misalnya, antara server dengan klien atau antar server) agar platform dapat bekerja secara **sinkron** dan **terintegrasi**.

## 3. Efisiensi Operasional
Penggunaan metode dan strategi data delivery yang baik, seperti **caching**, **load balancing**, atau **content delivery networks (CDN)**, dapat meningkatkan **performa** platform, mengurangi **latensi**, dan memaksimalkan **pengalaman pengguna**.

## 4. Skalabilitas
Dalam platform yang melayani banyak pengguna secara simultan, data delivery memungkinkan **skala** yang lebih besar. Ini membantu mengelola distribusi data agar bisa diakses secara efisien oleh banyak pengguna tanpa mengganggu kinerja platform.

## 5. Keamanan Data
Data delivery juga melibatkan pengaturan **keamanan**, seperti **enkripsi** selama transmisi untuk mencegah akses tidak sah atau manipulasi data saat dalam perjalanan.

## 6. Sinkronisasi Data
Dalam platform yang menangani banyak pengguna atau perangkat, **sinkronisasi data** sangat penting. Data delivery memastikan semua pihak atau perangkat memiliki akses ke data yang paling mutakhir dan **konsisten**.

---

Tanpa **data delivery** yang efisien, sebuah platform akan mengalami masalah dalam kecepatan akses, keamanan, dan kualitas layanan yang ditawarkan.

# XML vs JSON: Mana yang Lebih Baik?

Ketika berbicara tentang format untuk pertukaran data, dua format yang sering digunakan adalah **XML (Extensible Markup Language)** dan **JSON (JavaScript Object Notation)**. Masing-masing memiliki keunggulan tersendiri, namun JSON menjadi lebih populer dalam banyak kasus.

## 1. XML (Extensible Markup Language)
XML adalah format markup yang dirancang untuk menyimpan dan mengangkut data. Beberapa fitur utama XML:

- **Struktur hierarki**: XML menggunakan struktur berbasis elemen dengan tag pembuka dan penutup, memungkinkan representasi data yang kompleks.
- **Skema yang ketat**: XML dapat menggunakan skema (XSD) untuk memastikan data mengikuti format tertentu.
- **Fleksibel**: XML tidak bergantung pada platform atau bahasa pemrograman tertentu.
- **Lebih banyak fitur**: XML mendukung namespace, transformasi (XSLT), dan validasi yang kuat, yang membuatnya ideal untuk aplikasi lebih kompleks.

Namun, XML memiliki kelemahan dalam hal **ukuran** dan **kompleksitas** karena markup yang lebih verbose dan lebih sulit untuk diproses tanpa alat atau parser khusus.

## 2. JSON (JavaScript Object Notation)
JSON adalah format data berbasis teks yang lebih ringan dan lebih mudah dibaca. Beberapa fitur utama JSON:

- **Kesederhanaan**: JSON memiliki struktur yang lebih sederhana dan ringkas, hanya terdiri dari key-value pairs, array, dan objek.
- **Ukuran lebih kecil**: Karena lebih ringkas, JSON membutuhkan lebih sedikit ruang penyimpanan dan bandwidth dibandingkan XML.
- **Native ke JavaScript**: JSON bekerja secara native di banyak bahasa pemrograman, terutama JavaScript, yang menjadikannya pilihan populer untuk pengembangan web modern.
- **Kemudahan parsing**: JSON lebih mudah diproses dan diparse dalam banyak bahasa pemrograman dengan sedikit overhead.

JSON cocok untuk penggunaan umum dalam aplikasi web modern yang membutuhkan **kecepatan**, **efisiensi**, dan **kesederhanaan**.

---

# Mengapa JSON Lebih Populer Dibandingkan XML?

Berikut adalah alasan-alasan mengapa JSON lebih populer, terutama dalam pengembangan aplikasi web dan pertukaran data modern:

## 1. **Ringkas dan Efisien**
JSON memiliki struktur yang lebih sederhana dan lebih ringkas dibandingkan XML. Ini berarti bahwa JSON lebih hemat bandwidth dan penyimpanan karena tidak memerlukan tag pembuka dan penutup yang panjang seperti XML.

## 2. **Lebih Mudah Dibaca dan Ditulis**
Berkat formatnya yang lebih simpel, JSON lebih mudah dibaca oleh manusia dan ditulis oleh mesin. Struktur key-value yang dimiliki JSON lebih intuitif dibandingkan struktur XML yang berbasis tag.

## 3. **Kecepatan Parsing**
JSON dapat diparse lebih cepat dibandingkan XML. Ini menjadi keuntungan besar untuk aplikasi web yang memerlukan respons cepat dari server. Sebagian besar bahasa pemrograman modern memiliki parser JSON yang sangat efisien.

## 4. **Native untuk JavaScript**
JSON dirancang untuk bekerja dengan JavaScript, bahasa yang mendominasi pengembangan web saat ini. Karena JSON dapat dengan mudah diubah menjadi objek JavaScript, ini menjadi pilihan yang logis untuk aplikasi web front-end dan back-end.

## 5. **Dukungan Lebih Luas**
JSON telah menjadi standar de facto untuk pertukaran data pada aplikasi web API modern (RESTful APIs). Banyak layanan dan framework lebih mendukung JSON daripada XML karena kelebihan performanya.

---

## Kapan Menggunakan XML?

Meskipun JSON lebih populer, XML masih relevan dalam kasus-kasus tertentu:

- **Dokumen yang kompleks**: XML lebih cocok untuk dokumen dengan struktur yang sangat kompleks, seperti dokumen legal atau data ilmiah.
- **Validasi ketat**: XML mendukung validasi dengan menggunakan skema (XSD) untuk memastikan bahwa data mengikuti aturan tertentu.
- **Transformasi data**: XML mendukung XSLT untuk mentransformasi data ke dalam format lain, yang tidak dapat dilakukan oleh JSON.

---

Secara umum, **JSON** lebih cocok untuk aplikasi modern, sementara **XML** lebih baik digunakan untuk kasus yang memerlukan kontrol yang lebih ketat atas struktur data dan validasi.

# Django Forms: Fungsi `is_valid()` Method

Dalam framework **Django**, form adalah alat penting untuk mengelola input data dari pengguna. Salah satu method paling penting yang sering digunakan pada form Django adalah **`is_valid()`**. 

## Fungsi `is_valid()`

`is_valid()` adalah method yang digunakan untuk memeriksa apakah data yang dimasukkan ke dalam form sudah memenuhi aturan validasi yang ditetapkan pada form tersebut. Method ini akan:

1. **Menjalankan validasi**: Saat `is_valid()` dipanggil, Django akan memeriksa semua field yang ada pada form sesuai dengan aturan validasi yang telah didefinisikan.
2. **Mengembalikan True atau False**: Jika data yang dimasukkan sesuai dengan aturan validasi (valid), maka `is_valid()` akan mengembalikan `True`. Jika ada kesalahan (invalid), maka `is_valid()` akan mengembalikan `False`.
3. **Mengisi cleaned_data**: Jika valid, data yang telah divalidasi dan dibersihkan akan dimasukkan ke dalam atribut `cleaned_data` dari form tersebut.


# Mengapa Kita Membutuhkan `csrf_token` dalam Form Django?

Dalam framework **Django**, penggunaan **`csrf_token`** sangat penting untuk menjaga keamanan aplikasi dari serangan **Cross-Site Request Forgery (CSRF)**. CSRF adalah jenis serangan yang memanfaatkan kepercayaan pengguna terhadap suatu situs untuk menjalankan tindakan yang tidak sah atas nama pengguna tersebut.

## Apa Itu CSRF?

**CSRF (Cross-Site Request Forgery)** adalah serangan di mana penyerang mencoba membuat pengguna yang sah melakukan tindakan yang tidak diinginkan pada aplikasi web tanpa sepengetahuannya. Contohnya, jika pengguna sudah login ke situs tertentu, penyerang bisa mengirimkan permintaan berbahaya dari situs lain untuk mengeksekusi perintah di situs tersebut, seperti mengubah data atau melakukan transaksi tanpa sepengetahuan pengguna.

---

## Fungsi `csrf_token` dalam Django

`csrf_token` adalah **token keamanan** yang dihasilkan secara acak oleh Django dan disertakan dalam setiap form HTML yang akan mengirimkan data melalui metode **POST**. Token ini digunakan untuk memverifikasi bahwa permintaan yang datang benar-benar berasal dari pengguna yang sah dan bukan dari sumber eksternal atau pihak ketiga.

### Alasan Pentingnya `csrf_token`:

1. **Mencegah CSRF**: Token ini melindungi aplikasi dari serangan CSRF dengan memastikan bahwa setiap permintaan POST berasal dari sumber yang sah (yaitu, dari situs yang sama).
2. **Verifikasi Asal Permintaan**: Setiap kali pengguna mengirimkan form, Django memeriksa apakah token CSRF yang terkirim sesuai dengan token yang disimpan di sesi pengguna. Jika token tidak valid atau tidak ada, permintaan akan ditolak.
3. **Otomatis di Django**: Django secara otomatis menghasilkan dan memverifikasi token CSRF, sehingga pengembang hanya perlu menyertakannya dalam form dengan menggunakan tag template `{% csrf_token %}`.

---

## Apa yang Terjadi Jika Tidak Menambahkan `csrf_token`?

Jika form tidak menyertakan `csrf_token`, beberapa hal buruk bisa terjadi:

1. **Aplikasi Rentan Terhadap CSRF**: Tanpa token CSRF, aplikasi rentan terhadap serangan CSRF. Penyerang dapat dengan mudah mengirimkan permintaan berbahaya yang tampak sah kepada aplikasi, seperti memaksa pengguna untuk:
   - Mengirimkan formulir tanpa izin mereka.
   - Mengubah pengaturan akun pengguna.
   - Melakukan transaksi yang tidak diinginkan.
   
2. **Permintaan POST Ditolak oleh Django**: Django secara default akan menolak semua permintaan POST yang tidak memiliki token CSRF yang valid. Hal ini dilakukan untuk melindungi aplikasi dari serangan. Jadi, jika form POST dikirim tanpa token CSRF, pengguna akan mendapatkan respons "403 Forbidden" karena Django mendeteksi bahwa form tersebut tidak aman.

---

## Bagaimana CSRF Dapat Dimanfaatkan oleh Penyerang?

Jika token CSRF tidak digunakan, penyerang dapat memanfaatkan kelemahan ini untuk melakukan serangan CSRF, yang bisa terjadi dengan skenario berikut:

1. **Membuat Permintaan Berbahaya**: Penyerang bisa membuat tautan atau form berbahaya di situs lain yang mengirimkan permintaan POST ke aplikasi yang sah di mana pengguna sudah login. Misalnya:
   - Penyerang bisa membuat form tersembunyi yang mengirimkan permintaan untuk mengubah kata sandi atau melakukan pembayaran di situs korban.
   
2. **Mengelabui Pengguna**: Jika pengguna mengklik tautan atau memuat situs berbahaya tersebut saat mereka masih login ke aplikasi yang sah, permintaan akan tampak seperti berasal dari pengguna yang sah, dan server mungkin menganggap permintaan itu sah jika tidak ada validasi `csrf_token`.

3. **Eksekusi Perintah Berbahaya**: Tanpa `csrf_token`, server tidak dapat membedakan antara permintaan yang sah dan yang tidak sah, sehingga penyerang dapat menjalankan berbagai aksi yang tidak diinginkan atas nama pengguna.

---

## Contoh Serangan CSRF

Contoh serangan CSRF sederhana:

1. Pengguna login ke aplikasi **bank.com**.
2. Penyerang membuat situs berbahaya dengan form yang tampak sah dan memuatnya di situs **evil.com**.
3. Saat pengguna yang sudah login ke **bank.com** mengunjungi **evil.com**, form berbahaya tersebut dikirimkan ke **bank.com** tanpa sepengetahuan pengguna, dan server memprosesnya karena tidak ada validasi CSRF.
4. Penyerang berhasil menjalankan transaksi atas nama pengguna tanpa izin.

# Postman
![DJango Framework](https://github.com/PeterP535/uap-shop/blob/main/images/postman1.png)
![DJango Framework](https://github.com/PeterP535/uap-shop/blob/main/images/postman2.png)
![DJango Framework](https://github.com/PeterP535/uap-shop/blob/main/images/postman3.png)
![DJango Framework](https://github.com/PeterP535/uap-shop/blob/main/images/postman4.png)