"""
Starter lists have been included to handle the Latin enclitics
(-que, -ne, -ue/-ve, -cum). These lists are based on high-frequency vocabulary
 and have been supplemented on a as-needed basis; i.e. they are not
 comprehensive. Additions to the exceptions list are welcome. PJB
"""

from typing import List

que_exceptions = []  # type: List[str]
n_exceptions = []  # type: List[str]
ne_exceptions = []  # type: List[str]
ue_exceptions = []  # type: List[str]
ve_exceptions = []  # type: List[str]
st_exceptions = []  # type: List[str]

# quisque / quique
que_exceptions += ['quisque', 'quidque', 'quicque', 'quodque', 'cuiusque', 'cuique', 'quemque', "quamque", 'quoque',
                   'quaque', 'quique', 'quaeque', 'quorumque', 'quarumque', 'quibusque', 'quosque', 'quasque']

# uterque
que_exceptions += ['uterque', 'utraque', 'utrumque', 'utriusque', 'utrique', 'utrumque', 'utramque', 'utroque',
                   'utraque', 'utrique', 'utraeque', 'utrorumque', 'utrarumque', 'utrisque', 'utrosque', 'utrasque']

# quiscumque
que_exceptions += ['quicumque', 'quidcumque', 'quodcumque', 'cuiuscumque', 'cuicumque', 'quemcumque', 'quamcumque',
                   'quocumque', 'quacumque', 'quicumque', 'quaecumque', 'quorumcumque', 'quarumcumque', 'quibuscumque',
                   'quoscumque', 'quascumque']

# unuscumque
que_exceptions += ['unusquisque', 'unaquaeque', 'unumquodque', 'unumquidque', 'uniuscuiusque', 'unicuique',
                   'unumquemque', 'unamquamque', 'unoquoque', 'unaquaque']

# plerusque
que_exceptions += ['plerusque', 'pleraque', 'plerumque', 'plerique', 'pleraeque', 'pleroque', 'pleramque',
                   'plerorumque', 'plerarumque', 'plerisque', 'plerosque', 'plerasque']

# misc
que_exceptions += ['absque', 'abusque', 'adaeque', 'adusque', 'aeque', 'antique', 'atque', 'circumundique', 'conseque',
                   'cumque', 'cunque', 'denique', 'deque', 'donique', 'hucusque', 'inique', 'inseque', 'itaque',
                   'longinque', 'namque', 'neque', 'oblique', 'peraeque', 'praecoque', 'propinque', 'qualiscumque',
                   'quandocumque', 'quandoque', 'quantuluscumque', 'quantumcumque', 'quantuscumque', 'quinque',
                   'quocumque', 'quomodocumque', 'quomque', 'quotacumque', 'quotcumque', 'quotienscumque',
                   'quotiensque', 'quotusquisque', 'quousque', 'relinque', 'simulatque', 'torque', 'ubicumque',
                   'ubique', 'undecumque', 'undique', 'usque', 'usquequaque', 'utcumque', 'utercumque', 'utique',
                   'utrimque', 'utrique', 'utriusque', 'utrobique', 'utrubique']

