from django.shortcuts import render,redirect
from .models import Testlist
from .models import PrefectureMst
from django.db.models import Max
from django.core.paginator import Paginator

# Create your views here.
def frontpage(request):
    all_testlist = Testlist.objects.all()
    paginator = Paginator(all_testlist, 5) # 1ページに5件表示
    p = request.GET.get('p') # URLのパラメータから現在のページ番号を取得
    indexPage = paginator.get_page(p) # 指定のページのArticleを取得
    return render(request, 'frontpage.html',{'indexPage': indexPage})

def detail(request,pk):
    postForm = PrefectureMst.objects.all()
    post = Testlist.objects.get(pk=pk)
    return render(request, 'detailpage.html',{"post": post,"postForm": postForm})
def updateform(request,pk):
    post = Testlist.objects.get(pk=pk)
    postId = request.POST["id"]
    postName = request.POST["name"]
    postAge = request.POST["age"]
    postMail = request.POST["mail"]
    postPrefecture_no = request.POST["prefecture_no"]
    postPrefecture_name = request.POST["prefecture_name"]
    postPrefecture_kana = request.POST["prefecture_kana"]
    article = Testlist(
    postId,postName,postAge,postMail,postPrefecture_no,postPrefecture_name,postPrefecture_kana
    )
    article.save()

    return render(request, 'update.html',{"post": post,"postId": postId, "postName": postName,
    "postAge": postAge,"postMail":postMail,"postPrefecture_no":postPrefecture_no,"postPrefecture_name":postPrefecture_name
    ,"postPrefecture_kana":postPrefecture_kana})
def newform(request):
    post = Testlist.objects.all().aggregate(id=Max('id'))
    postId=post['id'] + 1
    postForm = PrefectureMst.objects.all()
    return render(request,'new.html',{'post':post,'postForm':postForm,'postId':postId})
def createfunction(request):
    postId = request.POST["id"]
    postName = request.POST["name"]
    postAge = request.POST["age"]
    postMail = request.POST["mail"]
    postPrefecture_no = request.POST["prefecture_no"]
    postPrefecture_name = request.POST["prefecture_name"]
    postPrefecture_kana = request.POST["prefecture_kana"]
    Testlist.objects.create(id=postId, name=postName,age=postAge,mail=postMail,prefecture_no=postPrefecture_no,
    prefecture_name=postPrefecture_name,prefecture_kana=postPrefecture_kana)
    return render(request, 'create.html',{"postId": postId, "postName": postName,
    "postAge": postAge,"postMail":postMail,"postPrefecture_no":postPrefecture_no,"postPrefecture_name":postPrefecture_name
    ,"postPrefecture_kana":postPrefecture_kana})
def deletefunction(request):
    check = request.POST.getlist("checkbox_list[]")
    print(1)
    Testlist.objects.filter(id__in=check).delete()
    return render(request,'delete.html',{"check":check})
def index(request):
    all_testlist = Testlist.objects.all()
    paginator = Paginator(all_testlist, 5) # 1ページに5件表示
    p = request.GET.get('p') # URLのパラメータから現在のページ番号を取得
    indexPage = paginator.get_page(p) # 指定のページのArticleを取得
    return render(request, 'index.html', {'indexPage': indexPage})


