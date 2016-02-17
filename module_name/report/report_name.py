# -*- coding: utf-8 -*-
# © 2016-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, models


class Name(models.AbstractModel):
    _name = "report.module.name_report"

    @api.multi
    def render_html(self, data=None):
        report_obj = self.env["report"]
        report = report_obj._get_report_from_name("module.name_report")
        docargs = {
            "doc_ids": self._ids,
            "doc_model": report.model,
            "docs": self,
        }
        return report_obj.render("module.name_report", docargs)
