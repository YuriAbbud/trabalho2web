from django.shortcuts import render

# Create your views here.
def dashboard(request):
    resumo = {
        'total_notas': 142,
        'notas_mes': 18,
        'valor_emitido': 'R$ 87.430,00',
        'impostos': 'R$ 4.371,50',
        'notas_pendentes': 5,
        'clientes_ativos': 34,
    }
    return render(request, 'dashboard.html', {'resumo': resumo})


def clientes(request):
    clientes_lista = [
        {'nome': 'Fernanda Lima',       'cpf_cnpj': '123.456.789-00', 'email': 'fernanda@email.com'},
        {'nome': 'Tech Solutions Ltda', 'cpf_cnpj': '12.345.678/0001-99', 'email': 'contato@techsol.com.br'},
        {'nome': 'Carlos Eduardo',      'cpf_cnpj': '987.654.321-11', 'email': 'carlos@email.com'},
        {'nome': 'Agência Criativa ME', 'cpf_cnpj': '98.765.432/0001-10', 'email': 'adm@agenciacriativa.com'},
        {'nome': 'Julia Martins',       'cpf_cnpj': '321.654.987-22', 'email': 'julia.m@email.com'},
    ]
    return render(request, 'clientes.html', {'clientes': clientes_lista})


def emitir_nota(request):
    clientes_lista = [
        {'id': 1, 'nome': 'Fernanda Lima'},
        {'id': 2, 'nome': 'Tech Solutions Ltda'},
        {'id': 3, 'nome': 'Carlos Eduardo'},
        {'id': 4, 'nome': 'Agência Criativa ME'},
        {'id': 5, 'nome': 'Julia Martins'},
    ]
    return render(request, 'emitir_nota.html', {'clientes': clientes_lista})