from django import forms
from .models import MeetingReservation
from django.contrib.auth import get_user_model


User = get_user_model()


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class MeetingReservationForm(forms.ModelForm):
    def __init__(self, current_user, *args, **kwargs):
        super(MeetingReservationForm, self).__init__(*args, **kwargs)
        self.fields['hr_representative'].queryset = User.objects.filter(username=current_user)

    class Meta:
        model = MeetingReservation
        fields = ('user', 'hr_representative', 'start_time', 'end_time', 'parties')
        widgets = {
            'start_time': DateTimeInput(),
            'end_time': DateTimeInput(),
        }