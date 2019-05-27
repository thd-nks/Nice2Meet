import os


# защита веб-форм от противной атаки под названием Cross-Site Request Forgery или CSRF
SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'