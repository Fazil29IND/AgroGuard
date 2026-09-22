"""
🌾 AgroGuard — Unified Agricultural Knowledge Base & Advisory Engine
Derived from TNAU (Tamil Nadu Agricultural University) Crop Protection Compendium (CPCPP)
and Standard Phytosanitary Diagnostics.

Standardized coverage for all 48 Unified Joint Crop-Pathology Classes across 9 Botanical Species:
Apple, Black_gram, Corn, Grape, Orange, Paddy, Pepper, Potato, Tomato.
"""

# ----------------------------------------------------------------------
# 1. BOTANICAL SPECIES & TAMIL NADU AGRO-CLIMATIC ZONAL METADATA
# ----------------------------------------------------------------------
CROP_INFO = {   'Apple': {   'botanical': 'Malus domestica',
                 'ta': 'ஆப்பிள் (Apple)',
                 'districts': 'Nilgiris (Coonoor, Ooty), Dindigul (Kodaikanal)'},
    'Black_gram': {   'botanical': 'Vigna mungo',
                      'ta': 'உளுந்து (Black gram)',
                      'districts': 'Thanjavur, Tiruvarur, Nagapattinam, Cuddalore, Thoothukudi'},
    'Corn': {   'botanical': 'Zea mays',
                'ta': 'மக்காச்சோளம் (Corn / Maize)',
                'districts': 'Perambalur, Ariyalur, Dindigul, Virudhunagar, Tiruppur'},
    'Grape': {   'botanical': 'Vitis vinifera',
                 'ta': 'திராட்சை (Grape)',
                 'districts': 'Theni (Cumbum Valley), Dindigul (Kodaikanal foothills)'},
    'Orange': {   'botanical': 'Citrus sinensis / Citrus aurantifolia',
                  'ta': 'ஆரஞ்சு / சிட்ரஸ் (Orange / Citrus)',
                  'districts': 'Dindigul (Sirumalai), Perambalur, Tirunelveli, Tenkasi, Nilgiris'},
    'Paddy': {   'botanical': 'Oryza sativa',
                 'ta': 'நெல் (Paddy / Rice)',
                 'districts': 'Thanjavur, Tiruvarur, Nagapattinam, Cauvery Delta, Tirunelveli'},
    'Pepper': {   'botanical': 'Capsicum annuum',
                  'ta': 'குடைமிளகாய் / மிளகாய் (Bell Pepper / Chilli)',
                  'districts': 'Ramanathapuram, Virudhunagar, Sivaganga, Thoothukudi'},
    'Potato': {   'botanical': 'Solanum tuberosum',
                  'ta': 'உருளைக்கிழங்கு (Potato)',
                  'districts': 'Nilgiris (Ooty), Dindigul (Kodaikanal)'},
    'Tomato': {   'botanical': 'Solanum lycopersicum',
                  'ta': 'தக்காளி (Tomato)',
                  'districts': 'Krishnagiri, Dharmapuri, Dindigul, Salem'},
    'Rice': {   'botanical': 'Oryza sativa',
                'ta': 'நெல் (Paddy)',
                'districts': 'Thanjavur, Tiruvarur, Nagapattinam, Cauvery Delta'},
    'Maize': {   'botanical': 'Zea mays',
                 'ta': 'மக்காச்சோளம் (Maize)',
                 'districts': 'Perambalur, Ariyalur, Dindigul, Virudhunagar'},
    'Citrus': {   'botanical': 'Citrus aurantifolia',
                  'ta': 'எலுமிச்சை / சிட்ரஸ்',
                  'districts': 'Dindigul, Perambalur, Tirunelveli, Tenkasi'},
    'Chilli': {   'botanical': 'Capsicum annuum',
                  'ta': 'மிளகாய் (Chilli)',
                  'districts': 'Ramanathapuram, Virudhunagar, Sivaganga'},
    'Grapes': {'botanical': 'Vitis vinifera', 'ta': 'திராட்சை', 'districts': 'Theni (Cumbum Valley), Dindigul'}}

