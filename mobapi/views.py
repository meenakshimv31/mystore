from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from mobapi.serializers import MobileModelSerializer
from mobapi.models import Mobiles

class MobileView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()

        if "band" in request.query_params:
            qs=Mobiles.objects.filter(band=request.query_params.get("band"))

        if "name" in request.query_params:
            qs=Mobiles.objects.filter(name__contains=request.query_params.get("name"))

        serializer=MobileSerializer(qs,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=MobileSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            Mobiles.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class MobileDetailView(APIView) :

    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Mobiles.objects.get(id=id)
        serializer = MobileSerializer(qs)
        return Response(data=serializer.data)


    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs = Mobiles.objects.get(id=id)
        qs.delete()
        return Response({"msg":"Deleted"})

    def put(self,request,*args,**kwargs):
        id = kwargs.get("id")
        qs = Mobiles.objects.filter(id=id)
        serializer = MobileSerializer(instance=qs,data=request.data)
        if serializer.is_valid():
            qs.update(**serializer.validated_data)

            return Response({"msg":"updated"})
        else:
            return Response(data=serializer.errors)


class MobileModelView (APIView) :
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()
        serializer=MobileModelSerializer(qs,many=True)
        return Response(data=serializer.data)


    def post(self,request,*args,**kwargs):
        serializer=MobileModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class MobileModelDetailView(APIView) :

    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Mobiles.objects.get(id=id)
        serializer = MobileModelSerializer(qs)
        return Response(data=serializer.data)

    def put(self, request, *args, **kwargs):
        id = kwargs.get("id")
        qs = Mobiles.objects.get(id=id)
        serializer = MobileModelSerializer(instance=qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)



