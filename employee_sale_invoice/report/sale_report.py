# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleReport(models.Model):
    _inherit = 'sale.report'

    hr_employee_id = fields.Many2one('hr.employee', string='Employee')

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res['hr_employee_id'] = 's.hr_employee_id'
        return res
