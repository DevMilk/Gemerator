from django.shortcuts import render
import os
from django.views.generic import   View
import requests
import eventlet


#192.168.1.38
#78.163.49.245
KERAS_REST_API_URL = "https://gemerrator.ey.r.appspot.com/generate"
KERAS_REST_API_URL_GAN = "https://gemerrator.ey.r.appspot.com/GANgenerate"
class requestAPI:
    def __init__(self,url):
        self.a=0
        self.url = url
    def getImages(self):
        with eventlet.Timeout(400):
            r = requests.request("GET",self.url )
        try:
            r = r.json()
        except:
            print("API'YE ULASILMADI")
            return None
        if(r["success"]):
            return r["Images"]
        else:
            return None
context = {"API": None,"API2":None}
class Page(View):
    """gecikme sıkıntııs: request ve response kısa sürüyor, uzun süren kısmı renderlnması-resmin templateye konması"""
    def get(self,*args,**kwargs):
        global context
        try:
            context["API"] =  requestAPI(KERAS_REST_API_URL)
            context["API2"] = requestAPI(KERAS_REST_API_URL_GAN)
        except:
            print("hoayda")


        return render(self.request,"Template.html"  ,context)

