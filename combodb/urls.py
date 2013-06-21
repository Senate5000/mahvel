from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
(r'new_game', 'combodb.views.new_game'),
(r'new_character', 'combodb.views.new_character'),
(r'new_ability', 'combodb.views.new_ability'),
)