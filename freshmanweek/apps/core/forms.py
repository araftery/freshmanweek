from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div
from crispy_forms.layout import HTML
from crispy_forms.layout import Field
from crispy_forms.layout import Fieldset
from crispy_forms.layout import Layout
from crispy_forms.layout import MultiField
from crispy_forms.layout import Submit

from core.models import Auditioner


class AuditionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AuditionForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = ''
        self.helper.form_id = 'audition-form'
        self.helper.form_name = 'audition-form'
        self.helper.label_class = 'control-label'
        self.helper.html5_required = True

        self.fields['description'].label = '(Very) brief description of act'

        self.helper.layout = Layout(
            Div(
                Div(
                    Field('first_name', css_class="form-control"),
                    css_class="form-group"
                ),
                Div(
                    Field('last_name', css_class="form-control"),
                    css_class="form-group"
                ),
                css_class="col-md-6"
            ),
            Div(
                Div(
                    Field('email', css_class="form-control"),
                    css_class="form-group"
                ),
                Div(
                    Field('phone', css_class="form-control"),
                    css_class="form-group"
                ),
                css_class="col-md-6"
            ),
            Div(
                Div(
                    Field('description', css_class="form-control"),
                    css_class="form-group"
                ),
                css_class="col-md-12"
            ),
            Div(
                Submit('submit', 'Submit', css_class="btn bg-red col-md-1 block"),
            ),
        )

    class Meta:
        model = Auditioner
