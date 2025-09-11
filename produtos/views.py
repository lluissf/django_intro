from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Produto, Categoria
from .serializers import ProdutoSerializer, CategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
  queryset = Produto.objects.all()
  serializer_class = ProdutoSerializer 
  # Filtros
  filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
  filterset_fields = ['preco', 'estoque', 'categoria']  # Filtragem exata por preço, estoque e categoria
  search_fields = ['nome', 'descricao']  # Busca textual
  ordering_fields = ['nome', 'preco', 'estoque']  # Ordenação
  ordering = ['id']  # Ordenação padrão 

class CategoriaViewSet(viewsets.ModelViewSet):
  queryset = Categoria.objects.all()
  serializer_class = CategoriaSerializer
  # Filtros
  filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
  filterset_fields = ['nome']  # Filtragem exata por nome
  search_fields = ['nome']  # Busca textual
  ordering_fields = ['nome']  # Ordenação
  ordering = ['id']  # Ordenação padrão