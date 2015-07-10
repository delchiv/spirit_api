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
from spirit.views.comment_like import like_create, like_delete

# Create your views here.

########################
#     Categories
########################

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


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
