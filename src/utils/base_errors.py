from django.utils.translation import gettext as _


class BaseErrors:

    @classmethod
    def _change_error_variable(cls, error_name, **kwargs):
        message = getattr(cls, error_name)
        for key, value in kwargs.items():
            message = message.replace('{%s}' % key, value)
        return message

    # project
    url_not_found = _('URL Not Found.')
    server_error = _('Server Error.')

    # user sign up, login, forget pass, change pass
    user_must_have_mobile_number = _('User Must Have Mobile Number.')
    user_must_have_email = _('User Must Have Email Address.')
    there_is_a_user_with_this_email = _('There is a user with this email')
    invalid_mobile_number_format = _('Invalid Mobile Number Format')
    user_must_have_password = _('User Must Have Password.')
    invalid_mobile_number_or_password = _('Invalid Mobile Number or Password.')
    user_account_with_mobile_number_exists = _('User Account With Mobile Number Exists.')
    passwords_did_not_match = _('Password And Repeat Password Did Not Match.')
    user_not_found = _('User Not Found')
    user_account_not_active = _('User Account Not Active.')
    user_account_is_active = _('User Account Is Active.')
    user_dont_have_forget_password_permission = _('You Do Not Have Access To Change The Password, Please Try Again First Step.')
    old_password_is_incorrect = _('Old Password Is Incorrect')

    # global
    parameter_is_required = _('parameter {param_name} is required')
    object_not_found = _('{object} Not Found')
