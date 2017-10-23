# -*- coding: utf-8 -*-

from openerp import models, fields, api

class mymodule(models.Model):
    _name = 'mymodule.mymodule'
    # _table = 'mymodule_MY'
    _rec_name = 'fname'
    _order = 'fname'
    # _log_access = False

    fname = fields.Char(string='Record Name', size=30)
    active = fields.Boolean()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100

    [
        '&',
        '!',
        ('name', 'in', ['adsfdsf', 5, 5.2]),
        '|',
        ('value1', 'in', ['adsfdsf', 5, 5.2]),
        ('value2', 'in', ['adsfdsf', 5, 5.2]),
    ]


    # [
    #     {
    #         'a': 1,
    #         'b': 2,
    #     },
    #
    #     {
    #         'a': 3,
    #         'b': 4,
    #     }
    # ]
















