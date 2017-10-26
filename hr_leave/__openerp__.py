{
    'name': "Leaves",
    'version': '0.1',
    'website': 'http://www.slnee.com',
    'depends': [
        'hr',
    ],
    'author': "Mohamed Hammad",
    'category': 'Human Resources',
    'description': """
Employee can request for a leave.
    """,
    'data': [
        'sequences/hr_leave_seq.xml',
        'views/hr_leave_view.xml',
        'views/hr_leave_type_view.xml',
        'views/hr_employee_view.xml',
        'wizards/views/hr_leave_wizard_view.xml',
    ],
    'application': True,
}
