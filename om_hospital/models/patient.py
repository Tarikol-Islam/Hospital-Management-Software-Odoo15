from odoo import api, models, fields, _
from datetime import date
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    name = fields.Char(string="Patient Name", tracking=True)
    image = fields.Image(string="Patient Image")
    ref = fields.Char(string="Patient Reference", tracking=True)
    unique_id = fields.Char(string="Unique ID")
    birthdate = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Patient Age", compute='_compute_age', store=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    active = fields.Boolean(string="Active", default=True)
    appointments_count = fields.Integer(string="Total appointments", compute="_compute_appointment_count", store=True)
    appointments_count_dependency_model = fields.One2many('hospital.appointment','patient_id',string="Patient Appointment")

    parent_name = fields.Char(string="Parent name")
    marital_status = fields.Selection([('single','Single'),('married','Married')])
    partner_name = fields.Char(string="Partner name")
    @api.depends('appointments_count_dependency_model') # if appointment_count does not change for any change in appointment record that time we should give new field as dependency
    def _compute_appointment_count(self):
        for rec in self:
            rec.appointments_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.ids)])

    @api.constrains('birthdate')
    def _check_birthdate(self):
        for rec in self:
            if rec.birthdate and rec.birthdate > fields.Date.today():
                raise ValidationError(_("Birthdate can't be tomorrow or more!!!"))

    @api.depends('birthdate')
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.birthdate:
                rec.age = today.year - rec.birthdate.year
            else:
                rec.age = 0

    @api.model
    def create(self, vals):
        # As vals_liist is a dict here, we can overwrite any key of vals_list here
        vals['unique_id'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        vals['ref'] = self.env.user.id
        return super(HospitalPatient, self).create(vals)

    def write(self, vals):
        if not self.unique_id:
            vals['unique_id'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        super(HospitalPatient, self).write(vals)

    def name_get(self):
        return [(record.id, "%s:%s" % (record.unique_id, record.name)) for record in self]
