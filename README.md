# inventori

Link to adaptable: https://inventoridwiky.adaptable.app/main/

## Tugas 6

### 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
synchronous programming merupakan cara kerja eksekusi sebuah perintah yang dilakukan secara berurut satu persatu dengan selalu menunggu perintah tersebut selesai dieksekusi terlebih dahulu lalu dilanjutkan ke perintah berikutnya, pada asynchronous programming, perintah akan dijalankan secara paralel sehingga perintah lainnya dapat tetap berjalan tanpa harus menunggu perintah sebelumnya untuk selesai di eksekusi, hal ini membuat aplikasi tetap responsif apabila terdapat perintah yang memerlukan waktu yang banyak sehingga aplikasi tidak terhenti untuk menunggu perintah tersebut selesai dahulu. 

### 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-driven programming merupakan pendekatan dalam pengembangan aplikasi yang di mana aplikasi tersebut merespons sebuah event/peristiwa secara asinkronus, hal ini dilakukan agar program dapat berjalan secara responsif dan interaktif, salah satu contoh penerapan yang dilakukan pada tugas ini adalah melakukan get product menggunakan fungsi asinkronus pada javascript yang akan melakukan fetch dari database dalam bentuk json. fungsi ini dijalankan saat melakukan refresh products dengan melakukan await dan menampilkannya dalam bentuk card, lalu juga dari fungsi add product pada javascript ditambahkan sebuah add event ke tombol add product by AJAX untuk melakukan add product dan menjalankan fungsi refresh product secara asinkronus.

### 3. Jelaskan penerapan asynchronous programming pada AJAX.
Asynchronous programming pada AJAX merupakan sebuah teknologi yang memungkinkan pertukaran data antara website dengan server tanpa perlu melakukan refresh pada halaman tersebut. Contoh penerapan yang dapat dilakukan adalah melakukan fetch untuk merequest data dari server dan menampilkannya pada browser, melakukan request untuk membuat instance object untuk disimpan ke database. Data yang digunakan dapat berupa bentuk XML atau JSON.

### 4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
Fetch Api:<br>
- Sudah menjadi bagian dari standar Javascript dan tersedia pada sebagian besar browser yang lebih baru
- Fetch API lebih ringan dari JQuery
- Menggunakan Promises, memerlukan kode yang lebih banyak
- Plugin dan ekstensi belum selengkap JQuery

JQuery:<br>
- Teknologi sudah hadir bertahun-tahun, mendukung banyak browser utama, termasuk yang lebih lama
- Memiliki ukuran yang besar karena library yang memiliki banyak fitur tambahan
- Lebih mudah digunakan karena sintaks yang mudah dipahami dan lebih singkat untuk AJAX
- Memiliki banyak plugin dan ekstensi untuk berbagai keperluan

Kedua teknologi memiliki kelebihan dan kekurangannya masing-masing, apabila proyek kita membutuhkan kinerja dan ukuran yang lebih ringan lebih baik kita menggunakan Fetch API, tetapi jika kita lebih membutuhkan kemudahan penggunaan dan dukungan pada jangkauan browser lebih luas seperti browser yang lebih lama, kita lebih baik menggunakan JQuery.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- AJAX GET:<br>
Untuk membuat ajax get, function get_product_json dibuat dengan menerima item yang berkaitan dengan user sedang login dan mengirim data tersebut dalam bentuk json melalui httpresponse dan menambahkan function tersebut ke urls. function tersebut akan digunakan pada script asinkronus pada main.html yaitu getProducts untuk menerima response menggunakan fetch API. Untuk menampilkan data items dibuat asynchronous function refreshProducts untuk melakukan await dari function getProducts dan menampilkan tiap items pada card yang nantinya akan di tempelkan ke div dengan class product_card melalui DOM HTML.

