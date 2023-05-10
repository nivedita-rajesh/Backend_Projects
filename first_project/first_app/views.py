from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponserRedirect
from first_app.models import Program, Student
from .forms import StudentForm  


# 'request' name is convention. It can be some other name too.
def index(request) :  
  #clicked+=1  
  program_values = Program.objects.all()
  student_values = Student.objects.all()
  my_dict = { 'program_rows' : program_values,
              'student_rows' : student_values,
  
  }
  return render(request,'index.html',context=my_dict)
# Create your views here.

def get_student(request):    
  if request.method == 'POST':          
    form = StudentForm(request.POST)     
    if form.is_valid():
        s_name = form.cleaned_data['name']
        s_roll = form.cleaned_data['roll']
        s_degree = form.cleaned_data['degree']        
        s_branch = form.cleaned_data['branch']
 
        print(s_name,s_roll,s_degree,s_branch)
        
    return HttpResponseRedirect('/student/')
  else: 
      form =StudentForm()
      return render(request, 'StudentForm.html', {'form': form})