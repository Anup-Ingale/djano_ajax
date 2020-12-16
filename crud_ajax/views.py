from django.views.generic import ListView
from .models import Employee
from django.views.generic import View
from django.http import JsonResponse

class CrudView(ListView):
    model = Employee
    template_name = 'crud_ajax/crud.html'
    context_object_name = 'users'

class CreateCrudUser(View):
    def  get(self, request):
        name = request.GET.get('name', None)
        roll_no = request.GET.get('roll_no', None)
        class_name = request.GET.get('class_name', None)

        obj = Employee.objects.create(
            name = name,
            roll_no = roll_no,
            class_name = class_name
        )

        user = {'id':obj.id,'name':obj.name,'roll_no':obj.roll_no,'class_name':obj.class_name}

        data = {
            'user': user
        }
        return JsonResponse(data)

class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Employee.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class UpdateCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name = request.GET.get('name', None)
        roll_no = request.GET.get('roll_no', None)
        class_name = request.GET.get('class_name', None)

        obj = Employee.objects.get(id=id1)
        obj.name = name
        obj.roll_no = roll_no
        obj.class_name = class_name
        obj.save()

        user = {'id':obj.id,'name':obj.name,'roll_no':obj.roll_no,'class_name':obj.class_name}

        data = {
            'user': user
        }
        return JsonResponse(data)