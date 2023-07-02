from django.contrib import admin
from django.urls import path, include
from . import views, user_login
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app'
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('base/', views.BASE, name='base'),
                  path('404/', views.PAGE_NOT_FOUND, name="404"),
                  path('', views.HOME, name='home'),
                  path('courses/', views.SINGLE_COURSE, name='single_course'),
                  path('courses/filter-data', views.filter_data, name="filter-data"),
                  path('course/<slug:slug>', views.COURSE_DETAILS, name='course_details'),
                  path('search', views.SEARCH_COURSE, name='search_course'),
                  path('contact/', views.CONTACT_US, name='contact_us'),
                  path('about/', views.ABOUT_US, name='about_us'),
                  path('accounts/register', user_login.REGISTER, name='register'),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('dologin/', user_login.DO_LOGIN, name="doLogin"),
                  path('accounts/profile', user_login.PROFILE, name='profile'),
                  path('accounts/profile/update', user_login.PROFILE_UPDATE, name='profile_update'),
                  path('checkout/<slug:slug>', views.CHECKOUT, name='checkout'),


                  path('password_reset/', views.password_reset_request, name='password_reset'),
                  path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
                  path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
                  path('reset/done/', views.password_reset_complete, name='password_reset_complete'),


                  path('my-course/', views.MY_COURSE, name="my_course"),
                  path('verify_payment/', views.VERIFY_PAYMENT, name="verify_payment"),
                  path('course/watch-course/<slug:slug>', views.WATCH_COURSE, name='watch-course'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
