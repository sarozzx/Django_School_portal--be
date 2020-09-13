from rest_framework import serializers

from .models import Assignment,Question,Choice,GAssignment, checkassignment, feed,assign,assignsubmit
from users.models import User
from datetime import datetime


class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, data):
        return data

class QuestionSerializer(serializers.ModelSerializer):
    choices=StringSerializer(many=True)
    class Meta:
        model=Question
        fields=('id','choices','question','order')

class AssignmentSerializer(serializers.ModelSerializer):
    questions=serializers.SerializerMethodField()
    teacher=StringSerializer(many=False)

    class Meta:
        model=Assignment
        fields=('__all__')

    def get_questions(self,obj):
        questions=QuestionSerializer(obj.questions.all(),many=True).data
        return questions

    def create(self,request):
        data=request.data
        print(data)

        assignment=Assignment()
        teacher=User.objects.get(username=data['teacher'])
        assignment.teacher=teacher
        assignment.title=data['title']
        assignment.save()

        order=1
        for q in data['questions']:
            newQ=Question()
            newQ.question=q['question']
            newQ.order=order
            order+=1
            newQ.save()

            for c in q['choices']:
                newC,created=Choice.objects.get_or_create(title=c)
                newQ.choices.add(newC)
            newQ.answer=Choice.objects.get(title=q['answer'])
            newQ.assignment=assignment
            newQ.save()
        return assignment

class GAssignmentSerializer(serializers.ModelSerializer):
    student=StringSerializer(many=False)
    assignment=StringSerializer(many=False)
    class Meta:
        model=GAssignment
        fields=('__all__')

    def create(self,request):
        data=request.data
        print(data)

        assignment=Assignment.objects.get(id=data['asntID'])
        student=User.objects.get(username=data['username'])

        graded_asnt=GAssignment()
        graded_asnt.assignment=assignment
        graded_asnt.student=student

        questions=[q for q in assignment.questions.all()]
        answers=[data['answer'][a] for a in data['answer']]

        correct_ans=0

        for i in range(len(questions)):
            if questions[i].answer.title==answers[i]:
                correct_ans+=1
            i+=1
        grade=correct_ans/len(questions)*100

        graded_asnt.grade=grade
        graded_asnt.save()
        return graded_asnt

class checkassignmentSerializer(serializers.ModelSerializer):
    student = StringSerializer(many=False)

    class Meta:
        model = checkassignment
        fields = ('__all__')

    def create(self, request):
        data = request.data
        print(data)

        assignment = Assignment.objects.get(id=data['asntID'])
        student = User.objects.get(username=data['username'])

        if GAssignment.objects.filter(assignment=assignment,student=student).exists():
            status={
                "exists":True
            }
        else:
            status={
                "exists":False
            }
        return status

class feedSeriliazer(serializers.ModelSerializer):
    teacher = StringSerializer(many=False)
    class Meta:
        model = feed
        fields=('__all__')

    def create(self, request):
        data=request.data
        print(data)

        teacher=User.objects.get(username=data['teacher'])
        feedt=feed()

        feedt.teacher=teacher
        feedt.feedtxt=data['feedtxt']

        x=datetime.now()
        d = x.strftime("%I%p,%d %b")
        print(d)

        feedt.created=d
        feedt.save()

class assignSerializer(serializers.ModelSerializer):
    class Meta:
        model=assign
        fields=('__all__')

class assignsubmitSerializer(serializers.ModelSerializer):
    # assignment = StringSerializer(many=False)
    student=StringSerializer(many=False)
    class Meta:
        model=assignsubmit
        fields=('__all__')


    def create(self, request):
        data=request.data
        print(data)
        hw=assignsubmit()
        hw.hwsubmitted = data['hwsubmitted']

        student = User.objects.get(id=data['student'])
        hw.student=student

        assignment=assign.objects.get(id=data['assignment'])
        hw.assignment=assignment
        hw.save()
        return hw

