from django.urls import path 
from  booktwo import views
												
urlpatterns = [
                 path('get_started',views.getstarted,name="get_started"),
                 path('fantasy',views.fantasy,name="fantasy"),
                 path('romance',views.romance,name="romance"),
                 path('horror',views.horror,name="horror"),
                 path('fiction',views.fiction,name="fiction"),
                 path('biography',views.biography,name="biography"),
                 path('fantasydomestic',views.fantasydomestic,name="fantasydomestic"),
                 path('fantasyinternational',views.fantasyinternational,name="fantasyinternational"),
                 path('romancedomestic',views.romancedomestic,name="romancedomestic"),
                 path('romanceinternational',views.romanceinternational,name="romanceinternational"),
                 path('horrordomestic',views.horrordomestic,name="horrordomestic"),
                 path('horrorinternational',views.horrorinternational,name="horrorinternational"),
                 path('fictiondomestic',views.fictiondomestic,name="fictiondomestic"),
                 path('fictioninternational',views.fictioninternational,name="fictioninternational"),
                 path('biographydomestic',views.biographydomestic,name="biographydomestic"),
                 path('biographyinternational',views.biographyinternational,name="biographyinternational"),
                 path("reviewfn",views.reviewbook,name="reviewfn"),
            ]

