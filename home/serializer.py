from rest_framework import serializers
from .models import Todo
import re
from django.template.defaultfilters import slugify
from .models import TimingTodo

class TodoSerializer(serializers.ModelSerializer):

    slug = serializers.SerializerMethodField()


    class Meta:
        model = Todo
       # fields = '__all__'
        fields = [ 'slug', 'todo_description']


    def get_slug(self, obj):
        return slugify(obj.todo_title)
        #return 'Anjali'    


    def validate(self, validated_data):
        print(validated_data)
        if validated_data.get('todo_title'):
            todo_title = validated_data['todo_title']
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
            if not regex.search(todo_title) == None:
                raise serializers.ValidationError('todo_title cannot contain special character') 

        return validated_data  




class TimingTodoSerializer(serializers.ModelSerializer):

    todoo = TodoSerializer()

    class Meta:
        model = TimingTodo
        exclude = ['created_at', 'updated_at']
      #  depth = 1