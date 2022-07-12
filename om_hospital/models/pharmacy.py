from odoo import api, models, fields
from datetime import date


class HospitalPharmacy(models.Model):
    _name = "hospital.pharmacy"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Pharmacy"

    name = fields.Char(string="Medicine name")
    power = fields.Integer(string="Medicine XP")
    times = fields.Integer(string="Piece Per Day")
    int_color = fields.Integer(string="Color")
    hex_color = fields.Char(string="Color")
    appointment_id = fields.Many2one("hospital.appointment", string="Appointment")

    _sql_constraints = [
        ('check_times', 'check(times > 0)',
         'You have to take medicine at least one time a day!'),
        ('unique_name', 'unique(name)', "You can't create a tag two or more time")
    ]
