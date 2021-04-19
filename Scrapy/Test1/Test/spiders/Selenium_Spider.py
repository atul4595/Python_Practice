import scrapy
from scrapy_selenium import SeleniumRequest
from scrapy.spiders import Spider
from scrapy.http import FormRequest
from selenium.webdriver import ActionChains
from selenium import webdriver
from scrapy.crawler import CrawlerProcess
import os
import time
from selenium.webdriver.common.keys import Keys
class Test(scrapy.Spider):
    name='Selenium_Spider'
    def start_requests(self):
        self.driver = webdriver.Chrome(os.getcwd() + "\\chromedriver.exe")
        self.driver.get('https://publicaccess.wycombe.gov.uk/idoxpa-web/search.do?action=advanced')
        self.driver.find_element_by_id('applicationValidatedStart').send_keys('01/12/2020')
        self.driver.find_element_by_id('applicationValidatedEnd').send_keys('14/12/2020')
        self.driver.find_element_by_xpath('//*[@id="advancedSearchForm"]/div[4]/input[2]').click()
        time.sleep(5)
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element_by_id('searchresults'))
        # sub_driver = self.driver.find_element_by_id('searchresults').find_elements_by_tag_name('li')
        # sub_driver[0].find_element_by_tag_name('a').click()
        #

        while True:
            # actions = ActionChains(browser)
            for i in self.driver.find_elements_by_xpath("// *[ @ id = 'searchresults'] / li / a"):
                actions = ""
                actions = ActionChains(self.driver)
                actions.key_down(Keys.CONTROL).click(i).key_up(Keys.CONTROL).perform()
                # i.send_keys(Keys.CONTROL + 't').click()

                self.driver.switch_to.window(self.driver.window_handles[1])

                time.sleep(5)
                new_url=''
                new_url = self.driver.current_url
                print('current url is: ' + new_url)
                yield SeleniumRequest(url=new_url, callback=self.parse)

                # data_of_proposal = self.driver.find_element_by_xpath("//*[@id='simpleDetailsTable']/tbody/tr[6]/td").text
                # print(data_of_proposal)
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[0])

            try:
                self.driver.find_element_by_link_text('Next').click()

            # url = browser.find('a', {'class': 'next'}).text
            # if url=='Next':
            #     browser.
            #     Next_url="https://publicaccess.wycombe.gov.uk"+str(soup.find('a', {'class': 'next'}).get('href'))
            #     print(Next_url)
            #     return Next_url
            except:
                print("No Page left to proceed")
                break
            # if not url:
            #     break
            # print(url)

        self.driver.close()






    def parse(self, response):
        try:
            # proposals = response.xpath('//*[@id="simpleDetailsTable"]/tbody/tr').extract()
            # print('This consist of products :' + str(len(proposals)))
            # print(response.xpath('//*[@id="simpleDetailsTable"]/tbody/tr[6]/td/text').extract_first().replace('\n',""))
            # p_text = response.selector.xpath('//*[@id="simpleDetailsTable"]/tbody/tr[6]/td').extract_first().strip()

            Proposal = response.css('tr:nth-child(6) td::text')[0].extract()
            Proposal = Proposal.strip()

            yield {'Proposal': Proposal}
        except Exception as e:
            print('the error is:' + str(e))


process=CrawlerProcess()
process.crawl(Test)
process.start()