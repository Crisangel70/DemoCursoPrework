from tkinter import END, Label, StringVar, Tk, Entry, Button
from tkinter.ttk import Combobox 

def send_data():

    data_tipo_cpid               = str(tipo_cpid.get())
    data_canal_cpid              = str(canal_cpid.get())
    data_medio_cpid              = str(medio_cpid.get())
    data_canal_mario             = str(canal_mario.get())
    data_group_site_mario        = str(group_site_mario.get())
    data_refering_site_mario     = str(refering_site_mario.get())
    data_campaign_name           = str(campaign_name.get())
    data_source_code             = str(source_code.get())
    data_product_tarjeta         = str(product_tarjeta.get())
    data_childs_mgm              = str(childs_mgm.get())
    data_buy_type_social         = str(buy_type_social.get())
    data_campaign_type_social    = str(campaign_type_social.get())
    data_publisher_social        = str(publisher_social.get())

 

    #Comprobación de captura de datos

    print(
    data_tipo_cpid, "|",
    data_canal_cpid, "|",
    data_medio_cpid, "|",
    data_canal_mario, "|",
    data_group_site_mario, "|",
    data_refering_site_mario, "|",
    data_campaign_name, "|",
    data_source_code, "|",
    data_product_tarjeta, "|",
    data_childs_mgm, "|",
    data_buy_type_social, "|",
    data_campaign_type_social, "|",
    data_publisher_social
    )

 

    #Creando el archivo con la solicitud

    newfile = open("solicitud.txt", "a")
    newfile.write(data_tipo_cpid)
    newfile.write("|")
    newfile.write(data_canal_cpid)
    newfile.write("|")
    newfile.write(data_medio_cpid)
    newfile.write("|")
    newfile.write(data_canal_mario)
    newfile.write("|")
    newfile.write(data_group_site_mario)
    newfile.write("|")
    newfile.write(data_refering_site_mario)
    newfile.write("|")
    newfile.write(data_campaign_name)
    newfile.write("|")
    newfile.write(data_source_code)
    newfile.write("|")
    newfile.write(data_product_tarjeta)
    newfile.write("|")
    newfile.write(data_childs_mgm)
    newfile.write("|")
    newfile.write(data_buy_type_social)
    newfile.write("|")
    newfile.write(data_campaign_name)
    newfile.write("|")
    newfile.write(data_publisher_social)
    newfile.write("\n")

    campo_campaign_name.delete(0,END)
    campo_source_code.delete(0,END)
    campo_childs_mgm.delete(0,END)


    newfile.close()

def selecciona_canal(e):

        if   campo_canal_cpid.get() == "Affiliates":
                campo_medio_cpid.config (values = opciones_affiliates)
        elif campo_canal_cpid.get() == "Brand":
                campo_medio_cpid.config (values = opciones_brand)
        elif campo_canal_cpid.get() == "Direct_Response":
                campo_medio_cpid.config (values = opciones_direct_response)
        elif campo_canal_cpid.get() == "Display":
                campo_medio_cpid.config (values = opciones_display)
        #elif canal_cpid.get() == "Display Google":
        #        medio_cpid.config (values = opciones_display_google)
        elif campo_canal_cpid.get() == "Google":
                campo_medio_cpid.config (values = opciones_google)
        elif campo_canal_cpid.get() == "Home_Page":
                campo_medio_cpid.config (values = opciones_home_page)
        elif campo_canal_cpid.get() == "Landing_Prosa":
                campo_medio_cpid.config (values = opciones_landing_prosa)
        elif campo_canal_cpid.get() == "MGM":
                campo_medio_cpid.config (values = opciones_mgm)
        elif campo_canal_cpid.get() == "Other":
                campo_medio_cpid.config (values = opciones_other)
        elif campo_canal_cpid.get() == "Partner":
                campo_medio_cpid.config (values = opciones_partner)
        elif campo_canal_cpid.get() == "PPC":
                campo_medio_cpid.config (values = opciones_ppc)
        elif campo_canal_cpid.get() == "SEO":
                campo_medio_cpid.config (values = opciones_seo)
        elif campo_canal_cpid.get() == "Social_Media":
                campo_medio_cpid.config (values = opciones_social_media)
        elif campo_canal_cpid.get() == "TMK":
                campo_medio_cpid.config (values = opciones_tmk)
 
