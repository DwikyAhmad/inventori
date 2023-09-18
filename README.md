# inventori

Link to adaptable: https://inventoridwiky.adaptable.app/main/

## Tugas 3

### 1. Apa perbedaan antara form POST dan form GET dalam Django?
form POST merupakan form yang menyimpan data pada HTTP request body lalu dikirimkan ke server, karena data tidak terlihat di URL, POST form dilakukan untuk melakukan submission sensitive data atau large data. Submission dari form tersebut akan dikirimkan ke server untuk melakukan aksi seperti membuat new object pada server. Sedangkan form GET digunakan untuk menerima data dari server dengan menambahkan query pada URL parameters.

### 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
XML merupakan sebuah format data yang menggunakan markup sebagai struktur datanya, XML umumnya digunakan untuk melakukan perpindahan data antara sistem yang berbeda. JSON merupakan format data yang berbasis objek berupa key value seperti dictionary, JSON umumnya digunakan untuk pertukaran data antara aplikasi web dan layanan web, serta untuk penyimpanan konfigurasi. HTML merupakan format data yang digunakan untuk menampilkan data dalam bentuk halaman web pada browser, HTML tidak biasanya dilakukan untuk pertukaran data.

### 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- JSON memiliki format yang ringan dan mudah dibaca karena menggunakan struktur objek dan array yang mirip dengan sintaks javascript 
- JSON dapat digunakan dalam berbagai bahasa pemrograman
- JSON mendukung struktur data terstruktur seperti objek, array, tipe data dasar seperti string, number, boolean, dan null
- JSON mendukung nested data yang memungkinkan suatu objek dalam objek atau array dalam array
- JSON mendukung RESTful APIs yang merupakan pendekatan umum dalam pengembangan website

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Sebelum membuat form, saya membuat base template pada direktori utama sebagai kerangka views web.

#### Membuat input form untuk menambahkan objek model pada app sebelumnya.
Membuat berkas forms.py pada direktori main lalu menambahkan class ProductForm dengan model Item dan field name, amount, description
```python
from django.forms import ModelForm
from main.models import Item

class ProductForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description"]
```

pada create_item.html di templates directory main akan diisi html dengan form POST request untuk mengirim data ke HTTP request.
```django
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Item</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```

Setelah itu membuat sebuah function baru untuk menampilkan form dan melakukan save ke database
```python
def create_item(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

```

#### Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
format html masuk dalam template main.html menggunakan fungsi `show_main` dengan mengiterasi tiap item dalam items sekaligus link untuk membuat objek baru, atribut items dalam data context berupa items = Item.objects.all()
```html
<table>
    <tr>
        <th>Name</th>
        <th>Amount</th>
        <th>Description</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

    {% for item in items %}
        <tr>
            <td>{{item.name}}</td>
            <td>{{item.amount}}</td>
            <td>{{item.description}}</td>
        </tr>
    {% endfor %}
</table>

<br />

<a href="{% url 'main:create_product' %}">
    <button>
        Add New Item
    </button>
</a>
```
format xml dan json ditampilkan pada fungsi `show_xml` dan `show_json` dengan menampilkan hasil query dari seluruh data pada Items
```python
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
format xml by id dan json by id pada fungsi show_xml_by_id dan show_json_by_id menggunakan filter dengan paramater pk=id
```python
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

#### Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
route untuk semua produk xml dan json diberi route xml/ dan json/ sedangkan untuk xml dan json by id menggunakan paramater query `<int:id>`
```python
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item/', create_item, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]
```

### 5. Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
- HTML

![html_postman](/image_tugas3/html.png)

- XML  

![xml_postman](/image_tugas3/xml.png)

- JSON

![json_postman](/image_tugas3/json.png)

- XML by ID

![xml_by_id_postman](/image_tugas3/xml_by_id.png)

- JSON by ID

![json_by_id_postman](/image_tugas3/json_by_id.png)

## Tugas 2

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

#### Membuat sebuah proyek Django baru
  1. Membuat virtual environment (python -m venv env)
  2. Mengaktifkan virtual environment (env\Scripts\activate.bat)
  3. Membuat berkas requirement.txt dengan isinya berupa dependencies:
       django, gunicorn, whitenoise, psycopg2-binary, requests, urllib3
  4. Menginstall dependencies (pip install -r requirements.txt)
  5. Membuat proyek django (django-admin startproject inventori .)

#### Membuat aplikasi dengan nama main pada proyek tersebut.
  1. Pada direktori utama, jalankan command (python manage.py startapp main)
  2. Menambahkan 'main' pada INSTALLED_APPS variabel pada settings.py di direktori proyek

#### Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
  1. Mengimpor include dari django.urls lalu menambahkan rute URL ke main pada urlpatterns menggunakan include main.urls

#### Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
    - name sebagai nama item dengan tipe CharField.
    - amount sebagai jumlah item dengan tipe IntegerField.
    - description sebagai deskripsi item dengan tipe TextField.
   
  1. Pada berkas models.py di main, buat class Item dengan argumen models.Model
  2. atribut pada class Item mengandung name, amount, dan description
  3. name diassign models.CharField()
  4. amount diassign models.IntegeField()
  5. description diassign models.TextField()
  6. Melakukan migration model dengan command (python manage.py makemigrations) lalu (python manage.py migrate) untuk migrasi ke dalam basis data lokal

#### Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
  1. Membuat sebuah fungsi (contoh: show_main) yang akan mereturn sebuah data dan template html yang berada di folder templates di main

#### Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
  1. Menambahkan sebuah path di urlpatterns pada urls.py di direktori main dengan mereturn fungsi show_main

#### Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
  1. Melakukan deploy adaptable dengan menyambungkan repo inventori di github

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Bagan MTV](/Bagan%20MTV.png)
Pertama-tama user akan melakukan http request ke web django, dari aplikasi tersebut urls.py akan memeriksa url routingnya dan akan menjalankan fungsi pada views.py sesuai dengan urlpatterns, dari views.py akan dijalankan fungsi yang akan mereturn sebuah berkas template html yang diberi data yang diakses melalui model di models.py, melalui model dapat dilakukan read/write data, setelah itu akan dikirimkan berupa http response berupa template html yang sudah di proses ke user. 

### 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment diperlukan jika kita memiliki multiple django project yang memiliki versi python dan dependencies yang berbeda, kita dapat memiliki banyak versi dari python libraries dan modules terisolasi dari proyek lainnya sehingga tidak terjadi conflict terhadap version yang digunakan. Menggunakan virtual environment juga dapat digunakan untuk melakukan tracking terhadap versi dependencies yang digunakan sehingga developer dapat mengetahui requirements apa yang dibutuhkan untuk menjalankan proyek.

### 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
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
