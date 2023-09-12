# inventori

Link to adaptable: ______

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

  - Membuat sebuah proyek Django baru
    1. Membuat virtual environment (python -m venv env)
    2. Mengaktifkan virtual environment (env\Scripts\activate.bat)
    3. Membuat berkan requirement.txt dengan isinya berupa dependencies:
       django, gunicorn, whitenoise, psycopg2-binary, requests, urllib3
    4. Menginstall dependencies (pip install -r requirements.txt)
    5. Membuat proyek django (django-admin startproject inventori .)

  - Membuat aplikasi dengan nama main pada proyek tersebut.
    1. Pada direktori utama, jalankan command (python manage.py startapp main)
    2. Menambahkan 'main' pada INSTALLED_APPS variabel pada settings.py di direktori proyek

  - Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
    1. Mengimpor include dari django.urls lalu menambahkan rute URL ke main pada urlpatterns menggunakan include main.urls

  - Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
      - name sebagai nama item dengan tipe CharField.
      - amount sebagai jumlah item dengan tipe IntegerField.
      - description sebagai deskripsi item dengan tipe TextField.
    
    1. Pada berkas models.py di main, buat class Item dengan argumen models.Model
    2. atribut pada class Item mengandung name, amount, dan description
    3. name diassign models.CharField()
    4. amount diassign models.IntegeField()
    5. description diassign models.TextField()
    6. Melakukan migration model dengan command (python manage.py makemigrations) lalu (python manage.py migrate) untuk migrasi ke dalam basis data lokal

  - Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
    1. Membuat sebuah fungsi (contoh: show_main) yang akan mereturn sebuah data dan template html yang berada di folder templates di main

  - Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
    1. Menambahkan sebuah path di urlpatterns pada urls.py di direktori main dengan mereturn fungsi show_main

  - Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    1. Melakukan deploy adaptable dengan menyambungkan repo inventori di github

2. 
