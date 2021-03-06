import factory
from core.models import HomePage, FeaturedSectionBlock
from functional_tests.factory import ContentTypeFactory
from functional_tests.factory.article_factory import ArticleFactory
from core.models import AffixImage

class HomePageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = HomePage
        django_get_or_create = ('title',)

    path = "00010002"
    depth = 2
    numchild = 0
    title = "Home Page"
    live = True
    has_unpublished_changes = False
    seo_title = " "
    show_in_menus = False
    search_description = " "
    go_live_at = '2011-10-24 12:43'
    expire_at = '2050-12-31 12:43'
    expired = False
    content_type = factory.SubFactory(ContentTypeFactory, app_label="core", model="homepage")
    locked = False
    latest_revision_created_at = '2011-10-24 12:43'
    first_published_at = '2011-10-24 12:43'

    carousel_0 = factory.SubFactory(ArticleFactory, title="carousel_0", content_type__app_label="article", content_type__model="article")
    carousel_1 = factory.SubFactory(ArticleFactory, title="carousel_1", content_type__app_label="article", content_type__model="article")
    in_focus_title = "In focus title"
    in_focus_link = "http://www.google.com"
    in_focus_link_text = "In focus link text"
    in_focus_page1 = factory.SubFactory(ArticleFactory, title="in_focus_page1", content_type__app_label="article", content_type__model="article")
    in_focus_page2 = factory.SubFactory(ArticleFactory, title="in_focus_page2", content_type__app_label="article", content_type__model="article")
    language = "en"

    @factory.post_generation
    def featured_content(self, create, extracted, **kwargs):
        image = AffixImage.objects.filter(title="toy story").first()
        self.featured_content = [('featured_section', {'title': 'No longer a toy story', 'link_text': 'A story',
                                                  'url': '/articles/no-longer-a-toy-story/',
                                                  'featured_image_label': 'FEATURED', 'featured_image': image})]

