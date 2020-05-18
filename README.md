Web-Scrapping menggunakan Beautifulsoup

Proyek web-scarapping ini dibuat untuk memenuhi syarat penyelesaian pelatihan Data Analytics menggunakan Phython dari Algoritma Academy. Dimana contoh website yang akan digali informasinya lebih lanjut adalah http://monexnews.com/kurs-valuta-asing.htm?kurs=JPY .

Data yang akan diekstraksi dari website tersebut adalah data history harga jual dan beli mata uang Japan Yen (JPY) atau konversinya terdahap rupiah selama tahun 2019.

Dependencies(Ketergantungan)
Sebelum anda melakukan clone source code ini, pastikan anda sudah menginstall jupyter notebook dan seluruh package pada file Requirement.txt di computer anda . Versi Phyton yang saya gunakan adalah : Python 3.7.6.

Daftar package yang wajib tersedia adalah sebagai berikut :
•	beautifulSoup4 : digunakan untuk mongolah data dalam bentuk HTML atau XML
•	pandas :  digunakan untuk mengolah dan menganalisa data dari berbagai sumber
•	flask : web application framework di Phyton yang akan digunakan sebagai tools untuk  melakukan publish website hasil pengolahan data.
•	matplotlib : library yang komprehensif untuk membuat visualisasi statis, dan animasi


Daftar File
•	README.md : file yang berisi penjelasan singkat terkait proyek
•	requirements.txt  : daftar package/library yang tersedia pada environtment yang saya gunakan 
•	app.py  : file yang berisi syntax atau script data analytic yang ditulis dengan menggunakan phyton.
•	ScrapMonexBaru.ipynb  : berisi syntax data analytic sebelum di publish menjadi index.html
•	Templates : folder berisi index.html yang berisi hasil data analytics terhadap data kurs di website 
