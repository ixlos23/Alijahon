from django.conf.urls.static import static
from root import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.contrib import admin
from django.urls import path, include

from apps.views import CategoryListView, CustomLoginView, ProductListView, \
    WishListView, OrderListView, Likedview, MarketListView, RequestsView, ConcourseView, \
    DiagramView, PaymentView, StreamFormView, StreamListView, ProductDetailView, StreamStatisticsListView, \
    Stream_indetail_DetailView, StreamOrderView, Button_adminView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', CategoryListView.as_view(), name='home'),
    path('product/list', ProductListView.as_view(), name='product_list'),
    path('product/detail/<str:slug>', ProductDetailView.as_view(), name='product_detail'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('wishlist', WishListView.as_view(), name='wishlist'),
    path('product/liked/<str:slug>', Likedview.as_view(), name='liked'),
    path('product/order-list', OrderListView.as_view(), name='order-list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                           document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('admin_page/market', MarketListView.as_view(), name='market'),
    path('diagram',DiagramView.as_view(), name='diagram'),
    path('payments',PaymentView.as_view(), name='payments'),
    path('requests',RequestsView.as_view(), name='requests'),
    path('councourse',ConcourseView.as_view(), name='concourse'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                           document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('stream/form', StreamFormView.as_view(), name='stream-form'),
    path('stream/statistics',StreamStatisticsListView.as_view(), name='statistics'),
    path('stream/list', StreamListView.as_view(), name='stream-list'),
    path('stream/in_detail/<str:slug>', Stream_indetail_DetailView.as_view(), name='in_detail'),
    path('oqim/<int:pk>', StreamOrderView.as_view(), name='in_detail'),
    path('buttons', Button_adminView.as_view(), name='buttons'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                           document_root=settings.STATIC_ROOT)


