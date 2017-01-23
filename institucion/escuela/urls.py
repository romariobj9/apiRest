from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from escuela import views

# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns = [
	#Te presenta en modo de vista el get y post
    url(r'^snippets/$', views.MateriaList.as_view()),
    #te presenta solo uno con sus metyodos de un CRUD
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.MateriaDetail.as_view()),
]
#solo se pone para que no me de problemas en el formato ... json , xml ....
urlpatterns = format_suffix_patterns(urlpatterns)
