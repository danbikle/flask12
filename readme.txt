readme.txt

This repo is a very simple flask app.

I use it to show tasks listed below:
  - how to deploy flask to heroku
  - how to create a static website with flask

I followed these steps to deploy it:

git add .
git commit -am hello
heroku create flask10
git push heroku master
curl https://flask10.herokuapp.com/

At that point a gunicorn webserver should be running on heroku.

I should see evidence of this from the shell command below:

heroku logs

To run this app on my laptop, I run this shell command:

python flask10.py

Which allows me to run this in another shell:

curl 0.0.0.0:5000/

Also I can rely on the Gunicorn web server instead of plain Python using this shell command:

gunicorn wsgi

Which allows me to run this in another shell:

curl 0.0.0.0:8000/


If you have questions, e-me: bikle101@gmail.com