ne_exceptions += ['absone', 'acharne', 'acrisione', 'acumine', 'adhucine', 'adsuetudine', 'aeetine', 'aeschynomene',
                  'aesone', 'agamemnone', 'agmine', 'albane', 'alcyone', 'almone', 'alsine', 'amasene', 'ambitione',
                  'amne', 'amoene', 'amymone', 'anadyomene', 'andrachne', 'anemone', 'aniene', 'anne', 'antigone',
                  'aparine', 'apolline', 'aquilone', 'arachne', 'arne', 'arundine', 'ascanione', 'asiane', 'asine',
                  'aspargine', 'babylone', 'barine', 'bellone', 'belone', 'bene', 'benigne', 'bipenne', 'bizone',
                  'bone', 'bubone', 'bulbine', 'cacumine', 'caligine', 'calymne', 'cane', 'carcine', 'cardine',
                  'carmine', 'catacecaumene', 'catone', 'cerne', 'certamine', 'chalbane', 'chamaedaphne',
                  'chamaemyrsine', 'chaone', 'chione', 'christiane', 'clymene', 'cognomine', 'commagene', 'commune',
                  'compone', 'concinne', 'condicione', 'condigne', 'cone', 'confine', 'consone', 'corone', 'crastine',
                  'crepidine', 'crimine', 'crine', 'culmine', 'cupidine', 'cyane', 'cydne', 'cyllene', 'cyrene',
                  'daphne', 'depone', 'desine', 'dicione', 'digne', 'dine', 'dione', 'discrimine', 'diutine', 'dracone',
                  'dulcedine', 'elatine', 'elephantine', 'elleborine', 'epidamne', 'erigone', 'euadne', 'euphrone',
                  'euphrosyne', 'examine', 'faune', 'femine', 'feminine', 'ferrugine', 'fine', 'flamine', 'flumine',
                  'formidine', 'fragmine', 'fraterne', 'fulmine', 'fune', 'germane', 'germine', 'geryone', 'gorgone',
                  'gramine', 'grandine', 'haecine', 'halcyone', 'hammone', 'harundine', 'hedone', 'helene', 'helxine',
                  'hermione', 'heroine', 'hesione', 'hicine', 'hicne', 'hierabotane', 'hippocrene', 'hispane',
                  'hodierne', 'homine', 'hominesne', 'hortamine', 'hucine', 'humane', 'hunccine', 'huncine', 'iasione',
                  'iasone', 'igne', 'imagine', 'immane', 'immune', 'impoene', 'impone', 'importune', 'impune', 'inane',
                  'inconcinne', 'indagine', 'indigne', 'inferne', 'inguine', 'inhumane', 'inpone', 'inpune', 'insane',
                  'insigne', 'inurbane', 'ismene', 'istucine', 'itone', 'iuuene', 'karthagine', 'labiene',
                  'lacedaemone', 'lanugine', 'latine', 'legione', 'lene', 'lenone', 'libidine', 'limine', 'limone',
                  'lumine', 'magne', 'maligne', 'mane', 'margine', 'marone', 'masculine', 'matutine', 'medicamine',
                  'melpomene', 'memnone', 'mesene', 'messene', 'misene', 'mitylene', 'mnemosyne', 'moderamine', 'moene',
                  'mone', 'mortaline', 'mucrone', 'munimine', 'myrmidone', 'mytilene', 'necne', 'neptune', 'nequene',
                  'nerine', 'nocturne', 'nomine', 'nonne', 'nullane', 'numine', 'nuncine', 'nyctimene', 'obscene',
                  'obsidione', 'oenone', 'omine', 'omne', 'oppone', 'opportune', 'ordine', 'origine', 'orphne',
                  'oxymyrsine', 'paene', 'pallene', 'pane', 'paraetacene', 'patalene', 'pectine', 'pelagine', 'pellene',
                  'pene', 'perbene', 'perbenigne', 'peremne', 'perenne', 'perindigne', 'peropportune', 'persephone',
                  'phryne', 'pirene', 'pitane', 'plane', 'pleione', 'plene', 'pone', 'praefiscine', 'prasiane',
                  'priene', 'priuigne', 'procne', 'proditione', 'progne', 'prone', 'propone', 'pulmone', 'pylene',
                  'pyrene', 'pythone', 'ratione', 'regione', 'religione', 'remane', 'retine', 'rhene', 'rhododaphne',
                  'robigine', 'romane', 'roxane', 'rubigine', 'sabine', 'sane', 'sanguine', 'saturne', 'seditione',
                  'segne', 'selene', 'semine', 'semiplene', 'sene', 'sepone', 'serene', 'sermone', 'serrane', 'siccine',
                  'sicine', 'sine', 'sithone', 'solane', 'sollemne', 'somne', 'sophene', 'sperne', 'spiramine',
                  'stamine', 'statione', 'stephane', 'sterne', 'stramine', 'subpone', 'subtegmine', 'subtemine',
                  'sulmone', 'superne', 'supine', 'suppone', 'susiane', 'syene', 'tantane', 'tantine', 'taprobane',
                  'tegmine', 'telamone', 'temne', 'temone', 'tene', 'testudine', 'theophane', 'therone', 'thyone',
                  'tiberine', 'tibicine', 'tiburne', 'tirone', 'tisiphone', 'torone', 'transitione', 'troiane',
                  'turbine', 'turne', 'tyrrhene', 'uane', 'uelamine', 'uertigine', 'uesane', 'uimine', 'uirgine',
                  'umbone', 'unguine', 'uolumine', 'uoragine', 'urbane', 'uulcane', 'zone']

n_exceptions += ['aenean', 'agmen', 'alioquin', 'an', 'attamen', 'cacumen', 'carmen', 'certamen', 'clymenen', 'cognomen', 
                 'crimen', 'culmen', 'dein', 'deucalion', 'discrimen', 'en', 'epitheton', 'erinyn', 'exin', 'flumen', 
                 'forsan', 'forsitan', 'fulmen', 'gramen', 'hymen', 'iason', 'in', 'limen', 'liquamen', 'lumen', 'nomen', 
                 'non', 'numen', 'omen', 'orion', 'paean', 'pan', 'pelion', 'phaethon', 'python', 'quin', 'semen', 'sin',
                 'specimen', 'tamen', 'themin', 'titan']

# Automatic from collatinus n_exceptions
# an exceptions for -n from Collatinus Data
n_exceptions += ['Acarnan', 'Aegipan', 'Alcman', 'Aman', 'Azan', 'Balaan', 'Balanan', 'Cainan', 'Chanaan', 'Chanan',
                 'Euan', 'Euhan', 'Joathan', 'Johanan', 'Laban', 'Leviathan', 'Madian', 'Magedan', 'Naaman',
                 'Nabuzardan', 'Nathan', 'Nisan', 'Pan', 'Pharan', 'Satan', 'Titan', 'dan', 'forsan', 'forsitan',
                 'fortan', 'fortassean', 'man', 'paean', 'tragopan']
