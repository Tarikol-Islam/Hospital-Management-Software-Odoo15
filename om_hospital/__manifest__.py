# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'summary': 'Hospital Management System',
    'sequence': -100,
    'description': """Hospital management system""",
    'category': 'Hospital',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/patient_data.xml',
        'data/sequence_data.xml',
        'data/hospital.patient.csv',
        'wizard/appointment_cancel_view.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/odoo_playground_view.xml',
        'views/pharmacy_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
