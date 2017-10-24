from openerp import models, fields, api, _


class LeaveType(models.Model):
    _name = 'hr.leave.type'
    _description = "Leave Type"

    name = fields.Char(string='Name')
