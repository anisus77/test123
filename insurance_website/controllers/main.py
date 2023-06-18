# from odoo import http
# from odoo.http import request

# class InsuranceForm(http.Controller):
#     @http.route('/insurance/form', type='http', auth='public', website=True)
#     def insurance_form(self, **kwargs):
#         if request.httprequest.method == 'POST':
#             # Get data from form
#             insurance_number = kwargs.get('insurance_number')
#             insured_id = kwargs.get('insured_id')
#             # ...

#             # Create new record in InsuranceInformation model
#             request.env['insurance.information'].sudo().create({
#                 'insurance_number': insurance_number,
#                 'insured_id': insured_id,
#                 # ...
#             })

#         # Render form view
#         return request.render('your_module.insurance_form')


# from odoo import http
# from odoo.http import request

# class InsuranceForm(http.Controller):
#     @http.route('/insurance/form', type='http', auth='public', website=True)
#     def insurance_form(self, **kwargs):
#         # Get the current user
#         current_user = request.env.user

#         if request.httprequest.method == 'POST':
#             # Get data from form
#             insurance_number = kwargs.get('insurance_number')
#             insured_id = kwargs.get('insured_id')
#             insurance_nominee_id = kwargs.get('insurance_nominee_id')
#             your_nominee_is_your = kwargs.get('your_nominee_is_your')
#             nominee_dob = kwargs.get('nominee_dob')
#             nominee_gender = kwargs.get('nominee_gender')
#             # ...

#             # Create new record in InsuranceInformation model
#             request.env['insurance.information'].sudo().create({
#                 'insurance_number': insurance_number,
#                 'insured_id': insured_id,
#                 'insurance_nominee_id': insurance_nominee_id,
#                 'your_nominee_is_your': your_nominee_is_your,
#                 'nominee_dob': nominee_dob,
#                 'nominee_gender': nominee_gender,
#                 'agent': current_user.id,  # Set agent to current user
#                 # ...
#             })

#         # Render form view
#         return request.render('insurance_website.insurance_form', {
#             'current_user': current_user,  # Pass current user to template
#         })
#######################################################""""""
# from odoo import http
# from odoo.http import request

# class InsuranceForm(http.Controller):
#     @http.route('/insurance/form', type='http', auth='public', website=True)
#     def insurance_form(self, **kwargs):
#         # Get the current user
#         current_user = request.env.user

#         if request.httprequest.method == 'POST':
#             # Get data from form
#             insurance_number = kwargs.get('insurance_number')
#             insured_id = kwargs.get('insured_id')
#             insurance_nominee_id = kwargs.get('insurance_nominee_id')
#             your_nominee_is_your = kwargs.get('your_nominee_is_your')
#             nominee_dob = kwargs.get('nominee_dob')
#             nominee_gender = kwargs.get('nominee_gender')
#             # ...

#             # Create new record in InsuranceInformation model
#             request.env['insurance.information'].sudo().create({
#                 'insurance_number': insurance_number,
#                 'insured_id': insured_id,
#                 'insurance_nominee_id': insurance_nominee_id,
#                 'your_nominee_is_your': your_nominee_is_your,
#                 'nominee_dob': nominee_dob,
#                 'nominee_gender': nominee_gender,
#                 'agent': current_user.id,  # Set agent to current user
#                 # ...
#             })

#         # Render form view
#         return request.render('insurance_website.insurance_form', {
#             'current_user': current_user,  # Pass current user to template
#             'current_user_partner_id': current_user.partner_id.id,  # Pass current user partner ID to template
#         })
######################################""
# from odoo import http
# from odoo.http import request
# from odoo.addons.your_module_name.models import insurance_category, insurance_sub_category, insurance_policy
# from odoo.addons.your_module_name.models import res_partner

# class InsuranceWebsiteController(http.Controller):

#     @http.route('/insurance/form', type='http', auth="public", website=True)
#     def insurance_form(self, **kwargs):
#         categories = http.request.env['insurance.category'].sudo().search([])
#         sub_categories = http.request.env['insurance.sub.category'].sudo().search([])
#         policies = http.request.env['insurance.policy'].sudo().search([])
#         insureds = http.request.env['res.partner'].sudo().search([('is_customer', '=', True)])

#         return http.request.render('your_module_name.insurance_form', {
#             'categories': categories,
#             'sub_categories': sub_categories,
#             'policies': policies,
#             'insureds': insureds,
#         })

#     @http.route('/insurance/form/submit', type='http', auth="public", methods=['POST'], website=True)
#     def insurance_form_submit(self, **post):
#         InsuranceInfo = request.env['insurance.information'].sudo()

#         # Extract field values from the submitted form data
#         category_id = post.get('insurance_category_id')
#         sub_category_id = post.get('insurance_sub_category_id')
#         policy_id = post.get('insurance_policy_id')
#         issue_date = post.get('issue_date')
#         buying_for = post.get('insurance_buying_for_id')
#         agent_id = post.get('agent_id')
#         insured_id = post.get('insured_id')
#         dob = post.get('dob')
#         gender = post.get('gender')
#         insurance_nominee_id = post.get('insurance_nominee_id')
#         your_nominee_is_your = post.get('your_nominee_is_your')
#         nominee_dob = post.get('nominee_dob')