- AJAX POST:<br>
Dari Bootstrap, akan diambil komponen berupa modal yang akan berisi sebuah form untuk membuat objek items yang akan ditampilkan melalui sebuah button. Untuk menambahkan objek melalui ajax akan dibuat function add_product_ajax yang akan menyimpan object ke database berdasarkan request yang diberikan, lalu function tersebut dimasukkan ke urls. Lalu pada javascript akan dibuat function addProduct untuk melakukan POST request dengan fetch untuk membuat item baru dan melakukan refresh product, setelah itu form pada modal akan dilakukan reset sehingga form menjadi kosong kembali.

- Melakukan perintah collectstatic.<br>
Untuk melakukan perintah collectstatic pada `settings.py` di folder proyek akan di tambahkan `STATIC_ROOT  = os.path.join(BASE_DIR, 'staticfiles')` untuk mengatur lokasi penyimpanan static dari berbagai aplikasi. Setelah itu dijalankan perintah `python manage.py collectstatic` pada terminal.

## Tugas 5

### 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
- Universal Selector<br>
Bermanfaat untuk memilih semua elemen, tepat digunakan saat membuat default style dalam sebuah halaman web seperti menghilangkan padding dan margin bawaan.

- Type Selector<br>
Bermanfaat untuk memilih semua elemen dengan jenis yang sama, tepat digunakan untuk mengatur style pada elemen khusus seperti mengatur font-size pada tag p saja.

- Class Selector<br>
Bermanfaat untuk memilih elemen dengan nama class tertentu, tepat digunakan untuk melakukan suatu styling pada elemen dengan nama class yang sama.

- ID Selector<br>
Bermaanfaat untuk memilih elemen dengan ID yang unik, tepat digunakan untuk mengubah styling suatu elemen khusus yang telah diberi ID yang unik.

- Descendant Selector<br>
Bermaanfaat untuk memilih elemen yang merupakan keturunan dari elemen lainnya, tepat digunakan untuk memilih suatu elemen dengan tingkat susunan hierarki tertentu.

- Child Selector<br>
Bermanfaat untuk memilih elemen direct child dari suatu element, tepat digunakan untuk mengubah styling suatu elemen yang merupakan direct child dari suatu elemen tertentu.

- Adjacent Sibling Selector<br>
Bermanfaat untuk memilih suatu elemen yang berkesampingan dengan suatu elemen lain, tepat digunakan untuk mengatur style elemen yang saling berdekatan.

- Atribute Selector<br>
Bermanfaat untuk memilih suatu elemen berdasarkan atribut, tepat digunakan untuk mengubah suatu style elemen yang spesifik hanya memiliki atribut tersebut.

### 2. Jelaskan HTML5 Tag yang kamu ketahui.
Pada HTML5 terdapat tag semantik yaitu berupa:

- `<header>`<br>
Digunakan untuk mengelompokkan elemen-elemen yang berada di atas halaman seperti judul, logo, `<h1>` atau link navigation.

- `<nav>`<br>
Digunakan sebagai pengelompokkan link navigasi seperti main menu.

- `<article>`<br>
Digunakan untuk konten seperti berita, posting blog, atau cerita.

- `<section>`<br>
Digunakan untuk mengelompokkan konten yang berkaitan seperti bagian dari sebuah artikel.

- `<footer>`<br>
Digunakan untuk mengelompokkan elemen-elemen yang biasa ditemukan pada bagian bawah halaman seperti informasi hak cipta, link ke media sosial.

### 3. Jelaskan perbedaan antara margin dan padding.
Margin merupakan batas terluar dari suatu elemen, margin mengatur jarak antara suatu elemen dengan elemen lainnya. Padding merupakan batas dari isi konten elemen dengan bordernya, berguna untuk mengatur ruang di dalam sekitar elemen.

### 4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
Tailwind lebih fokus pada pendekata utility-first, yaitu menggabungkan kelas-kelas utilitas untuk membuat sebuah tampilan seperti mengganti warna, font, size dll. Tailwind membuat proses desain lebih bebas karena kustomisasi yang didukung oleh utility class tersebut yang membuat desainnya menjadi fleksibel, ukuran tailwind juga cenderung kecil karena hanya menggunakan class yang digunakan dalam proyek.

