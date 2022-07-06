# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOder(models.Model):
    _inherit = "sale.order"

    customer_id = fields.Many2one("res.users", string="Order Placer")

    # inheriting the confirm button function
    def action_confirm(self):
        # Here we can don anything valid before confirming
        super(SaleOder, self).action_confirm()
        self.customer_id=self.env.user.id
        # Here we can don anything valid after confirming
