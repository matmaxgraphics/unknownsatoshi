from django.contrib.sitemaps import Sitemap
from django.urls import reverse



class StaticViewSitemap(Sitemap):

    def items(self):
        return ['home'] # path's name

    def location(self, item):
        return reverse(item)
