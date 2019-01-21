from rest_framework import serializers

from classview.models import Book


class BookInfoSerializer(serializers.ModelSerializer):
    """图书数据序列化器"""
    class Meta:
        model = Book
        fields = '__all__'

# serializers.ModelSerializer()
class Bookserializers(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_date = serializers.DateField(label='发布日期', required=True)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    image = serializers.ImageField(label='图片', required=False)
    # serializer = AccountSerializer(account, context={'request': request})
    # serializers.PrimaryKeyRelatedField()

# Bookserializers()