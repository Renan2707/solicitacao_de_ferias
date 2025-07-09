from rolepermissions.roles import AbstractUserRole

class RH(AbstractUserRole):
    available_permissions = {
        'view_dashboard': True,
        'manage_requests': True,
        'view_reports': True,
        'approve_requests': True,
        'reject_requests': True,
    }