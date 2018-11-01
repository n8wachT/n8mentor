import sys
sys.path.insert(0, '/var/www/n8mentor')

from n8mentor-flask import n8mentor-flask as application

<VirtualHost *>
        ServerName n8wacht.com
        WSGIScriptAlias / /var/www/n8mentor/n8mentor-flask.wsgi
        <Directory /var/www/n8mentor>
                Order deny,allow
                Allow from all
        </Directory>
</VirtualHost>
