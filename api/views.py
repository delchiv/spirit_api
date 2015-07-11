from django.http import JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from rest_framework import status, viewsets
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from spirit.models.category import Category
from spirit.models.topic import Topic
from spirit.models.comment import Comment
from spirit.models.comment_like import CommentLike
from spirit.models.comment_flag import Flag, CommentFlag
from spirit.models.comment_history import CommentHistory
from spirit.models.comment_bookmark import CommentBookmark
from spirit.models.topic_favorite import TopicFavorite
from spirit.views.comment_like import like_create, like_delete
from spirit.views.comment_flag import flag_create

from .models import CustomCategory

# Create your views here.

########################
#     Categories
########################

class CategorySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        try: 
            customcategory = CustomCategory.objects.get(category_ptr=obj)
            return customcategory.image.url
        except:
            pass
        return None

    class Meta:
        model = Category
        fields = map(lambda x: x.name, Category._meta.fields)
        fields += ['image']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

########################
#     Custom Categories
########################

class CustomCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomCategory

class CustomCategoryViewSet(viewsets.ModelViewSet):
    queryset = CustomCategory.objects.all()
    serializer_class = CustomCategorySerializer


########################
#     Topics
########################

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


########################
#     Comments
########################

class CommentSerializer(serializers.ModelSerializer):
    my_like_id = serializers.SerializerMethodField()

    def get_my_like_id(self, obj):
        request = self.context['request']
        user = request.user
        try: 
            like = CommentLike.objects.get(user=user.id, comment_id=obj.id)
            return like.id
        except:
            pass
        return None

    class Meta:
        model = Comment
        fields = map(lambda x: x.name, Comment._meta.fields)
        fields += ['my_like_id']

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def list(self, request, topic_pk=None):
        if topic_pk:
            queryset = Comment.objects.filter(topic_id=topic_pk)
        else:
            queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        serializer.context.update({'request': request})
        return Response(serializer.data)

    
########################
#     Comment Like
########################

@csrf_exempt
def api_like_create(request, comment_id):
    if request.method == 'POST':
        request.META['HTTP_X_REQUESTED_WITH'] = 'XMLHttpRequest'
        return like_create(request, comment_id)

    raise Http404

@csrf_exempt
def api_like_delete(request, pk):
    if request.method == 'POST':
        request.META['HTTP_X_REQUESTED_WITH'] = 'XMLHttpRequest'
        return like_delete(request, pk)

    raise Http404


########################
#     Topics
########################

class FlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flag

class FlagViewSet(viewsets.ModelViewSet):
    queryset = Flag.objects.all()
    serializer_class = FlagSerializer


########################
#     Comment Flag
########################

class CommentFlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentFlag

class CommentFlagViewSet(viewsets.ModelViewSet):
    queryset = CommentFlag.objects.all()
    serializer_class = CommentFlagSerializer


########################
#     Comment History
########################

class CommentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentHistory

class CommentHistoryViewSet(viewsets.ModelViewSet):
    queryset = CommentHistory.objects.all()
    serializer_class = CommentHistorySerializer


########################
#     Comment Bookmark
########################

class CommentBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentBookmark

class CommentBookmarkViewSet(viewsets.ModelViewSet):
    queryset = CommentBookmark.objects.all()
    serializer_class = CommentBookmarkSerializer


########################
#     Topic Favorite
########################

class TopicFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicFavorite

class TopicFavoriteViewSet(viewsets.ModelViewSet):
    queryset = TopicFavorite.objects.all()
    serializer_class = TopicFavoriteSerializer
