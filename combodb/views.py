from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from combodb.forms import GameForm, CharacterForm, AbilityForm, ComboForm
from combodb.models import Game, Character, Ability, Combo

def new_game(request):
    if request.method == 'POST':
        #print request.POST

        game = Game()
        form = GameForm(request.POST, instance=game)

        if form.is_valid():
            if request.POST.get('title', "").find(',') != -1:
                print 'submitting multiple'
                gameList = request.POST.get('title', "").split(',')
                for i in gameList:
                    game = Game()
                    game.title = i.lstrip()
                    game.save()
                    return HttpResponseRedirect('/combodb/new_game.html')
            else:
                try:
                    print 'submitting single'
                    game = form.save()
                    return HttpResponseRedirect('/combodb/new_game.html')
                except Exception, e:
                    print e

    else:
        form = GameForm()

    return render_to_response('combodb/new_game.html', {'form': form}, context_instance=RequestContext(request))


def new_character(request):
    if request.method == 'POST':

        character = Character()
        form = CharacterForm(request.POST, instance=character)
        game = request.POST.get('game', "")
        print game
        if form.is_valid():
            if request.POST.get('name', "").find(',') != -1:
                print 'submitting multiple'
                characterList = request.POST.get('name', "").split(', ')
                for i in characterList:
                    character = Character()
                    character.game = Game.objects.get(id=game)
                    character.name = i
                    character.save()
                    return HttpResponseRedirect('/combodb/new_character.html')
            else:
                try:
                    print 'submitting single'
                    character = form.save()
                    return HttpResponseRedirect('/combodb/new_character.html')
                except Exception, e:
                    print e

    else:
        form = CharacterForm()

    return render_to_response('combodb/new_character.html', {'form': form}, context_instance=RequestContext(request))


def new_ability(request):
    if request.method == 'POST':
        ability = Ability()
        form = AbilityForm(request.POST, instance=ability)

        if form.is_valid():
            try:
                ability = form.save()
                return HttpResponseRedirect('/combodb/new_ability.html')
            except Exception, e:
                print e

    else:
        form = AbilityForm()

    return render_to_response('combodb/new_ability.html', {'form': form}, context_instance=RequestContext(request))