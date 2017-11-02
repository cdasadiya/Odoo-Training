from openerp import models, fields, api, _

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    employee_num = fields.Char(string='Employee Number')
    leave_history_ids = fields.One2many('hr.leave.history', 'employee_id',
                                       string='Leave History')
    counter = fields.Integer(string='Counter')

    _sql_constraints = [
        ('unique_emp_num', 'UNIQUE(employee_num)', _("Employee number must be unique.")),
    ]

    @api.model
    def increase_counter(self, x):
        for rec in self.search([]):
            rec.counter += x


class HrLeaveHistory(models.Model):
    _name = 'hr.leave.history'
    _description = 'Employee Leave History'

    name = fields.Char(string='Sequence')
    leave_type_id = fields.Many2one('hr.leave.type', string='Leave Type')
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    employee_id = fields.Many2one('hr.employee', string='Employee Ref.', ondelete='cascade')