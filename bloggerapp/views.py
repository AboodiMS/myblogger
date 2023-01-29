from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Profile,Skill,ExCompany,Portifolio,Cover,Message
from django.urls import reverse
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required,permission_required
from .decorators import loggedUsers



# Create your views here.
def navbar(request):
    myprofile = Profile.objects.all().first()
    template = loader.get_template('navbar.html')
    context = {
    'myprofile': myprofile,
    }
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template('home.html')

    myprofile=Profile.objects.all().first()
    mycovers = Cover.objects.all()
    myexcompanies = ExCompany.objects.all()
    myskills = Skill.objects.all()

    context = {
    'myprofile': myprofile,
    'mycovers': mycovers,
    'myexcompanies': myexcompanies,
    'myskills': myskills,
    }
    return HttpResponse(template.render(context, request))

def portfolio(request):
    template = loader.get_template('portfolio.html')
    myportfolios = Portifolio.objects.all()
    context = {
    'myportfolios': myportfolios,
    }
    return HttpResponse(template.render(context, request))

def contactUs(request):
    template = loader.get_template('contactUs.html')
    return HttpResponse(template.render({}, request))


def addNewMessageRow(request):
    message = Message(
    email=request.POST['email'],
    name=request.POST['name'],
    message=request.POST['message'])
    message.save()
    return HttpResponseRedirect(reverse('contactUs')) 

# ------------------------------------------------------------------------------
# start edit
@loggedUsers
def loginUser(request):
    if request.method == 'POST':       
        user = authenticate(request, username =request.POST['username'],password=request.POST['password'])
        if user is None:         
           return HttpResponseRedirect(reverse('login')) 
        else : 
           login(request,user)
           return HttpResponseRedirect(reverse('editHome')) 
    else :
        template = loader.get_template('login.html')
        return HttpResponse(template.render({},request))


def editNavbar(request):
    myprofile = Profile.objects.all().first()
    template = loader.get_template('editNavbar.html')
    context = {
    'myprofile': myprofile,
    }
    return HttpResponse(template.render(context, request))

@login_required(redirect_field_name="login")
def editHome(request):
    myprofile = Profile.objects.all().first()
    if (myprofile is None):
        profile = Profile(
            fullname="الاسم الكامل",
            birthday="2000/12/30",
            livingin="المحافظة - المنطقة",
            university="اسم الحامعة",
            college="اسم الكلية",
            department="اسم القسم",
            yearofgraduation="سنة التخرج")
        profile.save()
        myprofile=Profile.objects.all().first()

    mycovers = Cover.objects.all()
    myexcompanies = ExCompany.objects.all()
    myskills = Skill.objects.all()

    template = loader.get_template('editHome.html')
    context = {
    'myprofile': myprofile,
    'mycovers': mycovers,
    'myexcompanies': myexcompanies,
    'myskills': myskills,
    }
    return HttpResponse(template.render(context, request))

@login_required(redirect_field_name="login")
def savePersonalInformation(request):
    myprofile = Profile.objects.all().first()
    myprofile.fullname=request.POST['fullname']
    myprofile.birthday=request.POST['birthday']
    myprofile.livingin=request.POST['livingin']
    myprofile.save()
    return HttpResponseRedirect(reverse('editHome'))

@login_required(redirect_field_name="login")
def saveStudyInformation(request):
    myprofile = Profile.objects.all().first()
    myprofile.university=request.POST['university']
    myprofile.college=request.POST['college']
    myprofile.department=request.POST['department']
    myprofile.yearofgraduation=request.POST['yearofgraduation']
    myprofile.save()
    return HttpResponseRedirect(reverse('editHome'))

@login_required(redirect_field_name="login")
def addNewCover(request):
    template = loader.get_template('addNewCover.html')
    return HttpResponse(template.render({}, request))

@login_required(redirect_field_name="login")
def addNewCoverRow(request):
    cover = Cover(
    titel=request.POST['titel'],
    details=request.POST['details'])
    cover.save()
    return HttpResponseRedirect(reverse('editHome'))  

@login_required(redirect_field_name="login")
def deleteCoverRow(request, id):
    cover = Cover.objects.get(id=id)
    cover.delete()
    return HttpResponseRedirect(reverse('editHome'))

@login_required(redirect_field_name="login")
def addNewExCompany(request):
    template = loader.get_template('addNewExCompany.html')
    return HttpResponse(template.render({}, request))

@login_required(redirect_field_name="login")
def addNewExCompanyRow(request):
    excompany = ExCompany(
    companyname=request.POST['companyname'],
    jobtitle=request.POST['jobtitle'],
    details=request.POST['details'])
    excompany.save()
    return HttpResponseRedirect(reverse('editHome'))  

@login_required(redirect_field_name="login")
def deleteExCompanyRow(request,id):
    excompany = ExCompany.objects.get(id=id)
    excompany.delete()
    return HttpResponseRedirect(reverse('editHome'))

@login_required(redirect_field_name="login")
def addNewSkill(request):
    template = loader.get_template('addNewSkill.html')
    return HttpResponse(template.render({}, request))

@login_required(redirect_field_name="login")
def addNewSkillRow(request):
    skill = Skill(
    skillname=request.POST['skillname'])
    skill.save()
    return HttpResponseRedirect(reverse('editHome'))  

@login_required(redirect_field_name="login")
def deleteSkillRow(request,id):
    skill = Skill.objects.get(id=id)
    skill.delete()
    return HttpResponseRedirect(reverse('editHome'))

@login_required(redirect_field_name="login")
def editContactUs(request):
    template = loader.get_template('editContactUs.html')
    mymessages = Message.objects.all()
    context = {
    'mymessages': mymessages,
    }
    return HttpResponse(template.render(context, request))

@login_required(redirect_field_name="login")
def deleteMessageRow(request,id):
    mymessage = Message.objects.get(id=id)
    mymessage.delete()
    return HttpResponseRedirect(reverse('editContactUs'))

@login_required(redirect_field_name="login")
def editPortifolio(request):
    template = loader.get_template('editPortifolio.html')
    myportfolios = Portifolio.objects.all()
    context = {
    'myportfolios': myportfolios,
    }
    return HttpResponse(template.render(context, request))

@login_required(redirect_field_name="login")
def addNewPortifolio(request):
    template = loader.get_template('addNewPortifolio.html')
    return HttpResponse(template.render({}, request))

@login_required(redirect_field_name="login")
def addNewPortifolioRow(request):
    portifolio = Portifolio(
    projecttitel =request.POST['projecttitel'],
    tools=request.POST['tools'],
    details=request.POST['details'])
    portifolio.save()
    return HttpResponseRedirect(reverse('editPortifolio'))  

@login_required(redirect_field_name="login")
def deletePortifolioRow(request,id):
    portifolio = Portifolio.objects.get(id=id)
    portifolio.delete()
    return HttpResponseRedirect(reverse('editPortifolio'))
# end edit
# ---------------------------------------------------------------