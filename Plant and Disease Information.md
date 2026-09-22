# 🌾 AgroGuard — Botanical Species & Phytosanitary Disease Taxonomy (v1.0.0)

AgroGuard provides a unified vision and diagnostic ecosystem covering **9 Botanical Crop Species** and **48 Unified Crop-Pathology Classes** spanning **51,320 standardized field leaf images**, synthesized with **Tamil Nadu Agricultural University (TNAU) Crop Protection Compendium (CPCPP)** agronomic protocols.

---

## 📊 Dataset Partition Overview

| Dataset Split                       |     Ratio     | Number of Images |    Percentage    |
| :---------------------------------- | :------------: | :--------------: | :---------------: |
| **Training Set (`train/`)** |      80%      | **41,057** |      80.00%      |
| **Validation Set (`val/`)** |      10%      | **5,130** |      10.00%      |
| **Test Set (`test/`)**      |      10%      | **5,133** |      10.00%      |
| **Total Standardized Images** | **100%** | **51,320** | **100.00%** |

---

## 🌿 Botanical Species Matrix (9 Species)

| Botanical Crop            | Tamil Common Name                       | Scientific / Botanical Name               | Key Tamil Nadu Cultivation Zones                           |   Classes   |   Total Images   |
| :------------------------ | :-------------------------------------- | :---------------------------------------- | :--------------------------------------------------------- | :----------: | :--------------: |
| **Apple**           | ஆப்பிள்                          | *Malus domestica*                       | Nilgiris (Coonoor, Ooty), Dindigul (Kodaikanal)            |      4      |      3,164      |
| **Black gram**      | உளுந்து                          | *Vigna mungo*                           | Thanjavur, Tiruvarur, Nagapattinam, Cuddalore, Thoothukudi |      5      |      1,007      |
| **Corn (Maize)**    | மக்காச்சோளம்                | *Zea mays*                              | Perambalur, Ariyalur, Dindigul, Virudhunagar, Tiruppur     |      4      |      3,852      |
| **Grape**           | திராட்சை                        | *Vitis vinifera*                        | Theni (Cumbum Valley), Dindigul (Kodaikanal foothills)     |      4      |      4,062      |
| **Orange (Citrus)** | ஆரஞ்சு / சிட்ரஸ்           | *Citrus sinensis* / *C. aurantifolia* | Dindigul (Sirumalai), Perambalur, Tirunelveli, Tenkasi     |      6      |      6,041      |
| **Paddy (Rice)**    | நெல்                                | *Oryza sativa*                          | Thanjavur, Tiruvarur, Nagapattinam, Cauvery Delta          |      10      |      10,407      |
| **Pepper (Chilli)** | குடைமிளகாய் / மிளகாய் | *Capsicum annuum*                       | Ramanathapuram, Virudhunagar, Sivaganga, Thoothukudi       |      2      |      2,475      |
| **Potato**          | உருளைக்கிழங்கு            | *Solanum tuberosum*                     | Nilgiris (Ooty), Dindigul (Kodaikanal)                     |      3      |      2,152      |
| **Tomato**          | தக்காளி                          | *Solanum lycopersicum*                  | Krishnagiri, Dharmapuri, Dindigul, Salem                   |      10      |      18,160      |
| **Total**           |                                         |                                           | **9 Major Botanical Crops**                          | **48** | **51,320** |

---

## 📈 Exhaustive 48-Class Image Distribution Matrix

