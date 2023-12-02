# from django.db import models
# from .game import Game
# from .gamer import Gamer


# class Event(models.Model):

#     game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='events')
#     description = models.CharField(max_length=100)
#     date = models.DateField()
#     time = models.TimeField()
#     organizer = models.ForeignKey(Gamer, on_delete=models.CASCADE, related_name='user_event')

#     objects = models.Manager()

# alternate code:
# from django.db import models
# from .game import Game
# from .gamer import Gamer


# class Event(models.Model):

#     game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='events')
#     description = models.CharField(max_length=300)
#     date = models.DateField()
#     time = models.TimeField()
#     organizer = models.ForeignKey(Gamer, on_delete=models.CASCADE)

#     @property
#     def joined(self):
#         """Join"""
#         return self.__joined

#     @joined.setter
#     def joined(self, value):
#         self.__joined = value

# alternate code 2:
from django.db import models
from .game import Game
from .gamer import Gamer


class Event(models.Model):

    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='event')
    description = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    organizer = models.ForeignKey(Gamer, on_delete=models.CASCADE, related_name='event')

# new code added here - delete if breaks:
    # def get_joined_users(self):
    #     return list(self.eventgamer_set.filter().values_list('gamer__bio', flat=True))

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
        