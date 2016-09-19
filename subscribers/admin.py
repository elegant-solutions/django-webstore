from django.contrib import admin

from .forms import SignUpForm
from .models import SignUp


# =========================================================================
# ----- Custom Admin Classes
# =========================================================================
class SignUpAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'timestamp', 'updated']
    form = SignUpForm

    class Meta:
        model = SignUp

# =========================================================================
# ----- Admin Model Registration
# =========================================================================
admin.site.register(SignUp, SignUpAdmin)
