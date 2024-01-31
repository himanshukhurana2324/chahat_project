from django.shortcuts import render,redirect,get_object_or_404
from django.shortcuts import HttpResponse
from .models import LongToShort
def home(request):
    form={
        "submitted":False,
        "error":False
        } #by default value is false when user not fill the form

    if request.method =='POST':
        longurl=request.POST['longurl']
        shorturl=request.POST['custom_name']
        
        try:
        # create operation
            obj=LongToShort(
                longurl=longurl,
                shorturl=shorturl
                )
            obj.save()

            date=obj.date
            clicks=obj.clicks

            form["longurl"]=longurl
            form["submitted"]=True #when user fill the form then urls shown
            form["shorturl"]=request.build_absolute_uri()+shorturl
            form["date"]=date
            form["clicks"]=clicks
        except:
          form['error']=True 
    return render(request,'index.html',form)

def redirect_url(request,shorturl):
    row=LongToShort.objects.filter(shorturl=shorturl)
    if len(row) == 0:
        return HttpResponse("No such short url here")
    obj=row[0]
    longurl=obj.longurl

    obj.clicks=obj.clicks+1
    obj.save()
    return redirect(longurl)

def all_analytics(request):
    row=LongToShort.objects.all()
    context={"row":row}
    return render(request,"all-analytics.html",context)

def analytic(request, id):
    pk= int(id)
    # row=LongToShort.objects.all()
    item_row = get_object_or_404(LongToShort, pk=pk)
    context = {"item_row": item_row}
    return render(request,'analytics.html', context)

