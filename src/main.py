from fastapi import FastAPI
from sqladmin import Admin

from src.admin.authentication_backend import authentication_backend
from src.admin.model_admin import UserAdmin, ParentAdmin, PotatoAdmin, EmployeeAdmin
from src.auth.router import router as auth_router
from src.database import engine, Base
from src.test_app.router import router as test_app_router

app = FastAPI()
admin = Admin(
    app=app,
    engine=engine,
    authentication_backend=authentication_backend
)

Base.metadata.create_all(bind=engine)

admin.add_view(UserAdmin)
admin.add_view(ParentAdmin)
admin.add_view(PotatoAdmin)
admin.add_view(EmployeeAdmin)

app.include_router(test_app_router,
                   prefix='/test',
                   tags=['Test'])
app.include_router(auth_router,
                   prefix='/auth',
                   tags=['Auth'])


@app.get('/')
async def root():
    return {'message': 'Start_font'}
