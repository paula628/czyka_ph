from django.conf import settings
from django.shortcuts import render

def main(request):
	args = {}
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		file_loc = settings.MEDIA_ROOT + "/contacts.txt"
		fh = open(file_loc, "a")
		fh.write('; ' + name + '-' + email)
		fh.close
		args['submit'] = True
	return render(request, 'main.html', args)