def selecciona_canal_mario(f):
        if   campo_canal_mario.get() == "Affiliates":
                campo_group_site_mario.config (values = opciones_group_site_mario_affiliates)
                campo_refering_site_mario.config (values = opciones_referring_site_mario_affiliates)
        elif campo_canal_mario.get() == "Media":
                campo_group_site_mario.config (values = opciones_group_site_mario_media)
                campo_refering_site_mario.config (values = opciones_referring_site_mario_media)
        elif campo_canal_mario.get() == "Partner":
                campo_group_site_mario.config (values = opciones_group_site_mario_partner)
                campo_refering_site_mario.config (values = opciones_referring_site_mario_partner)
        elif campo_canal_mario.get() == "Paid Search":
                campo_group_site_mario.config (values = opciones_group_site_mario_paid_search)
                campo_refering_site_mario.config (values = opciones_referring_site_mario_paid_search)
        elif campo_canal_mario.get() == "MGM":
                campo_group_site_mario.config (values = opciones_group_site_mario_mgm)
                campo_refering_site_mario.config (values = opciones_referring_site_mario_mgm)

root = Tk()

root.title("CAT ADMINTOOL")

tipo_cpid               = StringVar()
canal_cpid              = StringVar()
medio_cpid              = StringVar()
canal_mario             = StringVar()
group_site_mario        = StringVar()
refering_site_mario     = StringVar()
campaign_name           = StringVar()
source_code             = StringVar()
product_tarjeta         = StringVar()
childs_mgm              = StringVar()
buy_type_social         = StringVar()
campaign_type_social    = StringVar()
publisher_social        = StringVar()
 

#Listas
 
opciones_tipo_cpid          = [
    "Lead",
    "eApply"
    ]
opciones_canal_cpid         = [
    "Affiliates",
    "Brand",
    "Direct_Response",
    "Display",
    #Revisar en CAT original este canal y sus medios
    "Display google",
    "Google",
    "Home_Page",
    "Landing_Prosa",
    "MGM",
    "Other",
    "Partner",
    "PPC",
    "SEO",
    "Social_Media",
    "TMK"
    ]
opciones_tarjeta            = [
    "GRCC Gold Elite",
    "GRCC Platinum", 
    "GRCC Básica",
    "GRCC Gold Payback",
    "RCP Green",
    "RCP Gold", 
    "RCP Platinum"
    "RCP Green Aeroméxico",
    "RCP Gold Aeroméxico",
    "RCP Platinum Aeroméxico",
    "All Cards"
    ]
opciones_affiliates         = [
    "AhorraCredit",
    "AskRobin",
    "B12",
    "Bento",
    "BTGroup",
    "Buro de Credito"
    "Club Planeta"
    "Comparabien",
    "Comparaguru",
    "Destacame",
    "El Mejor Trato",
    "Financial Red",
    "FourConexxion",
    "Gnog",
    "Ikiwi",
    "Kardmatch",
    "Kreditiweb",
    "Mercado de Credito",
    "Multicredi",
    "Notonlymedia",
    "Ojo 7",
    "Poolpy",
    "Rankia",
    "Rastreador",
    "Rocket",
    "SolCredito",
    "Tarjetas de Credito",
    "Tudecide"
    ]
opciones_brand              = [
    "American Express",
    "Brand",
    "Campaña Gold Elite",
    "Campaña PlatinumGRCC",
    "Campaña PlatinumRCP",
    "ChatBot",
    "Coverage Invite Media",
    "DBM PMP Mobile",
    "DBM YT Exchange",
    "Google Search",
    "Invite Media",
    "Media",
    "Media AdwordsKeywords",
    "Media DBM",
    "Media DBM PMP",
    "Media DBM RON",
    "Media DBMBlue Kai",
    "Media DBMExchanges",
    "Media DBMYouTube",
    "Media Dynadmic",
    "Media Facebook",
    "Media Foursquare",
    "Media Foursquare Swarm",
    "Media FoursquareSwarm",
    "Media Full Screen",
    "Media Waze",
    "Media Youtube"
    ]
