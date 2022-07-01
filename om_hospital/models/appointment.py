from odoo import api, models, fields


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Appointment"
    _rec_name = "patient_id"  # Where 'name' is not a field for the model, then it will works

    patient_id = fields.Many2one("hospital.patient", string="Patient")
    age = fields.Integer(related='patient_id.age')  # not editable as its a reference
    date = fields.Datetime(string="Appointment Date")
    booking_date = fields.Date(string="Booking date", default=fields.Date.context_today)
    ref = fields.Char(string="Reference")
    prescription = fields.Html(string="Prescription")
    priority = fields.Selection(
        [('0', 'Low'),
         ('1', 'Normal'),
         ('2', 'High'),
         ('3', 'Very High')], string="Priority")

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref
