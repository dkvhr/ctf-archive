import math, random

vs = [31005360692828771386596353653543080975611848310275677906468025883091275536545167105261124978438034147369188014602835017411169298219342736416588987721898236006802048428404041584458078499270366055804924314464708385993225538155867778051617636634963113851057969608562494259051877395015398693466973087730499566816,
 17003437166562532515844106142524538192236293899469976413289579740724428355550116481428488291812235319677070040082605038993073040331140608920350241120022851558346432621670007181699937945547373727724759938611690319982732107888720517628308820580311202134000460906280625430109296787202502455537645045333723875752,
 29174185611116220962799861273321049541177801510857918591464872309427445827132983964415082854825522385424024880171489587050870327940507996424702159659128701464907642376464689444333141169481878286907345745404828547335614802358867901971902132545117165403375274703755554934141448611451802010293341880379370554561,
 125460590004305449147598588597557979060854193390844088734591499750759733001199888802591738726623448330311758719958038839952378685281112813215510694177186929054969282542095414098207160009054665089179363764003511090704679824298401019113194375501442314588314578517699812773773019403193586734854985273328635385055,
 19961294398306208246516388863238101732563713331299984864649284895060139019545904701008851276488071800446599645920026490167722906555546322707624066875634270141393732401477451591847349367408737337443347321838579886436683791129742451743718669743273896717234716046751184390492739638845925077804129476280894587678,
 85759222192752433194230697887711126281106122783081924950901615172513157367176074634125033381905762875617483238087728494458681538256649219217623424520916997213186188830148291657362762967628984919300629388058437915776797004797233986842897245030445740378865717209897013176637432910563576770716288211875307537517,
 85756446259856921508787301328839382632358568749059657140427887760093397703593939932207573717990801926895166230152544896721929259636016715518976734411563923826677102375960841166413322973739298659736043313753661245283753764679577053027839731159065511835543011526555470830658319777501171567780422415764654992056,
 82388131875829029661101368892682715986939359081248501091530913224018273957577087466263577726214250285693305077844539728656326817171067073853850608506120849994426900463296485737789551617317170895674315973559170374018674736805141600527972171162907019499396489435300753463848663364800413387059802301944791967154,
 61874622466735870459569083231063053251267849847000913303657112974804972902993400011219498998891866923360766164579107153740819838758946654392655104600224167442300655739937590833004721216390278521069704959271872181745467822038505719847771201473641058909334550358152794876346560209282634319394970440121173945552,
 696456830160336345571399183079182741633849680581905262467031047063176916643115772014345688408518942964376072396456547900927062045479626987185284640272622480349326540389607018847447286302777265518431029908665242525779132608960411992603618266965991610156140888732414587461875885957790157094122534925159346689,
 71804202927858745830267764119644267668129650849943354839400674871922181310019705024971084995567979858935550418547572368395805873047838678582034544829126818329655094801668736612934902996138698939011569804762884310261018579282273855111801383769541884936774208421184998499608044833422057806517766421872161132886,
 106022129909231001763061571981224795908743244297610781372585165509220208538934481499465999219069414858130465495020451194529977735536353918041012038153453667083523463694391202798426848791814698095144964507083362144746009311262885344497647348164258983213008548680124197839483415994938575552424579467559364226394,
 79780917201979725745607358268721020007826777143384453736848699642700745672137173971736311615633907786242787949553655269760889512741694366981329213468801870502366422166155726704782007053727452518531937861897316842120152867293007447953786050973095793666505368420908012089034040670612704915966483909560525727895,
 71557442214224827391469508394615301961602393583435791994377869878166990967262275214062328407117187137475555170232198898164685460045507551050582228050707942188085718362485298023919336310901655232305201374173084046735689446183908677611125291513420419391257086412077716834947280648573355262416021905501885448081,
 67594286124920462476627135231382127257002190779316200841220884236048746008966783849077000692260673412618118130199139132355982916586542143504156315436305992979554984024473698424640430169503131050669710368164448012799563109078824274602902218944141689141292330786328930992108442995656576429460357487607953684648,
 101583462751604776803243993092916816311165997626216071624266181903436631387504324465830005005386962747575225905966606713728165379859319120868463362676191328036131523437697792122960792959701853400135227605129646395597066487494604129199511056307707630333472846727757095032870573194684669438190245204424382540227,
 29043532212255484957446139638896400984289208179934060026479276758708631324599797061541074121781125966015258864597551222042987263443007351938876659168617793511003131118910137322436111104004390147581694271638980718344008124629582446582217883153690914798022031966640578663222585208907959178728356893175434723610,
 113340247020681948079695872194976603365438756195928636169270488788917611617814113546377399221147222383967017644725891131669673531498667023285512916587556607375207726512057338389146049968613792335715667746005162571620120695763511785836708610889000014042339862130979073911779127629605240998224547392575047876682,
 46955518876625368675822179494683910075678740531193723819896673420339533169552243807905153158613702064339351238345928246687600501515910421042905452498300246264603811562471815530515808019347916054179239559497819912359365282659383474647330398618675852858416854053277986827281681810780557251419111207395384329582,
 120049618241681569909297331132748153780024599551354169447395482524979354550145095689508448686689137027749682317450210890592755207357509317097636185840145549723162917702190119496725634407024403910897248195711908599301017670168856033698276539121376856533747174795130257635826700269955484116577244261132111699782,
 60432471682725082811759129481935215387315232681862328001741140440791554213018023010489880896595833371259778283949132264865412666062423360678545503784341426955365066642545574839397376104725781749864189394942679623268519980669230151124096948927295064323127086412146079703473349033037612579125128356650817487456,
 37418483423666402839690378221246465625830777504746117806684279632733829251216330191017630819870365706918196686286152419906279282424710986544493588315677256309469899069653777460941985890670325799772557996489677861822249868822961811308197155317508879408561403754321591134754997450382970689051378137266750684150,
 94174305519000724791322723317329750424096787028033711704339348290558759801740049477712054371174943463065457783285954839036454616821525907268058171065879142917786495838108198662366655161612057302696631811010611011255432667247182226813098616120103551428491424725197433682478003725612614176776020744086919222541,
 24164241604266297223727480356209579709626597863679665322047206314565390941211173439548364239141231528592770594273872245081689352467521934142614188404599821263744908154769724757582237869492893025673929736513067776621594315983578685131819723930259557347442783311769159432538118936437741231426466439416046894515,
 74622351574515732429790381710009931007866489477834175140157124276528406761996848988548319863921078012073579268829764616677869729971070246760618409482467230230803686916114021420025321663417775786933625703525549140238175443629067327379706879303686757054222768671452028284790228129715765919768466932861580177320,
 33937434233671439880375735724709263151905800341491069761198253595974939676740898135994731926683522580603065238113188655760345413710993518921798283138295535808198625333887785443443202146206856012920897507527127519126218980262002819131272588055386977789016168450026793837491263146307483296161517902030713517377,
 10565046949406254527259004982669830730136541099125452731723342603077281798643238458884681573548361200290844403261801977491071537055797916302144525394519319159626752240186678311227956848271289073464355638512015901912643836265454790756672118181585365806395738728791224300698625162338483047206782990009007697670,
 45811173098907052453006784108724539278636502672866844019358000284740987849657198740051498233451460856145761002845913988279624670560647919319575981910876044410412471633476034363962715376923711191994020783024820681562347221375725447749166869482488722405826252864632495369187682453210518381724556170610428602786,
 37611584083840831490614982219698954124380150735010410340428124992949372626303544516341138055985977817455320480587362067024966082099429303253313338863882848425274492128334874580589539103195746970062266826430461363725325127697110242929749428596070134635340701183252297726266360348704483104671237230680814287901,
 63566257454663927502592210664825649462300912342152118232791252636924231391880938521602773487560023194335856577303191126352162460670337534320352698547886676856711838450730563961823133844577285769273115911949304965589463357010794272474951671929048390288857822150939329767267412994414792438086489683307370084703,
 4382509570704473659016023535170200173820928728265283666614190827403468236099707584217820071734335424735984543344162682931307960434798257881978990978766599003220115166247656988541408469257367969448130796067767889157154616317680686438607572706708714502749949797831276453814186123967065644440309075672960825747,
 119585523909572054887470634581863538142805156350226237796155733329562580962263310326370106947802333782405813135361772225815937510220709539567577696634536092564064682426435237869943718053754860155062301650004865386777823106520550443602415692105791093795113771899736853625134293105156697170557701359916135902683]

n = 127065271926831953829075435795779161413833625790937903632507803948456546315363951012628967625137524987630310358727885075791147997786165834290015104663544334943097795607318784623877555709432254007987036792912055232108170428981314621636112866695628891544476820238732869726592273172162728945930329074829450057467

print('n =', n)
print('vs =', vs)

correct = 0

for _ in range(1000):
	r = 1
	for j in range(32):
		if mask[j] == '1':
			r *= pow(vs[j], -1, n)
	r = r % n

	print(r)
	x = int(input('Pick a random r, give me x = r^2 (mod n): '))
	assert x > 0
	mask = '{:032b}'.format(random.getrandbits(32))
	print("Here's a random mask: ", mask)
	y = int(input('Now give me r*product of IDs with mask applied: '))
	assert y > 0
	# i.e: if bit i is 1, include id i in the product--otherwise, don't
	
	val = x
	for i in range(32):
		if mask[i] == '1':
			val = (val * vs[i]) % n
	if pow(y, 2, n) == val:
		correct += 1
		print('Phase', correct, 'of verification complete.')
	else:
		correct = 0
		print('Verification failed. Try again.')

	if correct >= 10:
		print('Verification succeeded. Welcome.')
		print(flag)
		break