opciones_direct_response    = [
    "Actual Sales",
    "Adfi",
    "Ads Movil",
    "AdSalsa",
    "Aeromexico",
    "Afilio",
    "Amazon",
    "Ampliffica",
    "Antevenio",
    "Antevenio 1",
    "Antevenio 8",
    "Arkeroo",
    "Arkeroo CPA",
    "AT&T",
    "BASE NEXTEL",
    "Bebee",
    "Bid Manager",
    "Bumeran",
    "Cablevision",
    "Canal Mail",
    "catri",
    "Cellmedia",
    "Cerebro",
    "CIE",
    "Clever Click",
    "Click Magic",
    "CMI",
    "CMI CONTENEDOR",
    "CMI PUSH",
    "CMI SMS",
    "CMI/Landing Card Detail",
    "ContactaMas",
    "Darriens",
    "Destacame",
    "Dridco",
    "Eikon",
    "El Financiero",
    "El Universal",
    "Email",
    "Ergo Media",
    "F2F",
    "GLU",
    "GluCompany",
    "GnotMedia",
    "HMG",
    "I24",
    "IMS",
    "Inboxlabs",
    "inmuebles24",
    "Interjet",
    "Krediti",
    "Kwanko",
    "L&L",
    "Latam",
    "latam_Autos",
    "Link Factor",
    "Logan",
    "Mailing",
    "Media",
    "Mediaresponse",
    "Megadirect",
    "Mercado IM",
    "Mercado Libre",
    "Metros Cubicos",
    "Midcorp",
    "Mindshare",
    "MyCa",
    "Naranya",
    "Nextel",
    "Nice Lead",
    "NotOnlyMedia",
    "OCC",
    "Ojo7",
    "onlinepartner",
    "Payback",
    "Pegaso",
    "PML",
    "ProdigyMSN",
    "Prosa",
    "Public Ideas",
    "Publicideas",
    "Quiminet",
    "Reforma",
    "Rocket",
    "Smartclip",
    "SMS",
    "Soicos",
    "Spillover",
    "starafiliado",
    "starafiliado soriana",
    "Starnet",
    "Sun Media",
    "T2O",
    "Taboola",
    "Taboola Reposición",
    "TapTap",
    "Teads",
    "Teads Reposición",
    "Telintel",
    "Thundeer",
    "Time One",
    "Transid",
    "Uber",
    "VeInteractive",
    "VIva Anuncios",
    "Viwom ",
    "Wazo",
    "WOBI",
    "Yahoo"
    ]
opciones_home_page          = [
    "Home Page"
    ]
opciones_landing_prosa      = [
    "Landing PROSA"
    ]
opciones_other              = [
    "Actitud Fem",
    "Adscience",
    "Adsmovil",
    "ADTZ",
    "AEE",
    "Aeromexico",
    "All In Media",
    "Amadeus",
    "American Express",
    "AppSnack",
    "Atraccion 360",
    "Batanga",
    "BBC",
    "Bid Manager",
    "Bits en Imagen",
    "Brand Interjet",
    "C4D",
    "Cadena Tres",
    "Canalmail",
    "Caras",
    "Chilango",
    "CNN Expansion",
    "Conde Nast",
    "Credileads",
    "Criteo",
    "DBM",
    "de10",
    "Despegar",
    "Digilant",
    "Dinero en Imagen",
    "Direct Media",
    "Donde Ir",
    "Dridco",
    "Dtravel Network",
    "E!",
    "Ebay",
    "Editorial Televisa",
    "EIKON",
    "El Comercio Digital",
    "El Universal",
    "Email",
    "Esmas",
    "ESPN",
    "Estrategia 45",
    "Excelsior",
    "Expsansion",
    "Facebook",
    "Forbes",
    "Fox",
    "Full Screen",
    "Gamedots",
    "Garuyo",
    "Get Glue",
    "Gin Media",
    "Glu",
    "Google",
    "GQ",
    "Grupo Formula",
    "Grupo Medios",
    "Headway",
    "Home Page",
    "Hotwords",
    "Hunt",
    "Imagen",
    "IMS",
    "inav",
    "Inbound",
    "Internal",
    "Invent",
    "Kwanko",
    "Latam Autos",
    "Linkedin",
    "Logan",
    "Me Lo Dijo Lola",
    "Media",
    "Media Math",
    "Medio Tiempo",
    "Mens Health",
    "Mercado IM",
    "Mercado Libre",
    "Mindshare",
    "Mobile",
    "Multimedios",
    "MYCA",
    "One Amex",
    "One Tile",
    "Orange Advertising",
    "Outlook",
    "Payback",
    "ProdigyMSN",
    "PROSA",
    "Prosa",
    "Prospect Journey",
    "Quien",
    "Red Mas",
    "Reforma",
    "Reporte",
    "RSV Ponline",
    "Salud 180",
    "Seguros",
    "Skype",
    "Smart Display",
    "Soicos",
    "Sony",
    "Squire",
    "T2O",
    "Teads",
    "Televisa",
    "Terra",
    "Text Link",
    "Trip Advisor",
    "Turn",
    "US Media COnsulting",
    "USMC",
    "Vice",
    "Viva Anuncios",
    "Walmart",
    "Webzodes",
    "Wobi",
    "Xaxis",
    "Yahoo",
    "Yamplus",
    "Ybrand",
    "Amazon"
    ]
