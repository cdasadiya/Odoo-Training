from openerp import models, fields, api, _


class LeaveType(models.Model):
    _name = 'hr.leave.type'
    _description = "Leave Type"

    name = fields.Char(string='Name', translate=True)

    @api.multi
    def name_get(self):
        """ Customize record display name """
        ret = []
        for rec in self.search([]):
            ret.append((rec.id, "[%d] %s" % (rec.id, rec.name)))
        return ret