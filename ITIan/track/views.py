from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Track
from .serializers import TrackSerializer
from rest_framework import viewsets


# Function-based view for tracking updates
@api_view(["GET", "PUT"])
def track_update(request, pk):
    try:
        track = Track.objects.get(pk=pk)
    except Track.DoesNotExist:
        return Response({"error": "Track not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TrackSerializer(track)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = TrackSerializer(track, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
