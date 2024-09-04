# from advertisement.models import Advertisement
# from advertisement.serializers import AdvertisementSerializer
from common.utils.create_slug import create_slug
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError, transaction
from django.db.models import Case, ExpressionWrapper, F, FloatField, Sum, When
from django_filters.rest_framework import DjangoFilterBackend
# from openpyxl import load_workbook
from rest_framework import filters, status, viewsets
from rest_framework.generics import (
    DestroyAPIView,
    GenericAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .filters import ProductFilter
from .mixins import CheckProductManagerGroupMixin, CheckSupplierAdminGroupMixin
from .models import Brand,Category,Product
from .pagination import ProductPagination
from .serializers import (
    BrandSerializer,
    CategorySerializer,
    ProductSerializer,
)
from django.http import Http404



class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()

    def list(self, request):
        featured = request.GET.get("featured")
        parent_slug = request.GET.get("parent")
        if featured == "true":
            queryset = self.queryset.filter(is_featured=True)
        else:
            try:
                queryset = self.queryset.all()
                if parent_slug:
                    queryset = self.queryset.filter(parent__slug=parent_slug)
            except Category.DoesNotExist:
                raise Http404 ('Category not found.')
        serializer = CategorySerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)




class BrandViewSet( viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # limit = int(request.GET.get("limit")) if request.GET.get("limit") else None
        # if limit:
        #     queryset = queryset[:limit]

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

class ProductViewSet( viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ["created","name",]

    # filterset_class = ProductFilter
    # ordering = "name"
    # pagination_class = ProductPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_available=True, stock_quantity__gt=0)
        try:
            category_slug = self.request.GET.get("category")
            category=Category.objects.get(slug=category_slug)
            descendant_categories=category.get_descendants(include_self=False)
            queryset=queryset.filter(category__in=descendant_categories)
        except Category.DoesNotExist:
                raise Http404 ('Category not found.')
        return queryset


