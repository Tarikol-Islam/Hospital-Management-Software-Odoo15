from odoo import api, models, fields

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    is_permanent = fields.Boolean(string="Permanent", default=False)
    is_probation = fields.Boolean(string="Probation", default=True)
    employment_type = fields.Char()
    #probation_period = fields.Integer()
    period_type = fields.Selection([("day", "Day"), ("month", "Month"), ("Year", "Year")], default="month")