"""View module for handling requests about game views"""
# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game, Gamer, GameType

class GameView(ViewSet):
    """Level up game views"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game

        Returns:
            Response -- JSON serialized game
        """
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game)
            return Response(serializer.data)
        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        """Handle GET requests to get all games

        Returns:
            Response -- JSON serialized list of games
        """

        games = Game.objects.all()
        game_type = request.query_params.get('type', None)
        if game_type is not None:
            games = games.filter(game_type_id=game_type)
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        try:
            # Retrieve data from request.data
            user_id = request.data.get("gamer")
            game_type_id = request.data.get("gameType")

            # Creates Game data dictionary
            game_data = {
                "title": request.data.get("title"),
                "maker": request.data.get("maker"),
                "number_of_players": request.data.get("numberOfPlayers"),
                "skill_level": request.data.get("skillLevel"),
            }

            # Get or create Gamer and GameType instances
            gamer, created = Gamer.objects.get_or_create(uid=user_id)
            game_type = GameType.objects.get(pk=game_type_id)

            # Add game_type and gamer to the game_data dictionary
            game_data["game_type"] = game_type
            game_data["gamer"] = gamer

            # Create Game instances
            game = Game.objects.create(**game_data)

            serializer = CreateGameSerializer(game)
            return Response(serializer.data)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        game = Game.objects.get(pk=pk)
        game.title = request.data["title"]
        game.maker = request.data["maker"]
        game.number_of_players = request.data["numberOfPlayers"]
        game.skill_level = request.data["skillLevel"]

        game_type = GameType.objects.get(pk=request.data["gameType"])
        game.game_type = game_type
        game.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """ DELETE Function """
        game = Game.objects.get(pk=pk)
        game.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class CreateGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'title', 'maker', 'number_of_players',
                  'skill_level', 'game_type', 'gamer']

class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for games
    """
    class Meta:
        model = Game
        fields = ('id', 'game_type', 'title', 'maker',
                  'gamer', 'number_of_players', 'skill_level')
        depth = 1
