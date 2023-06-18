{
    'name': 'website insurance',
    'version': '1.0',
    'category': 'Website',
    'summary': 'Your Module Summary',
    'description': """
Your Module Description
""",
    'depends': ['website', 'tk_insurance_management'],
    'data': [
        'views/templates2.xml',
        'views/treeview.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            ('prepend', 'insurance_website/static/src/js/script.js'),
            #('prepend', 'insurance_website/static/src/js/scriptfield.js'),
            ('prepend', 'insurance_website/static/src/css/style.css'),
        ],
    },
}
