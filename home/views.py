from django.shortcuts import render,get_object_or_404
from workers.models import Position,Workers

from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
def home(request):
    query=request.GET.get('q')
    if query:
        object_list=Workers.objects.filter(Q(firstname__icontains=query)|Q(lastname__icontains=query)|Q(fathername__icontains=query)|Q(position__name__icontains=query))
    else:
        object_list=Workers.objects.all()
    paginator=Paginator(object_list,2)
    page=request.GET.get('page')
    try:
        workers=paginator.page(page)
    except PageNotAnInteger:
        workers=paginator.page(1)
    except EmptyPage:
        workers=paginator.page(paginator.num_pages)

    return render(request,'index.html',{'workers':workers})
def workers_detail(request,slug):
    worker=get_object_or_404(Workers,slug=slug)
    return render(request,'detail.html',{'worker':worker})