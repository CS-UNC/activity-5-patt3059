#words_file = open( 'file' , 'r')
#words = []
#words.append
#print([x for x in words_file if x in len(words_file) >= 20])

def more_than_20(file):
   data = open(file, 'r')
   word = [x.strip() for x in data if len(x.strip()) > 20]
   return word 

def has_no_e(word):
   if 'e' in word:
      return False
   else:
      return True
 

def uses_only(word,letters):
   for x in word:
      if x not in letters:
         return False
   return True

def all_uses_only(file, letters):
   words = open(file, 'r')
   for x in words:
      uses_only(words, letters)

