import datetime
from django.shortcuts import render
from .models import Company
from .forms import PredictForm
from .predictor import predict_price,get_data,dates_final,prices




def Home(request):

    predicted = 0
    errors=""
    ticker = ""

    qs=Company.objects.all()
    form = PredictForm(request.POST or None)

    if form.is_valid():

        compnay_name = form.cleaned_data['name_of_company']

        if compnay_name.upper() == "AAPL":
            ticker = "Apple Inc."
        if compnay_name.upper() == "GOOG":
            ticker = "Alphabet Inc."


        find_data_set= compnay_name.upper()+".csv"
        
        try:
            data_set = "Data-Set/"+find_data_set
            tday= datetime.datetime.now().day
            get_data(data_set)
            predicted_price, coefficient, constant = predict_price(dates_final,prices,tday)
            predicted ="%.2f" % (predicted_price)
        except:
            errors = "Company Not Found !!!"


    template_name="Prediction/home.html"
    context={
                "qs":qs,
                "form":form,
                "predicted":predicted,
                "errors":errors,
                "ticker":ticker
            }

    return render(request,template_name,context)
