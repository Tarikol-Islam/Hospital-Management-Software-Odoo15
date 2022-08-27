from odoo import fields, models, api
from datetime import date
from dateutil import relativedelta


class InheritedHrEmployee(models.Model):
    _inherit = "hr.employee"

    employee_type_id = fields.Many2one('hr.employee.type', string="Type of Employee", required=True)
    joining_date = fields.Date(required=True)
    probation_period_id = fields.Many2one('hr.employee.probation.period.settings', string="Probation Period")
    confirmation_date = fields.Date(compute='_compute_confirmation_date', store=True)

    @api.onchange('probation_period_id')
    @api.depends('joining_date')
    def _compute_confirmation_date(self):
        for rec in self:
            if rec.employee_type_id.is_probation:
                if rec.probation_period_id.value:
                    if rec.probation_period_id.unit == "day":
                        rec.confirmation_date = rec.joining_date + relativedelta.relativedelta(
                            days=rec.probation_period_id.value)
                    elif rec.probation_period_id.unit == "week":
                        rec.confirmation_date = rec.joining_date + relativedelta.relativedelta(
                            weeks=rec.probation_period_id.value)
                    elif rec.probation_period_id.unit == "month":
                        rec.confirmation_date = rec.joining_date + relativedelta.relativedelta(
                            months=rec.probation_period_id.value)
                    elif rec.probation_period_id.unit == "year":
                        print("Effect will be shown here")
                        rec.confirmation_date = rec.joining_date + relativedelta.relativedelta(
                            years=rec.probation_period_id.value)
                        print(rec.joining_date + relativedelta.relativedelta(years=rec.probation_period_id.value))

    def _probation_to_confirmation(self, cr, uid, context=None):
        print("Here is the cron and uid")
        print(cr, uid)
        print(context)
