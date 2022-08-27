from odoo import api, models, fields


class HrEmployeeType(models.Model):
    _name = "hr.employee.type"

    is_permanent = fields.Boolean("Is Permanent")
    is_probation = fields.Boolean("Is Probation")
    type_name = fields.Char('Type')

    def name_get(self):
        return [(record.id, '%s' % (record.type_name)) for record in self]

