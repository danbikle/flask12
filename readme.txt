readme.txt

This repo is a very simple flask app.

I use it to show tasks listed below:
  - how to deploy flask to heroku
  - how to create a static website with flask

I followed these steps to deploy it:

cd ~
git clone https://github.com/danbikle/flask10 myflask10
heroku create myflask10
git push heroku master
heroku ps:scale web=1

At that point a gunicorn webserver should be running on heroku.

I should see evidence of this from the shell commands below:

curl https://myflask10.herokuapp.com/static/home.html
heroku logs

To run this app on my laptop, I run this shell command:

python flask10.py

Which allows me to see the app at the URL listed below:

http://0.0.0.0:5000/static/home.html

Also I can rely on the Gunicorn web server instead of plain Python using this shell command:

gunicorn wsgi

Which allows me to see the app at the URL listed below:

http://0.0.0.0:8000/static/home.html

If you have questions, e-me: bikle101@gmail.com

