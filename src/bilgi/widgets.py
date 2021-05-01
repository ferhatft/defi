from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Kaldır')
    initial_text = _('Şuanki Resim')
    input_text = _('')
    template_name = 'custom_widget_templates/custom_clearable_file_input.html'