# ----------------------------------------------------------------------
# 2. UNIFIED 48-CLASS PHYTOSANITARY & ADVISORY DATABASE
# ----------------------------------------------------------------------
DISEASE_DB = {   'Apple___Black_rot': {   'crop_en': 'Apple',
                             'crop_ta': 'ஆப்பிள்',
                             'disease_en': 'Apple Black Rot (Frogeye Leaf Spot)',
                             'disease_ta': 'ஆப்பிள் கருப்பு அழுகல் நோய் / தவளைக்கண் இலைப்புள்ளி',
                             'is_healthy': False,
                             'pathogen': 'Botryosphaeria obtusa (Fungus 🍄)',
                             'field_sign': 'Circular purple-bordered frog-eye foliar spots; firm dark sunken fruit rot '
                                           'with concentric rings.',
                             'symptoms': [   'Small circular purple specks expanding into brown spots with distinct '
                                             'purple margins resembling a frog eye.',
                                             'Infected fruit develops a firm, brown rot expanding into black '
                                             'concentric rings with tiny black pycnidia.',
                                             'Twig and limb cankers causing shoot dieback and bark cracking in orchard '
                                             'canopies.'],
                             'chemical_control': 'TNAU CPCPP: Spray Mancozeb 75 WP @ 2g/L or Captan 50 WP @ 2.5g/L or '
                                                 'Thiophanate-methyl 70 WP @ 1g/L at petal fall and cover sprays.',
                             'organic_control': 'Apply 1% Bordeaux mixture before bud break; foliar application of '
                                                'Bacillus subtilis @ 5g/L; spray neem oil 3%.',
                             'prevention': 'Prune dead wood, mummified fruits, and limb cankers during winter '
                                           'dormancy; burn all orchard prunings.'},
    'Apple___Cedar_apple_rust': {   'crop_en': 'Apple',
                                    'crop_ta': 'ஆப்பிள்',
                                    'disease_en': 'Cedar Apple Rust',
                                    'disease_ta': 'சிடார் ஆப்பிள் துரு நோய்',
                                    'is_healthy': False,
                                    'pathogen': 'Gymnosporangium juniperi-virginianae (Rust Fungus 🍄)',
                                    'field_sign': 'Bright yellow-orange circular lesions on upper leaf surfaces; '
                                                  'tube-like aecia cups on leaf undersides.',
                                    'symptoms': [   'Pale yellow spots appear on upper leaf surface in spring, '
                                                    'enlarging into bright orange-yellow lesions with red borders.',
                                                    'Small black fungal pycnia exude sticky orange droplets in lesion '
                                                    'centers.',
                                                    'Underside of leaves develops raised cylindrical aecial spore cups '
                                                    'shedding powdery brown rust spores.',
                                                    'Premature defoliation and dwarfed, misshapen fruit in susceptible '
                                                    'cultivars.'],
                                    'chemical_control': 'TNAU CPCPP: Spray Myclobutanil 10 WP @ 0.5g/L or '
                                                        'Difenoconazole 25 EC @ 0.5 mL/L or Mancozeb 75 WP @ 2g/L from '
                                                        'pink bud through petal fall.',
                                    'organic_control': 'Foliar spray of Wettable Sulphur @ 3g/L or copper hydroxide '
                                                       '(2g/L); apply Trichoderma viride @ 5g/L.',
                                    'prevention': 'Remove and eradicate alternate host Eastern Red Cedar / Juniper '
                                                  'trees within 1–2 km radius; plant rust-resistant cultivars.'},
    'Apple___Healthy': {   'crop_en': 'Apple',
                           'crop_ta': 'ஆப்பிள்',
                           'disease_en': 'Healthy Crop Foliage',
                           'disease_ta': 'ஆரோக்கியமான பயிர்',
                           'is_healthy': True,
                           'pathogen': 'No pathogen detected (ஆரோக்கியமானது)',
                           'field_sign': 'Vibrant dark green serrated leaves on vigorous spur growth; no foliar '
                                         'lesions, rust spots, or powdery mildew.',
                           'symptoms': [   'Clean, uniform photosynthetic foliage with balanced terminal growth and '
                                           'fruit spur formation.',
                                           'Absence of fungal scab velvety lesions, rust aecia, or fire blight '
                                           'wilting.'],
                           'chemical_control': 'No chemical intervention required.',
                           'organic_control': 'Soil application of well-composted farmyard manure with Trichoderma '
                                              'viride; foliar spray of Panchagavya 3%.',
                           'prevention': 'Maintain optimal canopy training/pruning, ensure adequate sunlight '
                                         'penetration, and monitor soil moisture.'},
    'Apple___Scab': {   'crop_en': 'Apple',
                        'crop_ta': 'ஆப்பிள்',
                        'disease_en': 'Apple Scab',
                        'disease_ta': 'ஆப்பிள் செதில் நோய் / இலைக்கரும்புள்ளி',
                        'is_healthy': False,
                        'pathogen': 'Venturia inaequalis (Fungus 🍄)',
                        'field_sign': 'Velvety olive-green to dull brown circular spots on leaves; dark corky scabby '
                                      'lesions on developing apples.',
                        'symptoms': [   'Olive-green velvety circular spots with feathery margins on both leaf '
                                        'surfaces.',
                                        'Lesions turn dark brown to black, becoming raised, rigid, and corky as leaf '
                                        'tissue thickens.',
                                        'Severely infected leaves become distorted, turn yellow, and drop prematurely.',
                                        'Fruits develop severe scabby cracks, deformities, and stunted size reducing '
                                        'marketable yield.'],
                        'chemical_control': 'TNAU CPCPP: Spray Mancozeb 75 WP @ 2.5g/L or Captan 50 WP @ 2.5g/L at '
                                            'green tip; spray Difenoconazole 25 EC @ 0.5 mL/L or Trifloxystrobin 50 WG '
                                            '@ 0.2g/L at petal fall.',
                        'organic_control': 'Spray 1% Bordeaux mixture at silver tip stage; apply foliar Pseudomonas '
                                           'fluorescens @ 10g/L or 0.5% potassium bicarbonate.',
                        'prevention': 'Shred and compost fallen leaves or spray 5% urea solution post-harvest to '
                                      'accelerate leaf decomposition and eliminate overwintering pseudothecia.'},
    'Black_gram___Anthracnose': {   'crop_en': 'Black gram',
                                    'crop_ta': 'உளுந்து',
                                    'disease_en': 'Anthracnose',
                                    'disease_ta': 'ஆந்த்ராக்னோஸ் / கருகல் நோய்',
                                    'is_healthy': False,
                                    'pathogen': 'Colletotrichum lindemuthianum (Fungus 🍄)',
                                    'field_sign': 'Sunken dark brown to black circular cankers with raised borders on '
                                                  'leaves, petioles, and pods.',
                                    'symptoms': [   'Sunken circular necrotic lesions with dark borders on leaves, '
                                                    'stems, and pods.',
                                                    'Pinkish gelatinous spore masses appear in center of lesions under '
                                                    'humid field conditions.',
                                                    'Premature leaf shedding and severe pod withering leading to '
                                                    'stained, unmarketable seeds.'],
                                    'chemical_control': 'TNAU CPCPP: Spray Carbendazim 50 WP @ 1g/L or Difenoconazole '
                                                        '25 EC @ 0.5 mL/L or Mancozeb 75 WP @ 2g/L.',
                                    'organic_control': 'Seed treatment with Trichoderma viride @ 4g/kg seed + foliar '
                                                       'spray of vermiwash (5%) or Panchagavya 3%.',
                                    'prevention': 'Sow certified pathogen-free seeds; avoid overhead sprinkler '
                                                  'irrigation; practice 2-year crop rotation with non-legumes.'},
    'Black_gram___Healthy': {   'crop_en': 'Black gram',
                                'crop_ta': 'உளுந்து',
                                'disease_en': 'Healthy Crop Foliage',
                                'disease_ta': 'ஆரோக்கியமான பயிர்',
                                'is_healthy': True,
                                'pathogen': 'No pathogen detected (ஆரோக்கியமானது)',
                                'field_sign': 'Uniform dark green trifoliate foliage with no chlorosis, mottling, or '
                                              'necrosis.',
                                'symptoms': [   'Leaves show healthy turgidity, natural pubescence, and uniform green '
                                                'pigmentation.',
                                                'Absence of viral mosaic, powdery mildew mycelium, or anthracnose '
                                                'cankers.'],
                                'chemical_control': 'No chemical intervention required.',
                                'organic_control': 'Spray Panchagavya 3% or Jeevamrutham periodically to sustain soil '
                                                   'microbial activity and plant immunity.',
                                'prevention': 'Maintain proper plant spacing, weed management, and periodic monitoring '
                                              'for sap-feeding pests.'},
    'Black_gram___Leaf_crinkle': {   'crop_en': 'Black gram',
                                     'crop_ta': 'உளுந்து',
                                     'disease_en': 'Leaf Crinkle',
                                     'disease_ta': 'இலைச்சுருட்டு நோய்',
                                     'is_healthy': False,
                                     'pathogen': 'Urdbean Leaf Crinkle Virus (ULCV - vectored by aphids & whiteflies '
                                                 '🧬)',
                                     'field_sign': 'Enlargement, extreme rugosity, and crinkling of 3rd trifoliate '
                                                   'leaf with downward curling.',
                                     'symptoms': [   'Third trifoliate leaf becomes enlarged, thick, leathery, and '
                                                     'severely crinkled.',
                                                     'Down-curling of leaf lamina with prominent raised venation.',
                                                     'Flower bud malformation, delayed maturity, and bush-like sterile '
                                                     'branches with few pods.'],
                                     'chemical_control': 'Vector management: Spray Dimethoate 30 EC @ 1.7 mL/L or '
                                                         'Methyl demeton 25 EC @ 1.5 mL/L or Imidacloprid 17.8 SL @ '
                                                         '0.3 mL/L.',
                                     'organic_control': 'Spray garlic-chilli extract (3%) or 5% Neem Seed Kernel '
                                                        'Extract (NSKE); install yellow sticky traps (15/ha).',
                                     'prevention': 'Rogue and burn symptomatic plants within 30 days of sowing; sow '
                                                   '7-row border of sorghum or maize to intercept aphid vectors.'},
    'Black_gram___Powdery_mildew': {   'crop_en': 'Black gram',
                                       'crop_ta': 'உளுந்து',
                                       'disease_en': 'Powdery Mildew',
                                       'disease_ta': 'சாம்பல் நோய்',
                                       'is_healthy': False,
                                       'pathogen': 'Erysiphe polygoni (Fungus 🍄)',
                                       'field_sign': 'White powdery talcum-like patches covering the upper leaf '
                                                     'surface and pods.',
                                       'symptoms': [   'Small white powdery circular spots expanding across upper leaf '
                                                       'lamina like flour dust.',
                                                       'Infected leaves turn yellow, then necrotic dull brown, and '
                                                       'drop prematurely.',
                                                       'Pods become covered with white powdery fungal growth, '
                                                       'resulting in small shriveled seeds.'],
                                       'chemical_control': 'TNAU CPCPP: Spray Wettable Sulphur 80 WP @ 2.5g/L or '
                                                           'Hexaconazole 5 SC @ 2 mL/L or Dinocap 48 EC @ 1 mL/L.',
                                       'organic_control': 'Foliar spray of 10% fermented sour buttermilk or 3% Neem '
                                                          'oil with soap emulsifier.',
                                       'prevention': 'Early morning foliar dusting of fine sulphur; avoid late sowing; '
                                                     'select tolerant cultivars like Vamban 3 or Co 6.'},
    'Black_gram___Yellow_mosaic': {   'crop_en': 'Black gram',
                                      'crop_ta': 'உளுந்து',
                                      'disease_en': 'Yellow Mosaic Virus (MYMV)',
                                      'disease_ta': 'மஞ்சள் தேமல் நோய்',
                                      'is_healthy': False,
                                      'pathogen': 'Mungbean Yellow Mosaic Virus (MYMV - vectored by Bemisia tabaci '
                                                  'whiteflies 🧬)',
                                      'field_sign': 'Bright golden yellow mosaic patches alternating with green areas '
                                                    'on leaf blades.',
                                      'symptoms': [   'Small chlorotic yellow flecks expanding into brilliant golden '
                                                      'yellow patches on leaves.',
                                                      'Complete yellowing of leaf canopy with stunted vegetative '
                                                      'growth.',
                                                      'Severe reduction in flowering; pods are dwarfed, yellowed, and '
                                                      'produce distorted seeds.'],
                                      'chemical_control': 'Vector management: Spray Imidacloprid 17.8 SL @ 0.3 mL/L or '
                                                          'Acetamiprid 20 SP @ 0.2 g/L or Thiamethoxam 25 WG @ 0.25 '
                                                          'g/L.',
                                      'organic_control': 'Install yellow sticky traps (15-20/ha); spray 5% NSKE (Neem '
                                                         'Seed Kernel Extract) at 10-day intervals.',
                                      'prevention': 'Grow resistant cultivars (VBN 6, VBN 8, CO 6); plant 7-row border '
                                                    'crop of pearl millet/sorghum; treat seeds with Imidacloprid (5 '
                                                    'mL/kg).'},
    'Corn___Cercospora_leaf_spot': {   'crop_en': 'Corn / Maize',
                                       'crop_ta': 'மக்காச்சோளம்',
                                       'disease_en': 'Cercospora Leaf Spot (Gray Leaf Spot)',
                                       'disease_ta': 'சாம்பல் நிற இலைப்புள்ளி நோய்',
                                       'is_healthy': False,
                                       'pathogen': 'Cercospora zeae-maydis (Fungus 🍄)',
                                       'field_sign': 'Narrow, rectangular tan/gray lesions strictly delimited between '
                                                     'parallel leaf veins.',
                                       'symptoms': [   'Narrow rectangular lesions (1-5 cm) bounded strictly by leaf '
                                                       'veins.',
                                                       'Lesions turn pale gray to tan, merging to cause extensive '
                                                       'blighting of entire leaves.',
                                                       'Premature drying of canopy leading to stalk lodging and '
                                                       'reduced grain fill.'],
                                       'chemical_control': 'TNAU CPCPP: Spray Azoxystrobin 18.2% + Difenoconazole '
                                                           '11.4% SC @ 1 mL/L or Pyraclostrobin 20 WG @ 1 g/L.',
                                       'organic_control': 'Deep plow crop residue into soil; foliar spray of '
                                                          'Trichoderma harzianum @ 5g/L; apply compost tea.',
                                       'prevention': 'Practice 2-year crop rotation with pulses or cotton; avoid high '
                                                     'planting density; choose resistant hybrids (COH(M) 6).'},
    'Corn___Common_rust': {   'crop_en': 'Corn / Maize',
                              'crop_ta': 'மக்காச்சோளம்',
                              'disease_en': 'Common Rust',
                              'disease_ta': 'துரு நோய்',
                              'is_healthy': False,
                              'pathogen': 'Puccinia sorghi (Fungus 🍄)',
                              'field_sign': 'Golden-brown to cinnamon-brown powdery pustules erupting on both leaf '
                                            'surfaces.',
                              'symptoms': [   'Oval to elongated cinnamon-brown pustules (uredinia) scattered on both '
                                              'leaf surfaces.',
                                              'Epidermis ruptures releasing powdery rusty spores on fingers when '
                                              'touched.',
                                              'Severely rusted leaves turn chlorotic, dry prematurely, and shred.'],
                              'chemical_control': 'TNAU CPCPP: Spray Mancozeb 75 WP @ 2g/L or Tebuconazole 25.9 EC @ 1 '
                                                  'mL/L upon first sighting of pustules.',
                              'organic_control': 'Foliar spray of 5% Neem Seed Kernel Extract (NSKE) or spray 3% '
                                                 'fermented Panchagavya.',
                              'prevention': 'Avoid excessive nitrogenous fertilizers; maintain balanced potassium '
                                            'nutrition; plant early in the season.'},
    'Corn___Healthy': {   'crop_en': 'Corn / Maize',
                          'crop_ta': 'மக்காச்சோளம்',
                          'disease_en': 'Healthy Crop Foliage',
                          'disease_ta': 'ஆரோக்கியமான பயிர்',
                          'is_healthy': True,
                          'pathogen': 'No pathogen detected (ஆரோக்கியமானது)',
                          'field_sign': 'Broad arching green leaves with clear venation and no rust pustules or blight '
                                        'lesions.',
                          'symptoms': [   'Canopy exhibits robust vegetative growth with clean leaf blades.',
                                          'No signs of Cercospora rectangular spots, Common rust pustules, or Turcicum '
                                          'blighting.'],
                          'chemical_control': 'No chemical intervention required.',
                          'organic_control': 'Soil application of Azospirillum and Phosphobacteria (2 kg/ha each) with '
                                             'farmyard manure.',
                          'prevention': 'Follow recommended NPK scheduling, avoid water stagnation, and scout fields '
                                        'at knee-high stage.'},
    'Corn___Northern_Leaf_Blight': {   'crop_en': 'Corn / Maize',
                                       'crop_ta': 'மக்காச்சோளம்',
                                       'disease_en': 'Northern Corn Leaf Blight',
                                       'disease_ta': 'வடக்கு இலைக்கருகல் நோய்',
                                       'is_healthy': False,
                                       'pathogen': 'Exserohilum turcicum / Setosphaeria turcica (Fungus 🍄)',
                                       'field_sign': 'Large elliptical, cigar-shaped grayish-green to tan lesions '
                                                     '(3-15 cm long).',
                                       'symptoms': [   'Long elliptical cigar-shaped lesions (3-15 cm) running '
                                                       'parallel to veins.',
                                                       'Lesions appear grayish-green initially, then dry to tan '
                                                       'paper-like dead areas.',
                                                       'Dark olive-black fungal sporulation visible on lesions under '
                                                       'humid conditions.'],
                                       'chemical_control': 'TNAU CPCPP: Spray Propiconazole 25 EC @ 1 mL/L or Mancozeb '
                                                           '75 WP @ 2g/L at tasseling stage.',
                                       'organic_control': 'Foliar spray of Trichoderma harzianum formulation @ 5g/L + '
                                                          'Panchagavya 3%.',
                                       'prevention': 'Destroy previous crop stubble; practice balanced fertilization; '
                                                     'select resistant maize varieties (CO 6, Pioneer hybrids).'},
    'Grape___Black_rot': {   'crop_en': 'Grape',
                             'crop_ta': 'திராட்சை',
                             'disease_en': 'Black Rot',
                             'disease_ta': 'கரு அழுகல் நோய்',
                             'is_healthy': False,
                             'pathogen': 'Guignardia bidwellii (Fungus 🍄)',
                             'field_sign': 'Circular reddish-brown leaf spots with tiny black pycnidia rings; berries '
                                           'shrivel into hard black mummies.',
                             'symptoms': [   'Circular reddish-brown necrotic spots on leaves with raised margins and '
                                             'black dots in rings.',
                                             'Infected grape berries turn soft and rotten, then shrivel into hard, '
                                             'wrinkled black mummies.',
                                             'Cane lesions appear as dark, sunken, elongated cankers.'],
                             'chemical_control': 'TNAU CPCPP: Spray Myclobutanil 10 WP @ 1g/L or Mancozeb 75 WP @ '
                                                 '2.5g/L or Azoxystrobin 23 SC @ 1 mL/L.',
                             'organic_control': 'Thoroughly prune and remove all mummified berries from vines and '
                                                'ground; apply copper soap or 1% Bordeaux mixture.',
                             'prevention': 'Prune vines to improve air circulation and sunlight penetration; apply '
                                           'dormant copper spray before bud break.'},
    'Grape___Esca': {   'crop_en': 'Grape',
                        'crop_ta': 'திராட்சை',
                        'disease_en': 'Esca (Black Measles)',
                        'disease_ta': 'எஸ்கா / கருந்தட்டம் நோய்',
                        'is_healthy': False,
                        'pathogen': 'Complex fungal trunk disease (Phaeomoniella chlamydospora, Fomitiporia '
                                    'mediterranea 🍄)',
                        'field_sign': "Striking 'tiger-stripe' interveinal chlorosis and necrosis with green veins; "
                                      'purple spots on berries.',
                        'symptoms': [   "Dramatic 'tiger-stripe' pattern: interveinal necrosis bordered by yellow/red "
                                        'chlorotic bands.',
                                        'Leaves dry and drop suddenly under high summer heat (apoplexy).',
                                        "Grape berries develop dark purple or brown speckling ('black measles') and "
                                        'crack.'],
                        'chemical_control': 'Apply Thiophanate-methyl pruning wound paste immediately to all cane cuts '
                                            '> 1 cm.',
                        'organic_control': 'Paint pruning wounds with Trichoderma viride protective paste; rogue '
                                           'severely affected vines.',
                        'prevention': 'Avoid pruning during wet weather; sterilize pruning shears between vines with '
                                      '70% ethanol; inspect graft unions.'},
    'Grape___Healthy': {   'crop_en': 'Grape',
                           'crop_ta': 'திராட்சை',
                           'disease_en': 'Healthy Crop Foliage',
                           'disease_ta': 'ஆரோக்கியமான பயிர்',
                           'is_healthy': True,
                           'pathogen': 'No pathogen detected (ஆரோக்கியமானது)',
                           'field_sign': 'Vibrant, green, palmately-lobed leaves with smooth margins and clean '
                                         'petioles.',
                           'symptoms': [   'Foliage is free of downy mildew oil spots, powdery mildew white patches, '
                                           'or black rot lesions.',
                                           'Vines show strong cane extension and balanced shoot growth.'],
                           'chemical_control': 'No chemical intervention required.',
                           'organic_control': 'Apply foliar seaweed extract (2 mL/L) or humic acid for vigorous vine '
                                              'canopy development.',
                           'prevention': 'Maintain open trellising for optimal airflow, practice balanced drip '
                                         'fertigation, and monitor pest levels.'},
    'Grape___Leaf_blight': {   'crop_en': 'Grape',
                               'crop_ta': 'திராட்சை',
                               'disease_en': 'Grape Leaf Blight (Isariopsis Blight)',
                               'disease_ta': 'திராட்சை இலைக்கருகல் நோய்',
                               'is_healthy': False,
                               'pathogen': 'Pseudocercospora vitis / Isariopsis clavispora (Fungus 🍄)',
                               'field_sign': 'Irregular angular dark brown necrotic patches bordered by leaf veins '
                                             'with yellow borders.',
                               'symptoms': [   'Angular brown spots bounded by veinlets, later coalescing into large '
                                               'necrotic blotches.',
                                               'Dense olive-gray sooty fungal downy growth on lower leaf surfaces.',
                                               'Premature defoliation resulting in sunscald of exposed grape bunches.'],
                               'chemical_control': 'TNAU CPCPP: Spray Carbendazim 50 WP @ 1g/L or Kresoxim-methyl 44.3 '
                                                   'SC @ 0.7 mL/L or Mancozeb 75 WP @ 2g/L.',
                               'organic_control': 'Spray 1% Bordeaux mixture post-pruning; apply foliar Pseudomonas '
                                                  'fluorescens @ 10g/L.',
                               'prevention': 'Regulate canopy density by summer pruning; ensure adequate vine '
                                             'aeration; collect and burn fallen leaf litter.'},
    'Orange___Black_spot': {   'crop_en': 'Orange / Citrus',
                               'crop_ta': 'ஆரஞ்சு / சிட்ரஸ்',
                               'disease_en': 'Citrus Black Spot',
                               'disease_ta': 'சிட்ரஸ் கருப்பு புள்ளி நோய்',
                               'is_healthy': False,
                               'pathogen': 'Phyllosticta citricarpa / Guignardia citricarpa (Fungus 🍄)',
                               'field_sign': 'Sunken circular hard spots with gray centers, brick-red to black raised '
                                             'borders, and tiny pycnidia on citrus rinds.',
                               'symptoms': [   'Hard spots (circular sunken lesions 1–3 mm) with gray-tan centers and '
                                               'prominent dark red/black margins on leaves and fruit.',
                                               'Virulent black spots spreading into irregular necrotic lesions causing '
                                               'premature fruit drop.',
                                               'Freckle spots on ripe citrus rinds reducing fresh fruit commercial '
                                               'value.'],
                               'chemical_control': 'TNAU CPCPP: Spray Copper Oxychloride 50 WP @ 2.5g/L or '
                                                   'Pyraclostrobin 20 WG @ 1g/L or Mancozeb 75 WP @ 2g/L.',
                               'organic_control': 'Foliar application of 1% Bordeaux mixture after blossom drop; spray '
                                                  '3% Neem oil.',
                               'prevention': 'Remove leaf litter beneath citrus canopies; prune dead twigs and '
                                             'inter-canopy water shoots.'},
    'Orange___Canker': {   'crop_en': 'Orange / Citrus',
                           'crop_ta': 'ஆரஞ்சு / சிட்ரஸ்',
                           'disease_en': 'Citrus Canker',
                           'disease_ta': 'சிட்ரஸ் எலுமிச்சை திட்டு / புண் நோய்',
                           'is_healthy': False,
                           'pathogen': 'Xanthomonas citri subsp. citri (Bacterium 🦠)',
                           'field_sign': 'Raised blister-like corky lesions surrounded by characteristic yellow oily '
                                         'chlorotic halos on leaves and fruits.',
                           'symptoms': [   'Small, raised, blister-like pustules on leaf surfaces expanding into '
                                           'spongy, tan corky craters with distinct oily yellow halos.',
                                           'Crater-like rough brown cankers on fruit rinds with elevated margins, '
                                           'without affecting internal fruit pulp.',
                                           'Twig dieback, severe defoliation, and premature fruit shedding during '
                                           'rainy seasons.'],
                           'chemical_control': 'TNAU CPCPP: Spray Streptomycin sulphate + Tetracycline hydrochloride '
                                               '(100 ppm @ 1g/10L) combined with Copper Oxychloride 50 WP @ 2.5g/L.',
                           'organic_control': 'Spray 1% Bordeaux mixture or foliar copper hydroxide 77 WP @ 2g/L; '
                                              'apply fresh cow dung extract (20%).',
                           'prevention': 'Establish Casuarina or Bamboo windbreaks around orchards to reduce '
                                         'wind-blown rain spread; prune out and burn cankered twigs.'},
    'Orange___Citrus_greening': {   'crop_en': 'Orange / Citrus',
                                    'crop_ta': 'ஆரஞ்சு / சிட்ரஸ்',
                                    'disease_en': 'Citrus Greening (Huanglongbing)',
                                    'disease_ta': 'சிட்ரஸ் கிரீனிங் / மஞ்சள் நரம்பு நோய்',
                                    'is_healthy': False,
                                    'pathogen': 'Candidatus Liberibacter asiaticus (Fastidious Bacterium vectored by '
                                                'Diaphorina citri psyllids 🦠)',
                                    'field_sign': 'Asymmetric blotchy mottle chlorosis crossing leaf veins; lopsided '
                                                  'bitter green fruits.',
                                    'symptoms': [   'Asymmetric blotchy mottled chlorosis of leaf blades that crosses '
                                                    'the central vein.',
                                                    'Thickened, leathery, upright leaves resembling zinc deficiency; '
                                                    'yellow veins.',
                                                    'Lopsided, small, bitter fruits that fail to color properly at the '
                                                    'stylar end (remain green).',
                                                    'Dark, aborted seeds inside sliced fruit.'],
                                    'chemical_control': 'Manage psyllid vectors: Spray Imidacloprid 17.8 SL @ 0.5 mL/L '
                                                        'or Thiamethoxam 25 WG @ 0.3 g/L; trunk injection of '
                                                        'Oxytetracycline hydrochloride.',
                                    'organic_control': 'Release green lacewing predators (Chrysoperla zastrowi @ '
                                                       '50/tree); spray 2% horticultural mineral oil or NSKE 5%.',
                                    'prevention': 'Plant certified disease-free nursery stock; immediately rogue and '
                                                  'destroy confirmed greening-infected trees; control Murraya '
                                                  'paniculata hosts.'},
    'Orange___Healthy': {   'crop_en': 'Orange / Citrus',
                            'crop_ta': 'ஆரஞ்சு / சிட்ரஸ்',
                            'disease_en': 'Healthy Crop Foliage',
                            'disease_ta': 'ஆரோக்கியமான பயிர்',
                            'is_healthy': True,
                            'pathogen': 'No pathogen detected (ஆரோக்கியமானது)',
                            'field_sign': 'Glossy dark green winged-petiole citrus foliage with smooth flush growth '
                                          'and no chlorosis, cankers, or mottling.',
                            'symptoms': [   'Lush, uniform dark green leaf canopy displaying healthy photosynthetic '
                                            'turgor and balanced vegetative flush.',
                                            'No leaf curling, zinc deficiency chlorosis, greening mottle, canker '
                                            'pustules, or melanose sandpapery texture.'],
                            'chemical_control': 'No chemical intervention required.',
                            'organic_control': 'Foliar micronutrient spray (Zinc Sulphate 0.5% + Ferrous Sulphate 0.5% '
                                               '+ Borax 0.2%) with Panchagavya 3%.',
                            'prevention': 'Maintain optimal ring-basin irrigation avoiding waterlogging around trunk '
                                          'bases; practice regular canopy aeration pruning.'},
    'Orange___Melanose': {   'crop_en': 'Orange / Citrus',
                             'crop_ta': 'ஆரஞ்சு / சிட்ரஸ்',
                             'disease_en': 'Citrus Melanose',
                             'disease_ta': 'சிட்ரஸ் மெலனோஸ் / கரும்பழுப்பு சொறி நோய்',
                             'is_healthy': False,
                             'pathogen': 'Diaporthe citri / Phomopsis citri (Fungus 🍄)',
                             'field_sign': 'Discrete tiny rough dark brown/amber gum-filled pustules creating a '
                                           'sandpaper-like feel on leaves and fruit.',
                             'symptoms': [   'Minute circular raised dark reddish-brown to black spots feeling like '
                                             'coarse sandpaper on leaf blades.',
                                             'Tear-streaking and mudcake patterns running down fruits where '
                                             'spore-laden rainwater droplets wash down the rind.',
                                             'Premature yellowing and defoliation of young flushes.'],
                             'chemical_control': 'TNAU CPCPP: Spray Copper Oxychloride 50 WP @ 2.5g/L or Azoxystrobin '
                                                 '23 SC @ 1 mL/L or Carbendazim 50 WP @ 1g/L.',
                             'organic_control': 'Foliar spray of 1% Bordeaux mixture at 2/3 petal fall; spray '
                                                'fermented sour buttermilk (10%).',
                             'prevention': 'Prune out dead wood and twigs where Diaporthe fungus overwinters; ensure '
                                           'canopy is well aerated.'},
    'Orange___Scab': {   'crop_en': 'Orange / Citrus',
                         'crop_ta': 'ஆரஞ்சு / சிட்ரஸ்',
                         'disease_en': 'Citrus Scab',
                         'disease_ta': 'சிட்ரஸ் செதில் / சொறி நோய்',
                         'is_healthy': False,
                         'pathogen': 'Elsinoe fawcettii / Sphaceloma fawcettii (Fungus 🍄)',
                         'field_sign': 'Conical corky warty projections on leaves causing crinkling; irregular scabby '
                                       'crusts on citrus fruit surfaces.',
                         'symptoms': [   'Small pale yellow/pink translucent spots on young leaves developing into '
                                         'conical warty projections.',
                                         'Leaves become twisted, distorted, and severely wrinkled along the central '
                                         'vein.',
                                         'Fruit rinds develop rough, corky scabs that turn dirty gray or brown as '
                                         'fruits mature.'],
                         'chemical_control': 'TNAU CPCPP: Spray Copper Oxychloride 50 WP @ 2.5g/L or Difenoconazole 25 '
                                             'EC @ 0.5 mL/L or Chlorothalonil 75 WP @ 2g/L.',
                         'organic_control': 'Spray 1% Bordeaux mixture before spring flush initiation; foliar spray of '
                                            'Trichoderma viride @ 5g/L.',
                         'prevention': 'Prune infected shoots during winter dormancy; avoid overhead sprinkler wetting '
                                       'during leaf flush.'},
    'Paddy___Bacterial_leaf_blight': {   'crop_en': 'Paddy / Rice',
                                         'crop_ta': 'நெல்',
                                         'disease_en': 'Bacterial Leaf Blight (BLB)',
                                         'disease_ta': 'பாக்டீரியா இலைக்கருகல் நோய்',
                                         'is_healthy': False,
                                         'pathogen': 'Xanthomonas oryzae pv. oryzae (Bacterium 🦠)',
                                         'field_sign': 'Wavy, water-soaked to bleached yellow margins on leaf blades '
                                                       'with morning bacterial ooze beads.',
                                         'symptoms': [   'Water-soaked translucent stripes along leaf margins '
                                                         'developing a wavy yellow to white border.',
                                                         'Lesions progress downward along leaf edges, turning '
                                                         'paper-white or straw-colored.',
                                                         'Milky opaque bacterial exudate beads visible on young '
                                                         'lesions in early morning dew.'],
                                         'chemical_control': 'TNAU CPCPP: Spray Streptomycin sulphate + Tetracycline '
                                                             '(300 g/ha) mixed with Copper Oxychloride 50 WP (1.25 '
                                                             'kg/ha).',
                                         'organic_control': 'Foliar spray of fresh cow dung slurry extract (20%) or '
                                                            'Pseudomonas fluorescens (0.2% - 2 g/L).',
                                         'prevention': 'Drain field temporarily; avoid top-dressing nitrogen '
                                                       'fertilizers when disease is active; grow resistant varieties '
                                                       '(CR 1009, CO 51, ADT 45).'},
    'Paddy___Bacterial_leaf_streak': {   'crop_en': 'Paddy / Rice',
                                         'crop_ta': 'நெல்',
                                         'disease_en': 'Bacterial Leaf Streak',
                                         'disease_ta': 'பாக்டீரியா இலைக்கீற்று நோய்',
                                         'is_healthy': False,
                                         'pathogen': 'Xanthomonas oryzae pv. oryzicola (Bacterium 🦠)',
                                         'field_sign': 'Fine, interveinal water-soaked narrow streaks strictly '
                                                       'confined between leaf veins.',
                                         'symptoms': [   'Narrow, translucent, water-soaked interveinal streaks '
                                                         'running parallel to veins.',
                                                         'Streaks turn golden yellow, then necrotic brown, covered '
                                                         'with small amber exudate beads.',
                                                         'Leaves turn gray-brown and die, giving the canopy a scorched '
                                                         'appearance.'],
                                         'chemical_control': 'TNAU CPCPP: Spray Copper hydroxide 77 WP @ 2g/L or '
                                                             'Copper Oxychloride @ 2.5g/L.',
                                         'organic_control': 'Foliar spray of Bacillus subtilis (5 g/L) + 3% neem oil '
                                                            'spray.',
                                         'prevention': 'Regulate irrigation water; avoid high urea application; select '
                                                       'tolerant paddy lines.'},
    'Paddy___Bacterial_panicle_blight': {   'crop_en': 'Paddy / Rice',
                                            'crop_ta': 'நெல்',
                                            'disease_en': 'Bacterial Panicle Blight',
                                            'disease_ta': 'கதிர் கருகல் நோய்',
                                            'is_healthy': False,
                                            'pathogen': 'Burkholderia glumae (Bacterium 🦠)',
                                            'field_sign': 'Discolored panicles remaining upright due to light, empty, '
                                                          'unfilled grains.',
                                            'symptoms': [   'Florets turn reddish-brown to grayish-black from the base '
                                                            'upwards.',
                                                            'Panicles remain upright instead of bending because grains '
                                                            'are aborted and chaffy.',
                                                            'Severe yield loss under night temperatures exceeding 25°C '
                                                            'during heading.'],
                                            'chemical_control': 'Spray Oxolinic acid or Kasugamycin 3% SL @ 2 mL/L at '
                                                                '50% panicle emergence.',
                                            'organic_control': 'Seed treatment with Pseudomonas fluorescens (10 g/kg '
                                                               'seed) + foliar spray at booting and heading.',
                                            'prevention': 'Use certified pathogen-free seeds; manage field water '
                                                          'levels during flowering; sow at optimal seasonal dates.'},
    'Paddy___Blast': {   'crop_en': 'Paddy / Rice',
                         'crop_ta': 'நெல்',
                         'disease_en': 'Rice Blast (Leaf, Node & Neck Blast)',
                         'disease_ta': 'குலை நோய் (இலை, கணு & கழுத்து குலை நோய்)',
                         'is_healthy': False,
                         'pathogen': 'Magnaporthe oryzae / Pyricularia oryzae (Fungus 🍄)',
                         'field_sign': 'Diamond-shaped or spindle-shaped lesions with ash-gray center and dark '
                                       'reddish-brown margins.',
                         'symptoms': [   'Spindle-shaped / diamond-shaped lesions with whitish-gray centers and brown '
                                         'margins on leaves.',
                                         'Neck blast: panicle rachis node turns blackish-brown and breaks under wind, '
                                         'leading to empty grains.',
                                         'Node blast: culm nodes turn black, rot, and lodge easily.'],
                         'chemical_control': 'TNAU CPCPP: Spray Tricyclazole 75 WP @ 1g/L or Azoxystrobin 25 SC @ 1 '
                                             'mL/L or Isoprothiolane 40 EC @ 1.5 mL/L.',
                         'organic_control': 'Foliar spray of Pseudomonas fluorescens @ 10g/L or Panchagavya 3% (30 '
                                            'mL/L).',
                         'prevention': 'Split nitrogen application into 3-4 doses; soak seeds in Pseudomonas (10g/kg) '
                                       'for 24h; plant resistant cultivars (CO 51, ADT 43).'},
    'Paddy___Brown_spot': {   'crop_en': 'Paddy / Rice',
                              'crop_ta': 'நெல்',
                              'disease_en': 'Brown Spot',
                              'disease_ta': 'பழுப்பு இலைப்புள்ளி நோய்',
                              'is_healthy': False,
                              'pathogen': 'Bipolaris oryzae / Helminthosporium oryzae (Fungus 🍄)',
                              'field_sign': 'Circular to oval sesame-seed shaped dark brown spots with a distinct '
                                            'yellow halo.',
                              'symptoms': [   'Small circular to oval dark brown spots resembling sesame seeds on '
                                              'leaves and glumes.',
                                              'Spots develop gray/white center with dark brown margins surrounded by a '
                                              'chlorotic halo.',
                                              'Severe spotting causes premature leaf yellowing, seedling blight, and '
                                              'discolored grains.'],
                              'chemical_control': 'TNAU CPCPP: Spray Mancozeb 75 WP @ 2g/L or Propiconazole 25 EC @ 1 '
                                                  'mL/L or Carbendazim 50 WP @ 1g/L.',
                              'organic_control': 'Seed soaking in Pseudomonas fluorescens (10 g/kg); soil application '
                                                 'of neem cake (150 kg/ha).',
                              'prevention': 'Correct soil potassium and silicon deficiencies; provide balanced organic '
                                            'manures; do not stress crop for water.'},
    'Paddy___Dead_heart': {   'crop_en': 'Paddy / Rice',
                              'crop_ta': 'நெல்',
                              'disease_en': 'Stem Borer Dead Heart',
                              'disease_ta': 'குருத்துப்பூச்சி / குறுத்து வாடல்',
                              'is_healthy': False,
                              'pathogen': 'Scirpophaga incertulas (Yellow Stem Borer - Insect 🐛)',
                              'field_sign': "Central young shoot dies, withers ('dead heart'), and pulls out "
                                            'effortlessly with chewed base.',
                              'symptoms': [   "Central emerging shoot dries up and turns white/brown ('dead heart') "
                                              'during vegetative stage.',
                                              'Damaged tillers pull out easily by hand, revealing larval frass and '
                                              'chewed base.',
                                              'In reproductive stage, panicles turn completely white and erect with '
                                              "empty grains ('white ear')."],
                              'chemical_control': 'TNAU CPCPP: Spray Chlorantraniliprole 18.5 SC @ 0.3 mL/L or Cartap '
                                                  'hydrochloride 50 SP @ 2g/L or Fipronil 5 SC @ 2 mL/L.',
                              'organic_control': 'Release egg parasitoid Trichogramma japonicum @ 100,000/ha; install '
                                                 '12 pheromone traps/ha with yellow sticky liners.',
                              'prevention': 'Clip seedling leaf tips before transplanting to eliminate egg masses; '
                                            'harvest at ground level; plow stubble after harvest.'},
    'Paddy___Downy_mildew': {   'crop_en': 'Paddy / Rice',
                                'crop_ta': 'நெல்',
                                'disease_en': 'Downy Mildew (Crazy Top)',
                                'disease_ta': 'அடிச்சாம்பல் நோய்',
                                'is_healthy': False,
                                'pathogen': 'Sclerophthora macrospora (Oomycete 🍄)',
                                'field_sign': 'Twisted, deformed crazy-top flag leaves with multiple small leafy '
                                              'proliferations on panicles.',
                                'symptoms': [   'Chlorotic yellow flecks and mottling on young leaf blades.',
                                                'Flag leaves become severely twisted, spiraled, and crinkled.',
                                                "Abnormal leafy structures replace floral parts in panicles ('crazy "
                                                "top') with zero grain fill."],
                                'chemical_control': 'TNAU CPCPP: Spray Metalaxyl 8% + Mancozeb 64% WP @ 2g/L.',
                                'organic_control': 'Improve drainage to prevent flood inundation of nursery; rogue '
                                                   'crazy-top infected clumps; spray compost tea.',
                                'prevention': 'Avoid submergence of young rice seedlings for > 48 hours; use certified '
                                              'seeds from unflooded fields.'},
    'Paddy___Healthy': {   'crop_en': 'Paddy / Rice',
                           'crop_ta': 'நெல்',
                           'disease_en': 'Healthy Crop Foliage',
                           'disease_ta': 'ஆரோக்கியமான பயிர்',
                           'is_healthy': True,
                           'pathogen': 'No pathogen detected (ஆரோக்கியமானது)',
                           'field_sign': 'Upright, deep-green tillers with uniform leaves free from lesions, wilting, '
                                         'or discolorations.',
                           'symptoms': [   'Leaves exhibit uniform chlorophyll pigmentation without necrotic lesions '
                                           'or leaf streaks.',
                                           'Absence of blast spindle spots, bacterial leaf blight white margins, or '
                                           'stem borer dead hearts.'],
                           'chemical_control': 'No chemical intervention required.',
                           'organic_control': 'Apply Azolla biofertilizer (1 t/ha) or spray Panchagavya 3% (30 mL/L) '
                                              'at tillering stage.',
                           'prevention': 'Practice alternate wetting and drying (AWD) irrigation; ensure balanced '
                                         'potassium fertilization; monitor weekly.'},
    'Paddy___Hispa': {   'crop_en': 'Paddy / Rice',
                         'crop_ta': 'நெல்',
                         'disease_en': 'Rice Hispa',
                         'disease_ta': 'இலைவண்டு / ஹிஸ்பா வண்டு',
                         'is_healthy': False,
                         'pathogen': 'Dicladispa armigera (Rice Hispa - Spiny Beetle 🪲)',
                         'field_sign': 'Parallel white streaks along leaf blade scraped by adult spiny beetles; leaves '
                                       'turn papery white.',
                         'symptoms': [   'Adult beetles scrape upper leaf surface producing characteristic parallel '
                                         'white streaks.',
                                         'Larvae mine between leaf epidermal layers creating blister-like necrotic '
                                         'blotches.',
                                         'Damaged leaves wither, turn membranous white, and dry out across large field '
                                         'patches.'],
                         'chemical_control': 'TNAU CPCPP: Spray Profenofos 50 EC @ 2 mL/L or Chlorpyrifos 20 EC @ 2.5 '
                                             'mL/L.',
                         'organic_control': 'Clip seedling leaf tips containing hispa eggs prior to transplanting; '
                                            'sweep nursery canopy with collection nets.',
                         'prevention': 'Maintain optimal water depth; eliminate alternate wild grass hosts along '
                                       'bunds; monitor nursery beds closely.'},
    'Paddy___Tungro': {   'crop_en': 'Paddy / Rice',
                          'crop_ta': 'நெல்',
                          'disease_en': 'Rice Tungro Virus',
                          'disease_ta': 'துங்ரோ நச்சுயிரி நோய்',
                          'is_healthy': False,
                          'pathogen': 'Rice Tungro Bacilliform & Spherical Viruses (vectored by Nephotettix virescens '
                                      'green leafhoppers 🧬)',
                          'field_sign': 'Golden yellow to orange discoloration beginning from leaf tips accompanied by '
                                        'severe plant stunting.',
                          'symptoms': [   'Leaf yellowing or orange discoloration starting at leaf tip and progressing '
                                          'downward along margins.',
                                          'Severe stunting of infected plants and reduced tiller count.',
                                          'Delayed flowering; panicles remain small, poorly exerted, with high '
                                          'proportion of empty grains.'],
                          'chemical_control': 'Control leafhopper vectors: Spray Thiamethoxam 25 WG @ 0.2 g/L or '
                                              'Imidacloprid 17.8 SL @ 0.25 mL/L or Dinotefuran 20 SG @ 0.4 g/L.',
                          'organic_control': 'Set up light traps and yellow sticky traps (25/ha); foliar spray of 5% '
                                             'Neem Seed Kernel Extract (NSKE).',
                          'prevention': 'Plant resistant varieties (ADT 45, PY 3); synchronize transplanting within '
                                        'the community; plow in infected stubbles.'},
    'Pepper___Bacterial_spot': {   'crop_en': 'Pepper / Chilli',
                                   'crop_ta': 'மிளகாய் / குடைமிளகாய்',
                                   'disease_en': 'Bacterial Leaf Spot',
                                   'disease_ta': 'பாக்டீரியா இலைப்புள்ளி நோய்',
                                   'is_healthy': False,
                                   'pathogen': 'Xanthomonas campestris pv. vesicatoria (Bacterium 🦠)',
                                   'field_sign': 'Small water-soaked dark brown spots with a greasy appearance; heavy '
                                                 'premature defoliation.',
                                   'symptoms': [   'Small water-soaked circular to irregular dark brown spots on lower '
                                                   'leaf surface.',
                                                   'Lesions develop a sunken center with greasy borders and chlorotic '
                                                   'yellow rings.',
                                                   'Severe infection causes extensive yellowing, defoliation, and '
                                                   'rough scab-like spots on peppers.'],
                                   'chemical_control': 'TNAU CPCPP: Spray Copper Oxychloride 50 WP @ 2.5g/L combined '
                                                       'with Streptocycline @ 100 ppm (1g in 10L water).',
                                   'organic_control': 'Soak seeds in hot water (50°C for 25 mins); foliar spray of '
                                                      'Pseudomonas fluorescens @ 10g/L or 2% neem oil.',
                                   'prevention': 'Avoid overhead sprinkler irrigation; stake pepper plants to prevent '
                                                 'soil splash; practice 2-year crop rotation.'},
    'Pepper___Healthy': {   'crop_en': 'Pepper / Chilli',
                            'crop_ta': 'மிளகாய் / குடைமிளகாய்',
                            'disease_en': 'Healthy Crop Foliage',
                            'disease_ta': 'ஆரோக்கியமான பயிர்',
                            'is_healthy': True,
                            'pathogen': 'No pathogen detected (ஆரோக்கியமானது)',
                            'field_sign': 'Smooth, glossy, dark green lanceolate leaves with no leaf curl, stippling, '
                                          'or bacterial spots.',
                            'symptoms': [   'Active vegetative apical growth with healthy flower bud emergence.',
                                            'Foliage is free from thrips curl, mite bronze scorching, or bacterial '
                                            'necrotic spotting.'],
                            'chemical_control': 'No chemical intervention required.',
                            'organic_control': 'Foliar spray of vermiwash (5%) or fish amino acid (FAA 3 mL/L) for '
                                               'plant vigour.',
                            'prevention': 'Stake plants against lodging, apply organic mulch around root zones, and '
                                          'maintain clean field borders.'},
    'Potato___Early_blight': {   'crop_en': 'Potato',
                                 'crop_ta': 'உருளைக்கிழங்கு',
                                 'disease_en': 'Early Blight',
                                 'disease_ta': 'முன் பருவ கருகல் நோய்',
                                 'is_healthy': False,
                                 'pathogen': 'Alternaria solani (Fungus 🍄)',
                                 'field_sign': "Dark brown circular lesions with distinct 'target-board' concentric "
                                               'rings on older lower leaves.',
                                 'symptoms': [   'Dark brown to black circular lesions exhibiting prominent concentric '
                                                 "rings ('target-board').",
                                                 'Lesions start on older lower leaves, surrounded by a narrow '
                                                 'chlorotic halo.',
                                                 'Severe blight causes leaves to yellow, shrivel, and drop; dark '
                                                 'sunken lesions on potato tubers.'],
                                 'chemical_control': 'TNAU CPCPP: Spray Chlorothalonil 75 WP @ 2g/L or Mancozeb 75 WP '
                                                     '@ 2g/L or Difenoconazole 25 EC @ 0.5 mL/L.',
                                 'organic_control': 'Foliar spray of 5% neem leaf extract or Trichoderma viride @ '
                                                    '5g/L; apply balanced potassium fertilizer.',
                                 'prevention': 'Hill up soil well around stems; prune lower senescent leaves; plant '
                                               'certified disease-free seed tubers.'},
    'Potato___Healthy': {   'crop_en': 'Potato',
                            'crop_ta': 'உருளைக்கிழங்கு',
                            'disease_en': 'Healthy Crop Foliage',
                            'disease_ta': 'ஆரோக்கியமான பயிர்',
                            'is_healthy': True,
                            'pathogen': 'No pathogen detected (ஆரோக்கியமானது)',
                            'field_sign': 'Compound pinnate dark green foliage with vigorous erect haulm growth and no '
                                          'blight spots.',
                            'symptoms': [   'Leaves show crisp, uniform foliage without target-board rings or '
                                            'water-soaked margins.',
                                            'No signs of late blight downy sporulation or early blight lower-leaf '
                                            'necrosis.'],
                            'chemical_control': 'No chemical intervention required.',
                            'organic_control': 'Soil enrichment with well-rotted farmyard manure and Trichoderma '
                                               'viride enriched compost.',
                            'prevention': 'Ensure good earthing-up to protect tubers, maintain soil aeration, and '
                                          'scout foliage after rains.'},
    'Potato___Late_blight': {   'crop_en': 'Potato',
                                'crop_ta': 'உருளைக்கிழங்கு',
                                'disease_en': 'Late Blight',
                                'disease_ta': 'பின் பருவ கருகல் நோய்',
                                'is_healthy': False,
                                'pathogen': 'Phytophthora infestans (Oomycete 🍄)',
                                'field_sign': 'Rapidly spreading water-soaked dark brown blighted lesions with white '
                                              'downy mold on underside.',
                                'symptoms': [   'Irregular, rapidly spreading water-soaked pale-to-dark brown lesions '
                                                'starting from leaf edges.',
                                                'White cottony downy fungal sporulation visible on the underside of '
                                                'lesions under humid/foggy weather.',
                                                'Foliage and stems turn black, collapse rapidly, and emit a '
                                                'characteristic foul odor.'],
                                'chemical_control': 'TNAU CPCPP: Spray Cymoxanil 8% + Mancozeb 64% WP @ 2g/L or '
                                                    'Dimethomorph 50 WP @ 1g/L or Metalaxyl + Mancozeb @ 2g/L.',
                                'organic_control': 'Prophylactic spray of 1% Bordeaux mixture before monsoon mist; '
                                                   'plant certified Nilgiris-adapted resistant tubers.',
                                'prevention': 'Destroy cull piles; provide adequate hill spacing; avoid night '
                                              'sprinkler irrigation in high-altitude zones (Ooty, Kodaikanal).'},
    'Tomato___Bacterial_spot': {   'crop_en': 'Tomato',
                                   'crop_ta': 'தக்காளி',
                                   'disease_en': 'Bacterial Spot',
                                   'disease_ta': 'பாக்டீரியா இலைப்புள்ளி நோய்',
                                   'is_healthy': False,
                                   'pathogen': 'Xanthomonas campestris pv. vesicatoria (Bacterium 🦠)',
                                   'field_sign': 'Small (2-3 mm) angular water-soaked black spots with purplish cast '
                                                 'and yellow halo; shot-hole effect.',
                                   'symptoms': [   'Small angular water-soaked dark spots turning black with yellow '
                                                   'chlorotic halos.',
                                                   'Dead center of leaf lesions falls out creating a ragged '
                                                   "'shot-hole' appearance.",
                                                   'Black scabby blister spots (3-5 mm) on green tomato fruits making '
                                                   'them unmarketable.'],
                                   'chemical_control': 'TNAU CPCPP: Spray Copper hydroxide 77 WP @ 2g/L or Copper '
                                                       'Oxychloride @ 2.5g/L mixed with Streptocycline @ 100 ppm.',
                                   'organic_control': 'Foliar spray of 5% garlic bulb extract or Pseudomonas '
                                                      'fluorescens @ 10g/L.',
                                   'prevention': 'Treat seeds with 1.3% Sodium hypochlorite for 1 min; use drip '
                                                 'irrigation; avoid working in fields when wet.'},
    'Tomato___Early_blight': {   'crop_en': 'Tomato',
                                 'crop_ta': 'தக்காளி',
                                 'disease_en': 'Early Blight',
                                 'disease_ta': 'முன் பருவ இலைக்கருகல் நோய்',
                                 'is_healthy': False,
                                 'pathogen': 'Alternaria solani (Fungus 🍄)',
                                 'field_sign': 'Target-board concentric rings inside dark brown spots on lower leaves '
                                               'with yellow halos.',
                                 'symptoms': [   "Concentric ringed ('target-board') dark brown to black spots on "
                                                 'older lower leaves.',
                                                 'Leaves yellow and drop prematurely; collar rot cankers form at stem '
                                                 'bases.',
                                                 'Sunken leathery dark spots at the stem-end of tomato fruits.'],
                                 'chemical_control': 'TNAU CPCPP: Spray Difenoconazole 25 EC @ 1 mL/L or Azoxystrobin '
                                                     '23 SC @ 1 mL/L or Chlorothalonil 75 WP @ 2g/L.',
                                 'organic_control': 'Foliar spray of Pseudomonas fluorescens @ 10g/L or Trichoderma '
                                                    'viride @ 5g/L; spray NSKE 5%.',
                                 'prevention': 'Prune lower leaves touching soil; stake plants with bamboo poles to '
                                               'keep foliage dry; rotate with non-solanaceous crops.'},
    'Tomato___Healthy': {   'crop_en': 'Tomato',
                            'crop_ta': 'தக்காளி',
                            'disease_en': 'Healthy Crop Foliage',
                            'disease_ta': 'ஆரோக்கியமான பயிர்',
                            'is_healthy': True,
                            'pathogen': 'No pathogen detected (ஆரோக்கியமானது)',
                            'field_sign': 'Rich green serrated leaves with strong aromatic glandular trichomes and '
                                          'clean growing tips.',
                            'symptoms': [   'Foliage demonstrates strong photosynthetic turgor and balanced '
                                            'vegetative-reproductive balance.',
                                            'Absence of yellow leaf curl, early blight rings, bacterial speck, or '
                                            'spider mite webbing.'],
                            'chemical_control': 'No chemical intervention required.',
                            'organic_control': 'Foliar spray of Panchagavya 3% or diluted cow urine (10%) at 15-day '
                                               'intervals.',
                            'prevention': 'Stake plants on bamboo trellises, use drip irrigation to keep leaves dry, '
                                          'and practice crop rotation.'},
    'Tomato___Late_blight': {   'crop_en': 'Tomato',
                                'crop_ta': 'தக்காளி',
                                'disease_en': 'Late Blight',
                                'disease_ta': 'பின் பருவ இலைக்கருகல் நோய்',
                                'is_healthy': False,
                                'pathogen': 'Phytophthora infestans (Oomycete 🍄)',
                                'field_sign': 'Rapidly spreading pale green to dark brown water-soaked lesions with '
                                              'white downy mold underneath.',
                                'symptoms': [   'Pale green to brownish-black rapidly spreading water-soaked lesions '
                                                'on leaves and petioles.',
                                                'White downy sporulation visible on the underside of infected leaves '
                                                'under cool, humid conditions.',
                                                'Greasy brownish-bronze firm rot develops on green tomato fruits.'],
                                'chemical_control': 'TNAU CPCPP: Spray Metalaxyl 8% + Mancozeb 64% WP @ 2g/L or '
                                                    'Mandipropamid 23.4 SC @ 1 mL/L or Cymoxanil + Mancozeb @ 2g/L.',
                                'organic_control': 'Spray 1% Bordeaux mixture prophylactically; maintain good field '
                                                   'drainage and wide plant spacing.',
                                'prevention': 'Avoid overhead irrigation; remove and burn blighted plants immediately; '
                                              'do not plant near potato fields.'},
    'Tomato___Leaf_Mold': {   'crop_en': 'Tomato',
                              'crop_ta': 'தக்காளி',
                              'disease_en': 'Leaf Mold',
                              'disease_ta': 'இலை பூஞ்சை பூச்சு நோய்',
                              'is_healthy': False,
                              'pathogen': 'Passalora fulva / Cladosporium fulvum (Fungus 🍄)',
                              'field_sign': 'Pale yellow spots on upper leaf surface with olive-green velvety mold '
                                            'growth on lower surface.',
                              'symptoms': [   'Pale greenish-yellow chlorotic spots with indistinct borders on upper '
                                              'leaf surface.',
                                              'Dense olive-green to brown velvety fungal mold on the lower leaf '
                                              'surface corresponding to yellow spots.',
                                              'Infected leaves roll upward, wilt, wither, and drop prematurely.'],
                              'chemical_control': 'TNAU CPCPP: Spray Azoxystrobin 23 SC @ 1 mL/L or Copper Oxychloride '
                                                  '50 WP @ 2.5g/L or Difenoconazole 25 EC @ 0.5 mL/L.',
                              'organic_control': 'Spray baking soda (Sodium bicarbonate @ 5g/L) + soap emulsifier; '
                                                 'foliar spray of Trichoderma harzianum @ 5g/L.',
                              'prevention': 'Reduce greenhouse humidity below 85%; increase air circulation by staking '
                                            'and pruning; use drip irrigation.'},
    'Tomato___Septoria_leaf_spot': {   'crop_en': 'Tomato',
                                       'crop_ta': 'தக்காளி',
                                       'disease_en': 'Septoria Leaf Spot',
                                       'disease_ta': 'செப்டோரியா இலைப்புள்ளி நோய்',
                                       'is_healthy': False,
                                       'pathogen': 'Septoria lycopersici (Fungus 🍄)',
                                       'field_sign': 'Numerous small circular spots with dark brown margins and sunken '
                                                     'gray centers with black specks.',
                                       'symptoms': [   'Numerous small circular spots (2-3 mm) with dark brown borders '
                                                       'and ash-gray sunken centers.',
                                                       'Tiny black fruiting specks (pycnidia) clearly visible inside '
                                                       'lesion centers.',
                                                       'Leaves turn yellow, curl up, and fall off rapidly from the '
                                                       'bottom of the plant upwards.'],
                                       'chemical_control': 'TNAU CPCPP: Spray Mancozeb 75 WP @ 2g/L or Chlorothalonil '
                                                           '75 WP @ 2g/L or Propiconazole 25 EC @ 1 mL/L.',
                                       'organic_control': 'Prune lower 12 inches of foliage touching ground; apply '
                                                          'organic straw mulch to stop rain-splash spores.',
                                       'prevention': 'Practice 3-year crop rotation; sterilize tomato cages and '
                                                     'stakes; avoid handling plants when foliage is wet.'},
    'Tomato___Spider_mites': {   'crop_en': 'Tomato',
                                 'crop_ta': 'தக்காளி',
                                 'disease_en': 'Two-Spotted Spider Mite Damage',
                                 'disease_ta': 'செம்பேன் / சிலந்திப் பூச்சி தாக்குதல்',
                                 'is_healthy': False,
                                 'pathogen': 'Tetranychus urticae (Two-Spotted Spider Mite - Acarina 🕷️)',
                                 'field_sign': 'Fine yellow stippling/speckling on upper leaf blade with fine silken '
                                               'webbing on leaf underside.',
                                 'symptoms': [   'Yellowish-white speckled stippling on leaf surface caused by mite '
                                                 'sap-feeding.',
                                                 'Fine silken webbing spun across the undersides of leaves and growing '
                                                 'tips.',
                                                 'Foliage turns bronze, dries out, and takes on a scorched burned '
                                                 'appearance under hot dry weather.'],
                                 'chemical_control': 'TNAU CPCPP: Spray Spiromesifen 22.9 SC @ 1 mL/L or Fenazaquin 10 '
                                                     'EC @ 2 mL/L or Abamectin 1.9 EC @ 0.5 mL/L.',
                                 'organic_control': 'Spray Wettable Sulphur 80 WP @ 3g/L or 3% Neem oil with soap '
                                                    'emulsifier; release predatory mites (Phytoseiulus persimilis).',
                                 'prevention': 'Avoid dusty field edges; irrigate crops regularly to maintain relative '
                                               'humidity; remove weed hosts around field margins.'},
    'Tomato___Target_Spot': {   'crop_en': 'Tomato',
                                'crop_ta': 'தக்காளி',
                                'disease_en': 'Target Spot',
                                'disease_ta': 'இலக்கு இலைப்புள்ளி நோய்',
                                'is_healthy': False,
                                'pathogen': 'Corynespora cassiicola (Fungus 🍄)',
                                'field_sign': 'Pinpoint brown spots expanding into circular lesions (1 cm) with '
                                              'prominent concentric rings.',
                                'symptoms': [   'Small brown pinpoint spots on foliage expanding into circular lesions '
                                                'up to 1 cm wide.',
                                                'Concentric target-board rings with distinct chlorotic halos; lesions '
                                                'lack pycnidia specks.',
                                                'Fruit lesions appear as sunken brown craters with dark velvety '
                                                'centers.'],
                                'chemical_control': 'TNAU CPCPP: Spray Pyraclostrobin 20 WG @ 1g/L or Azoxystrobin + '
                                                    'Difenoconazole @ 1 mL/L or Mancozeb 75 WP @ 2g/L.',
                                'organic_control': 'Field sanitation and deep debris incorporation; foliar spray of '
                                                   'Bacillus amyloliquefaciens @ 5g/L.',
                                'prevention': 'Improve canopy airflow by wider row spacing; avoid nitrogen '
                                              'over-fertilization; rogue out infected plant tissue.'},
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': {   'crop_en': 'Tomato',
                                                  'crop_ta': 'தக்காளி',
                                                  'disease_en': 'Tomato Yellow Leaf Curl Virus (TYLCV)',
                                                  'disease_ta': 'மஞ்சள் இலை சுருள் நோய்',
                                                  'is_healthy': False,
                                                  'pathogen': 'Tomato Yellow Leaf Curl Virus (vectored by Bemisia '
                                                              'tabaci whiteflies 🧬)',
                                                  'field_sign': 'Severe upward cupping/curling of leaves, marginal '
                                                                'chlorosis, stunted bushy growth.',
                                                  'symptoms': [   'Severe upward and inward cupping/curling of leaf '
                                                                  'margins.',
                                                                  'Pronounced yellowing (chlorosis) along leaf edges '
                                                                  'with reduced leaflet size.',
                                                                  'Severe stunting of plant height giving a bushy '
                                                                  'appearance; complete blossom drop and zero fruit '
                                                                  'set.'],
                                                  'chemical_control': 'Manage whitefly vector: Spray Cyantraniliprole '
                                                                      '10.26 OD @ 1.8 mL/L or Diafenthiuron 50 WP @ '
                                                                      '1.2 g/L or Thiamethoxam 25 WG @ 0.3 g/L.',
                                                  'organic_control': 'Install yellow sticky traps (30/ha); protect '
                                                                     'nurseries with 40-mesh nylon insect netting; '
                                                                     'spray 5% NSKE.',
                                                  'prevention': 'Grow TYLCV-resistant hybrids (e.g. US 440, '
                                                                'ToMV-resistant lines); eliminate solanaceous weed '
                                                                'hosts (Solanum nigrum); rogue early infected plants.'},
    'Tomato___Tomato_mosaic_virus': {   'crop_en': 'Tomato',
                                        'crop_ta': 'தக்காளி',
                                        'disease_en': 'Tomato Mosaic Virus (ToMV)',
                                        'disease_ta': 'மொசைக் நச்சுயிரி நோய்',
                                        'is_healthy': False,
                                        'pathogen': 'Tomato Mosaic Virus (Tobamovirus - Mechanically transmitted 🧬)',
                                        'field_sign': 'Alternating light and dark green mosaic mottle with '
                                                      "'shoestring' fern-like thinning of leaflets.",
                                        'symptoms': [   'Mottling with alternating light green and dark green mosaic '
                                                        'patterns on foliage.',
                                                        'Leaflet distortion, puckering, and extreme thinning producing '
                                                        "a 'shoestring' or fern-like leaf.",
                                                        'Internal brown necrotic browning in the fruit wall (brown '
                                                        'wall) making fruits unmarketable.'],
                                        'chemical_control': 'No chemical viricide exists. Disinfect seeds in 10% '
                                                            'Trisodium phosphate (TSP) solution for 30 minutes before '
                                                            'sowing.',
                                        'organic_control': 'Wash hands and pruning tools with 20% skimmed milk or soap '
                                                           'solution before touching plants; spray buttermilk 10%.',
                                        'prevention': 'Prohibit tobacco use (smoking/chewing) inside fields and '
                                                      'polyhouses; rogue infected plants immediately; plant resistant '
                                                      'cultivars.'},
    'Apple___healthy': {   'crop_en': 'Apple',
                           'crop_ta': 'ஆப்பிள்',
                           'disease_en': 'Healthy Crop Foliage',
                           'disease_ta': 'ஆரோக்கியமான பயிர்',
                           'is_healthy': True,
                           'pathogen': 'No pathogen detected (ஆரோக்கியமானது)',
                           'field_sign': 'Vibrant dark green serrated leaves on vigorous spur growth; no foliar '
                                         'lesions, rust spots, or powdery mildew.',
                           'symptoms': [   'Clean, uniform photosynthetic foliage with balanced terminal growth and '
                                           'fruit spur formation.',
                                           'Absence of fungal scab velvety lesions, rust aecia, or fire blight '
                                           'wilting.'],
                           'chemical_control': 'No chemical intervention required.',
                           'organic_control': 'Soil application of well-composted farmyard manure with Trichoderma '
                                              'viride; foliar spray of Panchagavya 3%.',
                           'prevention': 'Maintain optimal canopy training/pruning, ensure adequate sunlight '
                                         'penetration, and monitor soil moisture.'},
    'Black_gram___healthy': {   'crop_en': 'Black gram',
                                'crop_ta': 'உளுந்து',
                                'disease_en': 'Healthy Crop Foliage',
                                'disease_ta': 'ஆரோக்கியமான பயிர்',
                                'is_healthy': True,
                                'pathogen': 'No pathogen detected (ஆரோக்கியமானது)',
                                'field_sign': 'Uniform dark green trifoliate foliage with no chlorosis, mottling, or '
                                              'necrosis.',
                                'symptoms': [   'Leaves show healthy turgidity, natural pubescence, and uniform green '
                                                'pigmentation.',
                                                'Absence of viral mosaic, powdery mildew mycelium, or anthracnose '
                                                'cankers.'],
                                'chemical_control': 'No chemical intervention required.',
                                'organic_control': 'Spray Panchagavya 3% or Jeevamrutham periodically to sustain soil '
                                                   'microbial activity and plant immunity.',
                                'prevention': 'Maintain proper plant spacing, weed management, and periodic monitoring '
                                              'for sap-feeding pests.'},
    'Corn___healthy': {   'crop_en': 'Corn / Maize',
                          'crop_ta': 'மக்காச்சோளம்',
                          'disease_en': 'Healthy Crop Foliage',
                          'disease_ta': 'ஆரோக்கியமான பயிர்',
                          'is_healthy': True,
                          'pathogen': 'No pathogen detected (ஆரோக்கியமானது)',
                          'field_sign': 'Broad arching green leaves with clear venation and no rust pustules or blight '
                                        'lesions.',
                          'symptoms': [   'Canopy exhibits robust vegetative growth with clean leaf blades.',
                                          'No signs of Cercospora rectangular spots, Common rust pustules, or Turcicum '
                                          'blighting.'],
                          'chemical_control': 'No chemical intervention required.',
                          'organic_control': 'Soil application of Azospirillum and Phosphobacteria (2 kg/ha each) with '
                                             'farmyard manure.',
                          'prevention': 'Follow recommended NPK scheduling, avoid water stagnation, and scout fields '
                                        'at knee-high stage.'},
    'Grape___healthy': {   'crop_en': 'Grape',
                           'crop_ta': 'திராட்சை',
                           'disease_en': 'Healthy Crop Foliage',
                           'disease_ta': 'ஆரோக்கியமான பயிர்',
                           'is_healthy': True,
                           'pathogen': 'No pathogen detected (ஆரோக்கியமானது)',
                           'field_sign': 'Vibrant, green, palmately-lobed leaves with smooth margins and clean '
                                         'petioles.',
                           'symptoms': [   'Foliage is free of downy mildew oil spots, powdery mildew white patches, '
                                           'or black rot lesions.',
                                           'Vines show strong cane extension and balanced shoot growth.'],
                           'chemical_control': 'No chemical intervention required.',
                           'organic_control': 'Apply foliar seaweed extract (2 mL/L) or humic acid for vigorous vine '
                                              'canopy development.',
                           'prevention': 'Maintain open trellising for optimal airflow, practice balanced drip '
                                         'fertigation, and monitor pest levels.'},
    'Orange___healthy': {   'crop_en': 'Orange / Citrus',
                            'crop_ta': 'ஆரஞ்சு / சிட்ரஸ்',
                            'disease_en': 'Healthy Crop Foliage',
                            'disease_ta': 'ஆரோக்கியமான பயிர்',
                            'is_healthy': True,
                            'pathogen': 'No pathogen detected (ஆரோக்கியமானது)',
                            'field_sign': 'Glossy dark green winged-petiole citrus foliage with smooth flush growth '
                                          'and no chlorosis, cankers, or mottling.',
                            'symptoms': [   'Lush, uniform dark green leaf canopy displaying healthy photosynthetic '
                                            'turgor and balanced vegetative flush.',
                                            'No leaf curling, zinc deficiency chlorosis, greening mottle, canker '
                                            'pustules, or melanose sandpapery texture.'],
                            'chemical_control': 'No chemical intervention required.',
                            'organic_control': 'Foliar micronutrient spray (Zinc Sulphate 0.5% + Ferrous Sulphate 0.5% '
                                               '+ Borax 0.2%) with Panchagavya 3%.',
                            'prevention': 'Maintain optimal ring-basin irrigation avoiding waterlogging around trunk '
                                          'bases; practice regular canopy aeration pruning.'},
    'Paddy___healthy': {   'crop_en': 'Paddy / Rice',
                           'crop_ta': 'நெல்',
                           'disease_en': 'Healthy Crop Foliage',
                           'disease_ta': 'ஆரோக்கியமான பயிர்',
                           'is_healthy': True,
                           'pathogen': 'No pathogen detected (ஆரோக்கியமானது)',
                           'field_sign': 'Upright, deep-green tillers with uniform leaves free from lesions, wilting, '
                                         'or discolorations.',
                           'symptoms': [   'Leaves exhibit uniform chlorophyll pigmentation without necrotic lesions '
                                           'or leaf streaks.',
                                           'Absence of blast spindle spots, bacterial leaf blight white margins, or '
                                           'stem borer dead hearts.'],
                           'chemical_control': 'No chemical intervention required.',
                           'organic_control': 'Apply Azolla biofertilizer (1 t/ha) or spray Panchagavya 3% (30 mL/L) '
                                              'at tillering stage.',
                           'prevention': 'Practice alternate wetting and drying (AWD) irrigation; ensure balanced '
                                         'potassium fertilization; monitor weekly.'},
    'Pepper___healthy': {   'crop_en': 'Pepper / Chilli',
                            'crop_ta': 'மிளகாய் / குடைமிளகாய்',
                            'disease_en': 'Healthy Crop Foliage',
                            'disease_ta': 'ஆரோக்கியமான பயிர்',
                            'is_healthy': True,
                            'pathogen': 'No pathogen detected (ஆரோக்கியமானது)',
                            'field_sign': 'Smooth, glossy, dark green lanceolate leaves with no leaf curl, stippling, '
                                          'or bacterial spots.',
                            'symptoms': [   'Active vegetative apical growth with healthy flower bud emergence.',
                                            'Foliage is free from thrips curl, mite bronze scorching, or bacterial '
                                            'necrotic spotting.'],
                            'chemical_control': 'No chemical intervention required.',
                            'organic_control': 'Foliar spray of vermiwash (5%) or fish amino acid (FAA 3 mL/L) for '
                                               'plant vigour.',
                            'prevention': 'Stake plants against lodging, apply organic mulch around root zones, and '
                                          'maintain clean field borders.'},
    'Potato___healthy': {   'crop_en': 'Potato',
                            'crop_ta': 'உருளைக்கிழங்கு',
                            'disease_en': 'Healthy Crop Foliage',
                            'disease_ta': 'ஆரோக்கியமான பயிர்',
                            'is_healthy': True,
                            'pathogen': 'No pathogen detected (ஆரோக்கியமானது)',
                            'field_sign': 'Compound pinnate dark green foliage with vigorous erect haulm growth and no '
                                          'blight spots.',
                            'symptoms': [   'Leaves show crisp, uniform foliage without target-board rings or '
                                            'water-soaked margins.',
                                            'No signs of late blight downy sporulation or early blight lower-leaf '
                                            'necrosis.'],
                            'chemical_control': 'No chemical intervention required.',
                            'organic_control': 'Soil enrichment with well-rotted farmyard manure and Trichoderma '
                                               'viride enriched compost.',
                            'prevention': 'Ensure good earthing-up to protect tubers, maintain soil aeration, and '
                                          'scout foliage after rains.'},
    'Tomato___healthy': {   'crop_en': 'Tomato',
                            'crop_ta': 'தக்காளி',
                            'disease_en': 'Healthy Crop Foliage',
                            'disease_ta': 'ஆரோக்கியமான பயிர்',
                            'is_healthy': True,
                            'pathogen': 'No pathogen detected (ஆரோக்கியமானது)',
                            'field_sign': 'Rich green serrated leaves with strong aromatic glandular trichomes and '
                                          'clean growing tips.',
                            'symptoms': [   'Foliage demonstrates strong photosynthetic turgor and balanced '
                                            'vegetative-reproductive balance.',
                                            'Absence of yellow leaf curl, early blight rings, bacterial speck, or '
                                            'spider mite webbing.'],
                            'chemical_control': 'No chemical intervention required.',
                            'organic_control': 'Foliar spray of Panchagavya 3% or diluted cow urine (10%) at 15-day '
                                               'intervals.',
                            'prevention': 'Stake plants on bamboo trellises, use drip irrigation to keep leaves dry, '
                                          'and practice crop rotation.'}}

