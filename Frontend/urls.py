from django.urls import path
from Frontend import views



urlpatterns = [
    path('home_page/', views.home_page, name="home_page"),
    path('single_mult_page/<int:videoid>/', views.single_mult_page, name="single_mult_page"),
    path('mal_film_single_page/<int:malid>/', views.mal_film_single_page, name="mal_film_single_page"),
    path('signup/', views.signup, name="signup"),
    path('save_signup/', views.save_signup, name="save_signup"),
    path('login_page/', views.login_page, name="login_page"),
    path('Subscription_page/', views.Subscription_page, name="Subscription_page"),
    path('payment/', views.payment, name="payment"),
    path('user_login/', views.user_login, name="user_login"),
    path('logout/', views.logout, name="logout"),
    path('cat_view_all/', views.cat_view_all, name="cat_view_all"),
    path('mal_view_all/', views.mal_view_all, name="mal_view_all"),
    path('searchBar/', views.searchBar, name="searchBar"),













]