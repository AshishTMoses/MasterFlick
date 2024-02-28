from django.urls import path
from Backend import views



urlpatterns = [
    path('index_page/', views.index_page, name="index_page"),
    path('category_page/', views.category_page, name="category_page"),
    path('save_cat/', views.save_cat, name="save_cat"),
    path('cat_disp/', views.cat_disp, name="cat_disp"),
    path('edit_cat/<int:dataid>/', views.edit_cat, name="edit_cat"),
    path('update_cat/<int:dataid>/', views.update_cat, name="update_cat"),
    path('remv_cat/<int:dataid>/', views.remv_cat, name="remv_cat"),
    path('multimedia_page/', views.multimedia_page, name="multimedia_page"),
    path('save_multimedia/', views.save_multimedia, name="save_multimedia"),
    path('mult_display/', views.mult_display, name="mult_display"),
    path('edit_mult/<int:dataid>', views.edit_mult, name="edit_mult"),
    path('update_mult/<int:dataid>', views.update_mult, name="update_mult"),
    path('mult_delt/<int:dataid>', views.mult_delt, name="mult_delt"),
    path('admin_login_page/', views.admin_login_page, name="admin_login_page"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('add_mallu_film/', views.add_mallu_film, name="add_mallu_film"),
    path('save_mallu_film', views.save_mallu_film, name="save_mallu_film"),
    path('display_mal_film', views.display_mal_film, name="display_mal_film"),
    path('edit_mal_film<int:dataid>', views.edit_mal_film, name="edit_mal_film"),
    path('update_mal_film<int:dataid>', views.update_mal_film, name="update_mal_film"),
    path('cnc_mal_film<int:dataid>', views.cnc_mal_film, name="cnc_mal_film"),



]
