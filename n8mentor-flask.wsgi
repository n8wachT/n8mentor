import sys
sys.path.insert(0, '/var/www/n8mentor')

from n8mentor import n8mentor-flask as application

<VirtualHost *>
        ServerName n8wacht.com
        WSGIScriptAlias / C:\Users\n9ghtLY\Projects\mentor\n8mentor-flask.wsgi
        <Directory C:\Users\n9ghtLY\Projects\mentor\>
                Order deny,allow
                Allow from all
        </Directory>
</VirtualHost>
