# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = User
#
#         fields = [
#             'last_name',
#             'first_name',
#             'email'
#         ]
#
#         widgets = {
#             'last_name': widgets.TextInput(attrs={'class': 'form-control'}),
#             'first_name': widgets.TextInput(attrs={'class': 'form-control'}),
#             'email': widgets.TextInput(attrs={'class': 'form-control'})
#         }
#
#
# class CustomCitiesChangeForm(CitesChangeForm):
#     class Meta:
#         model = Cites
#
#         fields = [
#             '',
#             '',
#             ''
#         ]

# Custom change user form, cites, addresses
# Skoða hvað er hægt að nota í properties forms og user forms
# Solla ætlaði eitthvað að breyta þeim þannig spjalla við þau með þetta