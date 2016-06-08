# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, models


class WizardModel(models.TransientModel):
    _name = "wizard.model"

    @api.multi
    def action_accept(self):
        self.ensure_one()
        return {'type': 'ir.actions.act_window_close'}