Bootstrap menggunakan pendekatan komponen sehingga membuat tampilan website menggunakna komponen yang telah dibuat sebelumnya seperti navbar, card, form, dll. Bootstrap lebih mudah digunakan untuk pemula karena hanya perlu memahami penggunaan komponennya. Bootstrap memiliki size yang lebih besar karena mengandung banyak komponen dan style bawaan.

Kita dapat menggunakan bootstrap jika kita membutuhkan waktu proses pengembangan yang lebih cepat karena komponen yang sudah jadi tinggal dipakai dan dikustomisasi sesuai kebutuhan, Tailwind bisa digunakan jika desain sebuah website membutuhkan kustomisasi yang lebih tinggi karena tailwind memiliki kontrol yang lebih besar atas kustomisasinya.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama-tama saya memasang bootstrap pada head di `base.html` lalu saya menambahkan dulu fitur edit dan delete product pada inventory, setelah itu saya memasang komponen navbar yang disediakan oleh bootstrap dan mengubah navigasi linknya menjadi judul, nama, dan link untuk login atau logout tergantung dengan halamannya, lalu untuk inventory saya mengganti tampilan informasi table menjadi card untuk masing-masing item dan ditambahkan tombol edit dan delete di sampingnya, semua tampilan juga saya tengahkan menggunakan flexbox dari class bootstrap, lalu saya menambahkan sedikit warna pada button dengan menggunakan class bawaan dari bootstrap.

## Tugas 4

### 1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreationForm merupakan sebuah built-in form dari framework django yang digunakan untuk melakukan registrasi user. 
Kelebihan yang dimiliki ialah:
- Form ini berguna untuk menghemat waktu development karena sudah siap pakai tanpa perlu menulis form registrasi dari awal
- UserCreationForm sudah terintegrasi dengan autentikasi bawaan django sehingga mudah diintegrasikan dengan sistem login dan logout
- UserCreationForm menyediakan fitur validasi untuk melakukan validasi pada data user.
Kekurangan yang dimiliki:
- Keterbatasan pada kustomisasi form, apabila form yang kita perlukan memerlukan kompleksitas yang cukup rumit, maka kita harus membuat formnya dari awal
- Form tidak memiliki validasi bisnis khusus, sehingga diperlukan validasi bisnis tambahan
- Tidak memiliki fungsionalitas seperti konfirmasi email, penanganan avatar, profil pengguna, dll. Sehingga perlu ditambahkan sendiri
- Tampilan form hanya menyediakan tampilan berupa formulir, sehingga kita perlu mengatur tampilan interfacenya sendiri

### 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
`autentikasi` merupakan bentuk verifikasi identitas user, dengan adanya autentikasi aplikasi dapat mengetahui siapa yang sedang mengakses halaman web tersebut, hal ini dapat berguna seperti untuk melacak aktivitas user. `otorisasi` adalah sebuah proses dalam mengatur akses yang dimiliki oleh sebuah user, dengan adanya otorisasi, kita dapat memastikan apa saja permissions dan access yang user punya dalam sebuah aplikasi website. Autentikasi dan otorisasi penting untuk diterapkan sebagai keamanan aplikasi dengan mengatur siapa saja pengguna yang memiliki akses dengan memberi batasan sehingga data sensitif dapat terlindungi tanpa adanya pengguna asing yang mendapatkan akses informasi tersebut.

### 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies merupakan sebagian kecil informasi yang dikirim oleh server ke sisi client. Cookies biasa digunakan untuk menyimpan informasi seperti session user, preferensi user, identifikasi user, dll. Cookies dapat membuat HTTP menjadi stateful sehingga setiap request tidak perlu untuk meminta informasi lagi seperti meminta login untuk setiap pergantian halaman website. Pada saat melakukan autentikasi, Django akan mengirim cookies ke user berupa session yang menyimpan informasi user yang sedang mengakses website yang akan digunakan tiap melakukan http request sehingga tiap request dapat diketahui data user yang mengakses halaman website. Selama interaksi user dengan web, django dapat memperbarui atau menghapus data sesi pada cookies jika user melakukan logout.

