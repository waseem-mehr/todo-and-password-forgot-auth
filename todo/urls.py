from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("",views.home),
    path("update/<int:id>/",views.update),
    path("add/",views.add,name="add"),
    path("delete/<int:id>/",views.delete),

    
   #############################################################

    
    #START OF PASSWORD RESET AUTHENTICATION SECTION 



    path('reset-password/',
    auth_view.PasswordResetView.as_view(
        template_name="reset-password.html"
    )
    ,name="password_reset"
    ),
    path('reset-password-done/',
    auth_view.PasswordResetDoneView.as_view(
        template_name="password-reset-done.html"
    )
    ,name="password_reset_done"
    ),
    path('reset-password-confirm/<uidb64>/<token>/',
    auth_view.PasswordResetConfirmView.as_view(
        template_name="password-reset-confirm.html"
    )
    ,name="password_reset_confirm"
    ),
    path('rest-password-complete/',
    auth_view.PasswordResetCompleteView.as_view(
        #password-reset-complete.html
        template_name="password-reset-complete.html"
    )
    ,name="password_reset_complete"
    )
]
