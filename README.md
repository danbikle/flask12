# README.md

How to deploy this repo to Ubuntu and Heroku.com?

I deployed this repo to my Ubuntu host with two shell commands:

```bash
cd ~
git clone https://github.com/danbikle/flask12 myflask12
```

This repo works well with Anaconda.

So I ran some shell commands to install Anaconda3-4.2.0:

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

To run this app on my laptop, I ran this shell command:

```bash
cd ~/myflask12
python flask12.py
```

Which allows me to see the app at the URL listed below:

http://0.0.0.0:5000

On my laptop, if I want to run a server which 'auto-reloads' after each file change, I should start the server with these shell commands:

```bash
cd ~/myflask12
export FLASK_DEBUG=1
export FLASK_APP=flask12.py
flask run
```
Also I can rely on the Gunicorn web server instead of plain Python by using this shell command:

```bash
cd ~/myflask12
gunicorn wsgi
```

Which allows me to see the app at the URL listed below:

http://0.0.0.0:8000

I created an account on the heroku.com website and memorized my password there.

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

I picked: myflask12

You should pick a different name.

```bash
cd ~
cd            myflask12
heroku create myflask12
git push heroku master
heroku ps:scale web=1
```

At that point a gunicorn webserver was running in my heroku deployment.

I saw evidence of this from the shell commands below:

```bash
curl https://myflask12.herokuapp.com
heroku logs
```


If you have questions, e-me: bikle101@gmail.com
