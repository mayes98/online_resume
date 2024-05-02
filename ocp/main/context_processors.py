from django.contrib.auth import get_user_model
CustomUser = get_user_model()

def project_context(request):

	me = CustomUser.objects.get(username='Kennedy')

	return {'me': me}