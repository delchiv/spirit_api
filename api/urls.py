from django.conf.urls import url, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'api/category', views.CategoryViewSet)
router.register(r'api/customcategory', views.CustomCategoryViewSet)
router.register(r'api/topic', views.TopicViewSet)
router.register(r'api/comment', views.CommentViewSet)
router.register(r'api/flag', views.FlagViewSet)
router.register(r'api/commentflag', views.CommentFlagViewSet)
router.register(r'api/commenthistory', views.CommentHistoryViewSet)
router.register(r'api/commentbookmark', views.CommentBookmarkViewSet)
router.register(r'api/topicfavorite', views.TopicFavoriteViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),

    url(r'^api/comments/(?P<topic_pk>\d+)/$', views.CommentViewSet.as_view({'get':'list'})),

    url(r'^api/like/(?P<comment_id>\d+)/create/$', views.api_like_create),
    url(r'^api/like/(?P<pk>\d+)/delete/$', views.api_like_delete),
]

