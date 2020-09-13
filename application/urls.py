from .views import AssignmentViewSet,AssignmentDetailSet,GAssignmentListView,GAssignmentCreateView,checkassignmentView,FeedViewSet,assignViewSet,assignsubmitViewSet,GAssignmentListView1
from rest_framework import routers
from django.urls import path


router = routers.DefaultRouter()
router.register(r'feed', FeedViewSet,basename="feeds")
router.register(r'hw',assignViewSet)
router.register(r'hwsubmit',assignsubmitViewSet)

urlpatterns = [
    path('assignment/', AssignmentViewSet.as_view()),
    path('assignment/<pk>', AssignmentDetailSet.as_view()),

    path('gassignment/',GAssignmentListView.as_view()),
    path('gassignment1/',GAssignmentListView1.as_view()),
    path('gassignment/create/',GAssignmentCreateView.as_view()),
    path('check/',checkassignmentView.as_view())
]
urlpatterns+=router.urls



