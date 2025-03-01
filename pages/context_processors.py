from mods.models import Game

def navbar_games(request):
  all_games = Game.objects.all()
  return {'navbar_games': all_games}