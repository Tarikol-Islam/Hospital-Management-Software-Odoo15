# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    medical_allowance_percentage = fields.Float(config_parameter = 'hr.contract.medical_allowance_percentage')
    house_rent_percentage = fields.Float()
    other_allowance_percentage = fields.Float()
    basic_salary_percentage = fields.Float()