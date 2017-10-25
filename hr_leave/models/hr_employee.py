from openerp import models, fields, api, _

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    employee_num = fields.Char(string='Employee Number')

    _sql_constraints = [
        ('unique_emp_num', 'UNIQUE(employee_num)', _("Employee number must be unique.")),
    ]