# README.md

How to deploy this site to Ubuntu and Heroku.com

I created an account on the heroku.com website and memorized my password there.

Then I ran some shell commands:

```bash
cd ~
rm -f Anaconda3-4.2.0-Linux-x86_64.sh
wget https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
bash Anaconda3-4.2.0-Linux-x86_64.sh
mv anaconda3/bin/curl anaconda3/bin/curl_ana
echo 'export PATH=${HOME}/anaconda3/bin:$PATH' >> ~/.bashrc
bash
conda install gunicorn
```

```bash
sudo apt-get install ruby ruby-dev gitk
cd ~
rm -rf heroku-client.tgz heroku-client
wget https://s3.amazonaws.com/assets.heroku.com/heroku-client/heroku-client.tgz
tar zxf heroku-client.tgz
echo 'export PATH=${HOME}/heroku-client/bin:${PATH}' >> ~/.bashrc
bash
heroku status
```

I thought of an ORIGINAL name from my new heroku app.

I picked: myflask11

You should pick a different name.

```bash
cd ~
git clone https://github.com/danbikle/flask11 myflask11
cd            myflask11
heroku create myflask11
git push heroku master
heroku ps:scale web=1
```

At that point a gunicorn webserver was running in my heroku deployment.

I saw evidence of this from the shell commands below:

```bash
curl https://myflask11.herokuapp.com
heroku logs
```

To run this app on my laptop, I ran this shell command:

```bash
python flask11.py
```

Which allows me to see the app at the URL listed below:

http://0.0.0.0:5000

Also I can rely on the Gunicorn web server instead of plain Python by using this shell command:

```bash
gunicorn wsgi
```

Which allows me to see the app at the URL listed below:

http://0.0.0.0:8000

# Enhancements

This repo offers enhancements over

https://github.com/danbikle/flask10

You should see the enhancements in this file:

https://github.com/danbikle/flask11/blob/master/flask11.py

First, I added a route for the path I call '/'.

This allows me to visit this URL:

https://flask11.herokuapp.com

The route will then serve this file:

https://github.com/danbikle/flask11/blob/master/static/home.html

Also I enhanced the site so it will serve a favicon.

I did this by placing a favicon.ico file in the static folder.

Next, I added a route so that if a browser asks for /favicon.ico, the server will find the the file in the static folder and then serve it.

If you have questions, e-me: bikle101@gmail.com
