from LZW import *
#from RSA import *
from vigenere import *


if __name__ == '__main__':

	text = 'Mi nombre es Santiago Gutiérrez Bárcenas, y estoy terminando mi 4° semestre de ITC!'
	text2 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum rutrum odio nisi, in molestie nulla ultricies egestas. Phasellus dapibus nibh eget magna pretium semper. Nullam eleifend in augue nec lobortis. Donec sodales odio et ex venenatis, in volutpat diam aliquet. Fusce lorem mauris, luctus nec justo eu, posuere ultricies ante. Nunc massa nunc, mattis eget lorem sit amet, suscipit tempor nisl. Vivamus tempor, eros vitae malesuada tristique, nisi est pulvinar sapien, eu luctus libero ante elementum diam. Cras sit amet est sapien. Phasellus fermentum eros ex, sed eleifend massa laoreet in. Nam scelerisque dui neque, id porttitor diam iaculis et. Nullam auctor sit amet erat quis pharetra. Nullam suscipit eros vitae dui aliquet, quis cursus sem varius. Morbi dui augue, pellentesque eu orci vel, pretium feugiat est. In porttitor ante in ligula ultricies fringilla. Nunc cursus nisi id consectetur blandit. Donec rhoncus justo at tellus venenatis aliquam. Pellentesque posuere pulvinar nulla, quis semper dui efficitur viverra. Sed at eleifend nibh. Proin placerat varius lorem a gravida. Nulla aliquet tempor tortor, eu lobortis sapien. Maecenas eu risus vitae mauris eleifend commodo eu et augue. Sed ornare massa eu neque pulvinar eleifend. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus vel porta nibh. Aliquam erat volutpat. Aliquam et augue fringilla, imperdiet mi in, fringilla neque. Vivamus accumsan pellentesque facilisis. Integer eros turpis, viverra et fermentum quis, cursus sit amet justo. Quisque blandit venenatis ligula a tincidunt. Vivamus et nibh fermentum nunc blandit dictum. Integer efficitur vulputate leo eget euismod. Etiam dapibus viverra erat, ac elementum nibh consectetur eget. Donec rutrum non arcu vel imperdiet. Aenean ut metus sed dolor dignissim elementum quis ac nisl. Aenean at hendrerit felis. Quisque porttitor suscipit elementum. Nam ut elementum massa. Suspendisse finibus ultricies elit, id faucibus tortor vestibulum ut. Integer feugiat est velit, at semper nulla accumsan ac. Nullam a erat a lacus aliquet vehicula. Morbi nec hendrerit massa. Donec mollis sapien sed vestibulum finibus. Ut aliquet congue eros et feugiat. Suspendisse potenti. Proin ut turpis quam. Morbi sem eros, ultricies id consectetur sed, sollicitudin sed sem. Praesent vitae tincidunt magna. Integer consectetur nunc non nisl porta, ut pharetra dolor commodo. Aliquam eu dui ex. Phasellus sit amet ex nisi.'
	compText = compress(text)
	print("compressed text: " + str(compText))
	compToInt = compToInt(compText)
	print("compressed text to int list: " + str(compToInt))
	#pasar de lista de ints a sting de ints con espacio
	#encryptar
	#mandar
	#recuperar
	#desencryptar
	#pasar de string de ints con espacio a lista de ints
	#descomprimir
	#(n, e, d) = newKey(10**10, 10**11, 50)

	#cipher = encrypt(compToInt, n, e, 8)
	cipher = vign(', '.join(str(i) for i in compToInt), 'super secret key', 'e')
	#print("compressed text encrypted: " + str(cipher))
	print("compressed text encrypted: " + cipher)

	#Amessage = decrypt(cipher, n, d, 8)
	Amessage = vign(cipher, 'super secret key', 'd')
	#print("compressed text decrypted: " + str(Amessage))
	print("compressed text decrypted: " + Amessage)

	#decompText = decompress(Amessage)
	AmessageList = Amessage.split(', ')
	AmessageList = list(map(int, AmessageList))
	decompText = decompress(AmessageList)
	print("decompress text: " + str(decompText))	