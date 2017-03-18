import bs4
import re
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


file = open("Reviews.txt", "w")

driver = webdriver.Chrome('/home/hari/chromedriver')
driver.implicitly_wait(10)
# product_url = 'https://www.flipkart.com/apple-iphone-6-space-grey-16-gb/p/itme8dvfeuxxbm4r?pid=MOBEYHZ2YAXZMF2J&srno=b_1_1&otracker=CLP_filters&lid=LSTMOBEYHZ2YAXZMF2JEVWVNC'
# product_url = 'https://www.flipkart.com/kelvinator-190-l-direct-cool-single-door-refrigerator/p/itmehd4ga3h6xgmg?pid=RFRE9WCMZMFXTA5R&srno=b_1_1&otracker=hp_omu_Best%20Deals%20on%20Appliances_2_0389ccb1-0d01-48c8-9761-52fa164e403d_0389ccb1-0d01-48c8-9761-52fa164e403d_5&lid=LSTRFRE9WCMZMFXTA5RAOIFC5'
# product_url = 'https://www.flipkart.com/hp-apu-quad-core-a8-4-gb-1-tb-hdd-windows-10-home-z1d89pa-15-bg002au-notebook/p/itmem22kcunphxb3?pid=COMEM22KKGZR4P4T&srno=s_1_1&otracker=search&lid=LSTCOMEM22KKGZR4P4TJQNRDU&qH=312f91285e048e09'
# product_url = 'https://www.flipkart.com/harry-potter-philosopher-s-stone/p/itme99sf4gd9rged?pid=9781408855652&srno=s_1_2&otracker=search&lid=LSTBOK9781408855652APHPIR&qH=b245005e8b3df99a' 
product_url = 'https://www.flipkart.com/redmi-note-3-gold-32-gb/p/itmeg3zzcbhxcdge?pid=MOBEG3ZZSGZD7WX8&srno=s_1_6&otracker=search&lid=LSTMOBEG3ZZSGZD7WX8YVC14E&qH=0c8952d06db7c7c7'
# product_url = 'https://www.flipkart.com/nikon-d3300-body-af-p-dx-nikkor-18-55-mm-f3-5-5-6-vr-kit-lens-dslr-camera/p/itmdsqgbwfpw8kqx?pid=CAMDSQGBWFPW8KQX&srno=b_1_1&otracker=browse&lid=LSTCAMDSQGBWFPW8KQXEQGXKJ'
# product_url = 'https://www.flipkart.com/canon-eos-700d-ef-s18-55-mm-ii-ef-s55-250-ii-dslr-camera/p/itme6fwcz9evqnxr?pid=CAME6FWA7RHNXGPF&lid=LSTCAME6FWA7RHNXGPFVAY7SP&fm=merchandising&iid=M_8a039264-18d6-4271-bf08-5da2a9a8d16c.56ef6d45-a39f-4a9e-a7c0-c9295a48db4e&otracker=hp_omu_Top+Selling+Gadgets_1_56ef6d45-a39f-4a9e-a7c0-c9295a48db4e_56ef6d45-a39f-4a9e-a7c0-c9295a48db4e_7'
# product_url = 'https://www.flipkart.com/samsung-80cm-32-hd-ready-led-tv/p/itme8yrfm32d4xzn?pid=TVSE8YRFSUBEHZB6&srno=b_1_3&otracker=product_breadCrumbs_Televisions&lid=LSTTVSE8YRFSUBEHZB680UQTL'
# product_url = 'https://www.flipkart.com/lg-6-kg-fully-automatic-front-load-washing-machine/p/itmefjwxxhycfxdz?pid=WMNEFJWXY9PYVNWT&srno=s_1_2&otracker=search&lid=LSTWMNEFJWXY9PYVNWTUFGDTY&qH=bcadf718d561cab9'
# product_url = 'https://www.flipkart.com/timex-mf13-expedition-analog-digital-watch-men-women/p/itmd9gjgbgpp3gyv?pid=WATD9H77MKCGVQZH&srno=b_1_1&otracker=hp_omu_Best%20of%20Fashion%20%26%20Lifestyle_3_792c420b-1eb7-4793-bcb0-28bbe1dff00b_792c420b-1eb7-4793-bcb0-28bbe1dff00b_8&lid=LSTWATD9H77MKCGVQZHAYRROA';
# product_url = 'https://www.flipkart.com/sansui-1-5-ton-5-star-split-ac-white/p/itme9qs4bd7xngch?pid=ACNE9QS4C6AAJWZK&srno=s_1_1&otracker=search&lid=LSTACNE9QS4C6AAJWZKV3OUPK&qH=fb2a25a33265e1ef'
# product_url = 'https://www.flipkart.com/micromax-60cm-23-6-hd-ready-led-tv/p/itmecek5rks234zz?pid=TVSECEK59SWDZS7C&fm=personalisedRecommendation/p2p-same&iid=R_6ab12cac-eeb7-46c5-b272-bc02ac1c595b.TVSECEK59SWDZS7C&otracker=hp_reco_TVs+You+May+Like_1_Micromax+60cm+%2823.6%29+HD+Ready+LED+TV_TVSECEK59SWDZS7C_8'
# product_url = 'https://www.flipkart.com/sennheiser-cx-180-wired-headphones/p/itmdaw7pjkbfrhha?pid=ACCDAW7PJXCC9QF3&srno=s_1_2&otracker=search&lid=LSTACCDAW7PJXCC9QF34KZRQV&qH=edd443896ef5dbfc'
# product_url = 'https://www.flipkart.com/bpl-6-5-kg-fully-automatic-front-load-washing-machine/p/itmehgywpfzd3zyr?pid=WMNEHGYWDWX2EJRT&otracker=productlist_pmu'
# product_url = 'https://www.flipkart.com/puma-strike-fashion-ii-dp-running-shoes/p/itmehgz7uzsk4e8b?pid=SHOEHGZ7TKYHEDBM&srno=b_1_1&otracker=hp_omu_Footwear%20for%20Men%20%26%20Women_1_c2274387-c732-40f7-be70-145b65789f21_c2274387-c732-40f7-be70-145b65789f21_15&lid=LSTSHOEHGZ7TKYHEDBMDUWFER'
# product_url = 'https://www.flipkart.com/sandisk-ultra-camera-32-gb-sdhc-class-10-48-mb-s-memory-card/p/itmedg8gp77cp8vv?pid=ACCEDG8GC9G4TYNE&srno=b_1_1&otracker=nmenu_sub_Electronics_0_Memory%20Cards&lid=LSTACCEDG8GC9G4TYNEQ5UYUG'
# product_url = 'https://www.flipkart.com/philips-qt4005-15-pro-skin-advanced-trimmer-men/p/itmdze53vthypqhb?pid=SHVDGGZPC8PXJ7HR&srno=s_1_3&otracker=search&lid=LSTSHVDGGZPC8PXJ7HRI5RWMR&qH=705a17deac7a99db'

