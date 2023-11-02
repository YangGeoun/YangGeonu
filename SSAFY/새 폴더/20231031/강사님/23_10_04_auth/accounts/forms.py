from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# accounts/forms.py
# 장고가 제공하는 UserCreationForm, UserUpdateForm을
# 그대로 사용못하니까... 상속받아서 변경해서 사용할 예정
# UserCreationForm, UserUpdateForm 은 auth.User 모델을 사용 하는데
# 우리는 우리가 만든 accounts.User를 인증 모델로 사용할 거기 때문에
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name','last_name','email',)
