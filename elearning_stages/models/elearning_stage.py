# -*- coding: utf-8 -*-
from odoo import fields, models

class elearningStage(models.Model):
    _name = "elearning.stage"
    _description = "Elearning Stage Description"

    
    name = fields.Char(help="What's name?",required = True)
    description= fields.Char(help="Give me a good description!")
    sequence= fields.Integer(help="Give me a sequence!", default=0)

    state = fields.Selection([('draft', 'Draft'), ('done', 'Done'),
   		('cancel', 'Cancelled'), ], required=True, default='draft')