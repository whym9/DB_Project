from django.shortcuts import render, redirect
from django import forms
from medical_service.models import *
from medical_service.forms import *
import json

def countr(request):  
    if request.method == "POST":  
        form = CountryForm(request.POST) 
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/country_view')  
            except:  
                pass  
    else:  
        form = Country()  
    return render(request,'index.html',{"Object":form, "link":"/country", "Name":"Country"}) 
def country_view(request):  
    countries = Country.objects.all()
    names = ['Name', 'Population']
    form = []
    keys = []
    for c in countries:
        keys.append(c.cname)
        x = []
        x.append(c.cname)
        x.append(c.population)
        form.append(x)  
    form_ = zip(form, keys)
    return render(request,"view.html",{'Objects':form_, "Name": "Country", "Names":names, "link": "/country"})  
def country_edit(request, cname):  
    country = Country.objects.get(cname=cname)
    form = dict()
    form['cname'] = country.cname
    form['population'] = country.population
    
    form_ = CountryForm(form, instance=country)
    return render(request,'edit.html', {'Object':form_, 'Name': 'Country', 'link': '/country_update', 'key': cname})  
def country_update(request, cname):  
    country = Country.objects.get(cname=cname)  
    form = CountryForm(request.POST, instance = country) 
    if form.is_valid():  
        form.save()  
        return redirect("/country_view")  
    return render(request, 'edit.html', {'Country': country, 'Name': 'Country', 'link': '/country_update', 'key': cname})  
def country_delete(request, cname): 
    Country_ = Country.objects.get(cname=cname)  
    Country_.delete()  
    return redirect("/country_view")  

def main_view(request):
    return render(request,"main.html")

def diseaseType(request):  
    if request.method == "POST":  
        form = DiseaseTypeForm(request.POST) 
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/diseaseType_view')  
            except:  
                pass  
    else:  
        form = Diseasetype()  
    return render(request,'index.html',{'Object':form, "Name": "Disease Type", "link":"/diseaseType"}) 

def diseaseT_view(request):  
    diseaseT = Diseasetype.objects.all()  
    names = ['ID', 'Description']
    form = []
    keys = []
    for d in diseaseT:
        keys.append(d.id)
        x = []
        x.append(d.id)
        x.append(d.description)
        form.append(x)  
    form = zip(form,keys)
    return render(request,"view.html",{'Objects': form, "Name":"Disease Type", "Names":names, "link":"/diseaseType"})  
def diseaseT_edit(request, id):  
    diseaseT = Diseasetype.objects.get(id=id)  
    form = dict()
    form['id'] = (diseaseT.id)
    form['description'] = diseaseT.description
    
    form_ = DiseaseTypeForm(form, instance=diseaseT)
    return render(request,'edit.html', {'Object':form_, 'Name': 'Disease Type', 'link': '/diseaseType_update', 'key': id})  
def diseaseT_update(request, id):  
    diseaseT = Diseasetype.objects.get(id=id)  
    form = DiseaseTypeForm(request.POST, instance = diseaseT) 
    if form.is_valid():  
        form.save()  
        return redirect("/diseaseType_view")  
    return render(request, 'edit.html', {'Object': form, 'Name': 'Disease Type', 'link': '/diseaseType_update', 'key': id})  
def diseaseT_delete(request, id):  
    diseaseT = Diseasetype.objects.get(id=id)  
    diseaseT.delete()  
    return redirect("/diseaseType_view")  

def disease(request):  
    if request.method == "POST":  
        form = DiseaseForm(request.POST) 
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/disease_view')  
            except:  
                pass  
    else:  
        form = Disease()  
    return render(request,'index.html',{'Object':form, "Name": "Disease Type", "link":"/disease"}) 

