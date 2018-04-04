# from django import forms



# class CustomSignupForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         self.sociallogin = kwargs.pop('sociallogin')
#         user = self.sociallogin.account.user
#         first_name = forms.CharField(label=_('First name'),
#                                      max_length=30,
#                                      min_length=2,
#                                      widget=forms.TextInput(attrs={
#                                          'placeholder':_('First name')}))
#         last_name = forms.CharField(label=_('Last name'),
#                                      max_length=30,
#                                      min_length=2,
#                                      widget=forms.TextInput(attrs={
#                                          'placeholder':_('Last name')}))
#         second_last_name = forms.CharField(label=_('Second last name'),
#                                      max_length=30,
#                                      empty='',
#                                      widget=forms.TextInput(attrs={
#                                          'placeholder':_('Second last name')}))
#         # TODO: Should become more generic, not listing
#         # a few fixed properties.
#         initial = {'email': user_email(user) or '',
#                    'username': user_username(user) or '',
#                    'first_name': user_field(user, 'first_name') or '',
#                    'last_name': user_field(user, 'last_name') or ''}
#         kwargs.update({
#             'initial': initial,
#             'email_required': kwargs.get('email_required',
#                                          app_settings.EMAIL_REQUIRED)})
#         super(SignupForm, self).__init__(*args, **kwargs)

#     def save(self, request):
#         adapter = get_adapter()
#         user = adapter.save_user(request, self.sociallogin, form=self)
#         # TODO: Add request?
#         super(SignupForm, self).save(user)
#         return user

#     def raise_duplicate_email_error(self):
#         raise forms.ValidationError(
#             _("An account already exists with this e-mail address."
#               " Please sign in to that account first, then connect"
#               " your %s account.")
#             % self.sociallogin.account.get_provider().name)