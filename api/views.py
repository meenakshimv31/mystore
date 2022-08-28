from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class MyView(APIView):
    def get(self,request,*args,**kwargs):
         return Response({"msg":"Hello World"})

class GoodMorningView(APIView):
    def get(self, request, *args, **kwargs):
          return Response({"msg":"Good Morning"})

class AddView(APIView):
    def post(self,request,*args,**kwags):
        num1 = int(request.data.get('num1'))
        num2 = int(request.data.get('num2'))
        res=num1+num2
        return Response({"Addition":res})

class SubView(APIView):
    def post(self,request,*args,**kwags):
        num1=int(request.data.get("num1"))
        num2=int(request.data.get("num2"))
        res=num1-num2
        return Response({"Substraction":res})

class MulView(APIView):
    def post(self,request,*args,**kwags):
        num1=int(request.data.get("num1"))
        num2=int(request.data.get("num2"))
        res=num1*num2
        return Response({"Multiplication":res})

class CubeView(APIView):
    def post(self,request,*args,**kwags):
        num1=int(request.data.get("num1"))
        res=num1*num1*num1
        return Response({"Cube":res})

class FactView(APIView):
    def post(self,request,*args,**kwags):
        num=int(request.data.get("num1"))
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        return Response({"Factorial":fact})

class PrimeView(APIView):
    def post(self,request,*args,**kwargs):
        num=int(request.data.get("num1"))
        for i in range(2, num):
            if (num % i == 0):
                return Response({"Not Prime"})
                break
        else:
                return Response({"Prime"})