def disease_view(request):  
    disease = Disease.objects.all()  
    names = ['Code', 'Pathogen', 'Description', 'ID']
    form = []
    keys = []
    for d in disease:
        keys.append(d.disease_code)
        x = []
        x.append(d.disease_code)
        x.append(d.pathogen)

        x.append(d.description)
        x.append(d.id.id)

        form.append(x)  
    form = zip(form, keys)
    return render(request,"view.html",{'Objects': form, "Name":"Disease", "Names":names, "link":"/disease"})  
def disease_edit(request, code):  
    disease = Disease.objects.get(disease_code=code)  
    form = dict()
    form['disease_code'] = (disease.disease_code)
    form['pathogen'] = (disease.pathogen)
    form['description'] = disease.description
    form['id'] = (disease.id)
    
    form_ = DiseaseForm(form, instance=disease)
    return render(request,'edit.html', {'Object':form_, 'Name': 'Disease', 'link': '/disease_update', 'key': code})  
def disease_update(request, code):  
    disease = Disease.objects.get(disease_code=code)  
    form = DiseaseForm(request.POST, instance = disease) 
    if form.is_valid():  
        form.save()  
        return redirect("/disease_view")  
    return render(request, 'edit.html', {'Object': form, 'Name': 'Disease', 'link': '/disease_update', 'key': code})  
def disease_delete(request, code):  
    disease = Disease.objects.get(disease_code=code)  
    disease.delete()  
    return redirect("/disease_view") 

def discover(request):  
    if request.method == "POST":  
        form = DiscoverForm(request.POST) 
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/discover_view')  
            except:  
                pass  
    else:  
        form = Discover()  
    return render(request,'index.html',{'Object':form, "Name": "Discover", "link":"/discover"}) 

def discover_view(request):  
    discover = Discover.objects.all()  
    names = ['Country', 'Disease', 'First Encounter']
    form = []
    keys = []
    for d in discover:
        
        keys.append(d.cname.cname + ',' + d.disease_code.disease_code)
        x = []
        x.append(d.cname.cname)
        x.append(d.disease_code.disease_code)
        x.append(d.first_enc_date)
        form.append(x)  
    form_ = zip(form, keys)
    return render(request,"view.html",{'Objects': form_, "Name":"Discover", "Names":names, "link":"/discover"})  
def discover_edit(request, cname, code):  
    discover = Discover.objects.get(cname=cname, disease_code=code)  
    form = dict()
    form['cname'] = discover.cname
    form['disease_code'] = (discover.disease_code)
    form['first_enc_date'] = (discover.first_enc_date)
    
    form_ = DiscoverForm(form, instance=discover)
    return render(request,'edit.html', {'Object':form_, 'Name': 'Discover', 'link': '/discover_update', 'key': (cname, code)})  
def discover_update(request, cname, code):  
    discover = Discover.objects.get(cname=cname, disease_code=code)  
    form = DiscoverForm(request.POST, instance = discover) 
    if form.is_valid():  
        form.save()  
        return redirect("/discover_view")  
    return render(request, 'edit.html', {'Object': form, 'Name': 'Discover', 'link': '/discover_update', 'key': (cname, code)})  
def discover_delete(request, cname, code):  
    disease = Discover.objects.get(cname=cname, disease_code=code)  
    disease.delete()  
    return redirect("/discover_view") 

def users(request):  
    if request.method == "POST":  
        form = UsersForm(request.POST) 
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/users_view')  
            except:  
                pass  
    else:  
        form = Users()  
    return render(request,'index.html',{'Object':form, "Name": "Users", "link":"/users"}) 

def users_view(request):  
    users = Users.objects.all()  
    names = ['Email', 'Name', 'Surname', 'Salary', 'Phone', 'Coutry']
    form = []
    keys = []
    for u in users:
        
        keys.append(u.email)
        x = []
        x.append(u.email)
        x.append(u.name)
        x.append(u.surname)
        x.append(u.salary)
        x.append(u.phone)
        x.append(u.cname.cname)
        form.append(x)  
    form = zip(form, keys)
    return render(request,"view.html",{'Objects': form, "Name":"Users", "Names":names, "link":"/users"})  
def users_edit(request, email):  
    users = Users.objects.get(email=email)  
    form = dict()
    form['email'] = users.email
    form['name'] = users.name
    form['surname'] = users.surname
    form['salary'] = users.salary
    form['phone'] = users.phone
    form['cname'] = users.cname.cname
    
    form = UsersForm(form, instance=users)
    return render(request,'edit.html', {'Object':form, 'Name': 'Users', 'link': '/users_update', 'key': email})  
def users_update(request,email):  
    users = Users.objects.get(email=email)  
    form = UsersForm(request.POST, instance = users) 
    if form.is_valid():  
        form.save()  
        return redirect("/users_view")  
    return render(request, 'edit.html', {'Object': form, 'Name': 'Users', 'link': '/users_update'})  
def users_delete(request, email):  
    disease = Users.objects.get(email=email)  
    disease.delete()  
    return redirect("/users_view") 

def public(request):  
    if request.method == "POST":  
        form = PublicForm(request.POST) 
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/public_view')  
            except:  
                pass  
    else:  
        form = Publicservant()  
    return render(request,'index.html',{'Object':form, "Name": "Public Serrvant", "link":"/public"}) 

def public_view(request):  
    public = Publicservant.objects.all()  
    names = ['Email', 'Department']
    form = []
    keys = []
    for p in public:
        
        keys.append(p.email.email)
        x = []
        x.append(p.email.email)
        x.append(p.department)
        form.append(x)  
    form = zip(form, keys)
    return render(request,"view.html",{'Objects': form, "Name":"Public Servant", "Names":names, "link":"/public"})  
def public_edit(request, email):  
    public = Publicservant.objects.get(email=email)  
    form = dict()
    form['email'] = public.email.email
    form['name'] = public.department
    
    
    form = PublicForm(form, instance=public)
    return render(request,'edit.html', {'Object':form, 'Name': 'Public Servant', 'link': '/public_update', 'key': email})  
def public_update(request,email):  
    public = Publicservant.objects.get(email=email)  
    form = PublicForm(request.POST, instance = public) 
    if form.is_valid():  
        form.save()  
        return redirect("/public_view")  
    return render(request, 'edit.html', {'Object': form, 'Name': 'Public Servant', 'link': '/public_update'})  
def public_delete(request, email):  
    disease = Publicservant.objects.get(email=email)  
    disease.delete()  
    return redirect("/public_view")


def doctor(request):  
    if request.method == "POST":  
        form = DoctorForm(request.POST) 
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/doctor_view')  
            except:  
                pass  
    else:  
        form = Doctor()  
    return render(request,'index.html',{'Object':form, "Name": "Doctor", "link":"/doctor"}) 

def doctor_view(request):  
    doctor = Doctor.objects.all()  
    names = ['Email', 'Degree']
    form = []
    keys = []
    for d in doctor:
        
        keys.append(d.email.email)
        x = []
        x.append(d.email.email)
        x.append(d.degree)
        form.append(x)  
    form = zip(form, keys)
    return render(request,"view.html",{'Objects': form, "Name":"Doctor", "Names":names, "link":"/doctor"})  
def doctor_edit(request, email):  
    doctor = Doctor.objects.get(email=email)  
    form = dict()
    form['email'] = doctor.email.email
    form['degrree'] = doctor.degree
    
    
    form = DoctorForm(form, instance=doctor)
    return render(request,'edit.html', {'Object':form, 'Name': 'Doctor', 'link': '/doctor_update', 'key': email})  
def doctor_update(request,email):  
    doctor = Doctor.objects.get(email=email)  
    form = DoctorForm(request.POST, instance = doctor) 
    if form.is_valid():  
        form.save()  
        return redirect("/doctor_view")  
    return render(request, 'edit.html', {'Object': form, 'Name': 'Doctor', 'link': '/doctor_update'})  
