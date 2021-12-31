print("Hoşgeldiniz ...")
print("Lütfen Sizden istenilen sayıları abartmadan girin yoksa uğraşırsınız benden söylemesi")
while True:
	vize = float(input("Vize notunuzu girin"))
	if (vize<0) or (vize>100) :
		print("dalga mı geçiyosun lan köpek...")
		
	else:
		break

while True:
	final = float(input("Final notunuzu girin"))
	if (final<0) or (final>100) :
		print("lan caz etme...")
       
	else:
		break

while True:
	while True:
		vize_etki = float(input("Vizenin etki yüzdesi"))
		if (vize_etki<0) or (vize_etki>100) :
			print("aaaa ayıp...")
			
		else:
			break

	while True:
		final_etki = float(input("Final etki yüzdesi"))
		if (final_etki<0) or (final_etki>100) :
			print("lan caz etme...")
	   	    
		else:
			break

	if vize_etki+final_etki != 100 :
		print("bi yanlışlık var koççum")
	else:
		break




print((vize*vize_etki)/100 + (final*final_etki)/100)

if ((vize*vize_etki)/100 + (final*final_etki)/100) > 60 :
	print("helqqqqqqql")
else:
	print("mal mısın bilader") 







