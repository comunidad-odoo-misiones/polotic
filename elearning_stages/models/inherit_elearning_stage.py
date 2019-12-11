# -*- coding: utf-8 -*-
from odoo import fields, models, api


class slideChannel(models.Model):
    _inherit = 'slide.channel'
    def _get_default_stage_id(self):
        """ Gives default stage_id """
        return self.env['elearning.stage'].search([('sequence', '=', '0')])[0]

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        search_domain = [('id', 'in', stages.ids)]
        stage_ids = stages._search([], order=order, access_rights_uid=SUPERUSER_ID)
        return stages.browse(stage_ids)

    stage_id = fields.Many2one('elearning.stage','Stage',default=_get_default_stage_id,
        group_expand='_read_group_stage_ids')