# en exceptions for -n from Collatinus Data
n_exceptions += ['Astarthen', 'Bethaven', 'Cebren', 'Cophen', 'Damen', 'Eden', 'Hellen', 'Manahen', 'Philopoemen',
                 'Ruben', 'Siren', 'Troezen', 'Tychen', 'Zosimen', 'abdomen', 'abdumen', 'absegmen', 'acumen',
                 'adaugmen', 'adfamen', 'adflamen', 'adhortamen', 'adjuvamen', 'adligamen', 'adnomen', 'aequamen',
                 'aeramen', 'agmen', 'agnomen', 'albamen', 'albumen', 'almen', 'alumen', 'amen', 'amicimen', 'anguen',
                 'arcumen', 'argyranchen', 'arsen', 'aspectamen', 'aspiramen', 'attagen', 'aucupiamen', 'augmen',
                 'bitumen', 'cacumen', 'caelamen', 'calceamen', 'calciamen', 'cantamen', 'carmen', 'catillamen',
                 'cavamen', 'certamen', 'chalasticamen', 'cicuticen', 'circen', 'citharicen', 'clinamen', 'cluden',
                 'cogitamen', 'cognomen', 'columen', 'conamen', 'consolamen', 'contamen', 'conttamen', 'cornicen',
                 'coronamen', 'coruscamen', 'crassamen', 'creamen', 'crimen', 'cruciamen', 'culmen', 'cunctamen',
                 'curmen', 'curvamen', 'cyclamen', 'decoramen', 'detramen', 'dictamen', 'discrimen', 'docimen',
                 'documen', 'dolamen', 'donamen', 'dulceamen', 'duramen', 'ebriamen', 'effamen', 'eliquamen',
                 'epinomen', 'examen', 'excusamen', 'exhortamen', 'famen', 'farcimen', 'femen', 'ferrumen', 'ferumen',
                 'fidamen', 'fidicen', 'figmen', 'filamen', 'firmamen', 'flamen', 'flemen', 'flumen', 'foramen',
                 'formidamen', 'fragmen', 'frumen', 'frustramen', 'fulcimen', 'fulmen', 'fundamen', 'generamen',
                 'genimen', 'germen', 'gestamen', 'glomeramen', 'gluten', 'gramen', 'gravamen', 'gubernamen', 'gumen',
                 'hortamen', 'hymen', 'hyphen', 'imitamen', 'inchoamen', 'inflamen', 'inguen', 'inspiramen',
                 'intercisimen', 'involumen', 'irritamen', 'juvamen', 'laetamen', 'lassamen', 'lateramen', 'legumen',
                 'lenimen', 'levamen', 'libamen', 'libramen', 'lichen', 'lien', 'ligamen', 'lignamen', 'limen',
                 'linamen', 'linimen', 'linteamen', 'liquamen', 'litamen', 'liticen', 'luctamen', 'lumen', 'lustramen',
                 'lyricen', 'machinamen', 'manamen', 'medicamen', 'meditamen', 'miseramen', 'moderamen', 'modulamen',
                 'molimen', 'momen', 'motamen', 'munimen', 'nemen', 'nodamen', 'nomen', 'notamen', 'novamen',
                 'nullificamen', 'numen', 'nutamen', 'nutrimen', 'objectamen', 'oblectamen', 'oblenimen', 'occamen',
                 'odoramen', 'oleamen', 'omen', 'ornamen', 'oscen', 'osmen', 'ostentamen', 'palpamen', 'peccamen',
                 'pecten', 'pedamen', 'perflamen', 'petimen', 'piamen', 'pilumen', 'pinguamen', 'placamen', 'polimen',
                 'pollen', 'postlimen', 'praecantamen', 'praeexercitamen', 'praefamen', 'praeligamen', 'praenomen',
                 'praesegmen', 'precamen', 'proflamen', 'prolimen', 'pronomen', 'propagmen', 'psalmicen', 'pullamen',
                 'pulpamen', 'purgamen', 'putamen', 'putramen', 'pyren', 'rasamen', 'refluamen', 'regimen', 'relevamen',
                 'religamen', 'remoramen', 'ren', 'renovamen', 'resegmen', 'respiramen', 'revocamen', 'rogamen',
                 'ructamen', 'rumen', 'saepimen', 'sagmen', 'salsamen', 'sanguen', 'sarcimen', 'sarmen', 'saturamen',
                 'sedamen', 'sedimen', 'segmen', 'semen', 'sepimen', 'signamen', 'simulamen', 'sinuamen', 'siticen',
                 'solamen', 'solen', 'solidamen', 'specimen', 'spectamen', 'speculamen', 'spiramen', 'splen',
                 'spurcamen', 'sputamen', 'stabilimen', 'stamen', 'statumen', 'stipamen', 'stramen', 'sublimen',
                 'substamen', 'substramen', 'subtegmen', 'suffimen', 'sufflamen', 'sulcamen', 'sumen', 'superlimen',
                 'susurramen', 'synanchen', 'tamen', 'tegimen', 'tegmen', 'tegumen', 'temptamen', 'tentamen',
                 'terebramen', 'termen', 'testamen', 'tibicen', 'tormen', 'tramen', 'tubicen', 'tumulamen', 'turben',
                 'tutamen', 'ululamen', 'unguen', 'vegetamen', 'velamen', 'velumen', 'verumtamen', 'veruntamen',
                 'vexamen', 'vibramen', 'vimen', 'vitreamen', 'vitulamen', 'vocamen', 'volumen']
# in exceptions for -n from Collatinus Data
n_exceptions += ['Arin', 'Attin', 'Benjamin', 'Cain', 'Corozain', 'Dothain', 'Eleusin', 'Eliacin', 'Engonasin',
                 'Joachin', 'Seraphin', 'Trachin', 'Tubalcain', 'ain', 'alioquin', 'atquin', 'ceteroquin', 'cherubin',
                 'delfin', 'delphin', 'hin', 'nostin', 'quin', 'satin', 'sin']
