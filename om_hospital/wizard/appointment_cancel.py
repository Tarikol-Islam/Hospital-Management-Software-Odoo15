from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class AppointmentCancel(models.TransientModel):
    _name = "hospital.appointment.cancel.wizard"
    _description = "Appointment Cancel Wizard"

    @api.model
    def default_get(self, fields_list):
        res = super(AppointmentCancel, self).default_get(fields_list)
        res['appointment_id'] = self.env.context.get('active_id')
        res['reason'] = "Test Reason"
        return res

    appointment_id = fields.Many2one("hospital.appointment", string="Appointment",
                                     domain=['|', ('state', '=', 'initiated'), ('priority', 'in', ('0', '1', False))])
    reason = fields.Text(string="Reason")



    def action_cancel(self):
        if self.appointment_id.date.date() == fields.Date.today():
            raise ValidationError("Sorry!!!\nYou can't cancel an appointment at the meeting date!!!")
        return
