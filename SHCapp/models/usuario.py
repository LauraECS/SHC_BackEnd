from django.db import models
from .tipoUsuario import Tipo_Usuario
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField('nombre', max_length = 100, null=True)
    apellidos = models.CharField('apellidos', max_length = 100, null=True)
    documento = models.CharField('documento', max_length = 100, null=True)
    direccion = models.CharField('direccion', max_length = 100, null=True)
    telefono = models.CharField('telefono', max_length = 100, null=True)
    genero = models.CharField('genero', max_length = 100, null=True)
    fecha_nacimiento = models.CharField('fecha_nacimiento', max_length = 100, null=True)
    contrasena = models.CharField('contraseña', max_length = 256, null=True)
    correo = models.EmailField('email', max_length = 254, unique= True, null=True)
    password = models.CharField('password', max_length = 128, null=True)
    username = models.CharField('username', max_length= 150, null=True)
    fecha_registro = models.CharField('fecha_registro', max_length = 100, null=True)
    id_tipo_usuario = models.ForeignKey(Tipo_Usuario, related_name="User", on_delete=models.CASCADE, null=False, default=2)

    def save(self, kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'correo'

    def __str__(self) -> str:
        return self.name