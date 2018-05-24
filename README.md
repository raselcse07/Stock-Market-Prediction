# Stock-Market-Prediction

Stock market prediction is a prediction app that can predict Stock Closing Prices.It is built with Python,Django.For ML technique I have used Linear regression. For data set I have used Yahoo Finance.

# Dependencies

	Django==1.11
	django-crispy-forms==1.7.2
	numpy==1.14.3
	pandas==0.23.0
	python-dateutil==2.7.3
	pytz==2018.4
	scikit-learn==0.19.1
	scipy==1.1.0
	six==1.11.0

# How To Use

Before runnig the app make sure you have installed python3.6 and virtualenv.You can download Python from https://www.python.org/downloads/
and virtualenv from https://virtualenv.pypa.io/en/stable/

	1. Download/clone the folder.
	2. Create a new directory.Let us our directory name is PredictionApp.This commands will work in Linux/OSX.If you are Windows user the download the Poweshell from https://github.com/PowerShell/PowerShell and use it. 
	
	mkdir PredictionApp
	cd PredictionApp
	virtualenv . 
	source bin/activate
	
	3. Then copy the src and static_in_env folder and paste it to PredictionApp.
	4. Run the following command.
	
	cd src
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver
	
	5. Now open your favourite browser and go to the link http://127.0.0.1:8000
	
