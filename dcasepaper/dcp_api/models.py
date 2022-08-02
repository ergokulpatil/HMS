from django.db import models

# Create your models here.


class PatientProfile(models.Model):
    P_name=models.CharField(max_length=64)
    P_DOB=models.DateField()
    P_Address=models.CharField(max_length=128)
    P_Email=models.EmailField()
    P_Mobile=models.CharField(max_length=12)
    P_Religion=models.CharField(max_length=64)
    P_Gender=models.CharField(max_length=64)
    P_Family=models.CharField(max_length=64)
    P_MaritalStatus=models.CharField(max_length=64)
    P_Anniversary=models.DateField()


class DoctorProfile(models.Model):
   D_name=models.CharField(max_length=64)
   D_DOB=models.DateField()
   D_Address=models.CharField(max_length=128)
   D_email=models.EmailField()
   D_mobile=models.CharField(max_length=12)
   D_Anniversary=models.DateField()


class DoctorClinic(models.Model):
    Doctor=models.ForeignKey(DoctorProfile,on_delete=models.CASCADE)
    C_Name=models.CharField(max_length=64)
    C_address=models.CharField(max_length=128)
    C_PhoneNumber=models.CharField(max_length=12)
    C_GoogleUrl=models.CharField(max_length=64)
    C_OpenTime=models.DateField()
    C_Closing=models.DateField()


class PatientMedicalProfile(models.Model):
    Patient=models.ForeignKey(PatientProfile,on_delete=models.CASCADE)
    P_Habbit=models.CharField(max_length=64)
    P_LevelOfHygins=models.CharField(max_length=128)
    P_CosmeticConcern=models.CharField(max_length=128)
    P_MedicalHistory=models.CharField(max_length=1024)


class Complaints(models.Model):
    Patient=models.ForeignKey(PatientProfile,on_delete=models.CASCADE)
    Doctor=models.ForeignKey(DoctorProfile,on_delete=models.CASCADE)
    C_TimeStamp=models.DateTimeField()
    C_ComplaintDetails=models.CharField(max_length=128)


class DoctorSpecialization(models.Model):
    Doctor=models.ForeignKey(DoctorProfile,on_delete=models.CASCADE)
    Treatement_Name=models.CharField(max_length=128)
    Treatment_Amount=models.IntegerField()


class Visits(models.Model):
    Patient=models.ForeignKey(PatientProfile,on_delete=models.CASCADE)
    Doctor=models.ForeignKey(DoctorProfile,on_delete=models.CASCADE)
    Complaint=models.ForeignKey(Complaints,on_delete=models.CASCADE)
    Treatement= models.ForeignKey(DoctorSpecialization,on_delete=models.CASCADE)
    Visit_Time_Stamp=models.CharField(max_length=64)
    Details=models.CharField(max_length=128)
    Advice=models.CharField(max_length=1028)
    Is_Visited=models.BooleanField(default=False)
    Visit_Type=models.CharField(max_length=64)


class WorkDoneLog(models.Model):
    Patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    Doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    Complaint = models.ForeignKey(Complaints, on_delete=models.CASCADE)
    Visits = models.ForeignKey(Visits, on_delete=models.CASCADE)
    Treatment = models.ForeignKey(DoctorSpecialization, on_delete=models.CASCADE)
    WorkDone_Time_Stamp = models.DateField()


class Prescription(models.Model):
    Patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    Visit=models.ForeignKey(Visits,on_delete=models.CASCADE)
    DrugName=models.CharField(max_length=128)
    Duration=models.CharField(max_length=64)
    Dose=models.CharField(max_length=64)
