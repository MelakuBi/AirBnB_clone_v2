#!/usr/bin/env bash
# 0. Prepare your web servers
sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
echo "
<html>
  <head>
    <title>TEST Nginx</title>
  </head>
  <body>
    <p>
      Testing Nginx configuration
    </p>
  </body>
</html>
" | sudo tee -a /data/web_static/releases/test/index.html
sudo rm -rf /data/web_static/current/
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
upd="\\\t# Update the Nginx configuration\n\t# to serve the content of /data/web_static/current/ to hbnb_static\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n"
sudo sed -i "38i $upd" /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