opciones_partner            = [
    "Aeromexico",
    "Club Premier",
    "Reforma",
    "Payback",
    "Interjet",
    "Forbes",
    "Medio Tiempo",
    "Revista T&L",
    "CMI ",
    "Kauso",
    "Post organico",
    "XBOX",
    "Excelsior",
    "WOBI",
    "Cabify",
    "CMI",
    "Boombuilders",
    "Rocket",
    "Hilton",
    "Krystal",
    "Samsung Pay"
    ]
opciones_google             = [
    "Aeromexico",
    "American Express",
    "Bing",
    "Bing - Incremental Offer $10k",
    "Bing - Incremental Offer $12k",
    "Bing - Incremental Offer $15k",
    "Brand",
    "Chatbot",
    "Display Google",
    "DV360",
    "GDN",
    "GDN - Discovery ",
    "GDN – Shortform",
    "Gmail",
    "Gmail - ADSS",
    "Google",
    "Interjet",
    "Media",
    "MGM",
    "Mobile",
    "MX Online ACQ Discovery campaigns",
    "MX Online ACQ Display RMK campaigns",
    "MX Online ACQ Gmail campaigns",
    "PPC",
    "PPC - Bing Incremental offer AM Green 10K",
    "PPC - Bing Incremental offer AM Green 4K",
    "PPC - Bing Incremental offer Green RCP 10K",
    "PPC - Bing Incremental offer Green RCP 4K",
    "PPC - Brand",
    "PPC - Brand Incremental Offer ",
    "PPC - Brand Incremental Offer $12k",
    "PPC – Brand Incremental Offer $15k",
    "PPC - Brand Incremental offer AM Green 10K",
    "PPC - Brand Incremental offer AM Green 4K",
    "PPC - Brand Incremental Offer GalleryAds",
    "PPC - Brand Incremental offer Green RCP 10K",
    "PPC - Brand Incremental offer Green RCP 4K",
    "PPC - Brand -Test Junio",
    "PPC - Brand Test Noviembre prequal",
    "PPC - DiPP",
    "PPC - GABM",
    "PPC - Generic",
    "PPC - Product",
    "PPC - Product Gold Elite 10k",
    "PPC - Product Gold Elite 15k",
    "PPC - Product Incremental Offer",
    "PPC - Product Incremental Offer $12K",
    "PPC - Product Incremental Offer 30k",
    "PPC - Product Incremental Offer 50k",
    "PPC - Product Incremental offer AM Green 10K",
    "PPC - Product Incremental offer AM Green 4K",
    "PPC - Product Incremental offer Green RCP 10K",
    "PPC - Product Incremental offer Green RCP 4K",
    "Producto",
    "Remarketing",
    "Search",
    "SEM",
    "Yahoo",
    "Youtube"
    ]
opciones_social_media       = [
    "Brand",
    "Facebook",
    "Facebook eapply",
    "Facebook SA",
    "Forbes",
    "Instagram",
    "Interjet",
    "LALCMList",
    "LALOnlineSignal",
    "Lead",
    "Linkedin",
    "Messenger",
    "Native",
    "Payback",
    "Twitter",
    "Us Media Consulting"
    ]
opciones_tmk                = [
    "SMS Base F",
    "WOBI",
    "PROSA",
    "SEQUENCE",
    "Winback",
    "Base Bconnect",
    "Cancel Miss",
    "Bconnect",
    "Impulse",
    "Base Especial"
    ]
