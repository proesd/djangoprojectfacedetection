# DJANGO FACE DETECTION

## INSTRUKSI

### Linux

Step dibawah ini dicoba pada Ubuntu 18.04 LTS, python 3.6, database mysql:

#### Instalasi

1. Aktifkan virtualenv, untuk tutorialnya ada di [Pyimagesearch](https://www.pyimagesearch.com/2018/05/28/ubuntu-18-04-how-to-install-opencv/), STEP 1 dan STEP 3
2. Install semua requirement dengan ```pip install -r requirements.txt```
3. Jika terdapat error pada mysqlclient, lakukan langkah berikut :
   * ```sudo apt-get update```
   * ```sudo apt-get upgrade```
   * ```sudo apt-get install python3.6-dev libmysqlclient-dev```
   * Lakukan ```pip install -r requirements.txt``` lagi, jika masih ada error ```sudo apt-get install dialog apt-utils build-essential checkinstall libreadline-gplv2-dev  libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev```
   * Lakukan ```pip install -r requirements.txt``` lagi

#### Deployment

1. Copy ```.env.example``` menjadi ```.env```
2. Isikan sesuai dengan konfigurasi database kalian
3. Lakukan ```python3 manage.py migrate```
4. Jika ada error ```no module tkinter```, lakukan install tkinter ```sudo apt-get install python3-tk```
5. Lakukan command berikut
   * ```sudo chmod 755 install.sh```
   * ```./install.sh```
6. Pindah ke folder static, lakukan ```bower install```, jika belum punya bower silakan install ```npm install -g bower```, jika belum punya npm silakan install nodejs
7. Jika diatas sukses dilakukan lakukan ```python3 manage.py runserver```, cek dimana listen port yang dipakai, buka pada browser kalian

### Windows

Windows Here