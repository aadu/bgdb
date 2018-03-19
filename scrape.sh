#!/bin/bash -e
DATABASE_URL="postgres://postgres:@localhost:5432/postgres" scrapy crawl $1 $2
