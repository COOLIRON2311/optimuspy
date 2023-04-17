# from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    # class Meta(UserCreationForm.Meta):
    #     labels = {
    #         'username': 'Пользователь',
    #         'password1': 'Пароль',
    #         'password2': 'Повторите пароль',
    #     }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for k, v in self.Meta.labels.items():
    #         self[k].label = v

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for name in ('username', 'password1', 'password2'):
            self.fields[name].help_text = None