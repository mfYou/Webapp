from rest_framework import serializers
from recommender.models import UserInfo, Community

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('idnum', 'realname', 'jobnum', 'phonenum', 'password', 'gender', 'sortkey', 'city', 'school', 'faceimage', 'rankscore', 'creditscore', 'createtime', 'job', 'nickname', 'sign', 'admin')

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ('message_id', 'user', 'message_text', 'message_type', 'message_url', 'update_time', 'praise')