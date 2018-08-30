import gensim
import logging
import os.path
import multiprocessing
import sys

from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

# each sentence is on one separate line
len_sentences = 1041518
# len_articles =


class SimpleWikiIterator:
	def __init__(self, max, path):
		self.max = max
		self.count = 0
		self.articles = None
		self.FileHandle = open(path, "r", encoding="utf-8")

	def __iter__(self):
		# self.articles = ReadInput("/Users/mihirumeshnimgade/Desktop/articles.txt")
		return self

	def __next__(self):
		article = self.FileHandle.readline()
		article = gensim.utils.simple_preprocess(article)
		self.count = self.count + 1
		if self.count >= self.max:
			raise StopIteration

		return article


def ReadInput(input_file_path):
	with open(input_file_path, "r", encoding="utf-8") as FileHandle:
		for line in FileHandle:
			yield gensim.utils.simple_preprocess(line)


if __name__ == "__main__":
	program = os.path.basename(sys.argv[0])
	logger = logging.getLogger(program)

	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
	logging.root.setLevel(level=logging.INFO)
	logging.info("Running {}".format(" ".join(sys.argv)))

	try:
		inp, outp = sys.argv[1:3]

	except ValueError:
		print("ERROR: Not enough arguments in command line.")
		sys.exit(1)

	model = Word2Vec(LineSentence(inp), size=300, window=10, min_count=3, workers=multiprocessing.cpu_count())

	model.init_sims(replace=True)

	model.save(outp)

#
# sentences = SimpleWikiIterator(len_sentences, file_path)
#
# model = gensim.models.Word2Vec(sentences, size=250, window=10, min_count=3, workers=10)
# model.train(sentences, total_examples=len_sentences, epochs=100)
#
# print("Training on: {}".format(file_path))
# model.save("SimpleWikiModel.model")


# w1 = ["polite"]

# model.wv.most_similar(positive=w1, topn=6)


