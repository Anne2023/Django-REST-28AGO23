from django.views import View
from django.http.response import HttpResponse, HttpResponseBadRequest
from rest_framework.exceptions import MethodNotAllowed

#class Based View - CBV  um aponta pra classe e outro aponta função
class CategoryView(View):


  def get(sef, request,*args,**kwargs):
    return HttpResponse("ok") #passagem de parametro
  
  def post(self, request,*arg, **kwargs):
    data_body = request.body.decode('utf-8')
    
    #deserialização
    print(data_body)
    return HttpResponseBadRequest("Dados invalidos")

  def put(self,request,*arg,**kwargs):
    raise MethodNotAllowed()