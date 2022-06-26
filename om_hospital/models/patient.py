from odoo import api, models, fields

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"

    name = fields.Char(string="Patient Name")
    ref = fields.Char(string="Patient Reference")
    age = fields.Integer(string="Patient Age")
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender")

