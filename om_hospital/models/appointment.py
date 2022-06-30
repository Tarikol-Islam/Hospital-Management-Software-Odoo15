from odoo import api, models, fields


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Appointment"

    patient_id = fields.Many2one("hospital.patient", string="Patient")
    age = fields.Integer(related='patient_id.age')#not editable as its a reference
    date = fields.Datetime(string="Appointment Date")
    booking_date = fields.Date(string="Booking date", default=fields.Date.context_today)
    ref = fields.Char(string="Reference")

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref
