from django.http import HttpResponse
from django.shortcuts import render
from .models import Student, Professor

def index(request):
    return render(request,'student/index.html')

def about(request):
    return HttpResponse('<h1>this is student about page</h1>')

def login(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username == "student" and password == "student@123": 
                message = "Login Successful " 
            else: 
                message = "Login Failed "
            print(f"username:{username},password:{password}")
            return HttpResponse('<h1>student login successfull</h1>')
    return render(request,'student/login.html')

def register(request):
    if request.method == 'POST':
        # Student registration
        if 'name' in request.POST and 'usn' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            usn = request.POST.get('usn')
            college = request.POST.get('college')
            degree = request.POST.get('degree')
            branch = request.POST.get('branch')
            semester = request.POST.get('semester')
            content = {
                'name': name,
                'email': email,
                'usn': usn,
                'college': college,
                'degree': degree,
                'branch': branch,
                'semester': semester,
            }
            student = Student(
                name=name,
                email=email,
                usn=usn,
                collage=college,
                degree=degree,
                branch=branch,
                semester=semester
            )
            student.save()
            return render(request, 'student/display.html', content)
        # Professor registration
        elif 'prof_name' in request.POST:
            name = request.POST.get('prof_name')
            email = request.POST.get('prof_email')
            phone = request.POST.get('prof_phone')
            collage = request.POST.get('prof_college')
            department = request.POST.get('prof_department')
            qualification = request.POST.get('prof_qualification')
            content = {
                'name': name,
                'email': email,
                'phone': phone,
                'collage': collage,
                'department': department,
                'qualification': qualification,
            }
            professor = Professor(
                name=name,
                email=email,
                phone=phone,
                collage=collage,
                department=department,
                qualification=qualification
            )
            professor.save()
            return render(request, 'student/professor_display.html', content)
    return render(request, 'student/register.html')