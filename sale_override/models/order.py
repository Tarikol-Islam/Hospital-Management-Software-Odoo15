# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOder(models.Model):
    _inherit = "sale.order"

    customer_id = fields.Many2one("res.users", string="Order Placer")
