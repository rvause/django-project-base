#!/usr/bin/env python
import os, sys
from django.core.servers.fastcgi import runfastcgi
 
# Figure out where we are
current_path = os.path.dirname(__file__) 
sys.path.extend([os.path.join(current_path, '../'), os.path.join(current_path, '../app/')])
 
# Set our settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
  
# Run FastCGI handler
runfastcgi()