opciones_mgm                = [
    "Amex App",
    "Direct Mail",
    "Email - Cross Supps",
    "Email - DDO",
    "Email - Forgotten MGMers",
    "Email - Inbound Telemarketing",
    "Email - Marketing",
    "Email - Marketing ",
    "Email - Marketing Bonus email",
    "Email - Marketing LTO",
    "Email - Marketing Persado",
    "Email - Outbound Telemarketing PROSA",
    "Email - Servicing",
    "Email - Thank you",
    "Email - Trigger",
    "Facebook",
    "Google",
    "Hub - Alerts",
    "Hub - Banner Aeromexico Site",
    "Hub - Banner Certificado AO",
    "Hub - Banner certificado online generic",
    "Hub - Banner Club Premier Site",
    "Hub - Banner Email",
    "Hub - Banner Email Paperless",
    "Hub - Banner email payment",
    "Hub - Banner email thank you",
    "Hub - Banner MGMer",
    "Hub - Banner MR",
    "Hub - Banner MYCA",
    "Hub - Dashboard Marketing",
    "Hub - Hero Banner",
    "Hub - Hero Banner LTO",
    "Hub - Icon",
    "Hub - iNav",
    "Hub - iNav 2016",
    "Hub - iNav CMS",
    "Hub - iNav MYCA",
    "Hub - iNav OneAmex",
    "Hub - Interstitial",
    "Hub - Log in Log Out",
    "Hub - Offers",
    "Hub - Unreferred Copy Paste",
    "Hub - Unreferred Email",
    "Hub - Unreferred Facebook",
    "Hub - Unreferred others",
    "Hub Alerts",
    "Hub Dashboard Marketing",
    "Hub Interstitial",
    "Hub Log in Log Out",
    "Hub Offers",
    "Influencers",
    "MYCA Widget",
    "OCA",
    "Others",
    "Winback MGM",
    "GDN - Discovery"
    ]
opciones_display            = [
    "Amazon"
    ]
opciones_seo                = [
    "SEO"
    ]
opciones_ppc                = [
    "Bing",
    "Bing - Incremental Offer $10k",
    "Bing - Incremental Offer $12k",
    "Bing - Incremental Offer $15k",
    "Brand",
    "PPC",
    "PPC - Bing Incremental offer AM Green 10K",
    "PPC - Bing Incremental offer AM Green 4K",
    "PPC - Bing Incremental offer Green RCP 10K",
    "PPC - Bing Incremental offer Green RCP 4K",
    "PPC - Brand",
    "PPC - Brand Incremental Offer ",
    "PPC - Brand Incremental Offer $12k",
    "PPC – Brand Incremental Offer $15k",
    "PPC - Brand Incremental offer AM Green 10K",
    "PPC - Brand Incremental offer AM Green 4K",
    "PPC - Brand Incremental Offer GalleryAds",
    "PPC - Brand Incremental offer Green RCP 10K",
    "PPC - Brand Incremental offer Green RCP 4K",
    "PPC - Brand -Test Junio",
    "PPC - Brand Test Noviembre prequal",
    "PPC - DiPP",
    "PPC - GABM",
    "PPC - Generic",
    "PPC - Product",
    "PPC - Product Gold Elite 10k",
    "PPC - Product Gold Elite 15k",
    "PPC - Product Incremental Offer",
    "PPC - Product Incremental Offer $12K",
    "PPC - Product Incremental Offer 30k",
    "PPC - Product Incremental Offer 50k",
    "PPC - Product Incremental offer AM Green 10K",
    "PPC - Product Incremental offer AM Green 4K",
    "PPC - Product Incremental offer Green RCP 10K",
    "PPC - Product Incremental offer Green RCP 4K"
    ]
 
opciones_asignacion         = [
    "Bconnect",
    "Telvista",
    "MegaDirect",
    "Impulse"
    ]

opciones_buy_type           = [
    "Acquisitions Direct Buy",
    "Acquisitions Programmatic Display",
    "Acquisitions Social Media",
    "Brand"
    ]
opciones_campaign_type      = [
    "Both",
    "Prospecting",
    "Retargeting"
    ]
opciones_publisher          = [
    "Antevenio",
    "Cerebro",
    "CMI",
    "Criteo",
    "DoubleClick Bid Manager (BDM)",
    "Eikon Digital",
    "El Financiero",
    "Expansion",
    "Exponential",
    "Facebook",
    "Invite Media",
    "OCC",
    "Other",
    "Outlook",
    "SeedTag",
    "Smartclip",
    "Sojern",
    "Tap Tap Networks",
    "Vice",
    "Yahoo"
    ]

opciones_canales_mario      = [
    "Affiliates",
    "Media",
    "Partner",
    "Paid Search",
    "MGM"
    ]
 
opciones_group_site_mario_affiliates = [
    "UM",
    "Fourconexxion",
    "Amex"
    ]
