# -*- coding: utf-8 -*-
from odoo import fields, models

class TodoTask(models.Model):
    _name = 'todo.task'

    name = fields.Char(help="What needs to be done?")
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
