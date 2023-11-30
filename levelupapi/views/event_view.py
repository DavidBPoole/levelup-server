"""View module for handling requests about game types"""
# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event, Game, Gamer

class EventView(ViewSet):
    """Level up game events view"""

    def retrieve(self, request, pk):
        """Handle GET requests for a single event

        Returns:
            Response -- JSON serialized event
        """
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all events

        Returns:
            Response -- JSON serialized list of events
        """
        # try:
        events = Event.objects.all()
        game = request.query_params.get('gameID', None)
        if game is not None:
            events = events.filter(game_id=game)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    # def create(self, request):
    #     """Handle POST operations

    #     Returns
    #         Response -- JSON serialized event instance
    #     """
    #     try:
    #         # Retrieve data from request.data
    #         user_id = request.data.get("userId")
    #         game_type_id = request.data.get("gameType")
    #         game = request.data.get("game")
    #         date = request.data.get("date")
    #         description = request.data.get("description")
    #         time= request.data.get("time")
    #         event_data = {
    #             "game": request.data.get("game"),
    #             "description": request.data.get("description"),
    #             "date": request.data.get("date"),
    #             "time": request.data.get("time"),
    #             "organizer": request.data.get("organizer"),
    #         }

    #         # Get or create Event and GameType instances
    #         event, created = Event.objects.get_or_create(uid=user_id)
    #         game_type = GameType.objects.get(pk=game_type_id)

    #         # Create Event instance
    #         event = Event.objects.create(
    #             game=game,
    #             description=description,
    #             date=date,
    #             time=time,
    #             **event_data,
    #         )

    #         serializer = CreateEventSerializer(event)
    #         return Response(serializer.data)
    #     except Exception as ex:
    #         return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # def create(self, request):
    #     """Handles POST operations"""
    #     try:

    #         request_data_dict = request.data[0]

    #         game = Game.objects.get(pk=request_data_dict["game"])
    #         organizer = Gamer.objects.get(uid=request_data_dict["userId"])

    #         event = Event.objects.create(
    #             description=request_data_dict["description"],
    #             date=request_data_dict["date"],
    #             time=request_data_dict["time"],
    #             game=game,
    #             organizer=organizer
    #         )
    #         serializer = EventSerializer(event)
    #         return Response(serializer.data)
    #     except Exception as ex:
    #         return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # create event final - allison
    # def create(self, request):
    #     """Handle POST operations
        
    #     Returns -- JSON serialized event instance"""

    #     game = Game.objects.get(pk=request.data["gameId"])
    #     organizer = Gamer.objects.get(uid=request.META['HTTP_AUTHORIZATION'])

    #     event = Event.objects.create(
    #         description=request.data["description"],
    #         date=request.data["date"],
    #         time=request.data["time"],
    #         organizer=organizer,
    #         game=game,
    #     )
    #     serializer = EventSerializer(event)
    #     return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized event instance
        """
        game = Game.objects.get(pk=request.data["game"])
        gamer = Gamer.objects.get(uid=request.data["organizer"])

        event = Event.objects.create(
            description=request.data["description"],
            date=request.data["date"],
            time=request.data["time"],
            game=game,
            organizer=gamer,
        )
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for an event

        Returns:
            Response -- Empty body with 204 status code
        """
        try:
            event = Event.objects.get(pk=pk)
            event.description = request.data["description"]
            event.date = request.data["date"]
            event.time = request.data["time"]

            game_id = request.data.get("game")
            if game_id:
                event.game = Game.objects.get(pk=game_id)

            event.save()

            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk):
        """ DELETE Function """
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'game', 'description', 'date', 'time']

class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    class Meta:
        model = Event
        fields = ('id', 'game', 'description', 'date', 'time', 'organizer')
        depth = 2