opciones_group_site_mario_media = [
    "Social - Prospecting",
    "Social - Retargeting",
    "Display Prospecting",
    "Display Retargeting"
    ]
opciones_group_site_mario_partner = [
    "Airline/Frequent Flyer Partner",
    "Travel Partner",
    "Online Retail Partner"
    ]
opciones_group_site_mario_paid_search = [
    "Brand",
    "Cardmembers",
    "Generic",
    "Product",
    "Upper Funnel",
    "GABM",
    "Test & Learn"
    ]
opciones_group_site_mario_mgm = [
    "MGM Pull",
    "Site Links Pull",
    "Amex Owned Placements Pull",
    "MGM Myca Widget Pull",
    "MGM Other Widgets Pull",
    "Amex Push Marketing",
    "Cobrand Partner Push Marketing",
    "CTT Value Gen",
    "Amex Paid Push Marketing",
    "Ad Hoc Push Marketing",
    "Test & Learn"
    ]

opciones_referring_site_mario_affiliates = [
    "AhorraCredit",
    "Bento",
    "Poolpy",
    "Rocket",
    "Destacame",
    "BT Group",
    "Comparabien",
    "Rankia",
    "Solcredito",
    "Askrobin",
    "Notonlymedia",
    "Kreditiweb",
    "Ratreador",
    "Others",
    "Subaff 1",
    "Subaff 2",
    "Subaff 3",
    "Subaff 4",
    "Subaff 5",
    "Subaff 6",
    "Subaff 7",
    "Subaff 8",
    "Subaff 9",
    "Subaff 10",
    "Subaff 11",
    "Subaff 12",
    "Subaff 13",
    "Subaff 14",
    "Subaff 15",
    "Subaff 16",
    "Subaff 17",
    "Subaff 18",
    "Subaff 19",
    "Subaff 20",
    "Comparaguru",
    "Kardmatch"
    ]
opciones_referring_site_mario_media = [
    "Facebook ShortApp Native",
    "Facebook ShortApp LALOnlineSignal",
    "Facebook ShortApp LALCMList",
    "Facebook LeadGen",
    "Facebook Eapply",
    "Other Media",
    "Facebook ShortApp ",
    "Facebook LeadGen",
    "Facebook EApply",
    "Other Media",
    "Gmail Similar To",
    "Gmail Custom Intent",
    "Gmail Affinity",
    "Gmail In market",
    "Discovery Campaigns Custom Intent",
    "Discovery Campaigns Similar To",
    "Discovery Campaigns Affinity",
    "Discovery Campaigns Inmarket",
    "Display Google Similar To",
    "Display Google Custom Intent",
    "Display Google Affinity",
    "Display Google In Market",
    "Programmatic ",
    "Gmail eapply",
    "Gmail shortform",
    "Discovery Campaigns eapply",
    "Discovery Campaigns shortform",
    "Display Google eapply",
    "Display Google shortform",
    "Programmatic eapply",
    "Programmatic shortform"
    ]
opciones_referring_site_mario_partner = [
   "Club Premier",
    "Aeromexico",
    "Payback",
    "Samsung Pay" 
    ]
opciones_referring_site_mario_paid_search = [
    "Other",
    "Sitelinks",
    "Non Acquisition",
    "Acquisition",
    "Branded terms",
    "Non Branded Terms",
    "Test & Learn"
    ]
opciones_referring_site_mario_mgm = [
    "Hub",
    "App",
    "Widget",
    "Direct SRL",
    "Test & Learn"
    ] 

## Creando Widgets

#Etiquetas
etiqueta_tipo_cpid               = Label(root, text="Tipo")
etiqueta_canal_cpid              = Label(root, text="Canal")
etiqueta_medio_cpid              = Label(root, text="Medio")
etiqueta_canal_mario             = Label(root, text="Canal Mario")
etiqueta_group_site_mario        = Label(root, text="Group Site Mario")
etiqueta_refering_site_mario     = Label(root, text="Refering Site Mario")
etiqueta_campaign_name           = Label(root, text="Nombre de Campaña")
etiqueta_source_code             = Label(root, text="Source Code")
etiqueta_product_tarjeta         = Label(root, text="Producto Tarjeta")
etiqueta_childs_mgm              = Label(root, text="Childs MGM")
etiqueta_buy_type_social         = Label(root, text="Buy Type Social Media")
etiqueta_campaign_type_social    = Label(root, text="Campaign Type Social Media")
etiqueta_publisher_social        = Label(root, text="Publisher Social Media")


