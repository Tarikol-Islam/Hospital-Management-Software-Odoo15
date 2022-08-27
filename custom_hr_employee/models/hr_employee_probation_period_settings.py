from odoo import models, fields

class HrEmployeeProbationPeriodSettings(models.Model):
    _name = 'hr.employee.probation.period.settings'

    unit = fields.Selection([("day", "Day"), ("week","Week"),("month", "Month"), ("year", "Year")])
    value = fields.Integer()

    def name_get(self):
        return [(record.id, '%s %s' % (record.value,record.unit)) for record in self]