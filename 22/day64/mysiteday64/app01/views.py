from django.shortcuts import render,HttpResponse,redirect
from app01 import models

# Create your views here.
# 出版社
def pub_list(request):
    if request.method == "GET":
        pub_list = models.Publisher.objects.all().order_by("id")
        return render(request,'pub_list.html',{'pub_list':pub_list})

def pub_add(request):
    shz = {
        'name':'素还真',
        'title': '半神半圣亦半仙，全儒全道是会贤。脑中真书藏万卷，掌握文武半边天。'
    }
    if request.method == "POST":
        new_name = request.POST.get('name',None)
        models.Publisher.objects.create(name=new_name)
        return redirect('/pub_list/')
    return render(request,'pub_add.html',{'shz':shz})

def pub_del(request):
    max_id = models.Publisher.objects.last().id
    del_id = request.GET.get('id',None)
    if del_id and int(del_id) <= int(max_id):
        del_obj = models.Publisher.objects.get(id=del_id)
        del_obj.delete()
        return redirect('/pub_list/')
    else:
        msg = "没有发现此信息"
        title = "删除页面"
        return render(request,'pub_not_found.html',{"msg":msg,"title":title})

def pub_edit(request):
    shz = {
        'name': '素还真',
        'title': '半神半圣亦半仙，全儒全道是会贤。脑中真书藏万卷，掌握文武半边天。'
    }
    if request.method == "GET":
        max_id = models.Publisher.objects.last().id
        edit_id = request.GET.get('id',None)
        if edit_id and int(edit_id) < int(max_id):
            edit_obj = models.Publisher.objects.get(id=edit_id)
            print(edit_obj)
            return render(request,'pub_edit.html',{'shz':shz,'edit':edit_obj})
        else:
            return redirect('/pub_list/')
    else:
        edit_id = request.POST.get('id',None)
        edit_name = request.POST.get('name',None)

        edit = models.Publisher.objects.get(id=edit_id)
        edit.name=edit_name
        edit.save()
        msg = '修改完成，正在跳转'
        title = '修改页面'
        return render(request,'pub_not_found.html',{'msg':msg,'title':title})


# 书
def book_list(request):
    book_list = models.Book.objects.all()
    title = "图书列表"
    return render(request,"book_list.html",locals())

def book_add(request):
    if request.method == "POST":
        new_name = request.POST.get('name')
        new_publisher_id = request.POST.get('publisher_id')
        models.Book.objects.create(title=new_name,publisher_id = new_publisher_id)
        return redirect('/book_list/')
    pub_list = models.Publisher.objects.all()
    title = "新增图书"
    return render(request,"book_add.html",locals())

def book_del(request):
    max_id = models.Book.objects.last().id
    del_id = request.GET.get('id',None)
    if del_id and int(del_id) <= int(max_id):
        del_obj = models.Book.objects.get(id=del_id)
        del_obj.delete()
        return redirect('/book_list/')
    else:
        msg = "没有发现此信息"
        title = "删除页面"
        return render(request,'pub_not_found.html',{"msg":msg,"title":title})

def book_edit(request):
    shz = {
        'name': '素还真',
        'title': '半神半圣亦半仙，全儒全道是会贤。脑中真书藏万卷，掌握文武半边天。'
    }
    if request.method == "GET":
        max_id = models.Book.objects.last().id
        edit_id = request.GET.get('id',None)
        if edit_id and int(edit_id) <= int(max_id):
            edit_obj = models.Book.objects.get(id=edit_id)
            pub_obj = models.Publisher.objects.all()
            print(edit_obj)
            return render(request,'book_edit.html',{'shz':shz,'edit':edit_obj,"pub":pub_obj})
        else:
            return redirect('/book_list/')
    else:
        edit_id = request.POST.get('id',None)
        edit_name = request.POST.get('name',None)
        edit_publisher_id = request.POST.get('publisher_id',None)

        edit = models.Book.objects.get(id=edit_id)
        edit.title = edit_name
        edit.publisher_id = edit_publisher_id
        edit.save()
        msg = '修改完成，正在跳转'
        title = '修改页面'
        return render(request,'book_not_found.html',{'msg':msg,'title':title})

def book_test(reuqest):
    book_list = models.Book.objects.all()
    for i in book_list:
        print(i)
        print(i.title)
        print(i.publisher_id)
    return HttpResponse("素还真")


# 作者

def author_list(request):
    author_list = models.Author.objects.all()
    return render(request,"author_list.html",locals())


def author_add(request):
    shz = {
        'name':'素还真',
        'title': '半神半圣亦半仙，全儒全道是会贤。脑中真书藏万卷，掌握文武半边天。'
    }
    book_list = models.Book.objects.all()
    if request.method == "POST":
        new_name = request.POST.get("name",None)
        new_books = request.POST.getlist("books",None)

        new_author = models.Author.objects.create(name=new_name)
        new_author.book.set(new_books)
        return redirect("/author_list/",{'shz':shz})
    else:
        return render(request,"author_add.html",{'shz':shz,"book_list":book_list})


def author_edit(request):
    if request.method == "POST":
        edit_id = request.POST.get("id",None)
        edit_name = request.POST.get("name",None)
        edit_books = request.POST.getlist("books",None)
        # print(edit_id,edit_name,edit_books)
        # return HttpResponse("素还真")
        author_obj = models.Author.objects.get(id=edit_id)
        author_obj.name =  edit_name
        author_obj.book.set(edit_books)
        author_obj.save()
        return redirect("/author_list/")
    else:
        book_list = models.Book.objects.all()
        edit_id = request.GET.get("id",None)
        author_obj = models.Author.objects.get(id=edit_id)

        shz = {
            'name':'素还真',
            'title': '半神半圣亦半仙，全儒全道是会贤。脑中真书藏万卷，掌握文武半边天。'
        }
        return render(request,"author_edit.html",{"shz":shz,"author_obj":author_obj,"book_list":book_list})

def author_del(request):
    delete_id = request.GET.get('id',None)
    models.Author.objects.get(id=delete_id).delete()
    return redirect("/author_list/")


def author_test(request):
    pass