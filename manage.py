"""
Diango management script
"""

import os
import sys
from dotenv import load_dotenv
# import ptvsd


if __name__ == '__main__':
    # address = ('0.0.0.0', 3000)
    # ptvsd.enable_attach('', address)
    load_dotenv(verbose=True)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
