#Requirements
* **Docker**
* **docker-compose** >= 3.9
* (environment tool of your choice)

#Setup
1. Clone this repository and change directory to the repository root
```
git clone git@github.com:kucerp21/pdfprocessor.git
cd pdfprocessor
```
2. Create an environment for this project (e.g. using pyenv and virtualenv)
```
pyenv global 3.9.2 
pyenv virtualenv pdfprocessor
pyenv activate pdfprocessor
```
3. Build Docker images
```
sudo docker-compose build
```
4. Run the app, migrate database, create super user
```
sudo docker-compose up (-d)
sudo docker-compose run api python manage.py migrate
sudo docker-compose run api python manage.py createsuperuser
```
5. You can now develop and test the application. To stop the application, run:
```
sudo docker-compose down
```

Tasks can be monitored locally in Flower:
[http://localhost:5555](http://localhost:5555)

Available endpoints can be viewed with command:
```
sudo docker-compose run api python manage.py show_urls
```

#Testing
For testing you have to have the application running locally using steps specified above.
To test the project run: 
```
sudo docker-compose run api python manage.py test
```

It is good to note here, that for testing purposes there is simulated 10 second delay on each task while using `development` settings
set by:
```
# simulate normalizing delay
    if settings.DEBUG:
        time.sleep(10)
```