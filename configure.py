import sys

# Bootstrap the Sentry environment
from sentry.utils.runner import configure
configure(sys.argv[1])

# Do something crazy
from sentry.models import Team, Project, ProjectKey, User, Organization

user = User()
user.username = 'admin'
if User.objects.filter(username = user.username).exists():
	print("User admin already exists")
else:	
	user.email = 'admin@localhost'
	user.is_superuser = True
	user.set_password('admin')
	user.save()
