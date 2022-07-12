from distutils.command.upload import upload
from django.db import models



class Employee(models.Model):
    GENDER =[
        ('M','M'),
        ('F','F')
    ]
    
    MARITAL = [
        ('Married','Married'),
        ('Single','Single')
    ]
    
    EMPLOYEE_TYPE = [
        ('Permanent','Permanent'),
        ('Contract','Contract')
    ]
    
    employee_id = models.CharField(max_length=15)
    staff_number = models.CharField(max_length=15)
    appointment_start_date = models.DateField()
    tin = models.CharField(max_length=255)
    ssnit = models.CharField(max_length=255)
    dob = models.DateField()
    title = models.CharField(max_length=6)
    surname = models.CharField(max_length=255)
    other_names = models.CharField(max_length=255)
    gender_code = models.CharField(max_length=1, choices=GENDER)
    marital_status = models.CharField(max_length=15, choices=MARITAL)
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=255)
    passport_photo = models.ImageField(upload_to='media/passport-photo/', default="media/passport.jpg")
    employment_date = models.DateField()
    designation = models.CharField(max_length=255, blank=True, null=True)
    job_grade = models.CharField(max_length=255, null=True, blank=True)
    employment_type = models.CharField(max_length=255, choices=EMPLOYEE_TYPE)
    branch = models.CharField(max_length=255)
    hod_name = models.CharField(max_length=255)
    contract_freq_code = models.CharField(max_length=255)
    contract_duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.other_names} {self.surname}  -  {self.staff_number}"
    