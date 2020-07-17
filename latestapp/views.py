from latestapp.models import Login, Userdetails, Legalofficer, Medicalofficer, Customsofficer, Narcoticofficer, \
    Socialworker, Event
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here#
def index(request):
    return render(request, 'index.html')
def drug_abuse(request):
    return render(request,'about_rehabilitation_centers.html')


def signup(request):
    if request.method == 'POST':
        login = Login()
        login.userid = request.POST.get("uname")
        login.password = request.POST.get("pname")
        login.usertype = request.POST.get("usertype")
        login.save()
        used = Userdetails()
        used.userid = request.POST.get("uname")
        used.password = request.POST.get("pname")
        used.conformpassword = request.POST.get("pname")
        used.first_name = request.POST.get("fname")
        used.middle_name = request.POST.get("mname")
        used.last_name = request.POST.get("lname")
        used.date_of_birth = request.POST.get("ddate")
        used.contact_number = request.POST.get("mno")
        used.gender = request.POST.get("gender")
        used.city = request.POST.get("city")
        used.address = request.POST.get("texteditor")
        used.district = request.POST.get("district")
        used.nation = request.POST.get("nation")
        used.profession = request.POST.get("profession")
        used.save()
        return render(request, "index.html")
    else:
        return render(request, "signuppagee.html")


def loginpage(request):
    if request.method == 'POST':
        if request.POST.get('uname') and request.POST.get('pname'):
            uid = request.POST.get('uname')
            up = request.POST.get('pname')
            if Login.objects.filter(userid=uid) and Login.objects.filter(password=up):
                return render(request, 'index.html')
            else:
                return render(request, 'loginnew.html')
    else:
        return render(request, 'loginnew.html')


def login(request):
    if request.method == 'POST':
        if request.POST.get('uname') and request.POST.get('pname'):
            uid = request.POST.get('uname')
            up = request.POST.get('pname')
            request.session['sname'] = uid

            # pwd="admin"
            if (Login.objects.filter(userid=uid).exists() and Login.objects.filter(password=up).exists()):
                sample_instance = Login.objects.get(userid=uid)
                value_of_usertype = sample_instance.usertype
                print(value_of_usertype)
                if value_of_usertype == 'medical_officer':
                    return render(request, 'medicalhome.html')
                elif value_of_usertype == 'legal_officer':
                    return render(request, 'LegalOfficer_page.html')
                elif value_of_usertype == 'customs_officer':
                    return render(request, 'customshome.html')
                elif value_of_usertype == 'narcotic_officer':
                    return render(request, 'narcotichome.html')
                elif value_of_usertype == 'socialworker':
                    return render(request, 'social_worker_homepage.html')
                elif value_of_usertype == 'admin':
                    return render(request, 'index.html')
                else:
                    return render(request, 'loginnew.html')
            else:
                return render(request, 'loginnew.html')
    else:
        return render(request, 'loginnew.html')


def signuplegalofficer(request):
    if request.method == 'POST':
        f = request.POST.get('fname')
        request.session['name'] = f

        signup = Legalofficer()
        signup.userid = request.POST.get("uname")
        signup.full_name = request.POST.get("fname")
        signup.professional_summary = request.POST.get("summary")
        signup.core_qualification = request.POST.get("qualification")
        signup.practice = request.POST.get("a")
        signup.experience = request.POST.get("experience")
        signup.save()
        return render(request, "LegalOfficer_page.html")
    else:
        umyname=request.session.get('sname')
        fullname=request.session.get('name')

        return render(request, "signuplegal.html", {"myname": umyname},{"fullname": fullname})


def signupmedical(request):
    if request.method == 'POST':
        f = request.POST.get('fname')
        request.session['name'] = f
        signup = Medicalofficer()
        signup.userid = request.POST.get("uname")
        signup.full_name = request.POST.get("fname")
        signup.professional_summary = request.POST.get("summary")
        signup.core_qualification = request.POST.get("qualification")
        signup.practice = request.POST.get("a")
        signup.experience = request.POST.get("experience")
        signup.save()
        return render(request, "medicalhome.html")
    else:
        umyname = request.session.get('sname')
        fullname = request.session.get('name')

        return render(request, "signupmedical.html",{"myname": umyname},{"fullname": fullname})


def signupcustoms(request):
    if request.method == 'POST':
        signup = Customsofficer()
        signup.userid = request.POST.get("uname")
        signup.full_name = request.POST.get("fname")
        signup.professional_summary = request.POST.get("summary")
        signup.core_qualification = request.POST.get("qualification")
        signup.practice = request.POST.get("a")
        signup.experience = request.POST.get("experience")
        signup.save()
        return render(request, "signup_customsofficer.html")
    else:
        ymyname = request.session.get('sname')
        return render(request, "signup_customsofficer.html",{"myname": ymyname})


def signupsocialworker(request):
    if request.method == 'POST':
        signup = Socialworker()
        signup.userid = request.POST.get("uname")
        signup.full_name = request.POST.get("fname")
        signup.professional_summary = request.POST.get("summary")
        signup.core_qualification = request.POST.get("qualification")
        signup.practice = request.POST.get("a")
        signup.experience = request.POST.get("experience")
        signup.save()
        return render(request, "social_worker_homepage.html")
    else:
        wmyname = request.session.get('sname')
        return render(request, "signup_socialworker.html",{"myname": wmyname})


def signupnarcotic(request):
    if request.method == 'POST':
        signup = Narcoticofficer()
        signup.userid = request.POST.get("uname")
        signup.full_name = request.POST.get("fname")
        signup.professional_summary = request.POST.get("summary")
        signup.core_qualification = request.POST.get("qualification")
        signup.practice = request.POST.get("a")
        signup.experience = request.POST.get("experience")
        signup.save()
        return render(request, "narcotichome.html")
    else:
        zmyname = request.session.get('sname')
        return render(request, "signup_narcotic_section.html",{"myname": zmyname})


def linkpage(request):
    return render(request, 'signuppagee.html')


def forlogin(request):
    return render(request, 'loginnew.html')


def forcontact(request):
    return render(request, 'contact.html')
def infographics(request):
    return render(request, 'infographics_drugs.html')
def commondrugs(request):
    return render(request, 'common_drugs_abuse.html')
def about(request):
    return render(request, 'about.html')
def logout(request):
    return render(request, 'index.html')
def legalinform(request):
    return render(request, 'index.html')


def events(request):
    evt1=Event(name='Fest',event_date='2020-01-28',venue='Kasaragod',manager='Anu',description='Welcome')
    evt1.save()

def event1(request):
    ev1=Event(name='Fashion week',event_date='2020-03-25',venue='Kollam',manager='Treesa',description='Fashion Week')
    ev1.save()

def event2(request):
    ev2=Event(name='Food Fest',event_date='2020-02-25',venue='Ernakulam',manager='Richa',description='Food Week')
    ev2.save()


def remove(request,id=None):
    p=Event.objects.get(id=3)
    p.delete()
    return HttpResponse(p)

def retrive(request):
    ev3=Event.objects.get(id=2)
    ev3.save()

def update(request):
    e1=Event.objects.filter(id=2,name='Fashion week').update(venue='Kerala')
    e1.save()
def ss(request):
    ss1=Event.objects.all()
    return render(request,"abc.html",{"rp":ss1})



