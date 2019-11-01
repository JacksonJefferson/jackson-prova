from django.shortcuts import render, redirect
from . models import Produto, Cliente, CarrinhoDeCompras
from . forms import ProdutoForm, ClienteForm, CarrinhoDeComprasForm
from django.views.generic import ListView

def home(request):
    return render (request, 'home.html')

def produto_list(request):
    if (request.method == "POST"):
        q = request.POST.get('pesquisar_por')
        produtos = Produto.objects.filter(nome__icontains=q)
        return render (request, 'produto/list.html', {'produtos': produtos})   
    else:
        produtos = Produto.objects.all()
        return render (request, 'produto/list.html', {'produtos': produtos})

def produto_show(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    return render (request, 'produto/show.html', {'produto': produto})

def produto_form(request):
    if (request.method == "POST"):
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/primeira/produto/')
        else:
            return render (request, 'produto/form.html', {'form': form})
    else:
        form = ProdutoForm()
        return render (request, 'produto/form.html', {'form': form})

def produto_delete(request,produto_id):
    produto = Produto.objects.get(pk=produto_id)
    produto.delete()
    return redirect('/primeira/produto/')

def produto_editar(request,produto_id):
    if(request.method=='POST'):
        produto = Produto.objects.get(pk=produto_id)
        form = ProdutoForm(request.POST, instance = produto)
        if form.is_valid():
            form.save()
            return redirect('/primeira/produto/')
        else:
            return render(request,'produto/editar.html',{'form':form, 'produto_id':produto_id})       
    else:
        produto = Produto.objects.get(pk=produto_id)
        form = ProdutoForm(instance=produto)
        return render(request,'produto/editar.html',{'form':form, 'produto_id':produto_id})


def cliente_list(request):
    clientes = Cliente.objects.all()
    return render (request, 'cliente/list.html', {'clientes': clientes})

def cliente_show(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    return render (request, 'cliente/show.html', {'cliente': cliente})

def cliente_form(request):
    if (request.method == "POST"):
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/primeira/cliente/')
        else:
            return render (request, 'cliente/form.html', {'form': form})
    else:
        form = ClienteForm()
        return render (request, 'cliente/form.html', {'form': form})

def carrinho_list(request):
    carrinhos = CarrinhoDeCompras.objects.all()
    return render (request, 'carrinho/list.html', {'carrinhos': carrinhos})

def carrinho_form(request):
    if (request.method == "POST"):
        form = CarrinhoDeComprasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/primeira/carrinho/')
        else:
            return render (request, 'carrinho/form.html', {'form': form})
    else:
        form = CarrinhoDeComprasForm()
        return render (request, 'carrinho/form.html', {'form': form})




