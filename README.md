this project has been deployed: &nbsp; &nbsp; https://music-sand-xi.vercel.app/ \
\
\
1- clone the project with this command: \
&nbsp; &nbsp; &nbsp; git clone https://github.com/javad-najjari/music \
2- create a virtualenv with this command: \
&nbsp; &nbsp; &nbsp; virtualenv env \
3- activate it \
&nbsp; &nbsp; &nbsp; Linux: source env/bin/activate \
&nbsp; &nbsp; &nbsp; Windows: cd &nbsp;env\Scripts\activate <br>
4- install the requirements with this command: \
&nbsp; &nbsp; &nbsp; pip install -r requirements.txt \
5- run these commands: \
&nbsp; &nbsp; &nbsp; python3 manage.py makemigrations \
&nbsp; &nbsp; &nbsp; python manage.py migrate \
6- create your own user with this command: \
&nbsp; &nbsp; &nbsp; python manage.py createsuperuser \
7- finally, this command: \
&nbsp; &nbsp; &nbsp; python manage.py runserver 8000 \
\
you can see the project from the following address: \
&nbsp; &nbsp; &nbsp; http://localhost:8000/ \
you can go to the admin panel and create your objects: \
&nbsp; &nbsp; &nbsp; http://localhost:8000/admin/
