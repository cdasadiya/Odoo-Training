from openerp import models, fields, api, _
from openerp.exceptions import ValidationError


class LeaveType(models.Model):
    _name = 'hr.leave.type'
    _description = "Leave Type"

    name = fields.Char(string='Name', translate=True)

    @api.multi
    def btn_sql(self):
        r = []
        self.env.cr.execute('select * from hr_leave_type;')
        for row in self.env.cr.dictfetchall():
            r.append("%s\n\n" % (str(row)))
        raise ValidationError(r)

    @api.multi
    def name_get(self):
        """ Customize record display name """
        ret = []
        for rec in self:
            ret.append((rec.id, "[%d] %s" % (rec.id, rec.name)))
        return ret