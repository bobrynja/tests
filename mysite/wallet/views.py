from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template.response import TemplateResponse
from .models import Wallet, Operation
from django.contrib.auth.models import User
from django.db.models import Q
from .serializers import WalletSerializer, OperationSerializer, UserSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict



def index(request):
    return render(request, "wallet/home.html")


def create(request):
    if request.method == "POST":
        pass
    return HttpResponseRedirect("/")

def login(request):
        return render(request, "registration/login.html")

def profile(request):
        return render(request, "wallet/profile.html")

def add(request):   #функция добавление кошелька
    wallets = Wallet.objects.all()
    return render(request, "wallet/add.html", {"wallets":wallets})

def create_w(request):   #функция добавление кошелька
    if request.method == "POST":
        wal = Wallet()
        wal.balance_RUB = request.POST.get("balance_RUB")
        wal.balance_RUB = request.POST.get("balance_RUB")
        #wal.id_person = request.POST.get("id_person")
        wal.id_person = request.user.id
        wal.save()
    return HttpResponseRedirect("/accounts/profile/add/")


def transfer(request):
    wallets = Wallet.objects.all()
    if request.method == "POST":
        id = int(request.POST.get("wallet_1"))
        transfer1 = wallets.get(id=id)
        if transfer1.id_person == request.user.id:
            transfer2 = wallets.get(id=request.POST.get("wallet_2"))
            if request.POST.get("unit") == 'RUB':
                if transfer1.balance_RUB > float(request.POST.get("money")):
                    transfer1.balance_RUB = transfer1.balance_RUB - float(request.POST.get("money"))

                    transfer2.balance_RUB = transfer2.balance_RUB + float(request.POST.get("money"))
            elif request.POST.get("unit") == 'USD':
                if transfer1.balance_USD > float(request.POST.get("money")):
                    transfer1.balance_USD = transfer1.balance_USD - float(request.POST.get("money"))
                    transfer2.balance_USD = transfer2.balance_USD + float(request.POST.get("money"))
            transfer2.save()
            transfer1.save()
            operate = Operation()
            operate.type = request.POST.get("type")
            operate.money = request.POST.get("money")
            operate.unit = request.POST.get("unit")
            operate.id_wallet_1 = request.POST.get("wallet_1")
            operate.id_wallet_2 = request.POST.get("wallet_2")
            operate.save()
        else:
            return HttpResponseRedirect("/")
    return render(request, "wallet/transfer.html", {"wallets":wallets})

def user(request):
    #id = request.GET.get("id")
    id =  request.GET.get("id", 1)
    #users = User.objects.all()
    #use = users.get(id=id)
    #people = User.objects.all()

    #use = people.get(id=id)
    #use = User.objects.get(id=ide)
    u = User.objects.get(id=id)
    wallets = Wallet.objects.filter(id_person=u.id)
    return render(request, "wallet/user.html", {"use":u, "wallets":wallets})

def wallet(request):
    id =  request.GET.get("id", 1)
    w = Wallet.objects.get(id=id)
    operations = Operation.objects.filter(Q(id_wallet_1=w.id) | Q(id_wallet_2=w.id))
    return render(request, "wallet/wallet.html", {"wal":w, "operations":operations})

    #_________________________API_________________________________
class WalletList(APIView):
    def get(self, request):
        w = Wallet.objects.filter(id_person=request.user.id)
        return (Response({"wallets":WalletSerializer(w, many=True).data}))
    
    def post(self, request):
        serializer = WalletSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return (Response({"wallets":serializer.data}))
    



 
class WalletDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class OperationList(generics.ListCreateAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    def post(self, request):
        wallets = Wallet.objects.all()
        transfer1 = wallets.get(id=request.data["id_wallet_1"])
        transfer2 = wallets.get(id=request.data["id_wallet_2"])
        if request.data["unit"] == 'RUB':
            if transfer1.balance_RUB >= float(request.data["money"]):
                transfer1.balance_RUB = transfer1.balance_RUB - float(request.data["money"])
                transfer2.balance_RUB = transfer2.balance_RUB + float(request.data["money"])
        elif request.data["unit"] == 'USD':
            if transfer1.balance_USD >= float(request.data["money"]):
                transfer1.balance_USD = transfer1.balance_USD - float(request.data["money"])
                transfer2.balance_USD = transfer2.balance_USD + float(request.data["money"])
        transfer2.save()
        transfer1.save()
        operate = Operation()
        operate.type = request.data["type"]
        operate.money = request.data["money"]
        operate.unit = request.data["unit"]
        operate.id_wallet_1 = request.data["id_wallet_1"]
        operate.id_wallet_2 = request.data["id_wallet_2"]
        operate.save()
        return Response({"operation":operate.unit})
        
        

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names=['get']













# Create your views here.
