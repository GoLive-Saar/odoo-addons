from openerp.addons.web import http
from openerp.addons.web.http import request

class website_sale_german_additions(http.Controller):
    @http.route(['/page/terms', '/page/website.terms'], type='http', auth='public', website=True)
    def wsga_terms(self, **kw):
        return http.request.render('website_sale_german_additions.wsga_terms')
        
    @http.route(['/page/revocation', '/page/website.revocation'], type='http', auth='public', website=True)
    def wsga_revocation(self, **kw):
        return http.request.render('website_sale_german_additions.wsga_revocation')
        
    @http.route(['/page/delivery', '/page/website.delivery'], type='http', auth='public', website=True)
    def wsga_delivery(self, **kw):
        return http.request.render('website_sale_german_additions.wsga_delivery')
        
    @http.route(['/page/privacy', '/page/website.privacy'], type='http', auth='public', website=True)
    def wsga_privacy(self, **kw):
        return http.request.render('website_sale_german_additions.wsga_privacy')

    @http.route(['/page/imprint', '/page/website.imprint'], type='http', auth='public', website=True)
    def wsga_privacy(self, **kw):
        return http.request.render('website_sale_german_additions.wsga_imprint')