from odoo import api, models, fields


class AppointmentCancel(models.TransientModel):
    _name = "hospital.appointment.cancel.wizard"
    _description = "Appointment Cancel Wizard"

    @api.model
    def default_get(self, fields_list):
        res = super(AppointmentCancel, self).default_get(fields_list)
        res['reason'] = "Test Reason"
        return res

    appointment_id = fields.Many2one("hospital.appointment", string="Appointment")
    reason = fields.Text(string="Reason")

    def action_cancel(self):
        pass