# Backward compatibility alias
TN_DATASET_32_DB = DISEASE_DB


def get_unified_advisory(class_name: str) -> dict:
    """
    Fast O(1) standardized advisory lookup for all 48 unified agricultural classes.
    Deconstructs Crop___Condition into botanical species, pathological diagnosis,
    and returns concise, professional English and Tamil farm treatment protocols.
    """
    norm = class_name.strip()

    # Exact match in DISEASE_DB
    if norm in DISEASE_DB:
        entry = dict(DISEASE_DB[norm])
        entry['class_id'] = norm
        return entry

    # Case-insensitive / format fallback
    norm_lower = norm.lower().replace('___', '_')
    for k, v in DISEASE_DB.items():
        if k.lower().replace('___', '_') == norm_lower:
            entry = dict(v)
            entry['class_id'] = k
            return entry

    # Fallback derivation from class name
    if '___' in norm:
        parts = norm.split('___', 1)
        crop_part = parts[0].replace('_', ' ')
        dis_part = parts[1].replace('_', ' ')
    else:
        crop_part = norm.replace('_', ' ')
        dis_part = 'Healthy'

    is_healthy = 'healthy' in dis_part.lower()

    if is_healthy:
        return {
            'class_id': norm,
            'crop_en': crop_part,
            'crop_ta': crop_part,
            'disease_en': 'Healthy Crop Foliage',
            'disease_ta': 'ஆரோக்கியமான பயிர்',
            'is_healthy': True,
            'pathogen': 'No pathogen detected (Healthy Plant)',
            'field_sign': f'Uniform vibrant green foliage on {crop_part} with no visible lesions or distress.',
            'symptoms': [
                f'Active vigorous growth and clean leaf canopy on {crop_part}.',
                'Absence of fungal mycelium, rust pustules, or bacterial water-soaking.'
            ],
            'chemical_control': 'No chemical intervention required.',
            'organic_control': 'Maintain balanced nutrition with farmyard manure and Panchagavya 3% foliar spray.',
            'prevention': 'Continue standard irrigation scheduling, weekly crop scouting, and field sanitation.'
        }
    else:
        return {
            'class_id': norm,
            'crop_en': crop_part,
            'crop_ta': crop_part,
            'disease_en': dis_part,
            'disease_ta': dis_part,
            'is_healthy': False,
            'pathogen': f'{dis_part} Pathogen',
            'field_sign': f'Visible foliar pathology and discoloration on {crop_part} leaves.',
            'symptoms': [
                f'Localized foliar lesions and tissue necrosis affecting {crop_part} canopy.',
                'Progressive chlorosis or spot expansion observed under field conditions.'
            ],
            'chemical_control': 'Spray standard recommended fungicide/bactericide (e.g., Mancozeb 75 WP @ 2.0 g/L or Copper Oxychloride @ 2.5 g/L).',
            'organic_control': 'Foliar application of Pseudomonas fluorescens @ 10 g/L or 5% Neem Seed Kernel Extract (NSKE).',
            'prevention': 'Remove and safely destroy infected leaf debris; avoid overhead sprinkler wetting; maintain clean field borders.'
        }
