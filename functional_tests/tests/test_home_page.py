from functional_tests.base import Test
from functional_tests.pages import HomePage
from functional_tests.factory import HomePageFactory
from functional_tests.factory import AuthorFactory
from functional_tests.factory import LocationFactory
from functional_tests.factory import CategoryFactory
from functional_tests.factory import ImageFactory
from functional_tests.data_setup import DataSetup

class TestHomePage(Test):
    home_page = None

    @classmethod
    def setUpClass(cls):
        super(TestHomePage, cls).setUpClass()
        author = AuthorFactory.create()
        category1 = CategoryFactory.create(name="Resource Conflicts", slug="resource-conflicts", order=1, description="Jal, jungle, zameen")
        category2 = CategoryFactory.create(name="Adivasis", slug="adivasis", order=2, description="The first dwellers")
        category3 = CategoryFactory.create(name="Dalits", slug="dalits", order=3, description="Struggles of the oppressed")
        category4 = CategoryFactory.create(name="Rural Sports", slug="sports-games", order=4, description="Games people play")
        location = LocationFactory.create()
        image = ImageFactory.create(photographers=(author,), locations=(location,))
        setup = DataSetup()
        article1 = setup.create_article("article1", author, category1, location, image)
        article2 = setup.create_article("article2", author, category2, location, image)
        video_article = setup.create_video_article("video article", author, location, image)
        talking_album = setup.create_talking_album(image)
        photo_album = setup.create_photo_album(image)
        HomePageFactory.create(carousel_0=article1, carousel_1=article2, in_focus_page1=article1, in_focus_page2=article2, video=video_article, talking_album=talking_album, photo_album=photo_album)

    def setUp(self):
        page_lambda = lambda : HomePage(self.driver)
        self.__class__.home_page = self.load_page_if_not_loaded(self.home_page, page_lambda)

    def test_home_page_title(self):
        assert self.home_page.title == "People's Archive of Rural India"

    def test_first_category_of_all_that_you_can_discover_on_pari_section(self):
        discover_on_pari_section = self.home_page.all_that_you_can_discover_on_pari_section
        assert discover_on_pari_section().title_of_first_category() == "Resource Conflicts"
        assert discover_on_pari_section().sub_text_of_first_category() == "Jal, jungle, zameen"

    def test_second_category_of_all_that_you_can_discover_on_pari_section(self):
        discover_on_pari_section = self.home_page.all_that_you_can_discover_on_pari_section
        assert discover_on_pari_section().title_of_second_category() == "Adivasis"
        assert discover_on_pari_section().sub_text_of_second_category() == "The first dwellers"

    def test_third_category_of_all_that_you_can_discover_on_pari_section(self):
        discover_on_pari_section = self.home_page.all_that_you_can_discover_on_pari_section
        assert discover_on_pari_section().title_of_third_category() == "Dalits"
        assert discover_on_pari_section().sub_text_of_third_category() == "Struggles of the oppressed"

    def test_fourth_category_of_all_that_you_can_discover_on_pari_section(self):
        discover_on_pari_section = self.home_page.all_that_you_can_discover_on_pari_section
        assert discover_on_pari_section().title_of_fourth_category() == "Rural Sports"
        assert discover_on_pari_section().sub_text_of_fourth_category() == "Games people play"