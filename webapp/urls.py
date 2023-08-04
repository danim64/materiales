from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("listar-materiales/", views.materiales, name="listar-materiales"),
    path("eliminar/<int:id>", views.eliminar, name="eliminar"),
    path("materiales/crear", views.crearMaterial, name="crear-material"),
    path("materiales/confirm-create", views.confirm_create, name="confirm-create"),
    path("materiales/editar/confirm-edit", views.confirm_edit, name="confirm-edit"),
    path("materiales/editar/<int:id>", views.editar_material, name="editar-material"),
    path("listar-grupo/", views.listar_grupo, name="listar-grupo"),
    path("grupo/eliminar/<int:id>", views.eliminar_grupo, name="eliminar-grupo"),
    path("grupo/eliminar/cant-erase", views.cant_erase, name= "cant-erase"),
    path("grupo/crear", views.crearGrupo, name="crear-grupo"),
    path("grupo/confirm-create", views.confirm_create_gr, name="confirm-create"),
    path("listar-marca/", views.listar_marca, name="listar-marca"),
    path("marca/crear", views.crearMarca, name="crear-marca"),
    path("marca/confirm-create", views.confirm_create_mkr, name="confirm-create"),
    path("marca/eliminar/<int:id>", views.eliminar_marca, name="eliminar-marca"),
    path("marca/eliminar/cant-erase", views.cant_erase_mk, name= "cant-erase_mk"),
    path("listar-proveedor/", views.listar_proveedor, name="listar-proveedor"),
    path("proveedor/crear", views.crearProveedor, name="crear-proveedor"),
    path("proveedor/confirm-create", views.confirm_create_prvd, name="confirm-create"),
    path("proveedor/editar/confirm-edit-prv", views.confirm_edit_prv, name="confirm-edit-prv"),
    path("proveedor/editar/<int:id>", views.editar_proveedor, name="editar-proveedor"),
    path("proveedor/eliminar/<int:id>", views.eliminar_proveedor, name="eliminar-proveedor"),
    path("proveedor/eliminar/cant-erase", views.cant_erase_mk, name= "cant-erase_mk"),
    path("listar-unidades/", views.listar_unidades, name="listar-unidades"),
    path("unidades/eliminar/<int:id>", views.eliminar_unidad, name="eliminar-unidades"),
    path("unidades/eliminar/cant-erase", views.cant_erase, name= "cant-erase"),
    path("unidades/crear", views.crearUnidades, name="crear-unidades"),
    path("unidades/confirm-create", views.confirm_create_und, name="confirm-create_unds"),
    path("registration", views.registerPage, name="register"),
    path("registration/confirm-create", views.confirm_create_reg, name="confirm-create_reg"),
    path('registration/login/', views.login_view, name="login"),
    path('registration/logout/', views.logout_view, name="logout"),
    path("registration/relogin/", views.relogin_view, name="relogin"),
    #path('logout/', logout_view),
    
]
