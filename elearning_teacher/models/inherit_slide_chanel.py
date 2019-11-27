# -*- coding: utf-8 -*-
from odoo import fields, models

class slideChannel(models.Model):
    _inherit = 'slide.channel'
    #teacher_id = fields.Many2Many('res.users','Teacher')
    teacher_ids = fields.Many2many(
        'res.users',
        'slide_channel_teacher',
        'slide_channel_id',
        'teacher_id',
        'Teachers'
        )