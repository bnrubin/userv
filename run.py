#!/usr/bin/env python3
from userv import app

context = ('/etc/ssl/ubottu.com.crt', 'ubottu.com.key') 
app.run(host='0.0.0.0', port=8000, debug=True, ssl_context=context)
