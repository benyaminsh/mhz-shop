from django.utils.translation import gettext as _

# class RedisKeys:
#     activate_account = "activate_account"
#     forget_password = "forget_password"
#
#


user_work_type_options = (
    ('clerk', _('clerk')),
    ('driver', _('driver')),
    ('student', _('student')),
    ('corporate', _('corporate')),
    ('freelancer', _('freelancer')),
    ('customer', _('customer')),
)

user_vehicle_options = (
    ('car', _('car')),
    ('motor', _('motorCycle')),
    ('bike', _('bike')),
)

porter_status_option = (
    ('comp', _('complate')),
    ('waitt', _('WattingForConfirmation')),
    ('cancel', _('canceled')),
)

position_option = (
    ('index', _('index')),
    ('our_service', _('Our Service')),
    ('prices_costs', _('Prices And Costs')),
)

language_option = (
    ('en', _('English')),
    ('de', _('Germany')),
)

option_position_option = (
    ('footer', _('Footer')),
    ('email', _('Email')),
    ('phone', _('Phone Number')),
    ('instagram', _('Instagram')),
    ('twitter', _('Twitter')),
    ('facebook', _('Facebook')),
    ('linkedin', _('Linkedin')),
    ('moving_service', _('Moving Service')),
    ('kitchen_service', _('Kitchen Service')),
)

kitchen_installation_requests_request_status = (
    ('NotConfirmed', _('NotConfirmed')),
    ('AwaitingReview', _('AwaitingReview')),
    ('Accepted', _('Accepted')),
)

furniture_assembly_requests_request_status = (
    ('NotConfirmed', _('NotConfirmed')),
    ('AwaitingReview', _('AwaitingReview')),
    ('Accepted', _('Accepted')),
)

furniture_assembly_requests_assembly_service = (
    ('WithDisassemblyAndAssembly', _('WithDisassemblyAndAssembly')),
    ('DisassemblyOnly', _('DisassemblyOnly')),
    ('AssemblyOnly', _('AssemblyOnly')),
    ('WithoutDisassemblyAndAssembly', _('WithoutDisassemblyAndAssembly')),
)

furniture_assembly_requests_private_or_company = (
    ('private', _('Private')),
    ('company', _('Company')),
)

visit_requests_request_status = (
    ('NotConfirmed', _('NotConfirmed')),
    ('AwaitingReview', _('AwaitingReview')),
    ('Accepted', _('Accepted')),
)

type_of_visit_options = (
    ('Online', _('Online')),
    ('InPerson', _('InPerson')),
)

kitchen_installation_requests_assembly_service = (
    ('WithDisassemblyAndAssembly', _('WithDisassemblyAndAssembly')),
    ('DisassemblyOnly', _('DisassemblyOnly')),
    ('AssemblyOnly', _('AssemblyOnly')),
    ('WithoutDisassemblyAndAssembly', _('WithoutDisassemblyAndAssembly')),
)

kitchen_installation_requests_private_or_company = (
    ('private', _('Private')),
    ('company', _('Company')),
)

freight_requests_private_or_company = (
    ('private', _('Private')),
    ('company', _('Company')),
)

site_options_email_messages_section = (
    # Furniture Assembly
    ('FurnitureAssemblyRequestsForUser',_('FurnitureAssemblyRequestsForUser')),
    ('FurnitureAssemblyRequestsForAdmin',_('FurnitureAssemblyRequestsForAdmin')),
    # Kitchen Installation
    ('KitchenInstallationRequestsForAdmin', _('KitchenInstallationRequestsForAdmin')),
    ('KitchenInstallationRequestsForUser', _('KitchenInstallationRequestsForUser')),
    # Freight
    ('FreightRequestsForUser', _('FreightRequestsForUser')),
    ('FreightRequestsForAdmin', _('FreightRequestsForAdmin')),
    # Freight Landing
    ('FreightLandingPageRequestsForUser', _('FreightLandingPageRequestsForUser')),
    ('FreightLandingPageRequestsForAdmin', _('FreightLandingPageRequestsForAdmin')),
    # Visit
    ('VisitRequestsForUser', _('VisitRequestsForUser')),
    ('VisitRequestsForAdmin', _('VisitRequestsForAdmin')),
    # Apply
    ('UserApplyForAdmin', _('UserApplyForAdmin')),
    ('UserReject', _('UserReject')),
    # ResetPassword
    ('UserResetPasswordSendCode', _('UserResetPasswordSendCode')),
    # Authentication
    ('UserAuthenticationSendCode', _('UserAuthenticationSendCode')),
)

freight_requests_request_status = (
    ('NotConfirmed', _('NotConfirmed')),
    ('AwaitingReview', _('AwaitingReview')),
    ('Accepted', _('Accepted')),
)


freight_landing_page_family_members = (
    ('one', _('one')),
    ('two', _('two')),
    ('three', _('three')),
    ('more', _('more')),
)
