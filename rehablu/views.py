# Phase 1: Create a Django app named "rehablu" and set up the models

# rehablu/views.py

from rest_framework import viewsets
from .models import SubjectGrade
from .serializers import SubjectGradeSerializer

class SubjectGradeViewSet(viewsets.ModelViewSet):
    queryset = SubjectGrade.objects.all()
    serializer_class = SubjectGradeSerializer

# Phase 3: Career & Brain Boosters (3 Features)
# Feature 1: Find a Job

from rest_framework import viewsets
from .models import Job
from .serializers import JobSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

# Feature 2: Pick a Movie

from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

# Feature 3: Random Fun Fact

from .models import FunFact
from .serializers import FunFactSerializer

class FunFactViewSet(viewsets.ModelViewSet):
    queryset = FunFact.objects.all()
    serializer_class = FunFactSerializer

# Phase 4: Hero Dashboard

from rest_framework import viewsets, permissions
from .models import StudyGroup, HeroDashboard
from .serializers import StudyGroupSerializer, HeroDashboardSerializer

class StudyGroupViewSet(viewsets.ModelViewSet):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer

class HeroDashboardViewSet(viewsets.ModelViewSet):
    queryset = HeroDashboard.objects.all()
    serializer_class = HeroDashboardSerializer
    
# chatbot for  mood tracker/ Mental Health
from .models import OpenAIChat
from .serializers import OpenAIChatSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import openai
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class OpenAIChatViewSet(viewsets.ViewSet):
    queryset = OpenAIChat.objects.all()
    serializer_class = OpenAIChatSerializers
    
    def create(self, request):
        api_key = settings.OPENAI_API_KEY
        user_message = request.data.get("messages", "").strip()

        if not api_key:
            logger.error("OpenAI API key is missing")
            return Response(
                {"error": "API key is missing."}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        if not user_message:
            logger.error("Empty message received")
            return Response(
                {"error": "Message is required."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        openai.api_key = api_key

        try:
            # Get response from OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_message}],
                temperature=0.7,
                max_tokens=500
            )
            
            ai_response = response['choices'][0]['message']['content']
            
            # Save conversation to database
            chat = OpenAIChat.objects.create(
                messages=f"User: {user_message}\nAI: {ai_response}"
            )
            
            # Return both the AI response and saved chat data
            return Response({
                "response": ai_response,
                # "messages": f"User: {user_message}\nAI: {ai_response}",
                "chat_id": chat.id
            }, status=status.HTTP_201_CREATED)
            
        except openai.error.AuthenticationError:
            logger.error("OpenAI authentication failed")
            return Response(
                {"error": "Authentication with OpenAI failed."}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
        except openai.error.RateLimitError:
            logger.error("OpenAI rate limit exceeded")
            return Response(
                {"error": "Rate limit exceeded. Please try again later."}, 
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )
        except Exception as e:
            logger.error(f"OpenAI API error: {str(e)}")
            return Response(
                {"error": f"Failed to get response from OpenAI: {str(e)}"}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
# Run Hablu, Run

from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Marathon
from .serializers import MarathonSerializer

class MarathonViewSet(ViewSet):
    queryset = Marathon.objects.all()
    serializer_class = MarathonSerializer

    def list(self, request, *args, **kwargs):
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')

        queryset = self.queryset

        if lat and lon:
            try:
                lat = float(lat)
                lon = float(lon)
                queryset = queryset.filter(
                    latitude__range=(lat - 0.5, lat + 0.5),
                    longitude__range=(lon - 0.5, lon + 0.5)
                )
            except ValueError:
                return Response({'error': 'lat and lon must be float values.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = MarathonSerializer(queryset, many=True)
        return Response(serializer.data)