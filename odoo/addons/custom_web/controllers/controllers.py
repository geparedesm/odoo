# -*- coding: utf-8 -*-
from odoo import http


class CustomWeb(http.Controller):
    @http.route('/', type='http', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('custom_web.portfolio_page', {})

    # @http.route('/custom_web/custom_web/objects/', type='http', auth='public', website=True)
    # def list(self, **kw):
    #     return http.request.render('custom_web.listing', {
    #         'root': '/custom_web/custom_web',
    #         'objects': http.request.env['custom_web.custom_web'].search([]),
    #     })

    # @http.route('/custom_web/custom_web/objects/<model("custom_web.custom_web"):obj>/', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('custom_web.object', {
    #         'object': obj
    #     })
