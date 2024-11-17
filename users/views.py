from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def admin_dashboard(request):
    if request.user.is_admin:
        return render(request, 'admin_dashboard.html')
    else:
        return render(request, 'unauthorized.html')