#         # Create a new record in insurance.information model
#         InsuranceInfo.create({
#             'category_id': category_id,
#             'sub_category_id': sub_category_id,
#             'policy_id': policy_id,
#             'issue_date': issue_date,
#             'buying_for': buying_for,
#             'agent_id': agent_id,
#             'insured_id': insured_id,
#             'dob': dob,
#             'gender': gender,
#             'insurance_nominee_id': insurance_nominee_id,
#             'your_nominee_is_your': your_nominee_is_your,
#             'nominee_dob': nominee_dob,
#         })

#         return request.render('insurance_website.insurance_form_success')
###################################""""""
# from odoo import http
# from odoo.http import request

# class InsuranceFormController(http.Controller):

#     @http.route('/insurance/form', type='http', auth="public", website=True)
#     def insurance_form(self, **post):
#         categories = request.env['insurance.category'].sudo().search([])
#         sub_categories = request.env['insurance.sub.category'].sudo().search([])
#         policies = request.env['insurance.policy'].sudo().search([])
#         insureds = request.env['res.partner'].sudo().search([('is_customer', '=', True)])

#         return http.request.render('insurance_website.insurance_form', {
#             'categories': categories,
#             'sub_categories': sub_categories,
#             'policies': policies,
#             'insureds': insureds,
#             'current_user': request.env.user,
#         })

#     @http.route('/insurance/form/submit', type='http', auth="public", website=True)
#     def insurance_form_submit(self, **post):
#         insurance_information = request.env['insurance.information'].sudo().create({
#             'insurance_category_id': post.get('insurance_category_id'),
#             'insurance_sub_category_id': post.get('insurance_sub_category_id'),
#             'insurance_policy_id': post.get('insurance_policy_id'),
#             'issue_date': post.get('issue_date'),
#             'insurance_buying_for_id': post.get('insurance_buying_for_id'),
#             'agent_id': request.env.user.id,
#             'insured_id': post.get('insured_id'),
#             'dob': post.get('dob'),
#             'gender': post.get('gender'),
#             'insurance_nominee_id': post.get('insurance_nominee_id'),
#             'your_nominee_is_your': post.get('your_nominee_is_your'),
#             'nominee_dob': post.get('nominee_dob'),
#         })

#         return http.request.render('insurance_website.insurance_form_success')
from odoo import http
from odoo.http import request

class InsuranceForm(http.Controller):
    @http.route('/insurance/form', type='http', auth="public", website=True)
    def insurance_form(self, **post):
        categories = request.env['insurance.category'].sudo().search([])
        sub_categories = request.env['insurance.sub.category'].sudo().search([])
        policies = request.env['insurance.policy'].sudo().search([])
        insureds = request.env['res.partner'].sudo().search([('is_customer', '=', True)])

        return http.request.render('insurance_website.insurance_form', {
            'categories': categories,
            'sub_categories': sub_categories,
            'policies': policies,
            'insureds': insureds,
            'current_user': request.env.user,
        })

    @http.route('/insurance/form/submit', type='http', auth="public", website=True)
    def insurance_form_submit(self, **post):
        insurance_information = request.env['insurance.information'].sudo().create({
            'insurance_number': post.get('insurance_number'),
            'commission_type': post.get('commission_type'),
            'commission': post.get('commission'),
            'insurance_category_id': post.get('insurance_category_id'),
            'insurance_sub_category_id': post.get('insurance_sub_category_id'),
            'insurance_policy_id': post.get('insurance_policy_id'),
            'issue_date': post.get('issue_date'),
            'insurance_buying_for_id': post.get('insurance_buying_for_id'),
            #'agent_id': request.env.user.id,
            'agent_id': post.get('agent_id'),
            'insured_id': post.get('insured_id'),
            'dob': post.get('dob'),
            'gender': post.get('gender'),
            'insurance_nominee_id': post.get('insurance_nominee_id'),
            'your_nominee_is_your': post.get('your_nominee_is_your'),
            'nominee_dob': post.get('nominee_dob'),
            'policy_amount': post.get('policy_amount'),
            'monthly_installment' : post.get('monthly_installment'),
        })

        return http.request.render('insurance_website.insurance_form_success')

    @http.route('/insurance/tree_view', type='http', auth="public", website=True)
    def insurance_tree_view(self, **post):
        return http.request.render('insurance_website.insurance_tree_view', {
                'current_user': request.env.user,
                 })

    # Get the insurance record from the database
    @http.route('/insurance/form', type='http', auth="public", website=True)
    def insurance_form(self, id=None, **post):
        # Get the insurance record from the database
        insurance = request.env['insurance.information'].sudo().browse(int(id)) if id else None
        # Get the insurance categories, subcategories, policies and insureds from the database
        categories = request.env['insurance.category'].sudo().search([])
        sub_categories = request.env['insurance.sub.category'].sudo().search([])
        policies = request.env['insurance.policy'].sudo().search([])
        insureds = request.env['res.partner'].sudo().search([('is_customer', '=', True)])
        # Render the insurance form template with the insurance data
        return http.request.render('insurance_website.insurance_form', {
        'insurance': insurance,
        'categories': categories,
        'sub_categories': sub_categories,
        'policies': policies,
        'insureds': insureds,
        'current_user': request.env.user,
    })
