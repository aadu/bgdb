#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bgdb.config.local")
    os.environ.setdefault("DJANGO_SECRET_KEY", "433ashd8a07$&SH$&*)@HF")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
