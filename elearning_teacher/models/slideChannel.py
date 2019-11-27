# -*- coding: utf-8 -*-
from odoo import fields, models

class slideChannel(models.Model):
    _inherit = 'slide.channel'

    
    teacher_ids = fields.Many2many(
                    'res.users',
                    'slide_channel_teacher',
                    'slide_channel_id',
                    'teacher_id',
                    'Teachers'
                                )
    
    #teacher_id = fields.Many2one('res.users','Teacher') //esto es cuando es many2one
    # name = fields.Char(help="What needs to be done?")
    # is_done = fields.Boolean('Done?')
    # active = fields.Boolean('Active?', default=True)
