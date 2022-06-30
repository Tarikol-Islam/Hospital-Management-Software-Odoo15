from odoo import api, models, fields


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Appointment"

    patient_id = fields.Many2one("hospital.patient", string="Patient")
    date = fields.Datetime(string="Appointment Date")
    booking_date = fields.Date(string="Booking date", default=fields.Date.context_today)
