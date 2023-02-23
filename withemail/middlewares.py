from django.shortcuts import render
class UnderConstructionMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response


    def __call__(self,request):
        print('middleware is called ')
        response = render(request,'underconstruction.html')
        return response