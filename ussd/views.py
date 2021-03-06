from django.shortcuts import render
from .models import userModel
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
@require_POST
def dataget(request):
    if request.method=='POST':
        text=request.POST.get('text')
        userInput = text.split('*')
        step = len(userInput)
        if (text.endswith('#')==True):
            response="Request Hasn't been made successfully...Please try again END"
            return 0;
        else:
            response = ""
            print('Currently at step: ',step)

            if step == 1:
                response = "CON Enter District Number(1 for Thiruvanathapuram and 14 for Kasargod): \n"
            elif step== 2:
                response="CON Enter your Name: \n"
            elif step==3:
                response="CON Enter your Mobile Number: \n"
            elif step ==4 :
                response = "CON Enter your report message: \n"

            elif step == 5:
                userModel.object.create(
                    dist=userInput[-4],
                    Name=userInput[-3],
                    mob=userInput[-2],
                    message=userInput[-1]
                )
                response = "Help Request successfully Made!... A Volunteer will call you for validating and Confirming"
            
    return HttpResponse(response)