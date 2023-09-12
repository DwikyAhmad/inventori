# inventori

Link to adaptable: (https://inventoridwiky.adaptable.app/main/)

## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### Membuat sebuah proyek Django baru
  1. Membuat virtual environment (python -m venv env)
  2. Mengaktifkan virtual environment (env\Scripts\activate.bat)
  3. Membuat berkas requirement.txt dengan isinya berupa dependencies:
       django, gunicorn, whitenoise, psycopg2-binary, requests, urllib3
  4. Menginstall dependencies (pip install -r requirements.txt)
  5. Membuat proyek django (django-admin startproject inventori .)

### Membuat aplikasi dengan nama main pada proyek tersebut.
  1. Pada direktori utama, jalankan command (python manage.py startapp main)
  2. Menambahkan 'main' pada INSTALLED_APPS variabel pada settings.py di direktori proyek

### Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
  1. Mengimpor include dari django.urls lalu menambahkan rute URL ke main pada urlpatterns menggunakan include main.urls

### Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
    - name sebagai nama item dengan tipe CharField.
    - amount sebagai jumlah item dengan tipe IntegerField.
    - description sebagai deskripsi item dengan tipe TextField.
   
  1. Pada berkas models.py di main, buat class Item dengan argumen models.Model
  2. atribut pada class Item mengandung name, amount, dan description
  3. name diassign models.CharField()
  4. amount diassign models.IntegeField()
  5. description diassign models.TextField()
  6. Melakukan migration model dengan command (python manage.py makemigrations) lalu (python manage.py migrate) untuk migrasi ke dalam basis data lokal

### Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
  1. Membuat sebuah fungsi (contoh: show_main) yang akan mereturn sebuah data dan template html yang berada di folder templates di main

### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
  1. Menambahkan sebuah path di urlpatterns pada urls.py di direktori main dengan mereturn fungsi show_main

### Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
  1. Melakukan deploy adaptable dengan menyambungkan repo inventori di github

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Bagan MTV](https://github.com/DwikyAhmad/inventori/blob/main/Bagan%20MTV.png)
Pertama-tama user akan melakukan http request ke web django, dari aplikasi tersebut urls.py akan memeriksa url routingnya dan akan menjalankan fungsi pada views.py sesuai dengan urlpatterns, dari views.py akan dijalankan fungsi yang akan mereturn sebuah berkas template html yang diberi data yang diakses melalui model di models.py, melalui model dapat dilakukan read/write data, setelah itu akan dikirimkan berupa http response berupa template html yang sudah di proses ke user. 

## 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment diperlukan jika kita memiliki multiple django project yang memiliki versi python dan dependencies yang berbeda, kita dapat memiliki banyak versi dari python libraries dan modules terisolasi dari proyek lainnya sehingga tidak terjadi conflict terhadap version yang digunakan. Menggunakan virtual environment juga dapat digunakan untuk melakukan tracking terhadap versi dependencies yang digunakan sehingga developer dapat mengetahui requirements apa yang dibutuhkan untuk menjalankan proyek.

## 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC merupakan design pattern pada web yang meliputi:
1. Model: mengatur logika dan akses pada database
2. View: Mengatur cara kerja data ditampilkan pada aplikasi
3. Memanipulasi model dan melakukan render pada view yang berperan sebagai penghubung dari keduanya

MVT merupakan design pattern yang mirip dengan MVC akan tetapi controller sudah ditangani oleh frameworknya sendiri
1. Model: Berperan sebagai interface data dan struktur logika dari sebuah aplikasi
2. View: Melakukan business logic dan berinteraksi dengan model dan melakukan render template
3. Template: Berperan sebagai lapisan presentasi yang melakukan render pada data ke berkas html.

MVVM
Design pattern yang memiliki perbedaan yaitu pada viewmodel
1. Model: Berperan sebagai representasi dari data dan struktur logik pada aplikasi
2. View: Mengatur tampilan interface dan data pada aplikasi
3. ViewModel: Bertindak sebagai perantara antara Model dan View

Perbedaan: MVVM cocok digunakan untuk pengembangan aplikasi dengan antarmuka yang kompleks karena lebih fokus pada tampilan logika bisnis, MVC mempunyai controller yang bertanggung jawab atas alur pengendalian aplikasi, cocok digunakan untuk pengembangan aplikasi web dan desktop tradisional, MVT merupakan pendekatan yang digunakan pada framework Django dengan perbedaan controller sudah diurus oleh framework.
