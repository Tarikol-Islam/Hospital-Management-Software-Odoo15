# -*- coding:utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, models, _

class InheritedHrContract(models.Model):
    _inherit = 'hr.contract'
    _description = 'Employee Contract'

    gross_salary = fields.Float()
    medical_allowance = fields.Float(config_parameter = '')
    house_rent = fields.Float()
    other_allowance = fields.Float()
    basic_salary = fields.Float()