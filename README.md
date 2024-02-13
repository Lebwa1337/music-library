## music-library
My portfolio project
# Project description
This project was made to create and keep information for any music genre,album,track and music author what you think off.
It provide information for various music artist and their albums, tracks and also genres. It servers as a platform, for people who seek for new music 
# Technological stack
For this project i used:
- python 3.12
- django 5.0.1
- crispy-bootstrap 2023.1
- django-crispy-forms 2.1

As my html template i used free html template "Django Material Kit2"

# Installation instructions 
For beginning you have to install Python3+
In terminal write down following command:
```shell
git clone https://github.com/Lebwa1337/music-library.git
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python manage.py collectstatic
python manage.py runserver
```
Also for testing you can load already prepared data:
```shell
python manage.py loaddata music_library_db_data.json
```
# DB structure
![DB structure.jpeg](DB%20structure.jpg)
# Interface example
Bellow is example for index, list, detail pages
![img.png](demo_files/img.png)
![img_1.png](demo_files/img_1.png)
![img_2.png](demo_files/img_2.png)
![img_3.png](demo_files/img_3.png)
![img_4.png](demo_files/img_4.png)
