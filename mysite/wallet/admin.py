from django.contrib import admin
from .models import Wallet, Operation


from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html


#class WalletAdmin(admin.ModelAdmin):
    #list_display = ('balance.RUB', 'balance_USD')

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'balance_RUB', 'balance_USD', 'id_person', 'kard', 'view_wallets_link')
    def kard(self, obj):
        idd = str(obj.id)
        return format_html('<a href="/wallets/?id={}">Карточка</a>', idd)
        #return format_html('<a href="/">Карточка</a>')
    def view_wallets_link(self, obj):
        count = len(Operation.objects.filter(id_wallet_1=obj.id))+len(Operation.objects.filter(id_wallet_2=obj.id))
        #count = obj.wallet_set.count()
        url = (
            reverse("admin:wallet_operation_changelist")
            + "?"
            + urlencode({"id_wallet_1": f"3"})+"&"+ urlencode({"id_wallet_2": f"4"}))

            # + urlencode({"id_wallet_1": f"{obj.id}"})+"|"+ urlencode({"id_wallet_2": f"{obj.id}"}))


        return format_html('<a href="{}">{} Operations</a>', url, count)
    view_wallets_link.short_description = "Operations"

#admin.site.register(Wallet)
@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ('id', 'money', 'unit', 'type', 'id_wallet_1', 'id_wallet_2')
    list_filter = ("id_wallet_1", "id_wallet_2",)

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.unregister(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff', 'kard', 'view_users_link')
    def kard(self, obj):
        idd = str(obj.id)
        return format_html('<a href="/users/?id={}">Карточка</a>', idd)
        #return format_html('<a href="/">Карточка</a>')
    def view_users_link(self, obj):
        count = len(Wallet.objects.filter(id_person=obj.id))
        #count = obj.wallet_set.count()
        url = (
            reverse("admin:wallet_wallet_changelist")
            + "?"
            + urlencode({"id_person": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Wallets</a>', url, count)
    view_users_link.short_description = "Wallets"

admin.site.register(User, UserAdmin)


# Register your models here.