#Campos y listas

campo_tipo_cpid               = Combobox(root, values = opciones_tipo_cpid, textvariable = tipo_cpid,state = "readonly")  
campo_canal_cpid              = Combobox(root, values = opciones_canal_cpid, textvariable = canal_cpid, state = "readonly")            
campo_canal_cpid.bind("<<ComboboxSelected>>", selecciona_canal)
campo_medio_cpid              = Combobox(root, values = [" "], textvariable = medio_cpid, state = "readonly")

campo_canal_mario             = Combobox(root, values = opciones_canales_mario, textvariable = canal_mario, state = "readonly")
campo_canal_mario.bind("<<ComboboxSelected>>", selecciona_canal_mario)
campo_group_site_mario        = Combobox(root, values = [" "], textvariable = group_site_mario, state = "readonly")
campo_refering_site_mario     = Combobox(root, values = [" "], textvariable = refering_site_mario, state = "readonly")

campo_campaign_name           = Entry   (root, textvariable = campaign_name)
campo_source_code             = Entry   (root, textvariable = source_code)      
campo_product_tarjeta         = Combobox(root, values = opciones_tarjeta, state = "readonly")
campo_childs_mgm              = Entry   (root, textvariable = childs_mgm)
campo_buy_type_social         = Combobox(root, values = opciones_buy_type, textvariable = buy_type_social, state = "readonly")
campo_campaign_type_social    = Combobox(root, values = opciones_campaign_type, textvariable = campaign_type_social, state = "readonly")
campo_publisher_social        = Combobox(root, values = opciones_publisher, textvariable = publisher_social, state = "readonly")
request_Button                = Button(root, text = "Enviar Solicitud de Nuevos CPIDs", background="#26A7FF", command = send_data)


##Colocando widgets

#Etiquetas o nombres de campos
etiqueta_tipo_cpid.grid             (padx = 5, pady = 5, row=1, column=0)
etiqueta_canal_cpid.grid            (padx = 5, pady = 5, row=2, column=0)
etiqueta_medio_cpid.grid            (padx = 5, pady = 5, row=3, column=0)
etiqueta_canal_mario.grid           (padx = 5, pady = 5, row=4, column=0)
etiqueta_group_site_mario.grid      (padx = 5, pady = 5, row=5, column=0)
etiqueta_refering_site_mario.grid   (padx = 5, pady = 5, row=6, column=0)
etiqueta_campaign_name.grid         (padx = 5, pady = 5, row=7, column=0)
etiqueta_source_code.grid           (padx = 5, pady = 5, row=8, column=0)
etiqueta_product_tarjeta.grid       (padx = 5, pady = 5, row=9, column=0)
etiqueta_childs_mgm.grid            (padx = 5, pady = 5, row=10, column=0)
etiqueta_buy_type_social.grid       (padx = 5, pady = 5, row=11, column=0)
etiqueta_campaign_type_social.grid  (padx = 5, pady = 5, row=12, column=0)
etiqueta_publisher_social.grid      (padx = 5, pady = 5, row=13, column=0)
request_Button.grid                 (padx = 5, pady = 5, row=14, columnspan=2)

#Campos a llenar
campo_tipo_cpid.grid              (padx = 5, pady=5, row=1, column=1)
campo_canal_cpid.grid             (padx = 5, pady=5, row=2, column=1)
campo_medio_cpid.grid             (padx = 5, pady=5, row=3, column=1)
campo_canal_mario.grid            (padx = 5, pady=5, row=4, column=1)
campo_group_site_mario.grid       (padx = 5, pady=5, row=5, column=1)
campo_refering_site_mario.grid    (padx = 5, pady=5, row=6, column=1)
campo_campaign_name.grid          (padx = 5, pady=5, row=7, column=1)
campo_source_code.grid            (padx = 5, pady=5, row=8, column=1)
campo_product_tarjeta.grid        (padx = 5, pady=5, row=9, column=1)
campo_childs_mgm.grid             (padx = 5, pady=5, row=10, column=1)
campo_buy_type_social.grid        (padx = 5, pady=5, row=11, column=1)
campo_campaign_type_social.grid   (padx = 5, pady=5, row=12, column=1)
campo_publisher_social.grid       (padx = 5, pady=5, row=13, column=1)


root.mainloop()
