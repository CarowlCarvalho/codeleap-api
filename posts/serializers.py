from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    time_ago = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = [
            'id', 
            'username', 
            'title', 
            'content', 
            'created_datetime', 
            'updated_datetime', 
            'time_ago'
        ]
        read_only_fields = [
            'id', 
            'created_datetime', 
            'updated_datetime', 
            'time_ago'
        ]
    
    def get_time_ago(self, obj):
        from django.utils import timezone
        from django.utils.timesince import timesince
        
        now = timezone.now()
        difference = now - obj.created_datetime
        
        if difference.days == 0:
            if difference.seconds < 60:
                return "just now"
            elif difference.seconds < 3600:
                minutes = difference.seconds // 60
                return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
            else:
                hours = difference.seconds // 3600
                return f"{hours} hour{'s' if hours > 1 else ''} ago"
        elif difference.days == 1:
            return "yesterday"
        else:
            return timesince(obj.created_datetime) + " ago"

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['username', 'title', 'content']
    
    def validate_username(self, value):
        if not value.strip():
            raise serializers.ValidationError("Username cannot be empty")
        return value
    
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty")
        return value
    
    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Content cannot be empty")
        return value

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']
    
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty")
        return value
    
    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Content cannot be empty")
        return value