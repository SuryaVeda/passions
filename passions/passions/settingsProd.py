from passions.settings import * 
DEBUG = True
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
ALLOWED_HOSTS = ['ec2-3-16-187-92.us-east-2.compute.amazonaws.com', 'localhost']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
FILE_UPLOAD_PERMISSIONS=0o640
DATABASE_URL='postgres://kati:sur21997@localhost:5432/passions'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'passions',
        'USER': 'kati',
        'PASSWORD': 'sur21997',
        'HOST': 'localhost',
        'PORT': '5432',
    }        
}

