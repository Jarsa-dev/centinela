# -*- coding: utf-8 -*-
# © <2016> <Jarsa Sistemas, S.A. de C.V.>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class CentinelQuotation(models.Model):
    _name = 'centinel.quotation'
    _description = 'Quotation from salesman'

    name = fields.Char(
        string='Name')
    date = fields.Datetime(
        default=fields.Datetime.now)
    state = fields.Selection([
        ('suspect', 'Suspect'),
        ('prospect', 'Prospect'),
        ('pipeline', 'Pipeline'),
        ('forecast', 'Forecast'),
        ('won', 'Won'),
        ('lost', 'Lost'),
        ], default='prospect')
    customer_id = fields.Many2one(
        'res.partner',
        string='Customer',
        domain=[('customer', '=', 'True')])
    customer_type = fields.Char()
    location = fields.Char()
    latitude = fields.Float()
    longitude = fields.Float()
    address = fields.Char()
    recruitment_zone = fields.Selection([
        ('10_min', '10 minutes from distance'),
        ('30_min', 'A half of hour from distance'),
        ('3_km', '3 km from distance'),
        ], default='10_min')
    stand_ids = fields.One2many(
        'centinel.stand',
        'quotation_id',
        string='Stand')

    @api.model
    def create(self, values):
        quotation = super(CentinelQuotation, self).create(values)
        quotation.name = self.env['centinel.quotation'].search(
            []).ids[-1] + 1
        return quotation
