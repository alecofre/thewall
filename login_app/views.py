from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from login_app.models import User
import bcrypt

# Create your views here.
def login_page(request):
     return render(request,'login_app/login_page.html')
     return HttpResponse('llegué a la login_page')

def logout(request):
     request.session.flush()
     return redirect('login_page')


def register(request):
     if request.method == 'GET':
          return redirect('/')
     elif request.method == 'POST':
          errors = User.objects.validator_fields(request.POST)

          if len(errors) > 0 :
               for key,value in errors.items():
                    messages.error(request,value)
               request.session['firstName'] = request.POST['first_name']
               request.session['lastName'] = request.POST['last_name']
               request.session['email'] = request.POST['email']
               request.session['level_message'] = 'alert-danger'


          else:
               request.session['firstName'] = ''
               request.session['lastName'] = ''
               request.session['email'] = ''
               request.session['level_message'] = ''

               first_name = request.POST['first_name']
               last_name = request.POST['last_name']
               email = request.POST['email']
               pw = request.POST['password']

               pw_hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()

               new_user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password = pw_hash)
               new_user.save()
               messages.success(request,'Nuevo usuario registrado!!')
               request.session['level_message'] = 'alert-success'

          return redirect('login_page')

     return HttpResponse('llegué a views.register.FIN')

def login(request):
     if request.method == 'GET':
          return redirect('/')
     elif request.method == 'POST':
          request.session['firstName'] = ''
          request.session['lastName'] = ''
          request.session['email'] = ''
          request.session['level_message'] = ''

          email_login = request.POST['email_login']
          user_eval = User.objects.filter(email = email_login)
          if len ( user_eval ) > 0 :
               user_login = user_eval[0]
               pw = request.POST['password_login']

               if bcrypt.checkpw( pw.encode(), user_login.password.encode() ):
                    user = {
                         'id' : user_login.id,
                         'first_name' : user_login.first_name,
                         'last_name' : user_login.last_name,
                    }

                    request.session['user'] = user
                    request.session['email_login'] = ''
                    return redirect('/wall')

               else:
                    messages.error(request,'Usuario no existe o password errónea')
                    return redirect('login_page')
          else:
               messages.error(request,'Usuario no existe o password errónea')
               return redirect('login_page')
     return redirect('login_page')

