from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Appointment"
    _rec_name = "appointment_id"  # Where 'name' is not a field for the model, then it will work

    patient_id = fields.Many2one("hospital.patient", string="Patient", ondelete='cascade')
    appointment_id = fields.Char(string="Unique ID")
    doctor_id = fields.Many2one("res.users", string="Doctor")
    age = fields.Integer(related='patient_id.age')  # not editable as it's a reference
    date = fields.Datetime(string="Appointment Date")
    booking_date = fields.Date(string="Booking date", default=fields.Date.context_today)
    ref = fields.Char(string="Reference")
    prescription = fields.Html(string="Prescription")
    tag_ids = fields.Many2many("hospital.pharmacy", string="Tags")
    pharmacy_ids = fields.One2many("hospital.pharmacy", 'appointment_id', string="Pharmacy")
    priority = fields.Selection(
        [('0', 'Low'),
         ('1', 'Normal'),
         ('2', 'High'),
         ('3', 'Very High')], string="Priority")
    state = fields.Selection(
        [('initiated', 'Initiated'),
         ('processing', 'Processing'),
         ('done', 'Done'),
         ('cancelled', 'Cancelled')], default="initiated", string="Status")

    @api.model
    def create(self, vals_list):
        vals_list['appointment_id'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super(HospitalAppointment, self).create(vals_list)

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_done(self):
        for rec in self:
            if rec.state == "processing": rec.state = "done"

    def action_processing(self):
        for rec in self:
            if rec.state == "initiated": rec.state = "processing"

    def action_cancel(self):
        action = self.env.ref('om_hospital.action_appointment_cancel').read()[0]
        return action

    def unlink(self):
        if self.state != 'initiated':
            raise ValidationError(_("Warning!!!\nYou are not allowed to delete this record!!!"))
        return super(HospitalAppointment, self).unlink()

