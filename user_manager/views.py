from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import OwnUser


def user_manager_check(request):
    query_set = OwnUser.objects.all().order_by('-create_time')
    context = {'own_users': query_set}
    return render(request, 'user_manager/user_manager_view.html', context)


def user_manager_add(request):
    if request.method == 'GET':
        context = {}
        return render(request, 'user_manager/user_manager_add.html', context)

    if request.method == 'POST':
        name = request.POST.get('name', None)
        sex = request.POST.get('sex', None)
        address = request.POST.get('address', None)
        form_dict = {
            'name': name,
            'sex': sex,
            'address': address
        }
        print(form_dict)

        owner_user = OwnUser()
        owner_user.name = form_dict['name']
        owner_user.sex = form_dict['sex']
        owner_user.address = form_dict['address']
        owner_user.save()

        return HttpResponseRedirect('/user_manager/')


def user_manager_delete(request):
    del_id = request.GET.get('id', None)
    owner_user = OwnUser.objects.get(id=del_id)
    owner_user.delete()
    return HttpResponseRedirect('/user_manager/')


def user_manager_update(request):
    if request.method == 'GET':
        update_id = request.GET.get('id', None)
        owner_user = OwnUser.objects.get(id=update_id)
        context = {'owner_user': owner_user}
        return render(request, 'user_manager/user_manger_update.html', context)

    if request.method == 'POST':
        name = request.POST.get('name', None)
        sex = request.POST.get('sex', None)
        address = request.POST.get('address', None)
        form_dict = {
            'name': name,
            'sex': sex,
            'address': address
        }
        print(form_dict)

        update_id = request.GET.get('id', None)
        owner_user = OwnUser.objects.get(id=update_id)

        owner_user.name = form_dict['name']
        owner_user.sex = form_dict['sex']
        owner_user.address = form_dict['address']
        owner_user.save()
        return HttpResponseRedirect('/user_manager/')

