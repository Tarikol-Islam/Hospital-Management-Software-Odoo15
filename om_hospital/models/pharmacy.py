from odoo import api, models, fields
from datetime import date


class HospitalPharmacy(models.Model):
    _name = "hospital.pharmacy"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Pharmacy"

    name = fields.Char(string="Medicine name")
    power = fields.Integer(string="Medicine XP")
    times = fields.Integer(string="Piece Per Day")
    color = fields.Integer(string="Color")
    appointment_id = fields.Many2one("hospital.appointment", string="Appointment")



