# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError,ValidationError
from odoo.tools import float_is_zero, pycompat
from odoo.addons import decimal_precision as dp
from datetime import date
import os
import base64
from collections import defaultdict

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self,vals):
        if 'l10n_ar_afip_responsibility_type_id' not in vals or vals['l10n_ar_afip_responsibility_type_id'] == False:
            respon_id = self.env['l10n_ar.afip.responsibility.type'].search([('code','=','5')])
            if not respon_id:
                raise ValidationError('No se puede determinar el tipo de cliente, contacte al administrador')
            vals['l10n_ar_afip_responsibility_type_id'] = respon_id.id
        if 'vat' in vals and vals['vat'] == False:
            respon_id = self.env['l10n_latam.identification.type'].search([('name','=','Sigd')])
            if not respon_id:
                raise ValidationError('No se puede determinar el tipo de responsabilidad del cliente, contacte al administrador')
            vals['l10n_latam_identification_type_id'] = respon_id.id
        return super(ResPartner, self).create(vals)

