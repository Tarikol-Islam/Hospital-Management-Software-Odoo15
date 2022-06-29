from odoo import api, models, fields

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit =[ "mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    name = fields.Char(string="Patient Name",tracking=True)
    ref = fields.Char(string="Patient Reference",tracking=True)
    age = fields.Integer(string="Patient Age")
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender")
    active = fields.Boolean(string="Active", default=True)
