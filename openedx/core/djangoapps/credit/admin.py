"""
Django admin page for credit eligibility
"""
from ratelimitbackend import admin
from .models import CreditCourse, CreditProvider


class CreditProviderModelAdmin(admin.ModelAdmin):
    """
    Admin for `CreditProvider` model
    """
    pass

admin.site.register(CreditCourse)
admin.site.register(CreditProvider, CreditProviderModelAdmin)
