#!/bin/bash -e
DATABASE_URL="postgres://postgres:@localhost:5432/postgres" scrapy parse $1 --spider $2
