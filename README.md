## djangoblogproject

>https://github.com/zmrenwu/django-blog-tutorial


## requirements
#### Django==2.0.3
#### Markdown==2.6.11
#### Pygments==2.2.0
#### pytz==2018.3
#### django-haystack==2.8.1
#### jieba==0.39
#### Whoosh==2.7.4


   ```
   virtualenv blogproject_env

   # windows
   blogproject_env\Scripts\activate

   # linux
   source blogproject_env/bin/activate
   ```
   ```
   pip install -r requirements.txt
   ```
   
   ```
   python manage.py migrate
   python manage.py createsuperuser
   ```
##Nginx Config

```
python manage.py collectstatic
```
```
/etc/nginx/sites-available/demo.zmrenwu.com   ##replace domain

server {
    charset utf-8;
    listen 80;
    server_name demo.zmrenwu.com; ①

    location /static { ②
        alias /home/yangxg/sites/demo.zmrenwu.com/django-blog-tutorial/static;  ## replace too
    }

    location / { ③
        proxy_set_header Host $host;
        proxy_pass http://unix:/tmp/demo.zmrenwu.com.socket;   ##gunicorn server process
    }
}
```
```
gunicorn --bind unix:/tmp/demo.zmrenwu.com.socket blogproject.wsgi:application 
```
