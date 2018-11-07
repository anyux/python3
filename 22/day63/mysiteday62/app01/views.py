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

