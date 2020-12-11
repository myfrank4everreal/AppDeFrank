from collections import defaultdict
from django.shortcuts import redirect, render
import math 

def Calculate(request):
    return render(request, 'calculatorapp/calhome.html')


def mortgageCalc(request): 

    result = 0
    pay_off_year = 0
    pay_off_month = 0
    Loan_amount = 0
    interest = 0
    total_interest = 0
    total_mortgage_with_interest  = 0
    years = 0
    down_payment = 0

    err_msg = ''
    message = ''
    message_class = ''


    try:  
        if request.method =='POST':
            Loan_amount = float((request.POST.get('loan', False)))
                            
            interest = float((request.POST.get('interest', False)))/100
            years = int((request.POST.get('years', False)))
            down_payment = float((request.POST.get("downpayment", False )))
            

            month = request.POST.get('month')
            print(month)
            year = int((request.POST.get('year', False)))

            L = Loan_amount - down_payment
            c = interest/12
            n = years*12   #n is number of months

        
            monthlypayment = L*(c*(1 + c)**n)/((1 + c)** n - 1)
            result = round(monthlypayment, 3)

            

            # total mortgage amount paid will be 
            totalmortgage  = monthlypayment*n 
            total_mortgage_with_interest = (round(totalmortgage, 2))


            #  total interest paid 
            y = totalmortgage - L
            total_interest = (round(y, 2)) 

            
            
            
            # pay off date 
            pay_off_year = years + year
            pay_off_month = str(month)

    except ZeroDivisionError as zero_err :
        zero_err = 'not is not divisible by 0'
    except ValueError as err_msg:
        err_msg = "Invalid entry, please check your figures"
        
        message = err_msg
    message_class = "is_danger"
    
    context =  {
        'Loan_amount':Loan_amount,
        'message':message,
        "message_class":message_class,
        'result':result,
        'total_interest':total_interest,
        'pay_off_year':pay_off_year,
        # 'pay_off_month':pay_off_month,
        "total_mortgage_with_interest":total_mortgage_with_interest ,
    }
    return render(request, 'calculatorapp/mortgagecalc.html', context)



# ******************************BMI CALCULATOR***************************************
def Bmi(request):
    height = 0
    body_weight = 0 
    result = 0
    message = 0
    select_weight = 0
    user_message = 0
    convert_weight = 0
    kg = 0
    ibs = 0

    try:

        if request.method == "POST":
            body_weight = float(request.POST.get('bodyweight'))  
            input_height_cm = float(request.POST.get('height'))
            select_weight = (request.POST.get('weightselector'))

            # convert to meter
            height_meter = input_height_cm/100
            height = round(height_meter**2, 3)

            
            if select_weight == 'kg':
                result = round(body_weight/height, 2)
            else:
                if select_weight == 'Ibs':
                    convert_weight = round(body_weight/2.20462262185, 2)
                    result = round(convert_weight/height, 2)

            if result < 25 or result >= 18.5:
                user_message = "  weight is considered normal"
            if result > 24.9:
                user_message = "you are over weight"
            if result < 18.5 :
                user_message = " you are under weight"

    except ValueError as err_msg :
        err_msg = "Invalid entry, please check your figures"
        message = err_msg

    # select weight  
    
    context = {
        'select_weight':select_weight,
        'convert_weight': convert_weight,
        'height':height,
        'body_weight':body_weight,
        'result':result,
        'message':message,
        'user_message':user_message,
    }
    return render(request, 'calculatorapp/bmi.html', context)


def scientificHome(request):


    return render(request, 'calculatorapp/scientifichome.html')