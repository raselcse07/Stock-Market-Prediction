# Stock-Market-Prediction

The submitted web application has numerous company listed in it, which(companies) have their ledger on stock market.People can observe the current price of certain company stock on the stock market but they don't know the closing price of that stock. 

Closing price of any stock indicates the last price of that stock at the end of the day. If the pridiction is close to the real one, then it would bring significant business profit to the people or to any organization or bank. So,the more accurate the closing stock, the more chance to make a maximum profit out of it, no matter what the current value is. And this is the goal of our stock market prediction application. The user may search or select any listed company that opens their share to the market in this app and they see what may be the possible AI driven closing price for that stock at the end of that day for that market.

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

Before runnig the app make sure you have installed python3.6,pip and virtualenv.You can download Python from https://www.python.org/downloads/ and virtualenv from https://virtualenv.pypa.io/en/stable/ . While installing 
python in windows, choose the advance option.So that pip will automatically install which is very important.For 
Linux/OSX you don't need to install python and pip.Newer version of Linux and OSX has pre-installed Python3 and Pip. 
You can check the Python and Pip using following command.
	
	# Check Python Version

	open the terminal
	python3
	
	If works,then python3 and pip is insalled.If not works then you need to update python version.
	
	# Download and run the project
	
	1. Download/clone the folder.
	2. Open the terminal(Linux/OSX).For windows you can use Poweshell.You can download Poweshell from 
	https://github.com/PowerShell/PowerShell 
	
	Now we need to create a new directory.Let us our directory name is PredictionApp.
	
	mkdir PredictionApp
	cd PredictionApp
	virtualenv . 
	source bin/activate
	
	3. Then copy the src and static_in_env folder and paste it to PredictionApp.
	4. Run the following command.
	
	cd src
	pip install -r requirements.txt
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver
	
	5. Now open your favourite browser and go to the link http://127.0.0.1:8000
	
