# -*- coding: utf-8 -*-

from django.urls import reverse_lazy
from django.db.models import F
from django.views.generic.list import ListView


from SGEO.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView
from SGEO.apps.cadastro.forms import ProdutoForm, CategoriaForm, UnidadeForm, MarcaForm, StatusVendaForm, GrupoForm
from SGEO.apps.cadastro.forms import LoteFormSet
from SGEO.apps.cadastro.models import Produto, Categoria, Unidade, Marca, Fornecedor, StatusVenda, Grupo
from SGEO.apps.estoque.models import ItensMovimento, EntradaEstoque, ProdutoEstocado

from datetime import datetime


class AdicionarProdutoView(CustomCreateView):
    form_class = ProdutoForm
    template_name = "cadastro/produto/produto_add.html"
    success_url = reverse_lazy('cadastro:listaprodutosview')
    success_message = "Produto <b>%(descricao)s </b>adicionado com sucesso."
    permission_codename = 'add_produto'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, descricao=self.object.descricao)

    def get_context_data(self, **kwargs):
        context = super(AdicionarProdutoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'CADASTRAR PRODUTO'
        context['return_url'] = reverse_lazy('cadastro:listaprodutosview')
        return context

    def get(self, request, *args, **kwargs):
        self.object = None

        form = ProdutoForm(prefix='form')
        lote_form = LoteFormSet(prefix='lote_form')
        lote_form.can_delete = True

        return self.render_to_response(self.get_context_data(produto_form=form, lote_form=lote_form))

    def post(self, request, *args, **kwargs):
        self.object = None
        # Tirar . dos campos decimais
        req_post = request.POST.copy()

        for key in req_post:
            if ('venda' in key or
                'custo' in key or
                'estoque_minimo' in key or
                'depreciacao' in key or
                'peso_liquido' in key or
                'peso_bruto' in key or
                'altura' in key or
                'largura' in key or
                'profundidade' in key or
                'peso_com_embalagem' in key or
                'altura_com_embalagem' in key or
                'largura_com_embalagem' in key or
                'profundidade_com_embalagem' in key or
                    'estoque_atual' in key):
                req_post[key] = req_post[key].replace('.', '')

        if 'EX:' in req_post['ncm']:
            ncm = req_post['ncm'][0:8]
            ex_start = req_post['ncm'].find('EX:') + 3
            ex_end = req_post['ncm'].find(']')
            ex_tipi = req_post['ncm'][ex_start:ex_end]
            req_post['ncm'] = ncm + ex_tipi

        request.POST = req_post

        form = ProdutoForm(request.POST, prefix='form')

        lote_form = LoteFormSet(request.POST, prefix='lote_form')

        if form.is_valid() and lote_form.is_valid():
            self.object = form.save(commit=False)

            if self.object.controlado_por_lote:
                lote_form.instance = self.object
                lote_form.save()

            if self.object.controlar_estoque and form.cleaned_data['estoque_inicial'] > 0:
                # Gerar movimento de estoque inicial
                mov_inicial = EntradaEstoque()
                item_entrada = ItensMovimento()
                prod_estocado = ProdutoEstocado()

                mov_inicial.data_movimento = datetime.now().date()
                mov_inicial.quantidade_itens = 1
                mov_inicial.tipo_movimento = u'3'
                mov_inicial.observacoes = ''
                mov_inicial.valor_total = round(
                    self.object.venda * form.cleaned_data['estoque_inicial'], 2)

                if form.cleaned_data['fornecedor']:
                    mov_inicial.fornecedor = Fornecedor.objects.get(
                        id=form.cleaned_data['fornecedor'])
                if form.cleaned_data['local_dest']:
                    mov_inicial.local_dest = form.cleaned_data['local_dest']

                item_entrada.quantidade = form.cleaned_data['estoque_inicial']
                item_entrada.valor_unit = self.object.venda
                item_entrada.subtotal = mov_inicial.valor_total

                prod_estocado.local = mov_inicial.local_dest
                prod_estocado.quantidade = form.cleaned_data['estoque_inicial']

                self.object.estoque_atual = form.cleaned_data[
                    'estoque_inicial']
                self.object.save()
                mov_inicial.save()

                item_entrada.movimento_id = mov_inicial
                item_entrada.produto = self.object
                item_entrada.save()

                prod_estocado.produto = self.object
                prod_estocado.save()

            else:
                self.object.save()

            return self.form_valid(form=form)

        return self.form_invalid(form=form, lote_form=lote_form)


class ProdutosListView(CustomListView):
    template_name = 'cadastro/produto/produto_list.html'
    model = Produto
    context_object_name = 'all_produtos'
    success_url = reverse_lazy('cadastro:listaprodutosview')
    permission_codename = 'view_produto'

    def get_context_data(self, **kwargs):
        context = super(ProdutosListView, self).get_context_data(**kwargs)
        context['title_complete'] = 'PRODUTOS CADASTRADOS'
        context['add_url'] = reverse_lazy('cadastro:addprodutoview')
        return context


class ProdutosBaixoEstoqueListView(ProdutosListView):
    success_url = reverse_lazy('cadastro:listaprodutosbaixoestoqueview')

    def get_context_data(self, **kwargs):
        context = super(ProdutosBaixoEstoqueListView,
                        self).get_context_data(**kwargs)
        context['title_complete'] = 'PRODUTOS COM BAIXO ESTOQUE'
        return context

    def get_queryset(self):
        return Produto.objects.filter(estoque_atual__lte=F('estoque_minimo'))


class EditarProdutoView(CustomUpdateView):
    form_class = ProdutoForm
    model = Produto
    template_name = "cadastro/produto/produto_edit.html"
    success_url = reverse_lazy('cadastro:listaprodutosview')
    success_message = "Produto <b>%(descricao)s </b>editado com sucesso."
    permission_codename = 'change_produto'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, descricao=self.object.descricao)

    def get_context_data(self, **kwargs):
        context = super(EditarProdutoView, self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy('cadastro:listaprodutosview')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Tirar . dos campos decimais
        req_post = request.POST.copy()

        for key in req_post:
            if ('venda' in key or
                'custo' in key or
                'estoque_minimo' in key or
                'depreciacao' in key or
                'peso_liquido' in key or
                'peso_bruto' in key or
                'altura' in key or
                'largura' in key or
                'profundidade' in key or
                'peso_com_embalagem' in key or
                'altura_com_embalagem' in key or
                'largura_com_embalagem' in key or
                'profundidade_com_embalagem' in key or
                    'estoque_atual' in key):
                req_post[key] = req_post[key].replace('.', '')

        if 'EX:' in req_post['ncm']:
            ncm = req_post['ncm'][0:8]
            ex_start = req_post['ncm'].find('EX:') + 3
            ex_end = req_post['ncm'].find(']')
            ex_tipi = req_post['ncm'][ex_start:ex_end]
            req_post['ncm'] = ncm + ex_tipi

        request.POST = req_post

        form_class = self.get_form_class()
        form = form_class(request.POST, instance=self.object)

        if form.is_valid():
            self.object = form.save()
            return self.form_valid(form)

        return self.form_invalid(form)


class AdicionarOutrosBaseView(CustomCreateView):
    template_name = "base/popup_form.html"

    def get_context_data(self, **kwargs):
        context = super(AdicionarOutrosBaseView,
                        self).get_context_data(**kwargs)
        context['titulo'] = 'Adicionar ' + self.model.__name__
        return context


class EditarOutrosBaseView(CustomUpdateView):
    template_name = "base/popup_form.html"

    def get_context_data(self, **kwargs):
        context = super(EditarOutrosBaseView,
                        self).get_context_data(**kwargs)
        context['titulo'] = 'Editar {0}: {1}'.format(
            self.model.__name__, str(self.object))
        return context


class AdicionarCategoriaView(AdicionarOutrosBaseView):
    form_class = CategoriaForm
    model = Categoria
    success_url = reverse_lazy('cadastro:addcategoriaview')
    permission_codename = 'add_categoria'


class CategoriasListView(CustomListView):
    model = Categoria
    template_name = 'cadastro/produto/categoria_list.html'
    context_object_name = 'all_categorias'
    success_url = reverse_lazy('cadastro:listacategoriasview')
    permission_codename = 'view_categoria'


class EditarCategoriaView(EditarOutrosBaseView):
    form_class = CategoriaForm
    model = Categoria
    success_url = reverse_lazy('cadastro:listacategoriasview')
    permission_codename = 'change_categoria'


class AdicionarUnidadeView(AdicionarOutrosBaseView):
    form_class = UnidadeForm
    model = Unidade
    success_url = reverse_lazy('cadastro:addunidadeview')
    permission_codename = 'add_unidade'


class UnidadesListView(CustomListView):
    model = Unidade
    template_name = 'cadastro/produto/unidade_list.html'
    context_object_name = 'all_unidades'
    success_url = reverse_lazy('cadastro:listaunidadesview')
    permission_codename = 'view_unidade'


class EditarUnidadeView(EditarOutrosBaseView):
    form_class = UnidadeForm
    model = Unidade
    success_url = reverse_lazy('cadastro:listaunidadesview')
    permission_codename = 'change_unidade'


class AdicionarMarcaView(AdicionarOutrosBaseView):
    form_class = MarcaForm
    model = Marca
    success_url = reverse_lazy('cadastro:addmarcaview')
    permission_codename = 'add_marca'


class MarcasListView(CustomListView):
    model = Marca
    template_name = 'cadastro/produto/marca_list.html'
    context_object_name = 'all_marcas'
    success_url = reverse_lazy('cadastro:listamarcasview')
    permission_codename = 'view_marca'


class EditarMarcaView(EditarOutrosBaseView):
    form_class = MarcaForm
    model = Marca
    success_url = reverse_lazy('cadastro:listamarcasview')
    permission_codename = 'change_marca'


class AdicionarGrupoView(AdicionarOutrosBaseView):
    form_class = GrupoForm
    model = Grupo
    success_url = reverse_lazy('cadastro:addgrupoview')
    permission_codename = 'add_grupo'


class GrupoListView(CustomListView):
    model = Grupo
    template_name = 'cadastro/cliente/grupo_list.html'
    context_object_name = 'all_grupos'
    success_url = reverse_lazy('cadastro:listagrupoview')
    permission_codename = 'view_grupo'


class EditarGrupoView(EditarOutrosBaseView):
    form_class = GrupoForm
    model = Grupo
    success_url = reverse_lazy('cadastro:listagrupoview')
    permission_codename = 'change_grupo'

class AdicionarStatusVendaView(AdicionarOutrosBaseView):
    form_class = StatusVendaForm
    model = StatusVenda
    success_url = reverse_lazy('cadastro:addstatusvendaview')
    permission_codename = 'add_status_venda'


class StatusVendaListView(CustomListView):
    model = StatusVenda
    template_name = 'cadastro/produto/status_venda_list.html'
    context_object_name = 'all_status_venda'
    success_url = reverse_lazy('cadastro:listastatusvendaview')
    permission_codename = 'view_status_venda'

class EditarStatusVendaView(EditarOutrosBaseView):
    form_class = StatusVendaForm
    model = StatusVenda
    success_url = reverse_lazy('cadastro:listastatusvendaview')
    permission_codename = 'change_status_venda'

class StatusVendaViewEmNavegacao(ListView):
    template_name = "crm2/navegacao/navegacao.html"
    model = StatusVenda
    context_object_name = "all_status_venda"
