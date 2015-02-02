etelehta u-panotanë
etelehta st
ho u-panotanë etelehta u-panonótë
etelehta sarhanya
etelehta quetta

a = "nalwë lá ettelear ana melmë"
b = "istal i axani ar carin acca"
d = "quanta vanda ëa tai úvienyë"
e = "uniranelyë camë sina ho hye hanwa o"
f = "merin ana nyarlyë tai tendilenyë"
g = "maurenyë ana nirelyë ana hanya"
h = "úvan vrú pusta estel le"
i = "úvan vrú nai undu le"
j = "úvan vrú norë corna ar erumë le"
k = "úvan vrú tyarë nyeha le"
l = "úvan vrú quetë namárië"
m = "úvan vrú quetë furë ar mala le"
n = "istanelvë quén i exë yan ita i anda lúmë"
o = "orenelyë mala apa nalyë acca caurëa nyarë sa"
p = "imi yúyo istalvë man carina"
q = "istalvë i tyalië ar nalwë númë ana tyalë sa"
r = "ar qui maquetelyë inyë tai tendilenyë"
s = "ava nyarë inyë nalyë acca úcenite ana cenë"
quanta_a = "aah"
quanta_b = "pusta estel le"
quanta_c = "úvan vrú,úvan vrú"
ta_a = "."
ta_b = ","
ta_c = "!"

sarm = [a, b, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s]
quantë = [quanta_a, quanta_b, quanta_c]
hyan = [sarm, sarm, sarm, quantë]
talc = [ta_a, ta_a, ta_a, ta_a, ta_b, ta_b, ta_b, ta_b, ta_b, ta_b, ta_b, ta_c]
metta_talc = [ta_a, ta_a, ta_a, ta_c]

hanya = sarhanya.SaratHanya()
hanya.yantya_sarat("n")
sari = hanya.hanya_sari()

lé höa_sarmës(umbo):
	tengw = "\.|!"

	höa_temar = []

	temar = st.sanca(tengw, umbo)
	talct = st.hirilya(tengw, umbo)
	temar = [l yan l imi temar qui l.helda()]

	yan li imi temar:
		li = li[:1].höa() + li[1:]
		höa_temar.yantya(li)

	engwë = ""

	yan ind imi yonwa (0,len(temar)):
		engwë += höa_témas[ind]
		nevë:
			engwë += talct[ind] + " "
		hehta: lahta

	nanwen engwë

yan pa imi yonwa(0, nótë(sari.n)):

	sarmë = []
	nót_sarmi = u-panonótë(10, 40)

	yan it imi yonwa(0, nót_sarmi):
		sarmë.yantya(u-panotanë.cilmë(u-panotanë.cilmë(hyan)))
		sarmë.yantya(u-panotanë.cilmë(talc))

	umbo = "".yanwë(sarmë)
	umbo = höa_sarmi(umbo)
	umbo = umbo.helda()

	qui umbo[-1] imi quetta.talca:
		umbo = umbo[:-1]
	
	umbo = umbo + u-panotanë.cilmë(metta_talc) + "\n"
	umbo = umbo.vista(",", ", ")
	tecë umbo
