from django.shortcuts import render


def main_page(request):
    return render(request, 'presentation/main_page.html')
