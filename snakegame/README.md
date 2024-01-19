{\rtf1\ansi\ansicpg1254\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 .SFNS-Regular_wdth_opsz1B0000_GRAD_wght2580000;\f1\fnil\fcharset0 HelveticaNeue;\f2\fnil\fcharset0 .SFNS-Regular_wdth_opsz120000_GRAD_wght2580000;
\f3\fnil\fcharset0 Monaco;\f4\fnil\fcharset0 .SFNS-Regular_wdth_opsz110000_GRAD_wght2580000;\f5\froman\fcharset0 Times-Roman;
}
{\colortbl;\red255\green255\blue255;\red39\green40\blue50;\red0\green0\blue0;\red199\green203\blue211;
}
{\*\expandedcolortbl;;\cssrgb\c20392\c20784\c25490;\cssrgb\c0\c0\c0;\cssrgb\c81961\c83529\c85882;
}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{none\}}{\leveltext\leveltemplateid1\'00;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid1}
{\list\listtemplateid2\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid101\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid2}
{\list\listtemplateid3\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{none\}}{\leveltext\leveltemplateid201\'00;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid3}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}{\listoverride\listid2\listoverridecount0\ls2}{\listoverride\listid3\listoverridecount0\ls3}}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sa480\partightenfactor0

\f0\b\fs54 \cf0 \cb2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec3 Y\uc0\u305 lan Oyunu\
\pard\pardeftab720\sa400\partightenfactor0

\f1\b0\fs32 \cf4 \strokec4 Bu proje, Python programlama dilinde yaz\uc0\u305 lm\u305 \u351  basit bir y\u305 lan oyununu i\'e7ermektedir. Oyunun temel amac\u305 , y\u305 lan\u305 n yemleri yemesini ve engellerden ka\'e7mas\u305 n\u305  sa\u287 lamakt\u305 r.\
\pard\pardeftab720\sa240\partightenfactor0

\f2\b\fs36 \cf0 \strokec3 Nas\uc0\u305 l Oynan\u305 r\
\pard\pardeftab720\sa400\partightenfactor0

\f1\b0\fs32 \cf4 \strokec4 Oyunu oynamak i\'e7in \uc0\u351 u ad\u305 mlar\u305  takip edebilirsiniz:\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf4 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 		\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 Python'u bilgisayar\uc0\u305 n\u305 za kurun. {\field{\*\fldinst{HYPERLINK "https://www.python.org/"}}{\fldrslt Python'un resmi web sitesinden}} indirebilirsiniz.\cb1 \
\ls1\ilvl0\cb2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 		\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 Proje dosyalar\uc0\u305 n\u305  bilgisayar\u305 n\u305 za indirin.\cb1 \
\ls1\ilvl0\cb2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 		\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 Terminal veya komut istemcisinde proje dizinine gidin.\cb1 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0
\f3\fs28 \cf4 \cb2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 		\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 python snake_game.py
\f1\fs32  komutunu kullanarak oyunu ba\uc0\u351 lat\u305 n.\cb1 \
\pard\pardeftab720\sa120\partightenfactor0

\f4\b\fs30 \cf0 \cb2 \strokec3 Kontroller\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls2\ilvl0
\f1\b0\fs32 \cf4 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 Yukar\uc0\u305 : 
\f3\fs28 UP_ARROW
\f1\fs32  veya 
\f3\fs28 W
\f1\fs32 \cb1 \
\ls2\ilvl0\cb2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 A\uc0\u351 a\u287 \u305 : 
\f3\fs28 DOWN_ARROW
\f1\fs32  veya 
\f3\fs28 S
\f1\fs32 \cb1 \
\ls2\ilvl0\cb2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 Sol: 
\f3\fs28 LEFT_ARROW
\f1\fs32  veya 
\f3\fs28 A
\f1\fs32 \cb1 \
\ls2\ilvl0\cb2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 Sa\uc0\u287 : 
\f3\fs28 RIGHT_ARROW
\f1\fs32  veya 
\f3\fs28 D
\f1\fs32 \cb1 \
\ls2\ilvl0\cb2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 Duraklat/Devam Et: 
\f3\fs28 SPACE
\f1\fs32 \cb1 \
\ls2\ilvl0\cb2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 Yeniden Ba\uc0\u351 lat: 
\f3\fs28 ENTER
\f1\fs32 \cb1 \
\pard\pardeftab720\sa240\partightenfactor0

\f2\b\fs36 \cf0 \cb2 \strokec3 Ekran G\'f6r\'fcnt\'fcleri\
\pard\pardeftab720\sa400\partightenfactor0

\f1\b0\fs32 \cf4 \strokec4 \
\pard\pardeftab720\partightenfactor0

\f5\fs24 \cf0 \cb1 \strokec3 \
\pard\pardeftab720\sa240\partightenfactor0
\cf0 \
\pard\pardeftab720\sa240\partightenfactor0

\f2\b\fs36 \cf0 \cb2 Geli\uc0\u351 tirme\
\pard\pardeftab720\sa400\partightenfactor0

\f1\b0\fs32 \cf4 \strokec4 E\uc0\u287 er projeyi geli\u351 tirmek veya katk\u305 da bulunmak istiyorsan\u305 z, a\u351 a\u287 \u305 daki ad\u305 mlar\u305  takip edebilirsiniz:\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls3\ilvl0\cf4 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 		\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 Forklay\uc0\u305 n (sa\u287  \'fcst k\'f6\u351 ede bulunan "Fork" butonuna t\u305 klayarak kendi kopyan\u305 z\u305  olu\u351 turun).\cb1 \
\ls3\ilvl0\cb2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 		\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 Kendi bilgisayar\uc0\u305 n\u305 za projeyi klonlay\u305 n: 
\f3\fs28 git clone https://github.com/kullanici_adiniz/yilan-oyunu.git
\f1\fs32 \cb1 \
\ls3\ilvl0\cb2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 		\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 Yeniden yap\uc0\u305 land\u305 rmalar\u305 n\u305 z\u305  yap\u305 n ve de\u287 i\u351 ikliklerinizi uygulay\u305 n.\cb1 \
\ls3\ilvl0\cb2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 		\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 De\uc0\u287 i\u351 ikliklerinizi commit edin: 
\f3\fs28 git commit -m "Yapt\uc0\u305 \u287 \u305 n\u305 z de\u287 i\u351 ikliklerin a\'e7\u305 klamas\u305 "
\f1\fs32 \cb1 \
\ls3\ilvl0\cb2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 		\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 De\uc0\u287 i\u351 ikliklerinizi kendi forkinizdeki master branch'e pushlay\u305 n: 
\f3\fs28 git push origin master
\f1\fs32 \cb1 \
\ls3\ilvl0\cb2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 		\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 Orjinal depoya (bu depo) bir "Pull Request" g\'f6nderin.\cb1 \
}