#product_url='https://www.flipkart.com/haier-195-l-direct-cool-single-door-refrigerator/p/itmehpcfsmp2hhbu?pid=RFREHSMGTKCXSQJJ'

driver.get(product_url)
html = driver.page_source
soup = bs4.BeautifulSoup(html,'lxml')
review_link = soup.find_all('a',href=re.compile('.*product\-reviews*'))

reviewPagesNmberClassName = '_3v8VuN'
readMoreLinksClassName = '_1EPkIx'
actualReviewsClassName = 'qwjRop'

print review_link[0]['href']



driver.get('https://www.flipkart.com'+review_link[0]['href'])

reviewPagesNmber = driver.find_elements_by_class_name(reviewPagesNmberClassName)
numReviewPages = int(re.findall(r'(\d+)$' , reviewPagesNmber[-1].text)[0])
print 'Number of review pages is '
print numReviewPages
driver.get('https://www.flipkart.com'+review_link[0]['href'])
 
for i in range(1,numReviewPages+1):

	if i > 67 :
		break


	# url_data = urlsplit('https://www.flipkart.com'+review_link[0]['href'])
	# qs_data = parse_qs(url_data.query)
	# if not 'page' in qs_data:
	# 	qs_data['page']=[str(i)]
	# nextPageUrl = url_data._replace(query=urlencode(qs_data, True)).geturl()
	# print nextPageUrl
	# driver.get('https://www.flipkart.com'+review_link[0]['href'])
	readMoreLinks = []
	readMoreLinks = driver.find_elements_by_class_name(readMoreLinksClassName)

	for x in range(0,len(readMoreLinks)):

		ActionChains(driver).move_to_element(readMoreLinks[x]).perform()
		readMoreLinks[x].click()

	actualReviews = driver.find_elements_by_class_name(actualReviewsClassName)
	for x in range(0,len(actualReviews)):

		file.write(actualReviews[x].get_attribute('innerText').encode('utf-8'))
		# file.write("\n****************************************\n")
		# file.write("\n\n\n\n")


	
	# print actualReviews[0].get_attribute('innerText')
	print 'Number of reviews on page '+str(i)
	print len(actualReviews)

	nextPageLink = driver.find_elements_by_class_name('_2kUstJ')
	print len(nextPageLink)
	ActionChains(driver).move_to_element(nextPageLink[-1]).perform()
	nextPageLink[-1].click()


os.system('python analyzeReviews.py')

# print "Completed Scraping for Reviews"
# file.close

# print "Creating POS Tagged database"
# tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# pos_file = open("Reviews_HarryPotter_POS.txt", "w")
# review_file = open('Reviews_HarryPotter.txt','r')
# data = review_file.read().decode('utf-8')
# print data.encode('utf-8')
# print ''.join(tokenizer.tokenize(data)).encode('utf-8')
#       # '\n'.join(tokenizer.tokenize(data)).encode('utf-8')
# pos_file.write(''.join(tokenizer.tokenize(data)).encode('utf-8'))
# pos_file.close

# with open('Reviews_HarryPotter_POS.txt','r+') as pos_file:
#     for line in pos_file:
#         if line.strip():
#             pos_file.write(line)  
# pos_file.close










# readMoreLinks = []
# readMoreLinks = driver.find_elements_by_class_name('_1EPkIx')

# print len(readMoreLinks)

# for x in range(0,len(readMoreLinks)):

# 	ActionChains(driver).move_to_element(readMoreLinks[x]).perform()
# 	readMoreLinks[x].click()

# actualReviews = driver.find_elements_by_class_name('qwjRop')


# print len(actualReviews)


# print actualReviews[9].get_attribute('innerText')

# nextPageLink = driver.find_elements_by_class_name('_2kUstJ')
# print len(nextPageLink)


# ActionChains(driver).move_to_element(nextPageLink[-1]).perform()
# nextPageLink[-1].click()

# print (driver.page_source).encode('utf-8')