def doctor_delete(request, email):  
    doctor = Doctor.objects.get(email=email)  
    doctor.delete()  
    return redirect("/doctor_view")

def spec(request):  
    if request.method == "POST":  
        form = SpecForm(request.POST) 
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/spec_view')  
            except:  
                pass  
    else:  
        form = Specialize()  
    return render(request,'index.html',{'Object':form, "Name": "Specialize", "link":"/spec"}) 

def spec_view(request):  
    spec = Specialize.objects.all()  
    names = ['ID', 'Email']
    form = []
    keys = []
    for s in spec:
        keys.append(str(s.id.id) + ',' + s.email.email.email)
        x = [] 
        x.append(s.id.id)
        x.append(s.email.email.email)
        form.append(x)  
    form = zip(form, keys)
    return render(request,"view.html",{'Objects': form, "Name":"Specialize", "Names":names, "link":"/spec"})  
def spec_edit(request, id, email):  
    spec = Specialize.objects.get(id=id, email=email)  
    form = dict()
    
    key = str(spec.id.id) + ',' + spec.email.email.email
    form['id'] = spec.id.id
    form['email'] = spec.email.email.email
    
    
    
    form = SpecForm(form, instance=spec)
    return render(request,'edit.html', {'Object':form, 'Name': 'Specialize', 'link': '/spec_update', 'key': key})  
def spec_update(request,id, email):  
    spec = Specialize.objects.get(id=id, email=email)  
    form = SpecForm(request.POST, instance = spec) 
    if form.is_valid():  
        form.save()  
        return redirect("/spec_view")  
    return render(request, 'edit.html', {'Object': form, 'Name': 'Specialize', 'link': '/spec_update'})  
def spec_delete(request, id, email):  
    spec = Specialize.objects.get(id=id, email=email)  
    spec.delete()  
    return redirect("/spec_view")

def record(request):  
    if request.method == "POST":  
        form = RecordForm(request.POST) 
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/record_view')  
            except:  
                pass  
    else:  
        form = Record()  
    return render(request,'index.html',{'Object':form, "Name": "Record", "link":"/record"}) 

def record_view(request):  
    rec = Record.objects.all()  
    names = ['Email', 'Country', "Disease", "Total Deaths", "Total Patients"]
    form = []
    keys = []
    for r in rec:
        keys.append(r.email.email.email + ',' + r.cname.cname + "," + r.disease_code.disease_code)
        x = [] 
        x.append(r.email.email.email)
        x.append(r.cname.cname)
        x.append(r.disease_code.disease_code)
        x.append(r.total_deaths)
        x.append(r.total_patients)

        form.append(x)  
    form = zip(form, keys)
    return render(request,"view.html",{'Objects': form, "Name":"Record", "Names":names, "link":"/record"})  
def record_edit(request, email, cname, code):  
    rec = Record.objects.get(email=email, cname=cname, disease_code=code)  
    form = dict()
    
    key = rec.email.email.email + "," + rec.cname.cname + "," + rec.disease_code.disease_code

    form['email'] = rec.email.email.email
    form['cname'] = rec.cname.cname
    form['disease_code'] = rec.disease_code.disease_code
    form['email'] = rec.total_deaths
    form['email'] = rec.total_patients
    form = RecordForm(form, instance=rec)
    return render(request,'edit.html', {'Object':form, 'Name': 'Record', 'link': '/record_update', 'key': key})  
def record_update(request, email, cname, code):  
    rec = Record.objects.get(email=email, cname=cname, disease_code=code)  
    form = RecordForm(request.POST, instance = rec) 
    if form.is_valid():  
        form.save()  
        return redirect("/record_view")  
    return render(request, 'edit.html', {'Object': form, 'Name': 'Record', 'link': '/record_update'})  
def record_delete(request, email, cname, code):  
    rec = Record.objects.get(email=email, cname=cname, disease_code=code)  
    rec.delete()  
    return redirect("/record_view")