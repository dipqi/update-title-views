# update-title-views
Based on unique title like Tom Scott &amp; Agung Hapsah's videos.

### Cara Pertama 
Setup YouTube API, bisa dibuka link tersebut: https://developers.google.com/youtube/v3/quickstart/python

### Cara Kedua
Download & Simpan file "secret-blablabla-googleauthapalahgitu.json" ditempat yang bersamaan dengan file .py yang udah aku siapkan

### Cara Ketiga
Buka file update-judul-views.py (kalo blm download, didownload dulu)
* ganti client_secrets_file menjadi  "secret-blablabla-googleauthapalahgitu.json" (file oauth yang td kamu download n setup)
* ganti "id" menjadi URL video kamu yang bakal jadi target ganti views. 

### Cara Ke-Empat
Install "pip" & "python 3", caranya cari ae di google. gw lagi di hp bg, mager.
run command ini kalo udah install pip & python 3

> pip install google-auth-oauthlib
> pip install google-api-python-client

### Cara ke-Lima
di command prompt / terminal kamu, jalankan
> python3 update-judul-views.py

### Cara ke-Enam: 
Autentikasi, copy link yang dikasih di cmd/terminal pas run codenya, dan paste token yang diberi pas udah authenticate di cmd/terminal kamu.

** dah gitu aje, kalo ga ada error berarti udah work. **
** oiya, kalo biar terus keupdate, gw saranin pake crontab. **
