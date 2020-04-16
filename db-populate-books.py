import sqlite3

connie = sqlite3.connect('books.db')

c = connie.cursor()

c.execute("""
INSERT INTO books (ISBN, author, title, publisher, date, fiction, genre) 
VALUES 
('9780147514011','Alcott, Louisa May','Little Women','Penguin','2014','Fiction','Literature'),
('9780802144119','Anderson, Jon Lee','Che Guevara: A Revolutionary Life','Grove Press','2010','Non-fiction','Biography'),
('9781784742324','Atwood, Margaret','The Testaments','Vintage Publishing','2019','Fiction','Dystopia'),
('771008139','Atwood, Margaret','The Handmaid''s Tale','McLelland and Stewart','1985','Fiction','Dystopia'),
('9780812968255','Aurelius, Marcus','Meditations','Modern Library','2002','Non-fiction','Philosophy'),
('9780743247221','Bradbury, Ray','Fahreinheit 451','Ballantine Books','1953','Fiction','Dystopia'),
('9780241951446','Burgess, Anthony','A Clockwork Orange','Penguin','2011','Fiction','Dystopia'),
('9780241003008','Carle, Eric','The Very Hungry Caterpillar','Penguin','2019','Fiction','Children'),
('9780062898104','Dalton, Trent','Boy Swallows Universe','Harper','2019','Fiction','Coming of age'),
('436201585','de Bernieres, Louis','Captain Corelli''s Mandolin','Secker and Warburg','1994','Fiction','War'),
('9781840224306','Dostoyevsky, Fyodor','Crime and Punishment','Wordsworths','2000','Fiction','Literature'),
('9780007466863','Feist, Raymond E. ','Magician','Collins','1993','Fiction','Fantasy'),
('9780007509171','Feist, Raymond E. ','Silverthorn','Harper Voyager','2013','Fiction','Fantasy'),
('9780007509119','Feist, Raymond E. ','A Darkness at Sethanon','Voyager','2013','Fiction','Fantasy'),
('9780330375252','Fielding, Helen','Bridget Jones'' Diary','Picador','1996','Fiction','Comedy'),
('9780330367356','Fielding, Helen','Bridget Jones: The Edge of Reason','Pan Macmillan','1999','Fiction','Comedy'),
('9780152632243','Fox, Mem','Possum Magic','Voyager','1991','Fiction','Children'),
('9781681680521','Frankopan, Peter','The Silk Roads: A New History of the World','Bloomsbury','2016','Non-fiction','History'),
('9780393343892','Friedberg, Aaron L','A Contest for Supremacy','WW Norton','2012','Non-fiction','Politics'),
('9780099590088','Harari, Yuval Noah','Sapiens: A Brief History of Humankind','Vintage Publishing','2011','Non-fiction','History'),
('62464310','Harari, Yuval Noah','Homo Deus: A Brief History of Tomorrow','Vintage Publishing','2016','Non-fiction','History'),
('671128051','Heller, Joseph','Catch 22','Simon and Schuster','1961','Fiction','Satire'),
('9780441172719','Herbert, Frank','Dune','Ace','1965','Fiction','Science Fiction'),
('9780450022852','Herbert, Frank','Dune Messiah','Ace','1969','Fiction','Science Fiction'),
('9780723263661','Hill, Eric','Where''s Spot? ','Penguin','2011','Fiction','Children'),
('9780671510992','Kissinger, Henry','Diplomacy','Simon and Schuster','1995','Non-fiction','Politics'),
('9780141049427','Kissinger, Henry','On China','Penguin','2012','Non-fiction','Politics'),
('9780099549482','Lee, Harper','To Kill a Mockingbird: 50th Edition','Arrow','2010','Fiction','Literature'),
('9780060197766','Lee, Kuan Yew','From Third World to First: The Singapore Story','Harper Collins','2000','Non-fiction','History'),
('9781529105100','Mackesy, Charlie','The Boy, The Mole, The Fox and the Horse','Ebury Publishing','2019','Fiction','Growth'),
('9780099429791','McEwan, Ian','Atonement','Vintage Publishing','2002','Fiction','Literature'),
('9780522873153','Morton, Rick','One Hundred Years of Dirt','Melbourne University Press','2018','Non-fiction','Autobiography'),
('9780141036137','Orwell, George','Animal Farm','Penguin','2008','Fiction','Dystopia'),
('9780730324218','Pape, Scott','The Barefoot Investor 2019 Update','John Wiley and Sons','2018','Non-fiction','Finance'),
('9780674979857','Piketty, Thomas','Capital in the Twenty-First Century','Belknap Press','2017','Non-fiction','Economics'),
('9780385604413','Pullman, Phillip','La Belle Sauvage','David Fickling Books','2017','Fiction','Fantasy'),
('590541781','Pullman, Phillip','The Golden Compass','Scholastic Print','1995','Fiction','Fantasy'),
('9780241373347','Pullman, Phillip','The Secret Commonwealth','David Fickling Books','2017','Fiction','Fantasy'),
('9781101980996','Roberts, Andrew','Churchill','Viking Press','2018','Non-fiction','Biography'),
('684808293','Steel, Ronald','In Love with Night','Simon and Schuster','2000','Non-fiction','Biography'),
('9780316219266','Stone, Brad','the everything store','Little Brown and Co','2013','Non-fiction','Business'),
('9780733339745','Sullivan, Kevin','No Man''s Land: the untold story of automation and QF72','ABC Books','2019','Non-fiction','Memoir'),
('9780007420124','Tzu, Sun','The Art of War','Collins Classic','2011','Non-fiction','Military'),
('9780008220563','Vance, J.D.','Hillbilly Elegy','William Collins','2017','Non-fiction','Memoir'),
('9781760640996','White, Hugh','How to Defend Australia','La Trobe University Press','2019','Non-fiction','Military')
""")

connie.commit()
connie.close()
