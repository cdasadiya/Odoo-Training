from openerp import models, fields, api
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT
from openerp.exceptions import ValidationError
from datetime import datetime

class Leave(models.Model):
    _name = 'mymodule.leave'
    _description = 'Leaves Request'

    name = fields.Char(string='Sequence')
    date = fields.Date(string='Request Date', default=fields.Date.today())
    employee_id = fields.Many2one('hr.employee', string='Employee')
    title = fields.Char(string='Title')
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    duration = fields.Integer(string='Duration', compute='_compute_duration')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('hrm', 'HRM'),
        ('done', 'Done'),
    ], string='Status', default='draft')

    _sql_constraints = [
        ('unique_name', 'CHECK(1=1)', 'Name is duplicate')
    ]

    @api.model
    def create(self, vals):
        vals['name'] = 'ABC'
        return super(Leave, self).create(vals)

    @api.multi
    def write(self, vals):
        vals['name'] = 'XYZ'
        return super(Leave, self).write(vals)

    @api.multi
    def unlink(self):
        pass

    @api.onchange('employee_id')
    def onchange_title(self):
        if self.employee_id:
            self.title = 'Mr. %s' % self.employee_id.name

    @api.depends('date_from', 'date_to')
    def _compute_duration(self):
        for rec in self:
            if rec.date_from and rec.date_to:
                df = datetime.strptime(rec.date_from, DEFAULT_SERVER_DATE_FORMAT)
                dt = datetime.strptime(rec.date_to, DEFAULT_SERVER_DATE_FORMAT)
                diff = (dt - df).days + 1
                rec.duration = 0 if diff <= 0 else diff

    @api.constrains('date_from', 'date_to')
    def check_dates(self):
        if self.date_from > self.date_to:
            raise ValidationError("Invalid Dates")
        elif self.duration == 1:
            raise ValidationError('Duration is One')

