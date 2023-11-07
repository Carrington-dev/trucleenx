from django.contrib import admin
from django.urls import path, include
from myauth import views as myauth_views
from contact import views as contact_views
from django.conf import settings
from django.conf.urls.static import static
# from news.feeds import LatestNewsFeed
# from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('', myauth_views.home, name="home"),
    path('about/', myauth_views.about, name="about"),
    path('services/', myauth_views.services, name="services"),
    path('portfolio/', myauth_views.portfolio, name="portfolio"),
    path("contact/", contact_views.contact, name="contact"),
    path("subscribe/", contact_views.subcribe, name="subscribe"),
    path("bookings/", include("book.urls")),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # path('feed/', LatestNewsFeed(), name='course_feed'),
]



# from news.sitemaps import PostSitemap, StaticSitemap

# sitemaps = {
#  'courses': PostSitemap,
#  'static': StaticSitemap,
# }




admin.site.site_title = "Stemgon Admin Portal"
admin.site.site_header = "Stemgon Pty Ltd"
admin.site.index_title = "Stemgon welcomes you!!!"


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)