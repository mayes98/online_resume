from django.urls import path
from .import views

app_name = "main"

urlpatterns = [
	path('', views.IndexView.as_view(), name="home"),
	path('contact/', views.ContactView.as_view(), name="contact"),
	path('portfolio/', views.PortfolioView.as_view(), name="portfolio_list"),
	path('portfolio/<uuid:pk>', views.PortfolioDetailView.as_view(), name="portfolio_detail"),

	path('search/', views.searchview, name="search"),
	path('blog/', views.BlogView.as_view(), name="blog_list"),
	path('blog/<uuid:pk>', views.BlogDetailView.as_view(), name="blog_detail"),
	]
