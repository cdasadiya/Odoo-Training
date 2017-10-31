from openerp import models, fields, api, _
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT
from datetime import datetime
from umalqurra.hijri import Umalqurra


class HrLeaveCustomReport(models.AbstractModel):
    _name = 'report.hr_leave.hr_leave_custom_report'

    def get_hijri(self, date):
        """ Convert from Gegorean to Hijri"""
        dt_hijri = Umalqurra()
        if isinstance(date, str):
            dt = datetime.strptime(date, DEFAULT_SERVER_DATE_FORMAT)
        elif isinstance(date, datetime):
            dt = date
        hdt = dt_hijri.gegorean_to_hijri(dt.year, dt.month, dt.day)
        return '%02d/%02d/%04d' % (hdt[2],hdt[1],hdt[0])

    @api.multi
    def render_html(self, data=None):
        # Helper function to get record ids from dictionary
        get_ids = lambda x: x.get('id', False)
        # Objects
        report_obj = self.env['report']
        lv_obj = self.env['hr.leave']
        report = report_obj._get_report_from_name('hr_leave.hr_leave_custom_report')
        data = data.get('data', dict())
        # Get record ids from dictionary
        ids = list(map(get_ids, data))
        # Get records data set
        lv_rec = lv_obj.browse(ids)
        # Built report objects
        docargs = {
            'doc_ids': lv_rec._ids,
            'doc_model': report.model,
            'docs': lv_rec,
            'get_hijri': self.get_hijri,
        }
        return report_obj.render('hr_leave.hr_leave_custom_report', docargs)