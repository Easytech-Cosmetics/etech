
from odoo import fields, models,api


class Partner(models.Model):
	_inherit = 'sale.order'

	##Pronto_pago = fields.Float(string = "Dto_pto_pago %",store=True,compute='_ptopago')
	##descuento = fields.Float(string ="calc_desc",store=True)

	##@api.depends('Pronto_pago','descuento')
	##def _ptopago(self):
			##descuento = (self.amount_untaxed * self.Pronto_pago)/100
			##self.amount_untaxed = self.amount_untaxed - 100