from login_app.models import User
from thewall_app.models import Comment, Message
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages

# Create your views here.
def wall(request):
     msg = Message.objects.all().order_by('-created_at')
     cmm = Comment.objects.all().order_by('-created_at')
     mmm = [1,2,3]
     context = {
          'msg' : msg,
          'cmm' : cmm,
     }
     return render(request,'thewall_app/wall.html', context)
     return HttpResponse('Llegué al home de the WALL')

def new_message(request):
     if request.method == 'GET':
          return redirect("/wall")
     elif request.method == 'POST':
          error = Message.objects.verify_newMessage(request.POST)

          if len(error) > 0:
               for key,value in error.items():
                    messages.error(request,value)
               request.session['level_message'] = 'alert-danger'
               return redirect("/wall")
          else:
               user = User.objects.get(id = request.POST['user_id'])
               message = request.POST['new_message']
               new_msg = Message.objects.create(user = user, message = message)
               new_msg.save()
               return redirect("/wall")

     return redirect("/wall")
     return HttpResponse('Llegué a la rutina del new_message')

def new_comment(request):
     if request.method == 'GET':
          return redirect("/wall")
     elif request.method == 'POST':
          error = Comment.objects.verify_newComment(request.POST)

          if len(error) > 0:
               for key,value in error.items():
                    messages.error(request,value)
               request.session['level_message'] = 'alert-danger'
               return redirect("/wall")
          else:
               user = User.objects.get(id = request.POST['user_id'])
               message = Message.objects.get(id = request.POST['message_id'])
               comment = request.POST['new_comment']
               new_cmm = Comment.objects.create(user = user, message=message, comment= comment)
               new_cmm.save()
               return redirect("/wall")
     return redirect("/wall")
     return HttpResponse('Llegué a la rutina del new_comment')