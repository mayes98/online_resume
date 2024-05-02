from django.contrib import admin

from .models import (
	ContactProfile,
	Testimonial,
	Portfolio,
	UserProfile,
	Blog,
	Certificate,
	Skill,
	)

@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
	list_dispay = ('id', 'user')
	
@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('id', 'timestamp', 'name')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'is_active')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'is_active')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	list_display = ('timestamp', 'title', 'is_active')

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'score')
