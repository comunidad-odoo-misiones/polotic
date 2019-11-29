# -*- coding: utf-8 -*-
from odoo import fields, models

class elearningStage(models.Model):
    _name = "elearning.stage"
    _description = "elearning.stage"
    
    name = fields.Char(help="What's name?")
    description= fields.Char(help="Give me a good description!")
