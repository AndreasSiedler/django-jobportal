from rest_framework import viewsets, mixins, status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import Job, Skill
from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView
from .permissions import IsCreator
import json



class JobList(ListAPIView):
    serializer_class: JobSerializer

    def get_queryset(self):
        """
        This view should return a list of filtered Jobs
        """
        search_query = json.loads(self.request.body.decode('utf-8')).get('search')
        print(search_query)
        return Job.objects.filter(name__contains=search_query)


class JobViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows jobs to be viewed or edited.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes_by_action = {   
        'create': [permissions.IsAuthenticated],
        'partial_update': [permissions.IsAuthenticated, IsCreator],
        # 'default': [permissions.IsAuthenticated]
    }

    def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        # token = self.request.META.get('HTTP_AUTHORIZATION', '').split()[1]
        # payload = jwt_decode_handler(token)
        # auth0_user_id = payload.get('sub')
        # Set the user to the one in the token.
        serializer.save(created_by=self.request.user.id)

    # def get_queryset(self):
    #     """
    #     This view should return a list of all Tasks
    #     for the currently authenticated user.
    #     """
    #     # token = self.request.META.get('HTTP_AUTHORIZATION', '').split()[1]
    #     # payload = jwt_decode_handler(token)
    #     # auth0_user_id = payload.get('sub')
    #     return Job.objects.filter(created_by=self.request.user.id)


class SkillViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows skills to be viewed or edited.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
class SearchApiView(ListAPIView):
    serializer_class = JobSerializer

    def get_queryset(self):
        if 'location' in self.request.GET and 'position' in self.request.GET:
            return self.serializer_class.Meta.model.objects.filter(location__contains=self.request.GET['location'],
                                                                   title__contains=self.request.GET['position'])
        else:
            return self.serializer_class.Meta.model.objects.all()


class ApplyJobApiView(CreateAPIView):
    serializer_class = ApplicantSerializer
    http_method_names = [u'post']
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
