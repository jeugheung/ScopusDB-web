from django.shortcuts import render
from django.http import HttpResponse
from .models import Researchers

def about(request):
    return render(request, 'scopus/about.html')

def overviewSummary(request):
    #scopusFirstScreen = OverallScopus.objects.all()
    #print(request)
    return render(request, 'scopus/overview-summary.html')

def overviewRankings(request):
    return render(request, 'scopus/overview-rankings.html')

def overviewCollaboration(request):
    return render(request, 'scopus/overview-collaboration.html')

def overviewPublished(request):
    return render(request, 'scopus/overview-published.html')

def overviewViewed(request):
    return render(request, 'scopus/overview-viewed.html')

def overviewCited(request):
    return render(request, 'scopus/overview-cited.html')

def news(request):
    return render(request, 'scopus/news.html')

def researchers(request):
    data = Researchers.objects.all()
    data_1 = {
        "researchers_numbers": data
    }
    return render(request, 'scopus/researchers.html', data_1)

def benchmarking(request):
    return render(request, 'scopus/benchmarking.html')

