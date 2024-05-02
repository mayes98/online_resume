from django.shortcuts import render, redirect
from .models import(
	ContactProfile,
	Blog,
	Portfolio,
	Testimonial,
	Certificate,
	)

from django.views import generic

from .forms import ContactForm

	
def searchview(request):
	query = request.GET.get('q')
	qs = Blog.objects.search(query=query)
	context = {
	"blog_list": qs
	}
	return render (request, "main/search.html", context=context)


class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context["testimonials"] = Testimonial.objects.filter(is_active=True)
		context["certificates"] = Certificate.objects.filter(is_active=True)
		context["blogs"] = Blog.objects.filter(is_active=True).order_by('-timestamp')[:2]
		context["portfolios"] = Portfolio.objects.filter(is_active=True)
		return context

class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = ContactForm
	success_url = "/"

	def form_valid(self, form):
		form.save()
		messages.success(self.request, "Thank you, I'll get back to you ASAP")
		return super().form_valid(form)

class PortfolioView(generic.ListView):
	model = Portfolio
	context_object_name = "portfolio_checklist"
	template_name = "main/portfolio.html"
	paginate_by = 6

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)

class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	context_object_name = "portfolio_info"
	template_name = "main/portfolio-detail.html"

class BlogView(generic.ListView):
	model = Blog
	context_object_name = "blog_checklist"
	template_name = "main/blog.html"
	paginate_by = 8 

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)

class BlogDetailView(generic.DetailView):
	model = Blog
	context_object_name = "blog_info"
	template_name = "main/blog-detail.html"
