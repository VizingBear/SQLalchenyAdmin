from sqladmin import ModelView
from starlette.requests import Request

# from src.database import User


from src.auth.models import User
from src.many_to_many.models import Employee, Task
from src.one_to_one.models import Potato, Box
from src.one_to_many.models import Parent, Child


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.name, User.fullname]
    column_searchable_list = [User.name]
    column_sortable_list = [User.fullname]
    page_size = 5
    page_size_options = [25, 50, 100, 200]

    async def after_model_change(self):
        print('Модель изменена')

    async def is_accessible(self, request: Request) -> bool:
        return True

    async def is_visible(self, request: Request) -> bool:
        return True


class ParentAdmin(ModelView, model=Parent):
    name = "One to many"
    name_plural = "One to many"
    column_list = [Parent.id, Parent.name, Child.parent_id, Child.name]


class PotatoAdmin(ModelView, model=Potato):
    name = "One to one"
    name_plural = "One to one"
    column_list = [Potato.id, Potato.box, Box.id, Box.parent_id, Box.potato]


class EmployeeAdmin(ModelView, model=Employee):
    name = "Many to many"
    name_plural = "Many to many"
    column_list = [Employee.id, Employee.name, Employee.task, Task.id, Task.name]
