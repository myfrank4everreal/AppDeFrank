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


def get_result(request):   
    return redirect("mortgage")


def scientificHome(request):


    return render(request, 'calculatorapp/scientifichome.html')