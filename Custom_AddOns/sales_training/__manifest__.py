{
    'name': 'Training Sales',
    'author': 'Roaa',
    'description': '',
    'version': '17.0.0.1.0',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'security/groups.xml',
        'data/ir_sequence_data.xml',
        'views/sale_advanced.xml',
        'views/sale_training.xml',
        'views/training_wizard.xml'
    ],
    'application': True,
}