# on exceptions for -n from Collatinus Data
n_exceptions += ['Aaron', 'Abaddon', 'Abessalon', 'Abiron', 'Absalon', 'Accaron', 'Acheron', 'Achilleon', 'Acmon',
                 'Acroathon', 'Actaeon', 'Adipson', 'Adon', 'Aeantion', 'Aegaeon', 'Aegilion', 'Aegion', 'Aegon',
                 'Aemon', 'Aeson', 'Aethion', 'Aethon', 'Aetion', 'Agamemnon', 'Aglaophon', 'Ajalon', 'Alabastron',
                 'Alabon', 'Albion', 'Alcimedon', 'Alcmaeon', 'Alcon', 'Alcumaeon', 'Alcyon', 'Alebion', 'Alemon',
                 'Alexion', 'Aliacmon', 'Alison', 'Almon', 'Alymon', 'Amazon', 'Amithaon', 'Amithhaon', 'Ammon',
                 'Amnon', 'Amorion', 'Amphictyon', 'Amphimedon', 'Amphion', 'Amphitryon', 'Amydon', 'Amythaon',
                 'Amyzon', 'Anacreon', 'Anaon', 'Andraemon', 'Andremon', 'Androgeon', 'Androtion', 'Anticyricon',
                 'Antiphon', 'Antron', 'Aon', 'Apion', 'Apollyon', 'Apteron', 'Arethon', 'Arion', 'Aristocreon',
                 'Aristogiton', 'Ariston', 'Aristophon', 'Artacaeon', 'Arthedon', 'Asarhaddon', 'Asidon', 'Aspledon',
                 'Astragon', 'Astron', 'Aulion', 'Auson', 'Automedon', 'Auximon', 'Avenion', 'Axion', 'Babylon',
                 'Baeton', 'Barcinon', 'Batton', 'Bellerophon', 'Bethoron', 'Bion', 'Bithynion', 'Biton', 'Blascon',
                 'Blepharon', 'Borion', 'Branchiadon', 'Brauron', 'Bronton', 'Bruchion', 'Bryalion', 'Bryazon',
                 'Bryllion', 'Bubon', 'Bucion', 'Byzantion', 'Cacomnemon', 'Calcedon', 'Calchedon', 'Calliphon',
                 'Callon', 'Calon', 'Calydon', 'Carchedon', 'Carnion', 'Caulon', 'Cedron', 'Celadon', 'Cerberion',
                 'Cercyon', 'Ceron', 'Chaeremon', 'Chalaeon', 'Chalcedon', 'Chaon', 'Chardaleon', 'Charon', 'Cheraemon',
                 'Chersiphron', 'Chilon', 'Chimerion', 'Chion', 'Chiron', 'Choerogylion', 'Cimon', 'Cisamon',
                 'Cithaeron', 'Citheron', 'Claeon', 'Cleomedon', 'Cleon', 'Cleophon', 'Codrion', 'Colophon', 'Condylon',
                 'Conon', 'Corragon', 'Corrhagon', 'Corydon', 'Cothon', 'Cotton', 'Cotyaion', 'Crannon', 'Cranon',
                 'Cremmyon', 'Creon', 'Crialoon', 'Criumetopon', 'Cromyon', 'Ctesiphon', 'Cydon', 'Daedalion', 'Dagon',
                 'Daiphron', 'Dalion', 'Damasichthon', 'Damon', 'Dareion', 'Deltoton', 'Demetrion', 'Demoleon',
                 'Demophon', 'Demophoon', 'Deucalion', 'Dexon', 'Diaron', 'Didumaon', 'Didymaon', 'Didymeon',
                 'Dindymon', 'Dinon', 'Diomedon', 'Dion', 'Diptychon', 'Dipylon', 'Dolichaon', 'Dolon', 'Dorion',
                 'Doriscon', 'Dortigon', 'Dotion', 'Dracanon', 'Edon', 'Eetion', 'Eion', 'Electruon', 'Electryon',
                 'Eluron', 'Emathion', 'Endymion', 'Enguion', 'Engyon', 'Eon', 'Ephron', 'Erineon', 'Erisichthon',
                 'Erotopaegnion', 'Erysichthon', 'Esdrelon', 'Euagon', 'Euctemon', 'Eudaemon', 'Eudon', 'Euphorion',
                 'Euphron', 'Euprosopon', 'Eurymedon', 'Eurytion', 'Gabaon', 'Gargaron', 'Gedeon', 'Gehon', 'Gelon',
                 'Genethliacon', 'Geon', 'Georgicon', 'Gerrhon', 'Gerson', 'Geryon', 'Glycon', 'Gorgon', 'Gyrton',
                 'Habron', 'Haemon', 'Hagnon', 'Haliacmon', 'Hammon', 'Hannon', 'Harmedon', 'Harpocration', 'Hebon',
                 'Hebron', 'Helicaon', 'Helicon', 'Hephaestion', 'Hermacreon', 'Hesebon', 'Hexaemeron', 'Hexapylon',
                 'Hicetaon', 'Hieron', 'Hilarion', 'Hippocoon', 'Hippomedon', 'Hippon', 'Holmon', 'Holon', 'Hygienon',
                 'Hypaton', 'Hyperion', 'Iasion', 'Icadion', 'Icosion', 'Idmon', 'Ilion', 'Imaon', 'Iseon', 'Ixion',
                 'Jason', 'Lacedaemon', 'Lacon', 'Lacydon', 'Ladon', 'Laestrygon', 'Lagon', 'Lampon', 'Laocoon',
                 'Laomedon', 'Laucoon', 'Lauron', 'Lecton', 'Leocorion', 'Leon', 'Lepreon', 'Leprion', 'Lestrygon',
                 'Lethon', 'Lilybaeon', 'Lycaon', 'Lycon', 'Lycophon', 'Lycophron', 'Lydion', 'Lyson', 'Macedon',
                 'Machaon', 'Maeon', 'Maeson', 'Mageddon', 'Magon', 'Marathon', 'Marcion', 'Mathon', 'Medeon', 'Medon',
                 'Memnon', 'Menephron', 'Menon', 'Mentonomon', 'Metagon', 'Methion', 'Metion', 'Meton', 'Micon',
                 'Miction', 'Micton', 'Milanion', 'Milon', 'Mirsion', 'Mision', 'Mnason', 'Mnemon', 'Mnesigiton',
                 'Molon', 'Mulon', 'Mycon', 'Mydon', 'Mygdon', 'Myrmidon', 'Naasson', 'Nahasson', 'Naron', 'Narycion',
                 'Nasamon', 'Nebon', 'Neon', 'Nicephorion', 'Nicon', 'Noemon', 'Nomion', 'Oenopion', 'Olizon', 'Ophion',
                 'Orchomenon', 'Orion', 'Oromedon', 'Ortiagon', 'Paeon', 'Palaemon', 'Pallon', 'Pandion', 'Panopion',
                 'Pantaleon', 'Pantheon', 'Paphlagon', 'Paridon', 'Parion', 'Parmenion', 'Parthaon', 'Parthenion',
                 'Parthenon', 'Passaron', 'Patron', 'Paulon', 'Pedon', 'Pelagon', 'Pelion', 'Pellaon', 'Pergamon',
                 'Peteon', 'Phaedon', 'Phaenon', 'Phaethon', 'Phalerion', 'Phaleron', 'Phaon', 'Pharaon', 'Pharathon',
                 'Phidon', 'Philammon', 'Philemon', 'Philistion', 'Philon', 'Phison', 'Phlegethon', 'Phlegon',
                 'Phocion', 'Phradmon', 'Phryxelon', 'Physcon', 'Pion', 'Pitholeon', 'Pleuron', 'Pluton', 'Polemon',
                 'Polydaemon', 'Polygiton', 'Polypemon', 'Polyperchon', 'Porphyrion', 'Prion', 'Procyon', 'Protagorion',
                 'Protheon', 'Pseudostomon', 'Pteleon', 'Pygmalion', 'Pyracmon', 'Pyriphlegethon', 'Python', 'Region',
                 'Rhinthon', 'Rhinton', 'Rhion', 'Rhizon', 'Rhoetion', 'Rhytion', 'Rubicon', 'Rumon', 'Salomon',
                 'Samson', 'Sarion', 'Sarpedon', 'Sason', 'Satiricon', 'Satyricon', 'Sciron', 'Scyron', 'Sebeon',
                 'Sicyon', 'Sidon', 'Sigalion', 'Silaniion', 'Silanion', 'Simeon', 'Simon', 'Sinon', 'Sisichthon',
                 'Sisichton', 'Sithon', 'Socration', 'Solomon', 'Solon', 'Sophron', 'Spiridion', 'Stilbon', 'Stilpon',
                 'Stimichon', 'Stimon', 'Stratioton', 'Straton', 'Strenion', 'Strongylion', 'Strymon', 'Sunion',
                 'Taenaron', 'Tarracon', 'Tauron', 'Taygeton', 'Technopaegnion', 'Tecmon', 'Telamon', 'Telon',
                 'Tenthredon', 'Teredon', 'Teuthredon', 'Thabusion', 'Thelbon', 'Themison', 'Theon', 'Thermodon',
                 'Theromedon', 'Theron', 'Thesbon', 'Thronion', 'Thryon', 'Thylon', 'Timoleon', 'Timon', 'Topazion',
                 'Topazon', 'Trallicon', 'Trevidon', 'Triton', 'Tritonon', 'Tryphon', 'Tylon', 'Typhon', 'Ucalegon',
                 'Vibon', 'Vulchalion', 'Xenophon', 'Zabulon', 'Zenon', 'Zephyrion', 'Zon', 'Zopyrion', 'acanthion',
                 'aconiton', 'acopon', 'acoron', 'acratophoron', 'acrochordon', 'acrocolion', 'acron', 'adamenon',
                 'adipsatheon', 'aedon', 'aegolethron', 'aeon', 'aesalon', 'aeschrion', 'agaricon', 'agathodaemon',
                 'ageraton', 'agon', 'agriophyllon', 'aizoon', 'alazon', 'alexipharmacon', 'allasson', 'alphiton',
                 'alypon', 'alyseidion', 'alysidion', 'alysson', 'alyssson', 'amaracion', 'amerimnon', 'amethystizon',
                 'ammonitron', 'amomon', 'ampeloprason', 'amphibion', 'anabibazon', 'anacoluthon', 'anagon',
                 'anarrhinon', 'ancistron', 'ancon', 'ancyloblepharon', 'andron', 'androsaemon', 'annon', 'anodynon',
                 'anteridion', 'anthedon', 'anthereon', 'anthyllion', 'antibiblion', 'antipharmacon', 'antirrhinon',
                 'antiscorodon', 'antistrephon', 'antitheton', 'antizeugmenon', 'aphron', 'apiacon', 'apocynon',
                 'apographon', 'apologeticon', 'apoproegmenon', 'aposcopeuon', 'arcebion', 'archebion', 'archidiacon',
                 'archigeron', 'architecton', 'archon', 'arcion', 'arcoleon', 'arction', 'argemon', 'argemonion',
                 'argennon', 'aristereon', 'armon', 'arnion', 'arnoglosson', 'aron', 'arrhenogonon', 'arsenogonon',
                 'artemedion', 'artemon', 'arusion', 'asaron', 'asbeston', 'ascalon', 'asceterion', 'asclepion',
                 'ascyron', 'asphaltion', 'aspideion', 'asplenon', 'asterion', 'astrabicon', 'astrion', 'asyndeton',
                 'asyntrophon', 'athenogeron', 'athlon', 'atlantion', 'aulon', 'autochthon', 'autochton', 'automaton',
                 'axon', 'azymon', 'barbiton', 'barypicron', 'barython', 'basilicon', 'batrachion', 'bechion', 'belion',
                 'bisdiapason', 'bison', 'blachnon', 'blechhnon', 'blechon', 'blechron', 'bolbiton', 'botryon',
                 'boustrophedon', 'brochon', 'bryon', 'bubalion', 'bubonion', 'buleuterion', 'bunion', 'bupleuron',
                 'burrhinon', 'buselinon', 'bustrophedon', 'busycon', 'butyron', 'caballion', 'cacemphaton',
                 'cacodaemon', 'cacophaton', 'cacosyntheton', 'cacozelon', 'caesapon', 'calligonon', 'callion',
                 'callipetalon', 'callitrichon', 'calopodion', 'camelopodion', 'cammaron', 'canon', 'carcinethron',
                 'carcinothron', 'carpophyllon', 'caryllon', 'caryon', 'caryophyllon', 'caryphyllon', 'cassiteron',
                 'catalepton', 'causon', 'centaurion', 'cephalaeon', 'ceration', 'cerion', 'cestron', 'chaerephyllon',
                 'chalazion', 'chalcanthon', 'chalcanton', 'chamaedracon', 'chamaeleon', 'chamaemelon', 'chamaezelon',
                 'charisticon', 'charistion', 'chariton', 'charitonblepharon', 'chelidon', 'chelyon', 'chenoboscion',
                 'chiliophyllon', 'chirographon', 'chironomon', 'chlorion', 'chondrillon', 'chreston', 'chrysallion',
                 'chrysanthemon', 'cichorion', 'cinnamon', 'circaeon', 'cirsion', 'cissaron', 'cission', 'cleonicion',
                 'cleopiceton', 'clidion', 'clinopodion', 'cneoron', 'cnestron', 'coacon', 'cobion', 'coenon',
                 'colobathron', 'colon', 'comaron', 'contomonobolon', 'coriandron', 'corion', 'corisson', 'corymbion',
                 'cotyledon', 'crataegon', 'crataeogonon', 'crinon', 'crocodileon', 'crocodilion', 'croton',
                 'crysallion', 'crystallion', 'cuferion', 'cybion', 'cyceon', 'cyclaminon', 'cylon', 'cymation',
                 'cynocardamon', 'cynocephalion', 'cynodon', 'cynomazon', 'cynomorion', 'cynorrhodon', 'cynorrodon',
                 'cynozolon', 'cyperon', 'daemon', 'daimon', 'damasonion', 'daphnon', 'daucion', 'daucon', 'deleterion',
                 'diaartymaton', 'diabotanon', 'diacerason', 'diacheton', 'diachyton', 'diacochlecon', 'diacodion',
                 'diacon', 'diaglaucion', 'diagrydion', 'dialibanon', 'dialion', 'dialthaeon', 'dialyton',
                 'diameliloton', 'diameliton', 'diamoron', 'diapanton', 'diapason', 'diaprasion', 'diascorodon',
                 'diasmyrnon', 'diaspermaton', 'diatessaron', 'diatoichon', 'diatonicon', 'diazeugmenon', 'dichalcon',
                 'dichomenion', 'diezeugmenon', 'digammon', 'diospyron', 'dircion', 'disdiapason', 'distichon',
                 'dodecatemorion', 'dodecatheon', 'dorcadion', 'dorcidion', 'doron', 'dorycnion', 'dorypetron',
                 'dracon', 'dracontion', 'dryophonon', 'dysprophoron', 'ebenotrichon', 'echeon', 'echion', 'ectomon',
                 'egersimon', 'elaeon', 'elaphoboscon', 'elegeion', 'elegeon', 'elegidarion', 'elegidion', 'elegion',
                 'eleison', 'embadon', 'emmoton', 'emplecton', 'enchiridion', 'enemion', 'engonaton', 'enhaemon',
                 'enneaphyllon', 'epagon', 'ephedron', 'ephemeron', 'epicedion', 'epigrammation', 'epimedion',
                 'epinicion', 'epipetron', 'epiradion', 'epitaphion', 'epithalamion', 'epitheton', 'epithymon',
                 'epitonion', 'epomphalion', 'eranthemon', 'erigeron', 'erioxylon', 'eryngion', 'erysisceptron',
                 'erythraicon', 'erythranon', 'eschatocollion', 'etymon', 'eubolion', 'eucharisticon', 'eugalacton',
                 'eunuchion', 'euphrosynon', 'eupteron', 'eutheriston', 'euzomon', 'exacon', 'exonychon', 'exormiston',
                 'galeobdolon', 'galion', 'gamelion', 'ganglion', 'garyophyllon', 'geranion', 'gethyon', 'gingidion',
                 'glaucion', 'glechon', 'glinon', 'glycyrrhizon', 'gnaphalion', 'gnomon', 'gossipion', 'gossypion',
                 'hadrobolon', 'haematicon', 'halcyon', 'halicacabon', 'halimon', 'halipleumon', 'halmyridion', 'halon',
                 'hecatombion', 'hegemon', 'hegemonicon', 'heleoselinon', 'heliochryson', 'helioscopion',
                 'helioselinon', 'heliotropion', 'hemerobion', 'hemionion', 'hemisphaerion', 'hemitonion', 'hepatizon',
                 'heptaphyllon', 'heroion', 'heterocliton', 'hexaclinon', 'hexaphoron', 'hieracion', 'hieromnemon',
                 'hippolapathon', 'hippomarathon', 'hippophaeston', 'hippopheon', 'hippophlomon', 'hipposelinon',
                 'histon', 'hodoeporicon', 'holocyron', 'holosteon', 'homoeopropheron', 'homoeoprophoron',
                 'homoeoptoton', 'homoeoteleuton', 'horaeon', 'horizon', 'hormiscion', 'hyacinthizon', 'hydrogeron',
                 'hydrolapathon', 'hypecoon', 'hyperbaton', 'hypericon', 'hypocauston', 'hypogeson', 'hypoglottion',
                 'hypomochlion', 'hypopodion', 'ichneumon', 'icon', 'idolon', 'ion', 'iphyon', 'ischaemon',
                 'isocinnamon', 'isopleuron', 'isopyron', 'langon', 'larbason', 'ledon', 'leontocaron', 'leontopetalon',
                 'leontopodion', 'leptophyllon', 'leucanthemon', 'leuceoron', 'leucoion', 'leucon', 'leucophoron',
                 'leucrion', 'leuson', 'lexidion', 'libadion', 'lignyzon', 'limodoron', 'limonion', 'linostrophon',
                 'lirinon', 'lirion', 'lithizon', 'lithognomon', 'lithospermon', 'logarion', 'longanon', 'lucmon',
                 'lychnion', 'lyncurion', 'lyron', 'lytron', 'machaerophyllon', 'madon', 'maldacon', 'malobathron',
                 'mammon', 'manicon', 'manon', 'margarition', 'maron', 'maronion', 'mastichelaeon', 'mazonomon',
                 'mecon', 'meconion', 'medion', 'melamphyllon', 'melampodion', 'melanspermon', 'melanthion',
                 'melaspermon', 'melissophyllon', 'meliton', 'melocarpon', 'melophyllon', 'melothron', 'memecylon',
                 'menion', 'menogenion', 'mesanculon', 'metopion', 'metopon', 'metron', 'mileon', 'miuron',
                 'mnemosynon', 'monazon', 'monemeron', 'monobolon', 'monochordon', 'monosyllabon', 'morion',
                 'mormorion', 'myacanthon', 'myophonon', 'myosoton', 'myriophyllon', 'myrmecion', 'myron',
                 'myrtopetalon', 'mystron', 'myxarion', 'myxon', 'nardostachyon', 'naulon', 'nechon', 'necnon',
                 'nephelion', 'nerion', 'nession', 'neurospaston', 'nicephyllon', 'nitrion', 'non', 'notion',
                 'nyctegreton', 'nymphon', 'nysion', 'octaphhoron', 'octaphoron', 'octophoron', 'ololygon',
                 'onocardion', 'onochelon', 'onochilon', 'onopordon', 'onopradon', 'ophidion', 'ophiostaphylon',
                 'opion', 'opition', 'opocarpathon', 'orchion', 'oreon', 'oreoselinon', 'orestion', 'origanon',
                 'ornithon', 'orobethron', 'otion', 'oxybaphon', 'oxylapathon', 'oxytonon', 'oxytriphyllon',
                 'panathenaicon', 'pancration', 'panion', 'paradoxon', 'paranarrhinon', 'paranatellon', 'parelion',
                 'pareoron', 'parergon', 'parhelion', 'parhomoeon', 'parison', 'paromoeon', 'paronymon', 'parthenicon',
                 'pausilypon', 'pedalion', 'peganon', 'pelecinon', 'pellion', 'pentadactylon', 'pentagonon',
                 'pentaphyllon', 'pentaspaston', 'pentatomon', 'pentorobon', 'perichristarion', 'perinaeon', 'perineon',
                 'periosteon', 'peripodion', 'perispomenon', 'perisson', 'peristereon', 'petroselinon', 'peucedanon',
                 'phaenion', 'phaenomenon', 'phalaecion', 'phalangion', 'pharicon', 'pharnaceon', 'pharnacion',
                 'phasganion', 'phellandrion', 'pheuxaspidion', 'philanthropion', 'phlegmon', 'phorimon', 'phrenion',
                 'phryganion', 'phrynion', 'phyllon', 'phynon', 'physiognomon', 'pisselaeon', 'pitydion', 'pityon',
                 'platanon', 'platon', 'platyphyllon', 'plethron', 'polion', 'polyandrion', 'polyarchion', 'polyarcyon',
                 'polycnemon', 'polygonaton', 'polyneuron', 'polypodion', 'polyptoton', 'polyrrhizon', 'polyrrizon',
                 'polyspaston', 'polysyntheton', 'polytrichon', 'poppyzon', 'potamogeton', 'potamogiton', 'poterion',
                 'pramnion', 'prapedilon', 'prapedion', 'prasion', 'prason', 'proarchon', 'probation', 'procoeton',
                 'procomion', 'proegmenon', 'prognosticon', 'promnion', 'pronaon', 'propempticon', 'propnigeon',
                 'propylaeon', 'propylon', 'prosopon', 'protagion', 'protrepticon', 'protropon', 'pseudobunion',
                 'pseudoselinon', 'psychotrophon', 'psyllion', 'pteron', 'pycnocomon', 'pyrethron', 'pythion',
                 'pythonion', 'quilon', 'rhagion', 'rhapeion', 'rhaphanidion', 'rhigolethron', 'rhinion',
                 'rhododendron', 'rhopalon', 'rhuselinon', 'rhythmizomenon', 'saccharon', 'sacon', 'sagapenon',
                 'sagenon', 'sanchromaton', 'sangenon', 'saphon', 'sarcion', 'satyrion', 'saurion', 'scazon',
                 'scimpodion', 'sciothericon', 'scolecion', 'scolibrochon', 'scolopendrion', 'scordilon', 'scordion',
                 'scorodon', 'scorpioctonon', 'scorpion', 'scorpiuron', 'scybalon', 'selenion', 'selenogonon',
                 'selinon', 'selinophyllon', 'semimetopion', 'semnion', 'sepioticon', 'serapion', 'setanion',
                 'sicelicon', 'siderion', 'sindon', 'sion', 'siphon', 'sisonagrion', 'sisyrinchion', 'sisyringion',
                 'smilion', 'smyrnion', 'sophismation', 'sparganion', 'sparton', 'spathalion', 'sphaerion', 'sphingion',
                 'sphondylion', 'splenion', 'spondiazon', 'spondylion', 'stacton', 'staphylodendron', 'stasimon',
                 'statioron', 'stergethron', 'stomation', 'stratopedon', 'struthion', 'subdiacon', 'sycaminon',
                 'sycophyllon', 'symphyton', 'symposion', 'syndon', 'synemmenon', 'syngenicon', 'synoneton',
                 'synonymon', 'syntonon', 'syntononon', 'syreon', 'syron', 'taurophthalmon', 'technyphion', 'telephion',
                 'tenon', 'teramon', 'tetartemorion', 'tethalassomenon', 'tetrachordon', 'tetracolon', 'tetragnathion',
                 'tetraptoton', 'tetrastichon', 'tetrastylon', 'teucrion', 'teuthrion', 'theatridion', 'thelycon',
                 'thelygonon', 'thelyphonon', 'theobrotion', 'theodotion', 'theoremation', 'theribethron', 'therion',
                 'theriophonon', 'thermospodion', 'thesion', 'thorybethron', 'thorybetron', 'thrauston', 'thrion',
                 'thymion', 'thyon', 'tiphyon', 'tithymalon', 'tordylion', 'tordylon', 'toxicon', 'tragion',
                 'tragopogon', 'trapezophoron', 'tribon', 'trichalcon', 'tricolon', 'trigon', 'trihemitonion',
                 'tripolion', 'tryginon', 'trygon', 'typhonion', 'ulophonon', 'ulophyton', 'urion', 'xenon',
                 'xeromyron', 'xeron', 'xiphion', 'xyliglycon', 'xylion', 'xylon', 'xylophyton', 'zacon',
                 'zoophthalmon', 'zopyron', 'zopyrontion', 'zugon']

