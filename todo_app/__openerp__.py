{
    'name': 'Tarefas a fazer',
    'description': 'Gerencie as suas tarefas pessoais com este modulo.',
    'author': 'Milton Reis',
    'depends': ['mail'],
    'application': True,
    'data': [
        'views/todo_view.xml',
        'security/ir.model.access.csv',
        'security/todo_access_rules.xml',

    ]
}