### 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookies secara default belum tentu aman, masih ada risiko pihak ketiga untuk meretas informasi yang disimpan dalam cookies, maka dari itu, sebaiknya data yang disimpan dalam cookies bukan merupakan data yang sensitif seperti username dan password user, cukup id user saja yang disimpan. Cookies juga menjadi risiko dalam melacak aktivitas pengguna. Penggunaan cookies dianjurkan menggunakan atribut keamanan seperti mengirimkan cookies menggunakan koneksi HTTPS untuk meningkatkan keamanan pada cookies.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

#### Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
registrasi:<br>
melakukan import UserCreationForm dan messages dari django sebagai built-in registration form dan alert message. membuat fungsi register yang melakukan render `register.html` dengan isi template form dari UserCreationForm, apabila parameter request method berupa POST, maka akan dilakukan validasi pada form dan dilakukan save dan dikirim messages dan akan di redirect ke page login. lalu akan ditambahkan path login ke urls.py<br>

login:<br>
melakukan import authenticate dan login dari django.contrib.auth untuk diimplementasikan kedalam fungsi login_user pada views.py di main, dari POST request akan diterima username dan password di fungsi itu dan akan dilakukan autentikasi, apabila dikenal maka akan di redirect ke halaman main, apabila salah diberikan message username atau password incorrect. jika request bukan POST return halaman `login.html` untuk login ulang. login.html pada templates akan berisi form dengan input username dan password dengan method POST. Setelah itu tambahkan path login ke urls.py<br>

logout:<br>
melakukan import logout dari django.contrib.auth dan membuat fungsi logout pada views.py yang akan menjalakan fungsi logout dengan parameter request dan akan redirect ke login page. pada main.html ditambahkan hyperlink ke logout button yang akan menuju path logout.

#### Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
Dari implementasi fungsi yang telah dibuat. Server dinyalakan dan dimulai membuat dua akun dengan diisi masing-masing tiga dummy data yaitu menggunakan model Item.

#### Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
Sebelum menerapkan cookies, halaman main akan direstriksi menggunakan decorators login_required yang diimport dari django.contrib.auth.decorators decorators akan ditambahkan di atas kode fungsi show_main.

Pada penerapan cookies, akan diimport datetime untuk waktu, HttpResponseRedirect, dan reverse untuk redirect halaman. pada fungsi login_user sebelum di redirect ke main, akan diberikan cookies berupa last login dan pada fungsi show_main variabel context akan diberikan last_login dari request.cookies['last_login']. Lalu pada fungsi logout cookies akan di delete sebelum di redirect ke login page. Pada page main.html akan diberikan text untuk menampilkan last_login.

#### Menghubungkan model Item dengan User
Mengimport User dari django.contrib.auth.models lalu pada model Item akan dibuat variabel baru bernama user yang akan berisi models.ForeignKey(User, on_delete=models.CASCADE) yang akan menghubungkan user dengan model Item dan apabila user dihapus, maka item yang berkaitan juga akan ikut dihapus secara otomatis. lalu pada fungsi create_item akan diubah dengan form.save(commit=False) sehingga item yang dibuat bisa dikaitkan dengan usernya terlebih dahulu lalu disave ke dalam database. lalu pada context fungsi show_main name akan dirubah menjadi request.user.username sehingga name akan otomatis mengikuti nama user yang sedang login pada session tersebut.

Setelah itu akan dilakukan migrasi model dengan python manage.py makemigrations, jika muncul error berarti diberikan default value berupa 1 untuk field user pada semua row yang telah dibuat pada basis data. lalu ketik 1 lagi untuk menetapkan user dengan ID 1. Setelah itu akan dilakukan python manage.py migrate untuk mengaplikasikan migrasi ke database.

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