# English words; this list added to better handle English header, navigation, etc. in plaintext files of the Latin Library corpus.
n_exceptions += ['alcuin', 'caen', 'christian', 'chronicon', 'châtillon', 'claudian', 'john', 'justin', 'latin',
                 'lucan', 'martin', 'novatian', 'quintilian', 'roman', 'tertullian']

ue_exceptions += ['agaue', 'ambigue', 'assidue', 'aue', 'boue', 'breue', 'calue', 'caue', 'ciue', 'congrue', 'contigue',
                  'continue', 'curue', 'exigue', 'exue', 'fatue', 'faue', 'fue', 'furtiue', 'gradiue', 'graue',
                  'ignaue', 'incongrue', 'ingenue', 'innocue', 'ioue', 'lasciue', 'leue', 'moue', 'mutue', 'naue',
                  'neue', 'niue', 'perexigue', 'perspicue', 'pingue', 'praecipue', 'praegraue', 'prospicue', 'proterue',
                  'remoue', 'resolue', 'saeue', 'salue', 'siue', 'solue', 'strenue', 'sue', 'summoue', 'superflue',
                  'supplicue', 'tenue', 'uiue', 'ungue', 'uoue']

ve_exceptions += ['agave', 'ave', 'bove', 'breve', 'calve', 'cave', 'cive', 'curve', 'fave', 'furtive', 'gradive',
                  'grave', 'ignave', 'iove', 'lascive', 'leve', 'move', 'nave', 'neve', 'nive', 'praegrave',
                  'promiscue', 'prospicve', 'proterve', 'remove', 'resolve', 'saeve', 'salve', 'sive', 'solve',
                  'summove', 'vive', 'vove']

st_exceptions += ['abest', 'adest', 'ast', 'deest', 'est', 'inest', 'interest', 'post', 'potest', 'prodest', 'subest',
                  'superest']

latin_exceptions = list(set(que_exceptions
                            + ne_exceptions
                            + n_exceptions
                            + ue_exceptions
                            + ve_exceptions
                            + st_exceptions
                            ))
