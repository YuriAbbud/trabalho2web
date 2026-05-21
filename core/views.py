from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Cliente, NotaFiscal

# ---------- AUTH ----------

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

# ---------- DASHBOARD ----------

@login_required
def dashboard(request):
    from django.db.models import Sum
    from django.utils import timezone

    notas      = NotaFiscal.objects.all()
    mes_atual  = timezone.now().month
    ano_atual  = timezone.now().year

    total_notas    = notas.count()
    notas_mes      = notas.filter(criado_em__month=mes_atual, criado_em__year=ano_atual).count()
    valor_emitido  = notas.aggregate(total=Sum('valor'))['total'] or 0
    total_impostos = notas.aggregate(total=Sum('iss'))['total'] or 0

    resumo = {
        'total_notas':     total_notas,
        'notas_mes':       notas_mes,
        'valor_emitido':   f'R$ {valor_emitido:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'),
        'impostos':        f'R$ {total_impostos:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'),
        'clientes_ativos': Cliente.objects.count(),
    }
    return render(request, 'dashboard.html', {'resumo': resumo})

# ---------- CLIENTES ----------

@login_required
def clientes(request):
    clientes_lista = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes_lista})

# ---------- CRUD NOTAS FISCAIS ----------

@login_required
def lista_notas(request):
    notas = NotaFiscal.objects.select_related('cliente').order_by('-criado_em')
    return render(request, 'lista_notas.html', {'notas': notas})

@login_required
def emitir_nota(request):
    clientes_lista = Cliente.objects.all()
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        descricao  = request.POST.get('descricao')
        valor      = request.POST.get('valor')
        aliquota   = request.POST.get('aliquota')
        cliente    = get_object_or_404(Cliente, pk=cliente_id)
        NotaFiscal.objects.create(
            cliente=cliente,
            descricao=descricao,
            valor=valor,
            aliquota=aliquota,
        )
        return redirect('lista_notas')
    return render(request, 'emitir_nota.html', {'clientes': clientes_lista})

@login_required
def detalhe_nota(request, pk):
    nota = get_object_or_404(NotaFiscal, pk=pk)
    return render(request, 'detalhe_nota.html', {'nota': nota})

@login_required
def editar_nota(request, pk):
    nota           = get_object_or_404(NotaFiscal, pk=pk)
    clientes_lista = Cliente.objects.all()
    if request.method == 'POST':
        nota.cliente   = get_object_or_404(Cliente, pk=request.POST.get('cliente'))
        nota.descricao = request.POST.get('descricao')
        nota.valor     = request.POST.get('valor')
        nota.aliquota  = request.POST.get('aliquota')
        nota.save()
        return redirect('detalhe_nota', pk=nota.pk)
    return render(request, 'editar_nota.html', {'nota': nota, 'clientes': clientes_lista})

@login_required
def deletar_nota(request, pk):
    nota = get_object_or_404(NotaFiscal, pk=pk)
    if request.method == 'POST':
        nota.delete()
        return redirect('lista_notas')
    return render(request, 'deletar_nota.html', {'nota': nota})

    # ---------- CRUD CLIENTES ----------

@login_required
def novo_cliente(request):
    if request.method == 'POST':
        nome     = request.POST.get('nome')
        cpf_cnpj = request.POST.get('cpf_cnpj')
        email    = request.POST.get('email')
        Cliente.objects.create(nome=nome, cpf_cnpj=cpf_cnpj, email=email)
        return redirect('clientes')
    return render(request, 'novo_cliente.html')

@login_required
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.nome     = request.POST.get('nome')
        cliente.cpf_cnpj = request.POST.get('cpf_cnpj')
        cliente.email    = request.POST.get('email')
        cliente.save()
        return redirect('clientes')
    return render(request, 'editar_cliente.html', {'cliente': cliente})

@login_required
def deletar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')
    return render(request, 'deletar_cliente.html', {'cliente': cliente})