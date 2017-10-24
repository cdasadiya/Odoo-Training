from openerp import models, fields, api, _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT
from openerp.exceptions import ValidationError
from datetime import datetime


class Leave(models.Model):
    _name = 'hr.leave'
    _description = 'Leave Request'

    name = fields.Char(string='Sequence')
    date = fields.Date(string='Request Date', default=fields.Date.today())
    employee_id = fields.Many2one('hr.employee', string='Employee')
    department_id = fields.Many2one('hr.department', string='Department',
                                    related='employee_id.department_id')
    leave_type_id = fields.Many2one('hr.leave.type', string='Leave Type')
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    duration = fields.Integer(string='Duration', compute='_compute_duration')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('hr', 'HR'),
        ('done', 'Done'),
        ('refuse', 'Refuse'),
    ], string='Status', default='draft')

    @api.model
    def create(self, vals):
        res = super(Leave, self).create(vals)
        res.name = self.env['ir.sequence'].get('hr.leave.seq')
        return res

    @api.depends('date_from', 'date_to')
    def _compute_duration(self):
        for rec in self:
            if rec.date_from and rec.date_to:
                df = datetime.strptime(rec.date_from, DEFAULT_SERVER_DATE_FORMAT)
                dt = datetime.strptime(rec.date_to, DEFAULT_SERVER_DATE_FORMAT)
                diff = (dt - df).days + 1
                rec.duration = diff

    @api.constrains('date_from', 'date_to')
    def check_dates(self):
        for rec in self:
            if rec.date_from and rec.date_to:
                if rec.date_from > rec.date_to:
                    raise ValidationError(_("'Date To' must be greater than or equal to 'Date From'"))
