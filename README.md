# DJANGO FACE DETECTION

## INSTRUKSI

### Linux

Step dibawah ini dicoba pada Ubuntu 18.04 LTS :

1. Aktifkan virtualenv, untuk tutorialnya ada di [Pyimagesearch](https://www.pyimagesearch.com/2018/05/28/ubuntu-18-04-how-to-install-opencv/), STEP 1 dan STEP 3
2. Install semua requirement dengan ```pip install -r requirements.txt```
3. Jika terdapat error pada mysqlclient, lakukan langkah berikut :
   * ```sudo apt-get update```
   * ```sudo apt-get upgrade```
   * ```sudo apt-get install python3.6-dev libmysqlclient-dev```
   * Lakukan ```pip install -r requirements.txt``` lagi, jika masih ada error ```sudo apt-get install dialog apt-utils build-essential checkinstall libreadline-gplv2-dev  libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev```
   * Lakukan ```pip install -r requirements.txt``` lagi