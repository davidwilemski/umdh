
import umdh
import unittest

class SearchMenuForTests(unittest.TestCase):
    def test_search_menu(self):
        """
        Haven't yet figured out a good way of testing
        get_menu and get_menu_xml without other dependancies...

        So. This is the only test for now:
        """
        print self.blah
        self.assertTrue(
                umdh.search_menu_for(
                    self.menu,
                    'Strawberry Cheesecake'))
    
    def setUp(self):
        """
        Nasty setup function that stores what a real document looks like
        """
        self.xml = """
<dininghall>
	<name>Marketplace</name>
	<hours><!--Fall 2012 Hours<br />
Monday-Thursday: <br />
Continuous Service: 7:00am-9:00pm<br />
Friday: <br />
Continuous Service: 7:00am-8:00pm<br />
Saturday & Sunday: 10:30am-2:00pm, 5:00pm-8:00pm<br /><br />
Term Break Hours:<br />
December 19th : 7:00am - 10:00am, 11:00am-2:00pm, 5:00pm-8:00pm<br />
December 20th : 7:00am-10:00am, 11:00am-2:00pm, 5:00pm-7:00pm<br />
Closed on December 21st<br />
January 7th: 10:30am-2:00pm, 5:00pm-6:30pm<br />
January 8th: 10:30am-2:00pm, 5:00pm-9:00pm<br />
Regular Meal Services Resumes January 9th<br />--></hours>
	<address><!--<a href="http://www.housing.umich.edu/dining/hill-dining-center/">Hill Dining Center</a><br />200 Observatory<br /> Ann Arbor, MI 48109--></address>
	<contact><!--734.764.2111<br /><a href="mailto:hsg-ds-hill@umich.edu">hsg-ds-hill@umich.edu</a>--></contact>
	<link>
		<type>retail</type>
		<href>http://www.housing.umich.edu/dining/menus/#/victors</href>
		<text>Victors</text>
	</link>
	<link>
		<type>menu-url</type>
		<href>http://www.housing.umich.edu/dining/menus/#/marketplace/</href>
		<text>Marketplace Web Menu</text>
	</link>
	<menu>
		<date>Sunday, December 16</date>
		<meal>
			<name>BREAKFAST</name>
			<station>
				<course>
					<name>notice</name>
					<menuitem>Marketplace is not serving breakfast on this date.</menuitem>
				</course>
			</station>
		</meal>
		<meal>
			<name>LUNCH</name>
			<station>
				<name>Palmer Ave Deli</name>
				<course>
					<name>Soups</name>
					<menuitem>Homemade Chicken Noodle Soup
							<serving_size portion='Cups'></serving_size>
							<portion_size grams='247'></portion_size>
							<nutrition p="7 gm" f="5 gm" fc="49" cr="12 gm" cl="127 " so="1256 mg" ch="39 mg" fs="1 gm" fi="1 gm" su="2 gm" ft="1 gm" pro="9" fat="8" cho="4" sfa="6" tdfb="4" vitc="2" ca="2" fe="15" vtaiu="41" chol="13" fatrn="3" sugar="5" na="84"></nutrition></menuitem>
					<menuitem glutenfree="1" vegan="1">Southwestern Bean Soup 
							<serving_size portion='Cups'></serving_size>
							<portion_size grams='261'></portion_size>
							<nutrition p="2 gm" f="8 gm" fc="67" cr="8 gm" cl="104 " so="239 mg" ch="0 mg" fs="1 gm" fi="2 gm" su="2 gm" ft="0 gm" pro="2" fat="11" cho="3" sfa="5" tdfb="9" vitc="29" ca="2" fe="3" vtaiu="41" chol="0" fatrn="0" sugar="4" na="16"></nutrition></menuitem>
				</course>
				<course>
					<name>HotCereal</name>
					<menuitem vegan="1" msmart="1">Oatmeal 
							<serving_size portion='Cups'></serving_size>
							<portion_size grams='127'></portion_size>
							<nutrition p="3 gm" f="2 gm" fc="14" cr="16 gm" cl="90 " so="1 mg" ch="0 mg" fs="0 gm" fi="2 gm" su="0 gm" ft="0 gm" pro="4" fat="2" cho="6" sfa="1" tdfb="10" vitc="0" ca="1" fe="6" vtaiu="0" chol="0" fatrn="0" sugar="0" na="0"></nutrition></menuitem>
					<menuitem vegan="1" msmart="1">Cream of Wheat 
							<serving_size portion='Cups'></serving_size>
							<portion_size grams='113'></portion_size>
							<nutrition p="2 gm" f="0 gm" fc="2" cr="11 gm" cl="53 " so="68 mg" ch="0 mg" fs="0 gm" fi="1 gm" su="0 gm" ft="0 gm" pro="2" fat="0" cho="4" sfa="0" tdfb="2" vitc="0" ca="5" fe="23" vtaiu="13" chol="0" fatrn="0" sugar="0" na="5"></nutrition></menuitem>
				</course>
			</station>
			<station>
				<name>Homestyles</name>
				<course>
					<name>Rotisserie</name>
					<menuitem>Fritatta Bar
							<serving_size portion='TITLE'></serving_size>
							<portion_size grams='28'></portion_size>
							<nutrition></nutrition></menuitem>
				</course>
				<course>
					<name>Entree1</name>
					<menuitem glutenfree="1">Cheddar Potato &amp; Olive Fritatta 
							<serving_size portion='5 oz Serving'></serving_size>
							<portion_size grams='143'></portion_size>
							<nutrition></nutrition></menuitem>
					<menuitem glutenfree="1">Italian Fritatta W/ Meat 
							<serving_size portion='5 oz Serving'></serving_size>
							<portion_size grams='136'></portion_size>
							<nutrition></nutrition></menuitem>
					<menuitem glutenfree="1">Bacon 
							<serving_size portion='4 Slices'></serving_size>
							<portion_size grams='45'></portion_size>
							<nutrition p="6 gm" f="23 gm" fc="207" cr="0 gm" cl="234 " so="425 mg" ch="35 mg" fs="8 gm" fi="0 gm" su="0 gm" ft="0 gm" pro="8" fat="35" cho="0" sfa="35" tdfb="0" vitc="0" ca="0" fe="1" vtaiu="0" chol="12" fatrn="0" sugar="0" na="28"></nutrition></menuitem>
					<menuitem glutenfree="1" vegetarian="1">Scrambled Eggs  
							<serving_size portion='1/2 Cup'></serving_size>
							<portion_size grams='113'></portion_size>
							<nutrition p="13 gm" f="10 gm" fc="92" cr="2 gm" cl="157 " so="179 mg" ch="461 mg" fs="3 gm" fi="0 gm" su="0 gm" ft="0 gm" pro="18" fat="16" cho="1" sfa="15" tdfb="0" vitc="0" ca="4" fe="9" vtaiu="9" chol="154" fatrn="0" sugar="0" na="12"></nutrition></menuitem>
					<menuitem vegetarian="1">Buttermilk Pancakes 
							<serving_size portion='2 Pancakes'></serving_size>
							<portion_size grams='128'></portion_size>
							<nutrition p="10 gm" f="6 gm" fc="51" cr="47 gm" cl="284 " so="990 mg" ch="90 mg" fs="2 gm" fi="1 gm" su="10 gm" ft="1 gm" pro="14" fat="9" cho="17" sfa="9" tdfb="5" vitc="2" ca="31" fe="16" vtaiu="3" chol="30" fatrn="2" sugar="19" na="66"></nutrition></menuitem>
					<menuitem glutenfree="1" vegetarian="1" msmart="1">Scrambled Egg Whites 
							<serving_size portion='1/2 Cup'></serving_size>
							<portion_size grams='85'></portion_size>
							<nutrition p="7 gm" f="3 gm" fc="29" cr="1 gm" cl="59 " so="154 mg" ch="2 mg" fs="1 gm" fi="0 gm" su="1 gm" ft="1 gm" pro="9" fat="5" cho="0" sfa="3" tdfb="0" vitc="0" ca="1" fe="1" vtaiu="2" chol="1" fatrn="4" sugar="1" na="10"></nutrition></menuitem>
				</course>
				<course>
					<name>Starches1</name>
					<menuitem glutenfree="1" vegan="1">Tritaters 
							<serving_size portion='2 Tritaters'></serving_size>
							<portion_size grams='113'></portion_size>
							<nutrition p="4 gm" f="18 gm" fc="165" cr="44 gm" cl="356 " so="329 mg" ch="0 mg" fs="2 gm" fi="4 gm" su="1 gm" ft="0 gm" pro="6" fat="28" cho="16" sfa="11" tdfb="16" vitc="5" ca="1" fe="9" vtaiu="0" chol="0" fatrn="1" sugar="2" na="22"></nutrition></menuitem>
				</course>
				<course>
					<name>Vegetables1</name>
					<menuitem glutenfree="1" vegan="1" msmart="1">San Francisco Vegetable Blend
							<serving_size portion='1/2 Cup'></serving_size>
							<portion_size grams='113'></portion_size>
							<nutrition p="0 gm" f="0 gm" fc="0" cr="7 gm" cl="40 " so="131 mg" ch="0 mg" fs="0 gm" fi="3 gm" su="4 gm" ft="0 gm" pro="0" fat="0" cho="2" sfa="0" tdfb="11" vitc="40" ca="3" fe="0" vtaiu="9" chol="0" fatrn="0" sugar="8" na="9"></nutrition></menuitem>
				</course>
			</station>
			<station>
				<name>World Palate</name>
				<course>
					<name>Entree2</name>
					<menuitem glutenfree="1" vegetarian="1" msmart="1">Scrambled Egg Whites 
							<serving_size portion='1/2 Cup'></serving_size>
							<portion_size grams='85'></portion_size>
							<nutrition p="7 gm" f="3 gm" fc="29" cr="1 gm" cl="59 " so="154 mg" ch="2 mg" fs="1 gm" fi="0 gm" su="1 gm" ft="1 gm" pro="9" fat="5" cho="0" sfa="3" tdfb="0" vitc="0" ca="1" fe="1" vtaiu="2" chol="1" fatrn="4" sugar="1" na="10"></nutrition></menuitem>
					<menuitem glutenfree="1">Bacon 
							<serving_size portion='4 Slices'></serving_size>
							<portion_size grams='45'></portion_size>
							<nutrition p="6 gm" f="23 gm" fc="207" cr="0 gm" cl="234 " so="425 mg" ch="35 mg" fs="8 gm" fi="0 gm" su="0 gm" ft="0 gm" pro="8" fat="35" cho="0" sfa="35" tdfb="0" vitc="0" ca="0" fe="1" vtaiu="0" chol="12" fatrn="0" sugar="0" na="28"></nutrition></menuitem>
					<menuitem glutenfree="1" vegetarian="1">Scrambled Eggs  
							<serving_size portion='1/2 Cup'></serving_size>
							<portion_size grams='113'></portion_size>
							<nutrition p="13 gm" f="10 gm" fc="92" cr="2 gm" cl="157 " so="179 mg" ch="461 mg" fs="3 gm" fi="0 gm" su="0 gm" ft="0 gm" pro="18" fat="16" cho="1" sfa="15" tdfb="0" vitc="0" ca="4" fe="9" vtaiu="9" chol="154" fatrn="0" sugar="0" na="12"></nutrition></menuitem>
					<menuitem vegetarian="1">Buttermilk Pancakes 
							<serving_size portion='2 Pancakes'></serving_size>
							<portion_size grams='128'></portion_size>
							<nutrition p="10 gm" f="6 gm" fc="51" cr="47 gm" cl="284 " so="990 mg" ch="90 mg" fs="2 gm" fi="1 gm" su="10 gm" ft="1 gm" pro="14" fat="9" cho="17" sfa="9" tdfb="5" vitc="2" ca="31" fe="16" vtaiu="3" chol="30" fatrn="2" sugar="19" na="66"></nutrition></menuitem>
				</course>
				<course>
					<name>Starches2</name>
					<menuitem glutenfree="1" vegan="1">Tritaters 
							<serving_size portion='2 Tritaters'></serving_size>
							<portion_size grams='57'></portion_size>
							<nutrition p="2 gm" f="9 gm" fc="82" cr="22 gm" cl="178 " so="164 mg" ch="0 mg" fs="1 gm" fi="2 gm" su="0 gm" ft="0 gm" pro="3" fat="14" cho="8" sfa="5" tdfb="8" vitc="3" ca="1" fe="4" vtaiu="0" chol="0" fatrn="0" sugar="1" na="11"></nutrition></menuitem>
				</course>
			</station>
			<station>
				<name></name>
				<course>
					<name>MiddleEasternBar</name>
					<menuitem>Breakfast Topping Bar
							<serving_size portion='TITLE'></serving_size>
							<portion_size grams='28'></portion_size>
							<nutrition></nutrition></menuitem>
				</course>
			</station>
			<station>
				<name>Pizzeria</name>
				<course>
					<name>Pizza</name>
					<menuitem>Breakfast Stromboli
							<serving_size portion='TITLE'></serving_size>
							<portion_size grams='28'></portion_size>
							<nutrition></nutrition></menuitem>
					<menuitem>Fruit Pizza
							<serving_size portion='TITLE'></serving_size>
							<portion_size grams='28'></portion_size>
							<nutrition></nutrition></menuitem>
				</course>
				<course>
					<name>Entree3</name>
					<menuitem>PASTA BAR
							<serving_size portion='TITLE'></serving_size>
							<portion_size grams='28'></portion_size>
							<nutrition></nutrition></menuitem>
				</course>
			</station>
			<station>
				<name>Grill on the Hill</name>
				<course>
					<name>Entree4</name>
					<menuitem>BREAKFAST SANDWICH BAR
							<serving_size portion='TITLE'></serving_size>
							<portion_size grams=''></portion_size>
							<nutrition></nutrition></menuitem>
				</course>
			</station>
			<station>
				<name>Just Dessert</name>
				<course>
					<name>Desserts</name>
					<menuitem glutenfree="1" vegetarian="1" msmart="1">Vanilla Pudding 
							<serving_size portion='1/2 Cup'></serving_size>
							<portion_size grams='113'></portion_size>
							<nutrition p="3 gm" f="2 gm" fc="18" cr="25 gm" cl="132 " so="186 mg" ch="8 mg" fs="1 gm" fi="0 gm" su="22 gm" ft="0 gm" pro="4" fat="3" cho="9" sfa="6" tdfb="1" vitc="0" ca="12" fe="0" vtaiu="4" chol="3" fatrn="0" sugar="45" na="12"></nutrition></menuitem>
					<menuitem vegetarian="1">Blueberry Muffins 
							<serving_size portion='Muffin'></serving_size>
							<portion_size grams='54'></portion_size>
							<nutrition p="3 gm" f="9 gm" fc="85" cr="21 gm" cl="181 " so="138 mg" ch="35 mg" fs="2 gm" fi="0 gm" su="12 gm" pro="3" fat="14" cho="7" sfa="7" tdfb="0" vitc="0" ca="2" fe="3" vtaiu="2" chol="12" fatrn="" sugar="24" na="9"></nutrition></menuitem>
					<menuitem vegetarian="1">Chocolate Chocolate Chip Muffins 
							<serving_size portion='Muffin'></serving_size>
							<portion_size grams='54'></portion_size>
							<nutrition p="3 gm" f="8 gm" fc="71" cr="25 gm" cl="175 " so="190 mg" ch="30 mg" fs="2 gm" fi="1 gm" su="15 gm" ft="0 gm" pro="3" fat="12" cho="9" sfa="7" tdfb="4" vitc="0" ca="2" fe="6" vtaiu="0" chol="10" fatrn="0" sugar="29" na="13"></nutrition></menuitem>
					<menuitem vegetarian="1">Orange Blossom Muffins 
							<serving_size portion='Muffin'></serving_size>
							<portion_size grams='54'></portion_size>
							<nutrition p="2 gm" f="8 gm" fc="71" cr="24 gm" cl="172 " so="138 mg" ch="22 mg" fs="1 gm" fi="0 gm" su="15 gm" ft="0 gm" pro="2" fat="12" cho="9" sfa="5" tdfb="0" vitc="0" ca="2" fe="3" vtaiu="0" chol="7" fatrn="0" sugar="29" na="9"></nutrition></menuitem>
					<menuitem vegetarian="1">Raisin Bran Muffins 
							<serving_size portion='Muffin'></serving_size>
							<portion_size grams='54'></portion_size>
							<nutrition p="3 gm" f="7 gm" fc="61" cr="24 gm" cl="163 " so="224 mg" ch="0 mg" fs="1 gm" fi="2 gm" su="13 gm" ft="0 gm" pro="3" fat="10" cho="9" sfa="5" tdfb="6" vitc="0" ca="2" fe="9" vtaiu="0" chol="0" fatrn="0" sugar="26" na="15"></nutrition></menuitem>
					<menuitem vegetarian="1">Banana Bread 
							<serving_size portion='Slice'></serving_size>
							<portion_size grams='57'></portion_size>
							<nutrition p="2 gm" f="8 gm" fc="68" cr="28 gm" cl="186 " so="96 mg" ch="20 mg" fs="4 gm" fi="1 gm" su="16 gm" ft="0 gm" pro="3" fat="11" cho="10" sfa="17" tdfb="2" vitc="2" ca="0" fe="4" vtaiu="1" chol="7" fatrn="1" sugar="31" na="6"></nutrition></menuitem>
					<menuitem vegetarian="1" msmart="1">Low Fat Blueberry  Muffins 
							<serving_size portion='Muffin'></serving_size>
							<portion_size grams='54'></portion_size>
							<nutrition p="3 gm" f="3 gm" fc="25" cr="28 gm" cl="144 " so="286 mg" ch="0 mg" fs="0 gm" fi="1 gm" su="14 gm" ft="0 gm" pro="4" fat="4" cho="10" sfa="0" tdfb="4" vitc="2" ca="2" fe="6" vtaiu="0" chol="0" fatrn="0" sugar="27" na="19"></nutrition></menuitem>
					<menuitem vegetarian="1">Chocolate Chip Cookies 
							<serving_size portion='Cookie'></serving_size>
							<portion_size grams='38'></portion_size>
							<nutrition p="2 gm" f="7 gm" fc="63" cr="24 gm" cl="169 " so="115 mg" ch="7 mg" fs="4 gm" fi="1 gm" su="12 gm" ft="0 gm" pro="3" fat="11" cho="9" sfa="18" tdfb="4" vitc="0" ca="12" fe="6" vtaiu="4" chol="2" fatrn="0" sugar="24" na="8"></nutrition></menuitem>
				</course>
			</station>
		</meal>
		<meal>
			<name>DINNER</name>
			<station>
				<name>Palmer Ave Deli</name>
				<course>
					<name>Soups</name>
					<menuitem>Homemade Chicken Noodle Soup
							<serving_size portion='Cups'></serving_size>
							<portion_size grams='247'></portion_size>
							<nutrition p="7 gm" f="5 gm" fc="49" cr="12 gm" cl="127 " so="1256 mg" ch="39 mg" fs="1 gm" fi="1 gm" su="2 gm" ft="1 gm" pro="9" fat="8" cho="4" sfa="6" tdfb="4" vitc="2" ca="2" fe="15" vtaiu="41" chol="13" fatrn="3" sugar="5" na="84"></nutrition></menuitem>
					<menuitem glutenfree="1" vegan="1">Southwestern Bean Soup 
							<serving_size portion='Cups'></serving_size>
							<portion_size grams='261'></portion_size>
							<nutrition p="2 gm" f="8 gm" fc="67" cr="8 gm" cl="104 " so="239 mg" ch="0 mg" fs="1 gm" fi="2 gm" su="2 gm" ft="0 gm" pro="2" fat="11" cho="3" sfa="5" tdfb="9" vitc="29" ca="2" fe="3" vtaiu="41" chol="0" fatrn="0" sugar="4" na="16"></nutrition></menuitem>
				</course>
			</station>
			<station>
				<name>Homestyles</name>
				<course>
					<name>Rotisserie</name>
					<menuitem>PASTA BAR
							<serving_size portion='TITLE'></serving_size>
							<portion_size grams='28'></portion_size>
							<nutrition></nutrition></menuitem>
				</course>
				<course>
					<name>Entree1</name>
					<menuitem glutenfree="1" vegan="1">Marinara Sauce 
							<serving_size portion='1/2 Cup'></serving_size>
							<portion_size grams='113'></portion_size>
							<nutrition p="2 gm" f="5 gm" fc="40" cr="12 gm" cl="97 " so="614 mg" ch="0 mg" fs="0 gm" fi="0 gm" su="10 gm" ft="0 gm" pro="3" fat="7" cho="4" sfa="0" tdfb="0" vitc="9" ca="3" fe="6" vtaiu="13" chol="0" fatrn="0" sugar="20" na="41"></nutrition></menuitem>
					<menuitem>Florentine Meatballs
							<serving_size portion='8 oz Serving'></serving_size>
							<portion_size grams='227'></portion_size>
							<nutrition></nutrition></menuitem>
					<menuitem glutenfree="1">Italian Sausage 
							<serving_size portion='Sausage'></serving_size>
							<portion_size grams='85'></portion_size>
							<nutrition p="15 gm" f="17 gm" fc="155" cr="1 gm" cl="217 " so="780 mg" fs="5 gm" fi="0 gm" ft="0 gm" pro="19" fat="26" cho="0" sfa="25" tdfb="0" vitc="2" ca="2" fe="5" vtaiu="3" chol="" fatrn="0" sugar="" na="52"></nutrition></menuitem>
					<menuitem vegetarian="1">Creamy Pesto Sauce 
							<serving_size portion='1/4 Cup'></serving_size>
							<portion_size grams='85'></portion_size>
							<nutrition p="7 gm" f="17 gm" fc="149" cr="9 gm" cl="209 " so="370 mg" ch="37 mg" fs="8 gm" fi="0 gm" su="0 gm" ft="1 gm" pro="9" fat="25" cho="3" sfa="37" tdfb="1" vitc="2" ca="19" fe="3" vtaiu="9" chol="12" fatrn="6" sugar="0" na="25"></nutrition></menuitem>
					<menuitem vegan="1" msmart="1">Spaghetti Pasta 
							<serving_size portion='Cups'></serving_size>
							<portion_size grams='150'></portion_size>
							<nutrition p="8 gm" f="1 gm" fc="8" cr="45 gm" cl="224 " so="704 mg" ch="0 mg" fs="0 gm" fi="2 gm" su="2 gm" ft="0 gm" pro="10" fat="1" cho="16" sfa="1" tdfb="8" vitc="0" ca="1" fe="11" vtaiu="0" chol="0" fatrn="0" sugar="3" na="47"></nutrition></menuitem>
				</course>
				<course>
					<name>Starches1</name>
					<menuitem vegetarian="1">Garlic Bread 
							<serving_size portion='Piece'></serving_size>
							<portion_size grams='34'></portion_size>
							<nutrition p="3 gm" f="8 gm" fc="68" cr="13 gm" cl="131 " so="188 mg" ch="0 mg" fs="1 gm" fi="1 gm" su="1 gm" ft="2 gm" pro="4" fat="11" cho="5" sfa="6" tdfb="2" vitc="0" ca="1" fe="5" vtaiu="0" chol="0" fatrn="9" sugar="1" na="13"></nutrition></menuitem>
				</course>
				<course>
					<name>Vegetables1</name>
					<menuitem glutenfree="1" vegan="1" msmart="1">Broccoli 
							<serving_size portion='1/2 Cup'></serving_size>
							<portion_size grams='113'></portion_size>
							<nutrition p="1 gm" f="0 gm" fc="0" cr="6 gm" cl="40 " so="27 mg" ch="0 mg" fs="0 gm" fi="2 gm" su="2 gm" ft="0 gm" pro="2" fat="0" cho="2" sfa="0" tdfb="9" vitc="66" ca="3" fe="0" vtaiu="0" chol="0" fatrn="0" sugar="5" na="2"></nutrition></menuitem>
					<menuitem glutenfree="1" vegan="1" msmart="1">Italian Blend  
							<serving_size portion='1/2 Cup'></serving_size>
							<portion_size grams='113'></portion_size>
							<nutrition p="2 gm" f="0 gm" fc="0" cr="9 gm" cl="47 " so="40 mg" ch="0 mg" fs="0 gm" fi="2 gm" su="1 gm" ft="0 gm" pro="3" fat="0" cho="3" sfa="0" tdfb="9" vitc="21" ca="3" fe="0" vtaiu="53" chol="0" fatrn="0" sugar="2" na="3"></nutrition></menuitem>
				</course>
			</station>
			<station>
				<name>World Palate</name>
				<course>
					<name>Entree2</name>
					<menuitem vegetarian="1" msmart="1">Spinach &amp; Mushroom Enchiladas 
							<serving_size portion='6 oz Piece'></serving_size>
							<portion_size grams='172'></portion_size>
							<nutrition></nutrition></menuitem>
					<menuitem>Cream Style Chicken Enchilada
							<serving_size portion='Enchilada'></serving_size>
							<portion_size grams='142'></portion_size>
							<nutrition p="16 gm" f="19 gm" fc="167" cr="18 gm" cl="294 " so="717 mg" ch="65 mg" fs="8 gm" fi="1 gm" su="2 gm" ft="1 gm" pro="21" fat="28" cho="6" sfa="36" tdfb="4" vitc="4" ca="16" fe="7" vtaiu="8" chol="22" fatrn="5" sugar="3" na="48"></nutrition></menuitem>
				</course>
				<course>
					<name>Starches2</name>
					<menuitem glutenfree="1" vegan="1" msmart="1">Mexican Rice  
							<serving_size portion='1/2 Cup'></serving_size>
							<portion_size grams='113'></portion_size>
							<nutrition p="3 gm" f="3 gm" fc="28" cr="26 gm" cl="143 " so="169 mg" ch="0 mg" fs="1 gm" fi="1 gm" su="2 gm" ft="0 gm" pro="4" fat="5" cho="9" sfa="2" tdfb="5" vitc="7" ca="1" fe="7" vtaiu="1" chol="0" fatrn="0" sugar="4" na="11"></nutrition></menuitem>
				</course>
				<course>
					<name>Vegetables2</name>
					<menuitem glutenfree="1" vegan="1">Corn w/ Cumin, Chile, &amp; Tomato 
							<serving_size portion='1/2 Cup'></serving_size>
							<portion_size grams='113'></portion_size>
							<nutrition p="3 gm" f="2 gm" fc="14" cr="20 gm" cl="92 " so="525 mg" ch="0 mg" fs="0 gm" fi="3 gm" su="4 gm" ft="0 gm" pro="4" fat="2" cho="7" sfa="1" tdfb="10" vitc="13" ca="1" fe="3" vtaiu="7" chol="0" fatrn="0" sugar="7" na="35"></nutrition></menuitem>
				</course>
			</station>
			<station>
				<name></name>
				<course>
					<name>MiddleEasternBar</name>
					<menuitem>POTATO SKIN BAR
							<serving_size portion='TITLE'></serving_size>
							<portion_size grams='28'></portion_size>
							<nutrition></nutrition></menuitem>
				</course>
			</station>
			<station>
				<name>Pizzeria</name>
				<course>
					<name>Pizza</name>
					<menuitem vegetarian="1">Spinach Feta Pizza 
							<serving_size portion='Slice'></serving_size>
							<portion_size grams='123'></portion_size>
							<nutrition p="11 gm" f="10 gm" fc="90" cr="36 gm" cl="275 " so="522 mg" ch="19 mg" fs="4 gm" fi="2 gm" su="2 gm" ft="0 gm" pro="15" fat="15" cho="13" sfa="17" tdfb="7" vitc="10" ca="16" fe="14" vtaiu="28" chol="6" fatrn="0" sugar="4" na="35"></nutrition></menuitem>
					<menuitem>Chicken Broccoli Alfredo Pizza
							<serving_size portion='Slice'></serving_size>
							<portion_size grams='1052'></portion_size>
							<nutrition p="105 gm" f="74 gm" fc="667" cr="287 gm" cl="2228 " so="4391 mg" ch="261 mg" fs="37 gm" fi="13 gm" su="13 gm" ft="0 gm" pro="140" fat="112" cho="104" sfa="167" tdfb="53" vitc="138" ca="107" fe="100" vtaiu="49" chol="87" fatrn="0" sugar="25" na="293"></nutrition></menuitem>
				</course>
				<course>
					<name>Entree3</name>
					<menuitem>PASTA BAR
							<serving_size portion='TITLE'></serving_size>
							<portion_size grams='28'></portion_size>
							<nutrition></nutrition></menuitem>
				</course>
			</station>
			<station>
				<name>Grill on the Hill</name>
				<course>
					<name>Entree4</name>
					<menuitem glutenfree="1" msmart="1">Grilled Chicken Breast 
							<serving_size portion='3.4 oz Piece'></serving_size>
							<portion_size grams='95'></portion_size>
							<nutrition p="35 gm" f="4 gm" fc="36" cr="0 gm" cl="187 " so="84 mg" ch="96 mg" fs="1 gm" fi="0 gm" su="0 gm" pro="47" fat="6" cho="0" sfa="5" tdfb="0" vitc="0" ca="2" fe="7" vtaiu="0" chol="32" fatrn="" sugar="0" na="6"></nutrition></menuitem>
					<menuitem>Chili Burger
							<serving_size portion='TITLE'></serving_size>
							<portion_size grams='28'></portion_size>
							<nutrition></nutrition></menuitem>
					<menuitem>Hamburger and Hot Dog
							<serving_size portion='TITLE'></serving_size>
							<portion_size grams='28'></portion_size>
							<nutrition></nutrition></menuitem>
					<menuitem vegetarian="1">Spicy Black Bean Sandwich on Wheat
							<serving_size portion='Sandwich'></serving_size>
							<portion_size grams='145'></portion_size>
							<nutrition p="13 gm" f="5 gm" fc="45" cr="44 gm" cl="267 " so="591 mg" ch="0 mg" fs="0 gm" fi="5 gm" su="5 gm" ft="0 gm" pro="17" fat="8" cho="16" sfa="0" tdfb="20" vitc="0" ca="10" fe="16" vtaiu="0" chol="0" fatrn="0" sugar="10" na="39"></nutrition></menuitem>
				</course>
			</station>
			<station>
				<name>Just Dessert</name>
				<course>
					<name>Desserts</name>
					<menuitem vegetarian="1">Strawberry Cheesecake 
							<serving_size portion='Piece'></serving_size>
							<portion_size grams='116'></portion_size>
							<nutrition p="5 gm" f="23 gm" fc="204" cr="30 gm" cl="338 " so="256 mg" ch="102 mg" fs="11 gm" fi="0 gm" su="24 gm" ft="1 gm" pro="7" fat="34" cho="11" sfa="48" tdfb="2" vitc="3" ca="10" fe="4" vtaiu="14" chol="34" fatrn="4" sugar="48" na="17"></nutrition></menuitem>
					<menuitem vegetarian="1">Chocolate Chip Cookies 
							<serving_size portion='Cookie'></serving_size>
							<portion_size grams='38'></portion_size>
							<nutrition p="2 gm" f="7 gm" fc="63" cr="24 gm" cl="169 " so="115 mg" ch="7 mg" fs="4 gm" fi="1 gm" su="12 gm" ft="0 gm" pro="3" fat="11" cho="9" sfa="18" tdfb="4" vitc="0" ca="12" fe="6" vtaiu="4" chol="2" fatrn="0" sugar="24" na="8"></nutrition></menuitem>
				</course>
			</station>
		</meal>
	</menu>
</dininghall>
"""        
        self.menu = umdh.get_menu(self.xml)

if __name__ == '__main__':
    unittest.main()

