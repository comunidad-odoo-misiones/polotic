# -*- coding: utf-8 -*-
from odoo import fields, models

class slideChannel(models.Model):
    _inherit = 'slide.channel'
  
    stage_id = fields.Many2one('elearning.stage','Stage')