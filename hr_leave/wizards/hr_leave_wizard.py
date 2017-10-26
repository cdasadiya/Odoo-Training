from openerp import models, fields, api, _

class HrLeaveWizard(models.TransientModel):
    _name = 'hr.leave.wizard'

    search_date = fields.Boolean(string='Search by Date', default=True)
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    employee_id = fields.Many2one('hr.employee', string='Employee')

    @api.multi
    def btn_search(self):
        domain = []
        if self.search_date:
            domain.append(('date_from','>=',self.date_from))
            domain.append(('date_to','<=',self.date_to))
        else:
            domain.append(('employee_id', '=', self.employee_id.id))

        action = self.env.ref('hr_leave.action_hr_leave')
        action = action.read()
        action = action and action[0] or False
        action['domain'] = domain
        return action
        # return {
        #     'type': 'ir.actions.act_window',
        #     'res_model': 'hr.leave',
        #     'view_mode': 'tree',
        #     'domain': domain,
        # }