# -*- coding: utf-8 -*-
{
    'name': 'elearning_stages',
    'description': 'Módulo que agrega estados del curso.',
    'author': 'Comunidad Odoo Misiones',
    'depends': ['base','website_slides'],
    'application': True,
    'data': ['views/stage_menu.xml','views/stage_view.xml',
    		'data/data.xml','security/ir.model.access.csv',
    		'views/slide_view.xml']
}
