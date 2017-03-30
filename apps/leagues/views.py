from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"baseballs": League.objects.filter(sport = "Baseball"),
		"women": League.objects.filter(name__contains = "Women"),
		"puckers": League.objects.filter(sport = "Field Hockey")|League.objects.filter(sport = "Ice Hockey"),
		"schmootball": League.objects.exclude(sport = "Football"),
		"conferences": League.objects.filter(name__contains = "Conference"),
		"atlantic": League.objects.filter(name__contains = "Atlantic"),
		"dallas": Team.objects.filter(location = "Dallas"),
		'raptors': Team.objects.filter(team_name__contains = "Raptors"),
		'cities': Team.objects.filter(location__contains = "City"),
		'tteams': Team.objects.filter(team_name__startswith = "T"),
		'alphateam': Team.objects.order_by('location'),
		'betateam': Team.objects.order_by('team_name').reverse(),
		'coopers': Player.objects.filter(last_name = "Cooper"),
		'joshuas': Player.objects.filter(first_name = 'Joshua'),
		'notjoshcooper': Player.objects.filter(last_name = "Cooper").exclude(first_name = "Joshua"),
		'alexandwyatt': Player.objects.filter(first_name = "Alexander")|Player.objects.filter(first_name = "Wyatt"),
		# 'atlanticsoccer': Team.objects.filter(league__name = "Atlantic Soccer Conference"),
		# 'pengins': Players.objects.filter(curr_team__name__contains = "Penguinss"),
		# 'collegebball': Players.objects.filter(curr_team__league__name = "International Collegiate Baseball Conference"),
		# 'lopezez': Players.objects.filter(last_name = "Lopez", curr_team__league__name = "American Conference of Amateur Football"),
		# 'football': Players.objects.filters(curr_team__league__sport ="Football"),
		# 'sophia': Teams.objects.filter(curr_players__first_name = "Sophia"),
		# 'sophialeague': League.objects.filter(team__curr_players__first_name = "Sophia"),
		# 'flores': Players.objects.filter(last_name = "Flores").exclude(curr_team = "Rough Riders"),
		# 'samevans': Teams.objects.filter(all_players__first_name="Samuel", all_players__last_name="Evans"),
		# 'tigercats': Players.objects.filter(all_team__team_name = "tigercats"),
		# 'exvikings': Players.objects.filter(all_team__team_name = "Vikings").exclude(curr_team__team_name = "Vikings"),
		# 'jacob': Teams.objects.filter(all_players__first_name = 'Jacob', all_players__last_name = "Gray")
		# 'joshua': Team.objects.filter(all_teams__league__name = "")
	}
	print context['atlantic']
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
