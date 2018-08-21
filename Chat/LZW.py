from io import StringIO
import os

def compress(uncompressed):
	dict_size = 256 
	dictionary = {chr(i): chr(i) for i in range(dict_size)}

	w = ""
	result = []

	for c in uncompressed:
		
		wc = w + c
		if wc in dictionary:
			w = wc
		else:
			result.append(dictionary[w])
			dictionary[wc] = dict_size
			dict_size += 1
			w = c

	if w:
		result.append(dictionary[w])
	return result

def compToStr(compressed):
	strTemp = ""
	for c in compressed:
		strTemp += str(c)
	return strTemp

def compToInt(compressed):
	intTemp = []
	for c in compressed:
		if(isinstance(c,str)):
			c = ord(c)
		intTemp.append(c)
	return intTemp

def decompress(compressed):
	dict_size = 256
	dictionary = {chr(i): chr(i) for i in range(dict_size)}

	result = StringIO()
	w = compressed.pop(0)
	if(isinstance(w, int) and w<256):
		w = chr(w)	
	result.write(w)

	for k in compressed:
		if (isinstance(k,int) and k<256):
			k = chr(k)
		if k in dictionary:
			entry = dictionary[k]
		elif k == dict_size:
			entry = w + w[0]
		else:
			raise ValueError('Bad compressed k: %s' %k)
		result.write(entry)

		dictionary[dict_size] = w + entry[0]
		dict_size += 1

		w = entry
	return result.getvalue()

#if __name__ == '__main__':
#
#	text = 'Kai Kawasaki Ueda APPLEPIEAPPLEAPLEPPAPP'
#	compText = compress(text)
#	compToInt = compToInt(compText)
#
#	decompText = decompress(compToInt)
#
#	print(compText)
#	print(compToInt)
#	print(decompText)
