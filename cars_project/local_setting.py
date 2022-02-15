# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qsv^yc*e=!5($2dlshadf@+5chq-ub6+5nddy$-)#modzr9_mz'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'root'
    }
}