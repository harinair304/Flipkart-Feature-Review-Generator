import nltk
import re
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.corpus import stopwords
from nltk.corpus import sentiwordnet as swn
from sumy.parsers.plaintext import PlaintextParser 
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer

class Feature:

	def __init__(self, featureName):

		self.featureName = featureName
		self.positiveOp = []
		self.negativeOp = []
		self.summaryOp=[]



print "Creating POS Tagged database"
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

pattern = """
NP:
{<DT|PP\$>?<JJ>*<NN>}
{<NNP>+}
{<NN>+}
"""

stop = set(stopwords.words('english'))

# pattern = """
# NP:
# {<DT|PP\$>?<JJ>*<NN>}
# """


NPChunker = nltk.RegexpParser(pattern)


with open('Reviews.txt','rb') as fp:
	data = fp.readlines()

data_intermediate = ''.join(data).decode('utf-8')

with open('Reviews_POS.txt','w') as fp:
	fp.write('\n'.join(sent_tokenize(data_intermediate)).encode('ascii','ignore'))



with open('Reviews_POS.txt','rb') as fp:
	with open('test.txt','w') as fw:
		for line in fp:
			# fw.write('' pos_tag(word_tokenize(line)) )
			# fw.write('\n')
			
			# fw.write( ''.join(str(s) for s in pos_tag(word_tokenize(line))))
			# fw.write('\n')

			np_chunks = NPChunker.parse(pos_tag(word_tokenize(line)))
			# print np_chunks
		
			for n in np_chunks:
				if isinstance(n, nltk.tree.Tree):
					if n.label() == 'NP':
						# fw.write(str(n))
						# fw.write('\n')
						tree = nltk.Tree.fromstring(str(n), read_leaf=lambda x: x.split("/")[0])
						sentence = re.sub('[^a-zA-Z0-9\n\.]', ' ', str(tree).replace('NP',''))
						scrub_sentence = [i for i in sentence.lower().split(' ') if i not in stop]
						fw.write(' '.join(scrub_sentence))
			
			fw.write('\n')		



with open('test.txt','rb') as fp:
	data = fp.read().replace('\n', ' ')
 

data = data.split()

fdist1 = nltk.FreqDist(data)


common = (fdist1.most_common(100))

features = [x[0] for x in common]

print features

featureObs = [ Feature(features[i]) for i in range(100)]

featCount = 0


with open('Reviews_POS.txt','rb') as fp:
	with open('test1.txt','w') as fw:
		with open('OpinionWords','w') as fo:


			for word in features:
				fw.write('['+word+']')
				fw.write('\n')
				fo.write('['+word+']')
				fo.write('\n')
				for line in fp:


					if word in line:
						tagged_sentence = pos_tag(word_tokenize((line)))
						if any('JJ' in tag for tag in tagged_sentence):
							positive_score=0
							negative_score =0
							opinionWord = [t[0] for t in tagged_sentence if t[1] == 'JJ']
							for op in opinionWord:
								try:

									opinion = swn.senti_synset(op+'.a.01')
									positive_score+=opinion.pos_score()
									negative_score+=opinion.neg_score()

									

								except nltk.corpus.reader.wordnet.WordNetError:

									print op+' is not a word'
							fo.write(' '.join([t[0] for t in tagged_sentence if t[1] == 'JJ']))
							fo.write(' positive_score: '+str(positive_score))
							fo.write(' negative_score: '+str(negative_score))
							fo.write('\n')

							featureObs[featCount].summaryOp.append(line)

							if(positive_score >= negative_score):
								fw.write(line.rstrip()+' -> Positive')
								featureObs[featCount].positiveOp.append(line)
							else :
								fw.write(line.rstrip()+' -> Negative')
								featureObs[featCount].negativeOp.append(line)
							fw.write('\n')
				featCount+=1
				fp.seek(0)


stemmer = Stemmer("english")
summarizer = Summarizer(stemmer)



with open('Feature_Review.txt','w') as fw:

	for i in range(100) :
		fw.write('\n\n\n*****************************\n')
		fw.write('FEATURE: '+featureObs[i].featureName+' POSITIVE OPINIONS: '+str(len(featureObs[i].positiveOp))+' NEGATIVE OPINIONS: '+str(len(featureObs[i].negativeOp)))
		fw.write('\n*****************************\n')
		# fw.write('\n*******SUMMARY REVIEW*******\n')
		# parser = PlaintextParser(''.join(featureObs[i].summaryOp),Tokenizer("english"))
		# for sentence in summarizer(parser.document,50) :
		# 	fw.write(str(sentence))
		fw.write('\n*******POSITIVE REVIEWS*******\n')
		parser = PlaintextParser(''.join(featureObs[i].positiveOp),Tokenizer("english"))
		# fw.write(''.join(featureObs[i].negativeOp))
		for sentence in summarizer(parser.document,10) :
			fw.write(str(sentence))
		fw.write('\n\n\n')
		# fw.write(''.join(featureObs[i].positiveOp))
		fw.write('\n*******NEGATIVE REVIEWS*******\n')
		parser = PlaintextParser(''.join(featureObs[i].negativeOp),Tokenizer("english"))
		# fw.write(''.join(featureObs[i].negativeOp))
		for sentence in summarizer(parser.document,10) :
			fw.write(str(sentence))


# parser = PlaintextParser(''.join(featureObs[0].positiveOp),Tokenizer("english"))

# for sentence in summarizer(parser.document,50) :
# 	print sentence










					# fw.write(word+' : '+ ''.join(str(s) for s in pos_tag(word_tokenize((line)))))
					# fw.write('\n')


	




			# fw.write('\n'.join(str(s) for s in pos_tag(word_tokenize(''.join(line).decode('utf-8')))))

        