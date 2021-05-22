#48. WAP to delete element from counter generated in Que 43

from collections import Counter
import logging
logger=logging.getLogger()
fhandler=logging.FileHandler(filename='6test.log', mode='a')
formatter=logging.Formatter('%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)

ignore = ['the','a','if','in','it','of','or']
LIST=['the','war','Chistats','war']
ArtofWarCounter = Counter(LIST)
logging.warning(ArtofWarCounter)
for word in list(ArtofWarCounter):
    if word in ignore:
        del ArtofWarCounter[word]
logging.warning(ArtofWarCounter)

"""Output
21-May-21 19:04:30 - Counter({'war': 2, 'the': 1, 'Chistats': 1})
21-May-21 19:04:30 - Counter({'war': 2, 'Chistats': 1})"""