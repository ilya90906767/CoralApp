from web import create_app
# -*- coding: utf-8 -*-
import os,sys
#from celery import Celery

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
