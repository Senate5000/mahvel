from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
(r'new_game', 'combodb.views.new_game'),
(r'new_character', 'combodb.views.new_character'),
(r'new_ability', 'combodb.views.new_ability'),
(r'new_combo', 'combodb.views.new_combo'),
(r'view_combo/(\d+)', 'combodb.views.view_combo'),
(r'json_test', 'combodb.views.json_test'),
)