| Class Name                                 | Crop                 | Condition / Pathogen          |      Train      |       Val       |      Test      |      Total      |
| :----------------------------------------- | :------------------- | :---------------------------- | :--------------: | :-------------: | :-------------: | :--------------: |
| `Apple___Black_rot`                      | **Apple**      | Black rot                     |       497       |       62       |       62       |  **621**  |
| `Apple___Cedar_apple_rust`               | **Apple**      | Cedar apple rust              |       220       |       28       |       27       |  **275**  |
| `Apple___Healthy`                        | **Apple**      | Healthy                       |      1,310      |       164       |       164       | **1,638** |
| `Apple___Scab`                           | **Apple**      | Scab                          |       504       |       63       |       63       |  **630**  |
| `Black_gram___Anthracnose`               | **Black gram** | Anthracnose                   |       184       |       23       |       23       |  **230**  |
| `Black_gram___Healthy`                   | **Black gram** | Healthy                       |       177       |       22       |       22       |  **221**  |
| `Black_gram___Leaf_crinkle`              | **Black gram** | Leaf crinkle                  |       122       |       15       |       15       |  **152**  |
| `Black_gram___Powdery_mildew`            | **Black gram** | Powdery mildew                |       144       |       18       |       18       |  **180**  |
| `Black_gram___Yellow_mosaic`             | **Black gram** | Yellow mosaic                 |       179       |       22       |       23       |  **224**  |
| `Corn___Cercospora_leaf_spot`            | **Corn**       | Cercospora leaf spot          |       410       |       51       |       52       |  **513**  |
| `Corn___Common_rust`                     | **Corn**       | Common rust                   |       954       |       119       |       119       | **1,192** |
| `Corn___Healthy`                         | **Corn**       | Healthy                       |       930       |       116       |       116       | **1,162** |
| `Corn___Northern_Leaf_Blight`            | **Corn**       | Northern Leaf Blight          |       788       |       98       |       99       |  **985**  |
| `Grape___Black_rot`                      | **Grape**      | Black rot                     |       944       |       118       |       118       | **1,180** |
| `Grape___Esca`                           | **Grape**      | Esca                          |      1,106      |       138       |       139       | **1,383** |
| `Grape___Healthy`                        | **Grape**      | Healthy                       |       338       |       42       |       43       |  **423**  |
| `Grape___Leaf_blight`                    | **Grape**      | Leaf blight                   |       861       |       108       |       107       | **1,076** |
| `Orange___Black_spot`                    | **Orange**     | Black spot                    |       152       |       19       |       19       |  **190**  |
| `Orange___Canker`                        | **Orange**     | Canker                        |       193       |       24       |       24       |  **241**  |
| `Orange___Citrus_greening`               | **Orange**     | Citrus greening               |      4,406      |       551       |       550       | **5,507** |
| `Orange___Healthy`                       | **Orange**     | Healthy                       |        64        |        8        |        8        |   **80**   |
| `Orange___Melanose`                      | **Orange**     | Melanose                      |        10        |        1        |        2        |   **13**   |
| `Orange___Scab`                          | **Orange**     | Scab                          |        8        |        1        |        1        |   **10**   |
| `Paddy___Bacterial_leaf_blight`          | **Paddy**      | Bacterial leaf blight         |       383       |       48       |       48       |  **479**  |
| `Paddy___Bacterial_leaf_streak`          | **Paddy**      | Bacterial leaf streak         |       304       |       38       |       38       |  **380**  |
| `Paddy___Bacterial_panicle_blight`       | **Paddy**      | Bacterial panicle blight      |       270       |       34       |       33       |  **337**  |
| `Paddy___Blast`                          | **Paddy**      | Blast                         |      1,390      |       174       |       174       | **1,738** |
| `Paddy___Brown_spot`                     | **Paddy**      | Brown spot                    |       772       |       96       |       97       |  **965**  |
| `Paddy___Dead_heart`                     | **Paddy**      | Dead heart                    |      1,154      |       144       |       144       | **1,442** |
| `Paddy___Downy_mildew`                   | **Paddy**      | Downy mildew                  |       496       |       62       |       62       |  **620**  |
| `Paddy___Healthy`                        | **Paddy**      | Healthy                       |      1,411      |       176       |       177       | **1,764** |
| `Paddy___Hispa`                          | **Paddy**      | Hispa                         |      1,275      |       159       |       160       | **1,594** |
| `Paddy___Tungro`                         | **Paddy**      | Tungro                        |       870       |       109       |       109       | **1,088** |
| `Pepper___Bacterial_spot`                | **Pepper**     | Bacterial spot                |       798       |       100       |       99       |  **997**  |
| `Pepper___Healthy`                       | **Pepper**     | Healthy                       |      1,182      |       148       |       148       | **1,478** |
| `Potato___Early_blight`                  | **Potato**     | Early blight                  |       800       |       100       |       100       | **1,000** |
| `Potato___Healthy`                       | **Potato**     | Healthy                       |       122       |       15       |       15       |  **152**  |
| `Potato___Late_blight`                   | **Potato**     | Late blight                   |       800       |       100       |       100       | **1,000** |
| `Tomato___Bacterial_spot`                | **Tomato**     | Bacterial spot                |      1,702      |       213       |       212       | **2,127** |
| `Tomato___Early_blight`                  | **Tomato**     | Early blight                  |       800       |       100       |       100       | **1,000** |
| `Tomato___Healthy`                       | **Tomato**     | Healthy                       |      1,273      |       159       |       159       | **1,591** |
| `Tomato___Late_blight`                   | **Tomato**     | Late blight                   |      1,527      |       191       |       191       | **1,909** |
| `Tomato___Leaf_Mold`                     | **Tomato**     | Leaf Mold                     |       762       |       95       |       95       |  **952**  |
| `Tomato___Septoria_leaf_spot`            | **Tomato**     | Septoria leaf spot            |      1,417      |       177       |       177       | **1,771** |
| `Tomato___Spider_mites`                  | **Tomato**     | Spider mites                  |      1,341      |       168       |       167       | **1,676** |
| `Tomato___Target_Spot`                   | **Tomato**     | Target Spot                   |      1,123      |       140       |       141       | **1,404** |
| `Tomato___Tomato_Yellow_Leaf_Curl_Virus` | **Tomato**     | Tomato Yellow Leaf Curl Virus |      4,286      |       536       |       535       | **5,357** |
| `Tomato___Tomato_mosaic_virus`           | **Tomato**     | Tomato mosaic virus           |       298       |       37       |       38       |  **373**  |
| **Total Across All 48 Classes**      | —                   | —                            | **41,057** | **5,130** | **5,133** | **51,320** |

