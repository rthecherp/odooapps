# -*- coding: utf-8 -*-
from odoo import fields, models
from odoo.tools import SQL


class AccountInvoiceReport(models.Model):
    _inherit = 'account.invoice.report'

    hr_employee_id = fields.Many2one('hr.employee', string='Employee')

    def _select(self) -> SQL:
        return SQL("%s, move.hr_employee_id as hr_employee_id", super()._select())
