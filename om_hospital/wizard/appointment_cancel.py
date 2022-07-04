from odoo import api, models, fields


class AppointmentCancel(models.TransientModel):
    _name = "hospital.appointment.cancel.wizard"
    _description = "Appointment Cancel Wizard"

    appointment_id = fields.Many2one("hospital.appointment", string="Appointment")
    reason = fields.Text(string="Reason")

    def action_cancel(self):
        pass
