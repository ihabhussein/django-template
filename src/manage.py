#!/usr/bin/env python3

if __name__ == "__main__":
    import os
    import sys

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
