import email
from functools import partial
from django.shortcuts import render
import io

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .entity_extractor import extract_email_addresses,extract_phone_numbers
from .predict_model import predict

@method_decorator(csrf_exempt, name='dispatch')
class ResumeAPI(View):

    #insert data
    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)

        #define if nothing can be fetched
        res = {'Email': None,
                'Mobile': None }

        email=extract_email_addresses(pythondata.get('text'))
        mobile=extract_phone_numbers(pythondata.get('text'))
        
      
        # print(prediction.keys())
        try:
            prediction = predict(pythondata.get('text'))
            final_output = {'Email': email[0],
                            'Mobile': mobile[0] }
        except:
            pass

        final_output= dict(prediction)
        final_output.update(res)
        json_data = JSONRenderer().render(final_output)
        print(json_data)
        return HttpResponse(json_data, content_type= 'application/json')
        

'''
"Address",
"Can Relocate to",
"Certifications",
"College",
"College Name",
"Companies worked at",
"Degree",
"Designation",
"Email Address",
"Graduation Year",
"Links",
"Location",
"Name",
"Relocate to",
"Rewards and Achievements",
"Skills",
"UNKNOWN",
"University",
"Years of Experience",
"abc",
"des",
"links",
"projects",
"state",
"training"
'''
