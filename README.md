Nama : Peter Putra Lesmana
NPM : 2306152361
Kelas: PBP B
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
...python
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "<URL deployment PWS kamu>"]
...
5. Jalankan perintah yang terdapat pada informasi Project Command pada halaman PWS. Ketika kamu melakukan push ke PWS, akan ada window yang meminta username dan password. Gunakan credentials yang kamu terima dari PWS, bukan credentials SSO.

6. Setelah menjalankan perintah sebelumnya, jalankan perintah ini untuk kembali mengubah nama branch utama kamu menjadi main.
```
git branch -M main
```
7. Pada side bar situs PWS, klik proyek yang telah kamu buat. Kamu dapat melihat status deployment kamu saat ini. Apabila statusnya Building, artinya proyek kamu masih dalam proses deployment. Apabila statusnya Running, maka proyek kamu sudah bisa diakses pada URL deployment. Kamu bisa menekan tombol View Project yang terdapat pada halaman proyek kamu.

## *Request client* ke web aplikasi berbasis Django beserta responnya



Pertama, pengguna atau klien akan meminta akses atau resource. Django kemudian akan memproses URL dari klien dan mencocokkannya dengan pola yang ada di file urls.py (pemetaan URL). Selanjutnya, Django akan merujuk ke file views.py untuk mengakses tampilan yang sesuai. File models.py akan mengelola data yang diperlukan berdasarkan permintaan pengguna, sedangkan folder template menyimpan file-file dengan ekstensi html. File-file tersebut berisi kode HTML yang mengatur elemen seperti teks, tabel, ukuran, dan lainnya. Setelah semuanya diproses, hasil tampilan akan dikirim kembali ke pengguna atau klien. Source: https://intellipaat.com/blog/tutorial/python-django-tutorial/