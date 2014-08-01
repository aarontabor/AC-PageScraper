from django.test import TestCase
from django.contrib.auth.models import User


class ViewTestCase(TestCase):
  
  def setUp(self):
    self.workAroundForSessionBug()


  def workAroundForSessionBug(self):
    # work around for a known bug in dJango
    # in testing framework, session only works with a user context
    User.objects.create_user('bill', 'bill@email.com', 'password')
    self.client.login(username='bill', password='password')

  def setSession(self, sessionDict):
    session = self.client.session
    for k, v in sessionDict.items():
      session[k] = v
    session.save()

