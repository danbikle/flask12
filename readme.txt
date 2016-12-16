readme.txt

This repo is a very simple Flask app.

I use it to show tasks listed below:
  - how to deploy flask to heroku
  - how to create a static website with Flask

I followed these steps to deploy it on Ubuntu 16:

I created an account on the heroku.com website and memorized my password there.

cd ~
rm -f Anaconda3-4.2.0-Linux-x86_64.sh
wget https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
bash Anaconda3-4.2.0-Linux-x86_64.sh
mv anaconda3/bin/curl anaconda3/bin/curl_ana
echo 'export PATH=${HOME}/anaconda3/bin:$PATH' >> ~/.bashrc
bash
conda install gunicorn

sudo apt-get install ruby ruby-dev gitk
cd ~
rm -rf heroku-client.tgz heroku-client
wget https://s3.amazonaws.com/assets.heroku.com/heroku-client/heroku-client.tgz
tar zxf heroku-client.tgz
echo 'export PATH=${HOME}/heroku-client/bin:${PATH}' >> ~/.bashrc
bash
heroku status

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

Also I can rely on the Gunicorn web server instead of plain Python by using this shell command:

gunicorn wsgi

Which allows me to see the app at the URL listed below:

http://0.0.0.0:8000/static/home.html

If you have questions, e-me: bikle101@gmail.com

