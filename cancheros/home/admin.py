from django.contrib import admin
from .models import *

admin.site.register(Reserva)
admin.site.register(TipoDeporte)
admin.site.register(TipoDocumento)
admin.site.register(CanchaReserva)
admin.site.register(Usuario)