---

## 🔬 Unified 48-Class Pathology & Diagnostic Taxonomy

### 1. Apple (*Malus domestica*) — 4 Classes

- `Apple___Black_rot` — *Botryosphaeria obtusa* (Fungus 🍄)
- `Apple___Cedar_apple_rust` — *Gymnosporangium juniperi-virginianae* (Fungus 🍄)
- `Apple___Healthy` — Vigorous vegetative leaf tissue (No pathogen detected)
- `Apple___Scab` — *Venturia inaequalis* (Fungus 🍄)

### 2. Black gram (*Vigna mungo*) — 5 Classes

- `Black_gram___Anthracnose` — *Colletotrichum lindemuthianum* (Fungus 🍄)
- `Black_gram___Healthy` — Balanced trifoliate foliage (No pathogen detected)
- `Black_gram___Leaf_crinkle` — *Urdbean leaf crinkle virus* (ULCV)
- `Black_gram___Powdery_mildew` — *Erysiphe polygoni* (Fungus 🍄)
- `Black_gram___Yellow_mosaic` — *Mungbean yellow mosaic virus* (MYMV 🦠)

### 3. Corn (*Zea mays*) — 4 Classes

- `Corn___Cercospora_leaf_spot` — *Cercospora zeae-maydis* (Gray leaf spot)
- `Corn___Common_rust` — *Puccinia sorghi* (Fungus 🍄)
- `Corn___Healthy` — Vibrant linear maize foliage (No pathogen detected)
- `Corn___Northern_Leaf_Blight` — *Exserohilum turcicum* (Fungus 🍄)

### 4. Grape (*Vitis vinifera*) — 4 Classes

