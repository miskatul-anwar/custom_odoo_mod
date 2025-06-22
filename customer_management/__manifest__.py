{
    'name': 'Customer Management System',
    'version': '1.1.0',
    'category': 'Sales',
    'summary': 'Customer management with sales tracking and due management',
    'description': """
        Comprehensive customer management system featuring:
        - Sales tracking with earnings record from each customer
        - Due management with customer contact information
        - Dashboard showing best customers, worst debtors, and total earnings
        - Simple CRUD operations with automated due handling
        - Clean separation of sales and due tracking interfaces
    """,
    'author': 'Miskatul Anwar',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/customer_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
