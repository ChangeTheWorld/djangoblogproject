# djangoblogproject

>https://github.com/zmrenwu/django-blog-tutorial


# requirements
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
