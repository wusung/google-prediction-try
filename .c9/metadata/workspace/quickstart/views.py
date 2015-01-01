{"filter":false,"title":"views.py","tooltip":"/quickstart/views.py","undoManager":{"mark":2,"position":2,"stack":[[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.shortcuts import render","","# Create your views here.",""]},{"start":{"row":0,"column":0},"end":{"row":18,"column":38},"action":"insert","lines":["from django.contrib.auth.models import User, Group","from rest_framework import viewsets","from tutorial.quickstart.serializers import UserSerializer, GroupSerializer","","","class UserViewSet(viewsets.ModelViewSet):","    \"\"\"","    API endpoint that allows users to be viewed or edited.","    \"\"\"","    queryset = User.objects.all()","    serializer_class = UserSerializer","","","class GroupViewSet(viewsets.ModelViewSet):","    \"\"\"","    API endpoint that allows groups to be viewed or edited.","    \"\"\"","    queryset = Group.objects.all()","    serializer_class = GroupSerializer"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":5},"end":{"row":2,"column":13},"action":"remove","lines":["tutorial"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"remove","lines":["."]}]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":11,"column":0},"end":{"row":11,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1419929034171,"hash":"902e90c229ff6436db4cadc7b42a6a40944d1c25"}