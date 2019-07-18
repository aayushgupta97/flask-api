#Flask-API
This is a basic API that can be used to test your server. Here, this is used to distinguish the performance between the default python server and gunicorn server.

###Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

####Prerequisites

1) Installing nginx 
   ```
   sudo apt udpate 
   sudo apt install nginx 
   ```

    >To check the status of your server:-

    ````
    sudo systemctl status nginx
    sudo systemctl stop nginx.service
    sudo systemctl start nginx.service
    sudo systemctl restart nginx.service
    ````
    
    Setting Up Server Blocks
    open the default config file for nginx and add a location block at the bottom of the first server block.
    ````
    sudo nano /etc/nginx/sites-available/default
    
    location / {
         include proxy_params;
         proxy_pass http://localhost:8000;
        }
    ````
    
    Next, test to make sure that there are no syntax errors in any of your Nginx files:
    
    ````
    sudo nginx -t
    ````  
2) Create a python Virtual environment
    ````
    virtualenv venv -p python3.6
    source venv/bin/activate
    pip install gunicorn flask
    ```` 

3) Configuring gunicorn and running the app with gunicorn 

    ````
    gunicorn wsgi:app
    
    sudo systemctl start nginx.service
    gunicorn -w 8 wsgi:app 
    ````
