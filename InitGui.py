# -*- coding: utf-8 -*-
# FreeCAD init script of the Wood Frame module
# (c) 2019 Jerome Laverroux

#***************************************************************************
#*   (c) Jerome Laverroux (jerome.laverroux@free.fr) 2019                  *
#*                                                                         *
#*   This file is part of the FreeCAD CAx development system.              *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   FreeCAD is distributed in the hope that it will be useful,            *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Lesser General Public License for more details.                   *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with FreeCAD; if not, write to the Free Software        *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#*   Jerome Laverroux 2019                                                 *
#***************************************************************************/

import FreeCAD


class WFrame ( Workbench ):
    MenuText = "Wood Frame"
    ToolTip = "Wood Frame tools"
    Icon = """
    /* XPM */
static char *ferme[] = {
/* columns rows colors chars-per-pixel */
"228 63 72 1 ",
"  c #2F2C2A",
". c #332D27",
"X c #3C3127",
"o c #37322F",
"O c #3C342C",
"+ c #363534",
"@ c #3B3532",
"# c #3D3936",
"$ c #3D3C3A",
"% c #44362A",
"& c #4C3B2D",
"* c #533E2D",
"= c #433C36",
"- c #493F35",
"; c #433E3A",
": c #483F38",
"> c #53402F",
", c #4D4036",
"< c #47423E",
"1 c #4C423A",
"2 c #534235",
"3 c #5A4534",
"4 c #5C4937",
"5 c #52453A",
"6 c #594739",
"7 c #55483C",
"8 c #5C4A3B",
"9 c #614732",
"0 c #654A34",
"q c #634D3A",
"w c #694F39",
"e c #65513E",
"r c #6D523C",
"t c #73553B",
"y c #78563B",
"u c #77583E",
"i c #7C5A3D",
"p c #454341",
"a c #4B4642",
"s c #4E4A46",
"d c #4D4C4A",
"f c #544B44",
"g c #5B4E43",
"h c #524D4A",
"j c #54514F",
"k c #545352",
"l c #595756",
"z c #585856",
"x c #5C5C5B",
"c c #605042",
"v c #695240",
"b c #60605E",
"n c #646464",
"m c #825D3F",
"M c #835E40",
"N c #866040",
"B c #8D6442",
"V c #916743",
"C c #956A45",
"Z c #996C46",
"A c #9D6E48",
"S c #9F7048",
"D c #A4734A",
"F c #A9764C",
"G c #AD794E",
"H c #B17C4F",
"J c #B57E50",
"K c #B78051",
"L c #BC8353",
"P c #C28655",
"I c #C48856",
"U c None",
/* pixels */
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU9ZAZiUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUuIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU1yIIIZ=dUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU<wCKyIIIZZAwhUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU#4BLPILyIIIZZIILVehUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU<8NHIIIIILyIIIZZIIIIIJN4$UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU$5tGIIIIIIIILyIIIZZIIIIIIIPLig$UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU,tDPIIIIIIIIIILyIIIZAIIIIIIIIPIIFy7zUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU:rALIIIIIIIIIIIPZ0yIIIZ2CLIIIIIIIIIIIPAt:UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU=8CLPIIIIIIIIIIPDrfzUyIIIZUU:rALIIIIIIIIIIIPCqhUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU@8NLIIIIIIIIIIIPFygpUUUUyIIIZUUUUU,yDPIIIIIIIIIIILBqaUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU;8vJIIIIIIIIIIIPJMgdUUUUUUUyIIIZUUUUUUU$,yHIIIIIIIIIIIPJM8$UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU#,tHIIIIIIIIIIIIJBgdUUUUUUUUUUyIIIZUUUUUUUUUU#8MJIIIIIIIIIIIIJygkUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU1tDPIIIIIIIIIIILVw:UUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUoqBLIIIPIIIIIPIPDt7dUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU=wCLIPIIIIIIIIIPAwfbUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUU:qAPPIIIIIIIIIILDrsUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU=8BLIPIIIIIIIIIIDtfpUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUU:tDLIIIIIIIIIIPPCqhUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUp8NJIIIIIIIIIIIIGi5dUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUU-iFIIIIIIIIIIIIJN8pUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU#5iGPIPIIIIIIIIPLNckUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUU$2iJIIIIIIIIIIIPJigpUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU-tDIIIIIIIIIIIIKBqsUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUU=8NLPIIIIIIIIIPIGtflUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU1rALIIIIIIIIIIILCwfUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU@0CLIIIIIIIIIIIPSr:UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU=8VLPIIIIIIIIIIPDrfxUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU<wAPPIIIIIIIIIILZwhUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU@qMLIIIIIIIIIIIPFifpUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU1yFPIIIIIIIIIIILBeaUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUp7mGIIIIIIIIIIIIJighUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU$,yHIIIIIIIIIIIIJm8;UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU$,tGIIIIIIIIIIIILN8kUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU$6mLPIIIIIIIIIIPJvckUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU5rDPIIIIIIIIIPILVr:UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUoqBLPIIIIIIIIIIPDt1kUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU:wCLIIIIIIIIIIIPArfnUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU=wZLIIIIIIIIIIPPAv:UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU#8BLPIIIIIIIIIPPFyhUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU1rDPIIIIIIIIIIILC0hUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUaqNJIIIIIIIIIPIPGi5dUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU2iFPIIIIIIIIIPIJN81UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU$5vHIIIIIIIIIIIILMchUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU=5iHIIIIIIIIIIIIHi8dUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU-tDIIIIIIIIIIIILB8hUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUp8BJIIIIIIIIIIIPGtflUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUU5rAPIIIIIIIIIIILCrfUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU@0CLIIIIIIIIIIIPAr1UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUU#qVLIPIIIIIIIIIIDrhxUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU:qDIIIIIIIIIIIIPZrsUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUU#8NLPIIIIIIIIIIPFu5$UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU1yDLIPIIIIIIIIILBqsUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUp8iGIIIIIIIIIIIIHigsUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU$2iJPIIIIIIIIIIIJmg#UUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUU@-yFPIIIIIIIIIIILNcjUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU=7mLPIIIIIIIIIIPHigkUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUfrDPIIIIIIIIIIILBr#UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUpqBLIIIIIIIIIIPIFr5lUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUU:wCLIIIIIIIIIIIPSrfUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU=0CPIIPIIIIIIIIPZraUUUUUUUUUUUUUUUU",
"UUUUUUUUUU#6VLPIIIIIIIIIIIDtglUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU1wDPIIIIIIIIIIPLCwdUUUUUUUUUUUUU",
"UUUUUUU@8NLPIIIIIIIIIIPGi5sUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU-iFPIIPIIIIIPIILN81UUUUUUUUUU",
"UUUU; 2MAAAAAAAAAAAAAi-;dUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUyIIIZUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU+%iZAAAAAAAAAAAAN3@dUUUUUUU",
"UUUUOVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVByIIIZtVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVXUUUUUUU",
"UUUU&IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIILyIIIZZIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII&UUUUUUU",
"UUUU&IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIILyIIIZAIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII&UUUUUUU",
"UUUU-IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIILyIIIZZIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII&UUUUUUU",
"UUUU&IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIILyIIIZZIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII&UUUUUUU",
"UUUU.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000009%000**00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000=UUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU",
"UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
};

    """



    def Initialize(self):
        """This function is executed when FreeCAD starts"""
        '''
        disabling numpad shortcuts
        to use for positionning and quick launch
        '''
        preset = [
            ("Std_ViewAxo"   , "CTRL+0"),
            ("Std_ViewFront" , "CTRL+1"),
            ("Std_ViewTop"   , "CTRL+2"),
            ("Std_ViewRight" , "CTRL+3"),
            ("Std_ViewRear"  , "CTRL+4"),
            ("Std_ViewBottom", "CTRL+5"),
            ("Std_ViewLeft"  , "CTRL+6"),
        ]
        for (cmd, shortcut) in preset:
            FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Shortcut").SetString(cmd, shortcut)
        def QT_TRANSLATE_NOOP(scope, text):
            return text

        try:
            import os,Draft_rc,DraftTools, DraftGui,Arch,Arch_rc,WFrame
            from DraftTools import translate
            FreeCADGui.addLanguagePath(":/translations")
            FreeCADGui.addIconPath(":/icons")
        except Exception as inst:
            print(inst)
            FreeCAD.Console.PrintError("Error: Initializing one or more of the Draft modules failed, Draft will not work as expected.\n")
            
        
 
        
        
        self.wframe = ["WFrameAlignViewWPlane","WFrameBeam","Arch_CutPlane","Arch_MaterialTools","WFrameList"] # A list of command names created in the line above
        self.appendToolbar("Wood Frame",self.wframe) # creates a new toolbar with your commands
        self.appendMenu("Wood Frame",self.wframe) # creates a new menu
       # self.appendMenu(["An existing Menu","My submenu"],self.list) # appends a submenu to an existing menu
       
       #add draft toolbar
        self.drafttools = ["Draft_Line","Draft_Wire","Draft_Circle","Draft_Arc","Draft_Arc_3Points","Draft_Ellipse",
                        "Draft_Polygon","Draft_Rectangle", "Draft_Text",
                        "Draft_Dimension", "Draft_BSpline","Draft_Point",
                        "Draft_ShapeString","Draft_Facebinder","Draft_BezierTools","Draft_Label"]
        self.draftmodtools = ["Draft_Move","Draft_Rotate","Draft_Offset",
                        "Draft_Trimex", "Draft_Join", "Draft_Split", "Draft_Upgrade", "Draft_Downgrade", "Draft_Scale",
                        "Draft_Edit","Draft_WireToBSpline","Draft_AddPoint",
                        "Draft_DelPoint","Draft_Shape2DView","Draft_Draft2Sketch","Draft_Array",
                        "Draft_PathArray", "Draft_PointArray","Draft_Clone",
                        "Draft_Drawing","Draft_Mirror","Draft_Stretch"]
        self.draftextratools = ["Draft_WireToBSpline","Draft_AddPoint","Draft_DelPoint","Draft_ShapeString",
                                "Draft_PathArray","Draft_Mirror","Draft_Stretch"]
        self.draftcontexttools = ["Draft_ApplyStyle","Draft_ToggleDisplayMode","Draft_AddToGroup","Draft_AutoGroup",
                            "Draft_SelectGroup","Draft_SelectPlane",
                            "Draft_ShowSnapBar","Draft_ToggleGrid","Draft_UndoLine",
                            "Draft_FinishLine","Draft_CloseLine"]
        self.utils = ["Draft_VisGroup","Draft_Heal","Draft_FlipDimension",
                      "Draft_ToggleConstructionMode","Draft_ToggleContinueMode","Draft_Edit",
                      "Draft_Slope","Draft_SetWorkingPlaneProxy","Draft_AddConstruction"]
        self.snapList = ['Draft_Snap_Lock','Draft_Snap_Midpoint','Draft_Snap_Perpendicular',
                         'Draft_Snap_Grid','Draft_Snap_Intersection','Draft_Snap_Parallel',
                         'Draft_Snap_Endpoint','Draft_Snap_Angle','Draft_Snap_Center',
                         'Draft_Snap_Extension','Draft_Snap_Near','Draft_Snap_Ortho','Draft_Snap_Special',
                         'Draft_Snap_Dimensions','Draft_Snap_WorkingPlane']
        self.appendToolbar(QT_TRANSLATE_NOOP("Workbench","Draft creation tools"),self.drafttools)
        self.appendToolbar(QT_TRANSLATE_NOOP("Workbench","Draft modification tools"),self.draftmodtools)
       # self.appendToolbar(QT_TRANSLATE_NOOP("Workbench","Draft mod tools"),self.draftextratools)
        self.appendMenu(QT_TRANSLATE_NOOP("draft","&Draft"),self.drafttools+self.draftmodtools)
        self.appendMenu([QT_TRANSLATE_NOOP("draft","&Draft"),QT_TRANSLATE_NOOP("Workbench","Utilities")],self.utils+self.draftcontexttools)
        self.appendMenu([QT_TRANSLATE_NOOP("draft","&Draft"),QT_TRANSLATE_NOOP("Workbench","Snapping")],self.snapList)
        
        if hasattr(FreeCADGui,"draftToolBar"):
            if not hasattr(FreeCADGui.draftToolBar,"loadedArchPreferences"):
                FreeCADGui.addPreferencePage(":/ui/preferences-arch.ui","Arch")
                FreeCADGui.addPreferencePage(":/ui/preferences-archdefaults.ui","Arch")
                FreeCADGui.draftToolBar.loadedArchPreferences = True
            if not hasattr(FreeCADGui.draftToolBar,"loadedPreferences"):
                FreeCADGui.addPreferencePage(":/ui/preferences-draft.ui","Draft")
                FreeCADGui.addPreferencePage(":/ui/preferences-draftsnap.ui","Draft")
                FreeCADGui.addPreferencePage(":/ui/preferences-draftvisual.ui","Draft")
                FreeCADGui.addPreferencePage(":/ui/preferences-drafttexts.ui","Draft")
                FreeCADGui.draftToolBar.loadedPreferences = True
        Log ('Loading Draft module...done\n')
            
       
    
    def Activated(self):
        if hasattr(FreeCADGui,"draftToolBar"):
            FreeCADGui.draftToolBar.Activated()
        if hasattr(FreeCADGui,"Wood Frame"):
            FreeCADGui.draftToolBar.Activated()
        if hasattr(FreeCADGui,"Snapper"):
            FreeCADGui.Snapper.show()
        Log("Wood Frame workbench Activated\n")
        """This function is executed when the workbench is activated"""
        return
    def Deactivated(self):
        if hasattr(FreeCADGui,"draftToolBar"):
            FreeCADGui.draftToolBar.Deactivated()
        if hasattr(FreeCADGui,"Wood Frame"):
            FreeCADGui.draftToolBar.Deactivated()
        if hasattr(FreeCADGui,"Snapper"):
            FreeCADGui.Snapper.hide()
        Log("Wood Frame workbench deactivated\n")
        """This function is executed when the workbench is deactivated"""
        return
    
    def ContextMenu(self, recipient):
        """This is executed whenever the user right-clicks on screen"""
        # "recipient" will be either "view" or "tree"
        self.appendContextMenu("Utilities",self.draftcontexttools)
        self.appendContextMenu("Wood Frame",self.list) # add commands to the context menu

    def GetClassName(self): 
        # this function is mandatory if this is a full python workbench
        return "Gui::PythonWorkbench"
Gui.addWorkbench(WFrame())

# add import/export types
#FreeCAD.addImportType("Wood Working Machine (*.btl)","importBTL")
#FreeCAD.addExportType("Wood Working Machine (*.btl)","exportBTL")




