from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
     def  validator_fields(self, postData):
          JUST_LETTERS = re.compile(r'^[a-zA-Z.]+$')
          PASSWORD_REGEX = re.compile(r'^(?=\w*[a-zA-Z.])\S{8,16}$')
          # PASSWORD_REGEX = re.compile(r'^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$')
          EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
 
          errors = {}
 
          if len(User.objects.filter(email = postData['email'])) > 0 :
              errors['email_exists'] = 'email ya registrado'
          else:
               if ( len(postData['first_name'].strip()) < 2 ):
                   errors['fname_len'] = 'Nombre debe tener al menos 2 caracteres'

               if ( len(postData['last_name'].strip()) < 2 ):
                   errors['lname_len'] = 'Apellido debe tener al menos 2 caracteres'
  
               if not EMAIL_REGEX.match(postData['email']):
                   errors['bad_email'] = 'Formato de correo no válido'
  
               if ( len(postData['password'].strip()) < 8 ):
                   errors['password_len'] = 'Password debe tener al menos 8 caracteres sin espacios'
  
               if not PASSWORD_REGEX.match(postData['password']):
                   errors['bad_pw'] = "Formato de contraseña no válido. "
  
               if postData['password'] != postData['password_confirm']:
                   errors['nosame_pw'] = 'Contraseñas no coinciden'
 
          return errors



class User(models.Model):
     first_name = models.CharField(max_length=255)
     last_name = models.CharField(max_length=255)
     email = models.CharField(max_length=255)
     password = models.CharField(max_length=255)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     objects = UserManager()

     def __str__(self) -> str:
         return f'{self.first_name} {self.last_name}'

     def __repr__(self) -> str:
         return f'{self.first_name} {self.last_name}'
