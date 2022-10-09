from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

class ProfilesConfig(AppConfig):
    name = 'profiles'

    def ready(self):
        import users.signals
