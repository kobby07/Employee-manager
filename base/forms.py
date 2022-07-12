from random import choices
from django  import forms
from .models import Employee

TITLE_CHOICES = [
    ('Mr','Mr'),
    ('Mrs','Mrs'),
    ('Ms','Ms'),
    ('Dr','Dr'),
]

GENDER = [
    ('M','Male'),
    ('F','Female'),
]

MARITAL = [
    ('Single','Single'),
    ('Married','Married'),
]

EMPLOYEE_TYPE = [
    ('Permanent','Permanent'),
    ('Contract','Contract')
]

class CreateEmployeeForm(forms.ModelForm):
    employee_id = forms.CharField(max_length=15, label="Employee ID")
    staff_number = forms.CharField(max_length=15, label='Staff Number')
    appointment_start_date = forms.DateField(label="Appointment Start Date", widget=forms.DateInput, help_text="2006-07-20")
    tin = forms.CharField(max_length=255, label="Tin Number")
    ssnit = forms.CharField(max_length=255, label="SSNIT Number")
    dob = forms.DateField(widget=forms.DateInput, label="Date Of Birth", help_text="2006-07-20")
    title = forms.ChoiceField(label="Title", choices=TITLE_CHOICES)
    other_names = forms.CharField(max_length=255, label="Other Names")
    gender_code = forms.ChoiceField(label="Gender", choices=GENDER)
    marital_status = forms.ChoiceField(label="Marital Status", choices=MARITAL)
    passport_photo = forms.ImageField(label="Passport Photo")
    employment_date = forms.DateField(label="Employment Date", widget=forms.DateInput, help_text="2006-07-20")
    job_grade = forms.CharField(max_length=255, label='Job Grade', required=False)
    employment_type = forms.ChoiceField(label="Employment Type", choices=EMPLOYEE_TYPE)
    hod_name = forms.CharField(max_length=255, label="HOD Name")
    contract_freq_code = forms.CharField(max_length=255, required=False, label="Contract Frequency")
    contract_duration = forms.IntegerField(label="Contract Duration", help_text="Enter in number of months")
    

    
    
    class Meta:
        model=Employee
        fields="__all__"
        
        

