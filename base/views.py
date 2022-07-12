from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateEmployeeForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import Employee
import openpyxl



@login_required(login_url='/login')
def home(request):
    employees = Employee.objects.all()
    
    context = {
        "employees":employees
    }
    return render(request, 'base/index.html', context)



def mylogin(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect('home')
        else:
            messages.error(request, "Username or Password is incorrect")
            return redirect(request.META['HTTP_REFERER'])
    return render(request, 'base/login.html')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect(request.META['HTTP_REFERER'])
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exist")
            return redirect(request.META['HTTP_REFERER'])
        else:
            user = User.objects.create(
                username=username,
            )
            user.set_password(password1)
            user.save()
            messages.success(request, "Your account has been created")
            return redirect('login')
    else:
        return render(request, 'base/signup.html')
    
@login_required
def log_out(request):
    logout(request)
    return redirect('login')

@login_required
def create_employee(request):
    if request.method == "POST":
        form = CreateEmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee has been saved")
            return redirect('home')
        else:
            print(form.errors)
            messages.error(request, "Sorry something went wrong")
            return redirect(request.META['HTTP_REFERER']) 
    form = CreateEmployeeForm()
    return render(request, 'base/create_employee.html', {'form':form})

@login_required
def update_employee(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == "POST":
        form = CreateEmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee has been updated")
            return redirect('home')
        else:
            print(form.errors)
            messages.error(request, "Sorry something went wrong")
            return redirect(request.META['HTTP_REFERER']) 
    form = CreateEmployeeForm(instance=employee)
    return render(request, 'base/update_employee.html', {'form':form})


@login_required
def import_data(request):
    if request.method == "POST":
        file = request.FILES.get('file', None)
        if file is not None:
            extension = file.name.split('.')[1]
            if extension == 'xls' or extension =='xlsx':
                row_data = []
                wb = openpyxl.load_workbook(file)
                worksheet = wb["Sheet1"]
                row_no = 1
                try:
                    for row in worksheet.iter_rows():
                        if row_no > 1:
                            row_data.append(Employee(
                                employee_id = row[0].value,
                                staff_number = row[1].value,
                                appointment_start_date = row[2].value,
                                tin = row[3].value,
                                ssnit = row[4].value,
                                dob = row[5].value,
                                title = row[6].value,
                                surname = row[7].value,
                                other_names = row[8].value,
                                gender_code = row[9].value,
                                marital_status = row[10].value,
                                phone = row[11].value,
                                address = row[12].value,
                                employment_date = row[13].value,
                                designation = row[14].value,
                                job_grade = row[15].value,
                                employment_type = row[16].value,
                                branch = row[17].value,
                                hod_name = row[18].value,
                                contract_freq_code = row[19].value,
                                contract_duration = row[20].value
                            ))
                        row_no += 1
                        
                    Employee.objects.bulk_create(row_data)
                    messages.success(request,"Uploaded successfully")
                except Exception as e:
                    print(e)
                    messages.error(request,"Sorry something went wrong")
                                    
            else:
                messages.error(request, "Upload an excel file")
        return redirect(request.META['HTTP_REFERER'])