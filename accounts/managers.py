from django.contrib.auth.models import BaseUserManager



class UserManager(BaseUserManager):
    def create_user(self, username, email, password):
        if not username:
            raise ValueError('The username must be set')
        if not email:
            raise ValueError('The email must be set')
        if not password:
            raise ValueError('The password must be set')
        
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

