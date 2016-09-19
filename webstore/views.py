from django.shortcuts import render

# =========================================================================
# Renders about.html page
# =========================================================================

def about(request):
    return render(request, "about.html", {})
