import logging
import os.path
import six
import sys

from gensim.corpora import WikiCorpus

if __name__ == "__main__":  # if the program is being run directly and is not being imported...
	program = os.path.basename(sys.argv[0])
	logger = logging.getLogger(program)

	logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
	logging.root.setLevel(level=logging.INFO)
	logger.info("running %s" % ' '.join(sys.argv))

	if len(sys.argv) != 3:
		print("Use python3 ExtractArticles.py enwiki.xxx.xml.bz2 wikien.txt")
		sys.exit(1)  # exits from python

	inp, outp = sys.argv[1:3]
	space = " "
	i = 0

	output = open(outp, "w", encoding="utf-8")

	wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
	count = 0
	for text in wiki.get_texts():  # wiki.get_texts() is generator object
		output.write(bytes(' '.join(text), 'utf-8').decode('utf-8') + '\n')
		i = i + 1
		if (i % 10000 == 0):
			logger.info("Saved", str(i), "articles")

	output.close()
	logger.info("Finished saving", str(i), "articles")

