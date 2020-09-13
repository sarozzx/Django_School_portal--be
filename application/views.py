from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .serializers import AssignmentSerializer,GAssignmentSerializer,checkassignmentSerializer,feedSeriliazer,assignSerializer,assignsubmitSerializer
from rest_framework.views import APIView
from .models import Assignment,GAssignment,feed,assign,assignsubmit
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework import status,viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView,CreateAPIView


class AssignmentViewSet(APIView):

    # permission_classes = [
    #     IsAuthenticated
    # ]
    def get_queryset(self):
        return Assignment.objects.all().order_by('-id')


    def get(self, request):
        queryset=self.get_queryset()
        serializer_class = AssignmentSerializer(instance=queryset,many=True)
        return Response(serializer_class.data)

    def post(self,request):
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            assignment = serializer.create(request)
            if assignment:
                return Response(status=status.HTTP_201_CREATED)

class checkassignmentView(CreateAPIView):
    serializer_class = checkassignmentSerializer
    def post(self, request, *args, **kwargs):
        serializer = checkassignmentSerializer(data=request.data)
        # print(request.data)
        if serializer.is_valid(raise_exception=True):
            check_assignment = serializer.create(request)
            if check_assignment:
                return Response(check_assignment)




class AssignmentDetailSet(APIView):

    # permission_classes = [
    #     IsAuthenticated
    # ]

    # def filter(self, id):
    #     return self.queryset.filter(id=id)

    def get(self, request, pk):
        queryset = get_object_or_404(Assignment,id=pk)
        serializer_class = AssignmentSerializer(instance=queryset)
        return Response(serializer_class.data)

class GAssignmentListView(ListAPIView):
    serializer_class = GAssignmentSerializer
    def get_queryset(self):
        queryset = GAssignment.objects.all().order_by('-id')
        username=self.request.query_params.get('username',None)
        if username is not None:
            queryset=queryset.filter(student__username=username)
        return queryset

class GAssignmentListView1(ListAPIView):
    serializer_class = GAssignmentSerializer
    def get_queryset(self):
        queryset = GAssignment.objects.all().order_by('-id')
        assign_id=self.request.query_params.get('assign_id',None)
        if assign_id is not None:
            print(assign_id)
            queryset=queryset.filter(assignment_id=assign_id)
        return queryset

class GAssignmentCreateView(CreateAPIView):
    serializer_class = GAssignmentSerializer
    queryset = GAssignment.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = GAssignmentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            g_assignment = serializer.create(request)
            if g_assignment:
                return Response(status=status.HTTP_201_CREATED)


class FeedViewSet(viewsets.ModelViewSet):
    queryset=feed.objects.all().order_by('-id')
    serializer_class=feedSeriliazer

    def create(self, request, *args, **kwargs):
        serializer=feedSeriliazer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            feed_create = serializer.create(request)
            if feed_create:
                return Response(status=status.HTTP_201_CREATED)

class assignViewSet(viewsets.ModelViewSet):
    queryset = assign.objects.all().order_by('-id')
    serializer_class = assignSerializer

    def create(self, request, *args, **kwargs):
        hw=request.data['hw']
        title=request.data['title']
        assign.objects.create(title=title,hw=hw)
        return Response(status=status.HTTP_201_CREATED)

class assignsubmitViewSet(viewsets.ModelViewSet):
    queryset = assignsubmit.objects.all()
    serializer_class = assignsubmitSerializer
    def get_queryset(self):
        queryset = assignsubmit.objects.all().order_by('-id')
        assign_id = self.request.query_params.get('assign_id', None)
        if assign_id is not None:
            print(assign_id)
            queryset = queryset.filter(assignment_id=assign_id)
        return queryset

    def create(self, request, *args, **kwargs):

        serializer = assignsubmitSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            submitdata = serializer.create(request)
            if submitdata:
                return Response(status=status.HTTP_201_CREATED)