- `Grape___Black_rot` — *Guignardia bidwellii* (Fungus 🍄)
- `Grape___Esca` — *Phaeomoniella chlamydospora* / *Fomitiporia mediterranea*
- `Grape___Healthy` — High-turgor palmate vine leaves (No pathogen detected)
- `Grape___Leaf_blight` — *Pseudocercospora vitis* (Fungus 🍄)

### 5. Orange (*Citrus sinensis* / *C. aurantifolia*) — 6 Classes

- `Orange___Black_spot` — *Phyllosticta citricarpa* (Fungus 🍄)
- `Orange___Canker` — *Xanthomonas citri subsp. citri* (Bacterium 🦠)
- `Orange___Citrus_greening` — *Candidatus Liberibacter asiaticus* (Bacterium 🦠 via Asian Citrus Psyllid)
- `Orange___Healthy` — Glossy winged-petiole citrus leaves (No pathogen detected)
- `Orange___Melanose` — *Diaporthe citri* (Fungus 🍄)
- `Orange___Scab` — *Elsinoe fawcettii* (Fungus 🍄)

### 6. Paddy (*Oryza sativa*) — 10 Classes

- `Paddy___Bacterial_leaf_blight` — *Xanthomonas oryzae pv. oryzae* (Bacterium 🦠)
- `Paddy___Bacterial_leaf_streak` — *Xanthomonas oryzae pv. oryzicola* (Bacterium 🦠)
- `Paddy___Bacterial_panicle_blight` — *Burkholderia glumae* (Bacterium 🦠)
- `Paddy___Blast` — *Magnaporthe oryzae* / *Pyricularia oryzae* (Fungus 🍄)
- `Paddy___Brown_spot` — *Bipolaris oryzae* (Fungus 🍄)
- `Paddy___Dead_heart` — *Scirpophaga incertulas* (Yellow Stem Borer damage)
- `Paddy___Downy_mildew` — *Sclerophthora macrospora* (Oomycete)
- `Paddy___Healthy` — Clean erect tillering canopy (No pathogen detected)
- `Paddy___Hispa` — *Dicladispa armigera* (Rice Hispa damage)
- `Paddy___Tungro` — *Rice tungro bacilliform virus* (RTBV) + *Rice tungro spherical virus* (RTSV)

### 7. Pepper (*Capsicum annuum*) — 2 Classes

- `Pepper___Bacterial_spot` — *Xanthomonas campestris pv. vesicatoria* (Bacterium 🦠)
- `Pepper___Healthy` — Dark green lanceolate foliage (No pathogen detected)

### 8. Potato (*Solanum tuberosum*) — 3 Classes

- `Potato___Early_blight` — *Alternaria solani* (Fungus 🍄)
- `Potato___Healthy` — Turgid pinnate potato leaves (No pathogen detected)
- `Potato___Late_blight` — *Phytophthora infestans* (Oomycete 🍄)

### 9. Tomato (*Solanum lycopersicum*) — 10 Classes

- `Tomato___Bacterial_spot` — *Xanthomonas campestris pv. vesicatoria* (Bacterium 🦠)
- `Tomato___Early_blight` — *Alternaria solani* (Fungus 🍄)
- `Tomato___Healthy` — Glandular-haired vigorous tomato canopy (No pathogen detected)
- `Tomato___Late_blight` — *Phytophthora infestans* (Oomycete 🍄)
- `Tomato___Leaf_Mold` — *Passalora fulva* (Fungus 🍄)
- `Tomato___Septoria_leaf_spot` — *Septoria lycopersici* (Fungus 🍄)
- `Tomato___Spider_mites` — *Tetranychus urticae* (Two-spotted spider mite)
- `Tomato___Target_Spot` — *Corynespora cassiicola* (Fungus 🍄)
- `Tomato___Tomato_Yellow_Leaf_Curl_Virus` — Tomato yellow leaf curl virus (TYLCV, Whitefly vector)
- `Tomato___Tomato_mosaic_virus` — Tomato mosaic virus (ToMV)
