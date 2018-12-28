python -c "import os; import django; 
              os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ddp.settings'); 
              django.setup(); 
              from django.contrib.auth.management.commands.createsuperuser import get_user_model; 
              get_user_model()._default_manager.create_superuser( 
              username='tuandq', 
              email='tuan.dang@asiantech.vn', 
              password='@abcxyz$')