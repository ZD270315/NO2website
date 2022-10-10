from django.shortcuts import render, redirect
from website02 import models


# Create your views here.
def depart_list(request):
    """部门列表"""
    queryset = models.Department.objects.all()
    return render(request, 'depart_list.html', {'queryset': queryset})


def depart_add(request):
    """添加部门"""
    if request.method == "GET":
        return render(request, 'depart_add.html')
    # 获取用户通过post提交的数据
    title = request.POST.get("title")
    # 保存到数据库
    models.Department.objects.create(title=title)
    # 返回部门列表
    return redirect("/depart/list/")


def depart_delete(request):
    """删除部门"""
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect("/depart/list/")


def depart_edit(request, nid):
    """修改部门"""
    # 根据nid获取数据
    row_object = models.Department.objects.filter(id=nid).first()
    return render(request, 'depart_edit.html', {"row_object": row_object})