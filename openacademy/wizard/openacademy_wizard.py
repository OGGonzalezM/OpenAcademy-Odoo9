# -*- coding: utf-8 -*-
from openerp import models, fields, api

class Wizard(models.TransientModel):
	_name = 'openacademy.wizard'

	def _default_session(self):
		print "self._context", self._context
		return self.env['openacademy.session'].browse(self._context.get('active_ids'))

	session_wiz_ids = fields.Many2many('openacademy.session',
        string="Session", required=True, default=_default_session)

	attendee_wiz_ids = fields.Many2many('res.partner', 
		 string="Attendees")

	# La simbologia |= tambien significa concatenacion pero con objetos
	@api.multi
	def suscribe(self):
		for session_wiz_id in self.session_wiz_ids:
			session_wiz_id.attendee_ids |= self.attendee_wiz_ids
		return {}
