# Marc Mounzer's smoke test for the Bleacher Report homepage
# 8/29/2018

# A quick note: I'm still just learning how to use Selenium, since I have not used it professionally,
#  so it is entirely possible that I'm not using libraries
# correctly or potentially solving some problems that may not be up to standards.  I'm merely trying to get the tests
# to work.  In a normal SDET environment, I hope that participation in code reviews would solve any issues that arise.

import unittest
import time
from selenium import webdriver

BR_TITLE = 'Bleacher Report | Sports. Highlights. News. Now.'


# This smoke test for the BR homepage uses the Selenium Chrome webdriver, and assumes that the driver exists somewhere
# in the execution path.
class brTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://bleacherreport.com/')
        self.driver.maximize_window()
        time.sleep(1)

    # Verify that we are on the BR homepage
    def test_title(self):
        self.assertEqual(BR_TITLE, self.driver.title, 'Page title does not match expected value')

    # Verify that each element on the navigation bar has a link
    def test_navigation_links(self):
        navigation_links = self.driver.find_elements_by_class_name('nav-link')
        self.assertIsNotNone(navigation_links, 'The navigation bar has not loaded')
        for nav in navigation_links:
            if nav.get_attribute('id') != 'more':
                link = nav.find_element_by_tag_name('a')
                self.assertIsNotNone(link.get_attribute('href'),
                                     f'Navigation bar element with id "{nav.get_attribute("id")}" does not have a link')

    # Verify each link on the top dropdowns for each sport
    # NOTE 8/28/18 This test fails and catches an actual UI bug!  The NBA dropdown generates a column that has links that
    # don't go anywhere, and (in my opinion) shouldn't be there
    def test_dropdown_links(self):
        league_nav = self.driver.find_element_by_id('league-links')
        self.assertIsNotNone(league_nav, 'The leagues navigation bar has not loaded')
        league_links = league_nav.find_elements_by_class_name('nav-link')

        for league_link in league_links:
            league_id = league_link.get_attribute('id')

            dropdown = self.driver.find_element_by_id(league_id)
            self.assertIsNotNone(dropdown, f'The dropdown navigation menu with id "{league_id}" has not loaded')
            webdriver.ActionChains(self.driver).move_to_element(dropdown).perform()
            time.sleep(1)
            navigation_links = dropdown.find_elements_by_class_name('nav-link')
            for nav in navigation_links:
                if nav.get_attribute('id') != league_id:
                    link = nav.find_element_by_tag_name('a')
                    self.assertIsNotNone(link.get_attribute('href'),
                                         f'Link with id "{nav.get_attribute("id")}" under dropdown with id "{league_id}" does not have a link')

    # Verify the footer has loaded and that it has the social and about links
    def test_footer_links(self):
        footer_nav = self.driver.find_element_by_class_name('footer')
        self.assertIsNotNone(footer_nav, 'Footer has not loaded')

        social_links = footer_nav.find_element_by_class_name('social')
        self.assertIsNotNone(social_links, 'Social links have not loaded')

        about_links = footer_nav.find_element_by_class_name('links')
        self.assertIsNotNone(about_links, 'About links have not loaded')

    # Verify the various content streams have loaded
    def test_content_sections(self):
        main_content = self.driver.find_element_by_id('main-content')
        self.assertIsNotNone(main_content, 'The articles and features on the page have not loaded')

        featured_articles = main_content.find_element_by_class_name('featuredArticles')
        self.assertIsNotNone(featured_articles, 'The featured artiles have not loaded')

        team_stream = main_content.find_element_by_class_name('teamStreamList')
        self.assertIsNotNone(team_stream, 'The team content stream has not loaded')

        sidebar = main_content.find_element_by_class_name('sidebar')
        self.assertIsNotNone(sidebar, 'The sidebar has not loaded')

        trending = main_content.find_element_by_class_name('fireStream')
        self.assertIsNotNone(trending, 'The trending stream has not loaded')

        exclusives = main_content.find_element_by_class_name('exclusiveArticles')
        self.assertIsNotNone(exclusives, 'The exclusive articles carousel has not loaded')

    def tearDown(self):
        self.driver.close()


unittest.main()
