import random

BASE_URL = 'https://magento.softwaretestingboard.com'
MAIN_PAGE_URL = BASE_URL + '/'
LOGIN_URL = BASE_URL + '/customer/account/login'
CREATE_ACCOUNT_URL = BASE_URL + '/customer/account/create/'

WHATS_NEW_PAGE_URL = BASE_URL + '/what-is-new.html'

WOMEN_PAGE_URL = BASE_URL + '/women.html'
WOMEN_TOPS_URL = BASE_URL + '/women/tops-women.html'
WOMEN_TOPS_JACKETS_URL = BASE_URL + '/women/tops-women/jackets-women.html'
WOMEN_TOPS_HOODIES_URL = BASE_URL + '/women/tops-women/hoodies-and-sweatshirts-women.html'
WOMEN_TOPS_TEES_URL = BASE_URL + '/women/tops-women/tees-women.html'
WOMEN_TOPS_BRAS_URL = BASE_URL + '/women/tops-women/tanks-women.html'
WOMEN_BOTTOMS_URL = BASE_URL + '/women/bottoms-women.html'
WOMEN_BOTTOMS_PANTS_URL = BASE_URL + '/women/bottoms-women/pants-women.html'
WOMEN_BOTTOMS_SHORTS_URL = BASE_URL + '/women/bottoms-women/shorts-women.html'
WOMEN_SALE_PAGE_URL = BASE_URL + '/promotions/women-sale.html'

MEN_PAGE_URL = BASE_URL + '/men.html'
MEN_TOPS_URL = BASE_URL + '/men/tops-men.html'
MEN_TOPS_JACKETS_URL = BASE_URL + '/men/tops-men/jackets-men.html'
MEN_TOPS_HOODIES_URL = BASE_URL + '/men/tops-men/hoodies-and-sweatshirts-men.html'
MEN_TOPS_TEES_URL = BASE_URL + '/men/tops-men/tees-men.html'
MEN_TOPS_TANKS_URL = BASE_URL + '/men/tops-men/tanks-men.html'
MEN_BOTTOMS_URL = BASE_URL + '/men/bottoms-men.html'
MEN_BOTTOMS_PANTS_URL = BASE_URL + '/men/bottoms-men/pants-men.html'
MEN_BOTTOMS_SHORTS_URL = BASE_URL + '/men/bottoms-men/shorts-men.html'
MEN_SALE_PAGE_URL = BASE_URL + '/promotions/men-sale.html'

GEAR_PAGE_URL = BASE_URL + '/gear.html'
GEAR_BAGS_URL = BASE_URL + '/gear/bags.html'
GEAR_FITNESS_URL = BASE_URL + '/gear/fitness-equipment.html'
GEAR_WATCHES_URL = BASE_URL + '/gear/watches.html'

TRAINING_URL = BASE_URL + '/training.html'
VIDEO_DOWNLOAD_URL = BASE_URL + '/training/training-video.html'

SALE_URL = BASE_URL + '/sale.html'

POPULAR_SEARCH_TERMS_URL = BASE_URL + '/search/term/popular/'
PRIVACY_POLICY_PAGE_URL = BASE_URL + '/privacy-policy-cookie-restriction-mode'
ADVANCED_SEARCH_URL = BASE_URL + '/catalogsearch/advanced/'
ORDERS_RETURNS_URL = BASE_URL + '/sales/guest/form/'

ERIN_RECOMMENDS_URL = BASE_URL + '/collections/erin-recommends.html'
PERFORMANCE_FABRICS_URL = BASE_URL + '/collections/performance-fabrics.html'
ECO_FRIENDLY_URL = BASE_URL + '/collections/eco-friendly.html'

CONTACT_US_URL = BASE_URL + "/contact/"
CART_URL = BASE_URL + '/checkout/cart/'
YOGA_URL = BASE_URL + '/collections/yoga-new.html'

YOGA_LIST_URL = BASE_URL + '/collections/yoga-new.html?product_list_mode=list'
SET_YOGA_STRAPS_URL = BASE_URL + '/set-of-sprite-yoga-straps.html'
SPORT_URL = BASE_URL + '/collections/performance-new.html'
LAYLA_TEE_URL = BASE_URL + '/layla-tee.html'

SHIPPING_URL = BASE_URL + "/checkout/#shipping"
PAYMENT_URL = BASE_URL + "/checkout/#payment"
SOFTWARE_TESTING_BOARD_URL = BASE_URL + "/magento-store-notes/?utm_source=magento_store&utm_medium=banner&utm_" \
                                        "campaign=notes_promo&utm_id=notes_promotion"

CORPORATION_LIST_URL = BASE_URL + '/catalog/product_compare/'
WISH_LIST_URL = BASE_URL + '/wishlist'

random_product_url = BASE_URL + random.choice([
    '/antonia-racer-tank.html',
    '/radiant-tee.html',
    '/cassius-sparring-tank.html?qty=1',
    '/cronus-yoga-pant.html',
    '/deion-long-sleeve-evercool-trade-tee.html',
    '/helena-hooded-fleece.html',
    '/layla-tee.html',
    '/stellar-solar-jacket.html',
    '/nona-fitness-tank.html',
    '/bardot-capri.html',
    '/mimi-all-purpose-short.html',
    '/taurus-elements-shell.html',
    '/primo-endurance-tank.html',
    '/meteor-workout-short.html',
    '/savvy-shoulder-tote.html',
    '/dual-handle-cardio-ball.html',
    '/cruise-dual-analog-watch.html',
    '/adrienne-trek-jacket.html',
    '/quest-lumaflex-trade-band.html',
    '/affirm-water-bottle.html',
    '/sprite-foam-yoga-brick.html'
])

expected_anchor_urls = {
            "link1": PRIVACY_POLICY_PAGE_URL + "#privacy-policy-title-1",
            "link2": PRIVACY_POLICY_PAGE_URL + "#privacy-policy-title-2",
            "link3": PRIVACY_POLICY_PAGE_URL + "#privacy-policy-title-3",
            "link4": PRIVACY_POLICY_PAGE_URL + "#privacy-policy-title-4",
            "link5": PRIVACY_POLICY_PAGE_URL + "#privacy-policy-title-5",
            "link6": PRIVACY_POLICY_PAGE_URL + "#privacy-policy-title-6",
            "link7": PRIVACY_POLICY_PAGE_URL + "#privacy-policy-title-7",
            "link8": PRIVACY_POLICY_PAGE_URL + "#privacy-policy-title-8",
            "link9": PRIVACY_POLICY_PAGE_URL + "#privacy-policy-title-9",
            "link10": PRIVACY_POLICY_PAGE_URL + "#privacy-policy-title-10",
            "link11": PRIVACY_POLICY_PAGE_URL + "#privacy-policy-title-11",
            "link12": PRIVACY_POLICY_PAGE_URL + "#privacy-policy-title-12",
            "link13": PRIVACY_POLICY_PAGE_URL + "#privacy-policy-title-13",
            "link14": PRIVACY_POLICY_PAGE_URL + "#privacy-policy-title-14"
        }
