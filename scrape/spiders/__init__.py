# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bgdb.config.local")

django.setup()