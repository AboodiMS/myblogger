from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [

    path('login/',views.loginUser,name = 'login'),
    path('logout/',LogoutView.as_view(template_name='logout.html'),name = 'logout'),

    path('navbar',views.editNavbar,name = 'navbar'),
    path('',views.home,name = 'home'),

    path('portfolio',views.portfolio,name = 'portfolio'),

    path('contactUs/',views.contactUs,name = 'contactUs'),
    path('contactUs/addNewMessageRow',views.addNewMessageRow,name = 'addNewMessageRow'),



    path('editNavbar',views.editNavbar,name = 'editNavbar'),
    path('editHome',views.editHome,name = 'editHome'),

    path('savePersonalInformation' , views.savePersonalInformation , name = 'savePersonalInformation'),
    path('saveStudyInformation',views.saveStudyInformation,name = 'saveStudyInformation'),
 

    path('addNewCover/',views.addNewCover,name = 'addNewCover'),
    path('addNewCover/addNewCoverRow' , views.addNewCoverRow , name = 'addNewCoverRow'),
    path('deleteCoverRow/<int:id>', views.deleteCoverRow, name='deleteCoverRow'),

    path('addNewExCompany/',views.addNewExCompany,name = 'addNewExCompany'),
    path('addNewExCompany/addNewExCompanyRow' , views.addNewExCompanyRow , name = 'addNewExCompanyRow'),
    path('deleteExCompanyRow/<int:id>', views.deleteExCompanyRow, name='deleteExCompanyRow'),

    path('addNewSkill/',views.addNewSkill,name = 'addNewSkill'),
    path('addNewSkill/addNewSkillRow' , views.addNewSkillRow , name = 'addNewSkillRow'),
    path('deleteSkillRow/<int:id>', views.deleteSkillRow, name='deleteSkillRow'),

    path('editPortifolio',views.editPortifolio,name = 'editPortifolio'),
    path('addNewPortifolio/',views.addNewPortifolio,name = 'addNewPortifolio'),
    path('addNewPortifolio/addNewPortifolioRow' , views.addNewPortifolioRow , name = 'addNewPortifolioRow'),
    path('deletePortifolioRow/<int:id>', views.deletePortifolioRow, name='deletePortifolioRow'),

    path('editContactUs',views.editContactUs,name = 'editContactUs'),
    path('deleteMessageRow/<int:id>', views.deleteMessageRow, name='deleteMessageRow'),

]