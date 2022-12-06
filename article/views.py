from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import articleForms
from .models import article,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required




def Makaleler(request):
    
    keyword = request.GET.get("keyword")
    
    if keyword:
        
        makale = article.objects.filter(title__contains = keyword)
        return render(request,"Makaleler.html",{"makale":makale})
    
    
    
    makale  = article.objects.all()
    

    return render(request,"Makaleler.html",{"makale":makale})


def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")


@login_required(login_url="user:loginu")
def dashboard(request):
    articles = article.objects.filter(author = request.user)
    context = {
        "articles" : articles
    }
    
    return render(request,"dashboard.html",context)

@login_required(login_url="user:loginu")
def addarticle(request):
    form = articleForms(request.POST or None , request.FILES or None)
    if form.is_valid():
        
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale başarıyla kaydedildi!")
        return redirect("article:dashboard")
        
    context = {
        "form" : form
    }

    return render(request,"addarticle.html",context)


def detail(request,id):
    #makale = article.objects.filter(id = id).first()
    
    makale = get_object_or_404(article,id = id)
    
    comments = makale.comments.all()
    
    
    return render(request,"detail.html",{"makale":makale,"comments":comments})
    
@login_required(login_url="user:loginu")
def update(request,id):
    
    makale = get_object_or_404(article,id=id) 
    form = articleForms(request.POST or None , request.FILES or None,instance=makale)
    
    if form.is_valid():
        makale = form.save(commit=False)
        makale.author = request.user
        makale.save()
        messages.success(request,"Makale başarıyla güncellendi!")
        return redirect("article:dashboard")
    
    
    
    
    return render(request,'update.html',{"form":form})
    
@login_required(login_url="user:loginu")
def delete(request,id):
    
    makale = get_object_or_404(article,id=id)
    
    makale.delete()
    messages.success(request,"Makale başarıyla silindi!")
    return redirect("article:dashboard")



def addcomment(request,id):
    
    
    makale = get_object_or_404(article,id=id)
    
    if request.method == "POST":
        
        commentauthor = request.POST.get("commentauthor")
        commentcontent = request.POST.get("commentcontent")
        
        newComment = Comment(commentauthor = commentauthor ,commentarea = commentcontent)
        
        newComment.makale = makale
        
        newComment.save()
        
        messages.success(request,"Yorum başarıyla eklendi!")
        return redirect(reverse("article:detail",kwargs= {"id":id}))

    
    
# Create your views here.
