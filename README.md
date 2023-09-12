# inventori

Link to adaptable: ______

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Membuat sebuah proyek Django baru
1. Membuat virtual environment (python -m venv env)
2. Mengaktifkan virtual environment (env\Scripts\activate.bat)
3. Membuat berkan requirement.txt dengan isinya berupa dependencies:
  django, gunicorn, whitenoise, psycopg2-binary, requests, urllib3
4. Menginstall dependencies (pip install -r requirements.txt)
5. Membuat proyek django (django-admin startproject inventori .)

- Membuat aplikasi dengan nama main pada proyek tersebut.
1. Pada direktori utama, jalankan command (python manage.py startapp main)
