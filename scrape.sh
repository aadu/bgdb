#!/bin/bash -e
DATABASE_URL="postgres://postgres:@localhost:5432/postgres" scrapy runspider scrape/spiders/$1.py $2
