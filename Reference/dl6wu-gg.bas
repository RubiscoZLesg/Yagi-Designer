1   '>>>>>>>>>>>>>>>>>>>>>>> DL6WU.BAS <<<<<<<<<<<<<<<<<<<<<<<<<<<<
2   '
3   '  A program to design DL6WU yagis, based on the following references
4   '  by Gunter Hoch, DL6WU -
5   '  "Extremely Long Yagi Antennas", VHF Communications, 3/82
6   '  "Zelf Ontwerpen en Bouwen van VHF en UHF Antennes" (with PA0MS), VERON
7   '
8   '  - supplemented by direct information from DL6WU.
9   '
20  '  Original program by Jerry Haigwood KY4Z and Bob Stein, W6NBI 1983-86
21  '  Modifications by Ian White G3SEK 1986
22  '  Modifications recommended by DL6WU 1988
23  '  Modifications to reflector lengths (longer) 04/1989
24  '  PC version only -                                |
25  '   element spacings from table instead of formula  |
26  '   metric dimension changed to mm instead of cm,   |
27  '   menu selections by single keypress,             | G3SEK 06/89
28  '   screen preview of dimensions                    |
29  '   many line number changes                        |

    ' Line 1250 corrected to show correct               |
    ' electrical boom length in design summary          |
    ' for Yagi's up to 14 elements.                     | GW7KYT 10/2000
    ' Line 1522, reactance formula corrected            |
    ' (-320 missing in original).                       |

    ' Lines 1200-130 corrected correctly!               | G3SEK 09/2003

118 '
119 ' Printer control:
120 PINIT$ = ""               ' Printer-initializing string, default = null.
121 ' PINIT$=                 ' Install new printer-initializing string.
130 FF$ = CHR$(12)            ' Printer form-feed
140 MAXLEN = 60               ' Max lines per page, OK for A4 and 11-inch.
149 '
150 '   **** START ****
151 '
160 KEY OFF: CLS
170 PRINT STRING$(20, "*"); " DL6WU ANTENNA DESIGN PROGRAM "; STRING$(20, "*")
180 DIM S(100), D(100), DH(100), DL(100), T(100): FIRST = 1
190 PRINT : INPUT "Enter today's date           : ", D$: GOSUB 2300
200 PRINT : INPUT "Enter your callsign          : ", S$
205 IF S$ = "" THEN S$ = "G3SEK": PRINT TAB(32); CHR$(30); S$
210 PRINT : INPUT "Enter design frequency (MHz) : ", F
220 IF F <= 0 THEN GOSUB 2080: GOTO 210
230 CLS
238 '
239 ' Choose working dimensions (all internal calculations are in wavelengths)
240 MM = 299793! / F: INCH = 11802.9 / F 'Wavelength factors for mm and inches.
250 PRINT "You can enter all physical dimensions in either:"
260 PRINT : PRINT "      1 - inches"
270 PRINT : PRINT "      2 - millimetres"
280 PRINT : PRINT "or    3 - wavelengths"
290 PRINT : PRINT "Press 1, 2 or 3  > "; : P$ = INPUT$(1)
300 IF P$ <> "1" AND P$ <> "2" AND P$ <> "3" THEN GOSUB 2080: GOTO 290
310 IF P$ = "1" THEN U$ = "inches" ELSE IF P$ = "2" THEN U$ = "millimetres" ELSE U$ = "wavelengths"
315 PRINT U$: FOR I = 1 TO 2000: NEXT
318 '
319 ' Choose gain and estimate boom length, or boom length and estimate gain.
320 CLS
330 PRINT "You can either:"
340 PRINT : PRINT "     1 - Specify forward gain (in dBd) and accept estimated boom length,"
350 PRINT : PRINT "or   2 - Specify boom length and accept estimated gain."
360 PRINT : PRINT "Press 1 or 2  > "; : B$ = INPUT$(1)
370 IF B$ <> "1" AND B$ <> "2" THEN GOSUB 2080: GOTO 360 ELSE PRINT B$
380 IF B$ = "2" GOTO 530
389 ' Choose gain...
390 PRINT
400 PRINT "Forward gain must be between 11.8 dBd and 21.6 dBd"
410 PRINT : INPUT "Enter required gain (dBd) : ", G
419 ' and estimate boom length.
420 IF G < 11.8 OR G > 21.6 THEN PRINT CHR$(7); "GAIN IS OUT OF RANGE - TRY AGAIN!": GOTO 410
430 BL = EXP((G - 9.2) / 3.39)  'Boom wavelengths for specified gain
440 B1 = BL * INCH              'Boom length in in.
450 B2 = BL * MM                'Boom length in mm
460 B3 = B1 / 12                'Boom length in ft
470 PRINT
480 PRINT "Estimated overall boom length = "
490 PRINT USING "   ###.# ft = #### inches = ##### mm = ##.# wavelengths"; B3; B1; B2; BL
500 PRINT
510 PRINT "Is this boom length OK? (Y/n)  > "; : C$ = INPUT$(1)
520 IF C$ <> "N" AND C$ <> "n" GOTO 660 ELSE GOTO 320
529 ' Choose boom length...
530 PRINT
540 PRINT "Overall boom length must be between 2.2 and 39 wavelengths";
550 IF P$ = "3" THEN PRINT "." ELSE PRINT ", ie"
560 IF P$ = "1" THEN PRINT USING "between ###.# and ####.# inches."; 2.2 * INCH; 39 * INCH
570 IF P$ = "2" THEN PRINT USING "between ##### and #####  mm."; 2.2 * MM; 39 * MM
580 PRINT : PRINT "Enter boom length in "; U$; : INPUT " : ", BL
590 A = BL: GOSUB 2000: BL = A       'Convert boom length into wavelengths.
600 IF BL < 2.2 OR BL > 39 THEN GOSUB 2080: GOTO 580
609 ' and estimate gain from chosen boom length.
610 G = 9.2 + 3.39 * LOG(BL)
620 PRINT : PRINT USING "Estimated max. forward gain = ##.# dBd -- it may be less."; G
630 PRINT
640 PRINT "Is this gain OK? (Y/n)  > "; : A$ = INPUT$(1)
650 IF A$ = "N" OR A$ = "n" GOTO 320
658 '
659 ' Options for element mounting and boom diameter.
660 CLS
670 PRINT "You have the following choices for boom material and element mounting method:"
680 PRINT : PRINT "     1 - Metal boom; elements pass through and are BONDED, not insulated"
690 PRINT : PRINT "     2 - Metal boom; elements pass through but are INSULATED"
700 PRINT : PRINT "     3 - A non-metallic boom is used, or"
710 PRINT "                 elements are mounted on insulators above or below the boom,"
720 PRINT "                 with metal-to-metal spacing greater than the boom radius."
730 PRINT : PRINT "WARNING - option 3 means NO CORRECTION for influence of metal boom."
740 PRINT "If in doubt, select option 1 or 2 and you can review your decision later."
750 PRINT : PRINT "Press 1, 2 or 3  > "; : E$ = INPUT$(1)
760 IF E$ <> "1" AND E$ <> "2" AND E$ <> "3" THEN GOSUB 2080: GOTO 750 ELSE PRINT E$
770 IF E$ = "3" THEN BC1 = 0: GOTO 1070  'because boom diameter is irrelevant.
780 PRINT
790 PRINT "Diameter of metal boom must be less than 0.06 wavelengths";
800 IF P$ = "3" THEN PRINT "." ELSE PRINT ", ie": PRINT "less than ";
810 IF P$ = "1" THEN PRINT USING "##.### inches."; .06 * INCH
820 IF P$ = "2" THEN PRINT USING "###.# mm."; .06 * MM
830 PRINT : PRINT "Enter boom diameter (or width of square/rectangular boom) in "; U$
840 INPUT " : ", BD
850 A = BD: GOSUB 2000: BD = A       'Convert boom diameter into wavelengths.
860 IF BD > .06 THEN GOSUB 2080: GOTO 830
869 ' Boom-effect corrections.
870 CLS : PRINT "Your choice of boom material and element mounting method involves a"'  or PRINT CL$
880 PRINT "correction to all the element lengths.": PRINT
890 BC1 = 733 * BD * (.055 - BD) - 504 * BD * (.03 - BD) 'Fits DL6WU data for BD<=0.055
900 PRINT "If the elements pass diametrically through the boom, and are bonded to it,"
910 PRINT USING "the boom correction would be #.### of the boom diameter."; BC1
920 PRINT : IF E$ = "1" GOTO 950 ELSE BC1 = BC1 / 2
930 PRINT "Since you have chosen insulated elements, the boom correction is half of that,"
940 PRINT USING "ie #.### of the boom diameter."; BC1: PRINT
949 ' Option to redo element mounting, or input own boom correction.
950 PRINT "Is this boom correction OK? (Y/n)  > "; : A$ = INPUT$(1)
960 IF A$ <> "N" AND A$ <> "n" GOTO 1070 ELSE PRINT : PRINT "You can either:"
970 PRINT : PRINT "      1 - Enter your own boom correction"
980 PRINT : PRINT "      2 - Go back and choose another element mounting method"
990 PRINT : PRINT "or    3 - Accept the above boom correction after all"
1000 PRINT : PRINT "Press 1, 2 or 3  > "; : BC$ = INPUT$(1)
1010 IF BC$ <> "1" AND BC$ <> "2" AND BC$ <> "3" THEN GOSUB 2080: GOTO 1000
1020 IF BC$ = "3" GOTO 1070
1030 IF BC$ = "2" GOTO 660
1040 PRINT : PRINT "Enter your own boom correction (a fraction of boom diameter between 0 and 1)"
1050 INPUT " : ", BC1
1060 IF BC1 < 0 OR BC1 > 1 THEN GOSUB 2080: GOTO 1040
1070 BC = BC1 * BD
1078 '
1079 ' Choose element diameters.
1080 CLS : PRINT "Element diameter must be between 0.001 and 0.02 wavelengths";
1090 IF P$ = "3" THEN PRINT "." ELSE PRINT ", ie": PRINT "between ";
1100 IF P$ = "1" THEN PRINT USING "#.### and #.### inches."; .001 * INCH; .02 * INCH
1110 IF P$ = "2" THEN PRINT USING "##.# and ##.# mm."; .001 * MM; .02 * MM
1120 PRINT : PRINT "Enter driven element diameter in "; U$; : INPUT " : ", DD
1130 A = DD: D2 = DD: GOSUB 2000: DD = A   'Driven element diameter in wavelengths
1140 IF DD < .001 OR DD > .02 THEN GOSUB 2080: GOTO 1120
1150 PRINT : PRINT "Enter parasitic element diameter in "; U$; : INPUT " : ", ED
1160 A = ED: GOSUB 2000: ED = A    'Parasitic element diameters in wavelengths
1170 IF ED < .001 OR ED > .02 THEN GOSUB 2080: GOTO 1150
1178 '
1179 ' All parameters defined.
1180 M = 0: PRINT : PRINT : PRINT "Computing ..."
1188 '
1189 ' Calculate element spacings.
1190 SR = .2                      'Reflector spacing
1200 LA = BL                      'Available boom length
1209 ' Add directors until no more boom available
1210 FOR N = 1 TO 14              'First 14 directors have variable spacing
1220 READ S(N)                    'Director spacing from previous element
1230 IF N = 1 THEN T(1) = S(1) + SR ELSE T(N) = T(N - 1) + S(N) 'Total length used
1240 LA = LA - S(N)               'Decrement available boom length
1250 IF LA < 0 THEN M = N - 1: GOTO 1330 'Found last director
1260 NEXT N
1270 FOR N = 15 TO 100            'From director 15 on
1280 S(N) = S(14)                 'Constant spacing after director 14
1290 T(N) = T(N - 1) + S(N)       'Total distance from reflector
1300 LA = LA - S(N)               'Decrement available boom length
1310 IF LA < 0 THEN M = N - 1: GOTO 1330 'Found last director
1320 NEXT N
1330 LL = T(M)                    'Actual boom length used
1340 G1 = 9.2 + 3.39 * LOG(LL)    'Re-estimate gain from actual boom length
1350 '
1360 '
1368 '
1369 'Element lengths
1370 RESTORE 2160
1380 FOR Q = 1 TO 7            'Calculate factors for director length equation
1390 READ K, K1, K2, K3, K4    'K = standard element diameter
1400 IF K = ED THEN J = 0: GOTO 1480
1410 IF K < ED THEN L = K ELSE GOTO 1430
1420 KL1 = K1: KL2 = K2: KL3 = K3: KL4 = K4
1430 IF K > ED THEN H = K ELSE GOTO 1460
1440 KH1 = K1: KH2 = K2: KH3 = K3: KH4 = K4
1450 GOTO 1470
1460 NEXT Q
1470 J = (ED - L) / (H - L)    'Interpolation factor
1479 'Director lengths
1480 FOR N = 1 TO M
1490 IF J = 0 THEN D(N) = (K1 - K2 * LOG(N)) * (1 - K3 * EXP(-K4 * N)) ELSE GOSUB 2030
1500 D(N) = D(N) + BC          'Correction for metal booms
1510 NEXT N
1519 ' Reflector length
1520 XR = 20                   'Reflector reactance recommended by DL6WU.
1522 R = (((XR - 40) / (186.8769 * LOG(2 / ED) - 320)) + 1) / 2  'length-reactance formula
1524 R = R + BC                'Reflector length, corrected for metal booms
1529 ' Driven element length
1530 DE = (.4777 - (1.0522 * DD) + (.43363 * (DD ^ -.014891))) / 2
1539 ' Driven element length modified by DL6WU 1988 -
1540 DE = 1.02 * DE            ' 2% longer, for better match to folded dipole.
1546 '
1547 ' End of calculations.
1548 '
1549 ' Display and printing options.
1550 OPEN "SCRN:" FOR OUTPUT AS #1: GOSUB 2500: CLOSE #1  'Performance summary
1560 LOCATE 25, 7: PRINT "Preview dimensions?  (Y/n)  > "; : A$ = INPUT$(1)
1570 IF A$ <> "N" AND A$ <> "n" GOTO 1640 ELSE GOTO 1650
1580 CLS : PRINT "Run the program again for the same user? (Y/n)  > "; : R$ = INPUT$(1)
1590 IF R$ <> "N" AND R$ <> "n" THEN RESTORE: CLS : GOTO 210
1600 PRINT "New user? (Y/n)  > "; : R$ = INPUT$(1)
1610 IF R$ <> "N" AND R$ <> "n" THEN RESTORE: CLS : GOTO 200
1605 SYSTEM
1620 'PRINT "Exit to DOS? (Y/n)  > "; : R$ = INPUT$(1)
1630 'IF R$ <> "N" AND R$ <> "n" THEN SYSTEM ELSE END
1640 GOSUB 3000
1650 LOCATE 25, 7: PRINT "Print summary and dimensions?  (Y/n)  > "; : R$ = INPUT$(1)
1660 IF R$ = "N" OR R$ = "n" GOTO 1580
1670 CLS
1680 IF FIRST = 1 THEN PRINT : PRINT TAB(22); "--> TURN ON THE PRINTER, PLEASE <--": LPRINT PINIT$; : FIRST = 0
1690 CLS
1700 PRINT : PRINT "        --> PREPARE THE PRINTER, WITH PAPER SET TO TOP OF PAGE <--"
1710 PRINT : INPUT "      Press Enter when printer is ready : ", Z$
1720 LPRINT : LPRINT : LPRINT
1730 LPRINT TAB(34); "DL6WU ANTENNA DESIGN"
1740 LPRINT
1750 LPRINT "      Program written by Jerry Haigwood KY4Z, Bob Stein W6NBI & Ian White G3SEK"
1760 LPRINT TAB(16); "based on articles and design data by Gu"; CHR$(8); CHR$(34); "nter Hoch, DL6WU"
1770 LPRINT : LPRINT TAB(26); "DESIGNED FOR :-   "; S$; TAB(56); D$
1780 LPRINT
1790 OPEN "LPT1:" FOR OUTPUT AS #1
1800 GOSUB 2500                          ' LPRINT summary
1810 CLOSE #1
1820 LPRINT FF$
1830 GOSUB 3500                          ' LPRINT dimensions
1840 GOTO 1580
1997 '
1998 '  **** SUBROUTINES AND DATA ****
1999 '
2000 IF P$ = "1" THEN A = A / INCH      'Convert in. to wavelength
2010 IF P$ = "2" THEN A = A / MM        'Convert mm to wavelength
2020 RETURN
2030 'Interpolate for D(N)
2040 DL(N) = (KL1 - KL2 * LOG(N)) * (1 - KL3 * EXP(-KL4 * N))
2050 DH(N) = (KH1 - KH2 * LOG(N)) * (1 - KH3 * EXP(-KH4 * N))
2060 D(N) = DL(N) + J * (DH(N) - DL(N))
2070 RETURN
2080 PRINT CHR$(7); "Value of of range - try again!"
2090 RETURN
2097 '
2098 ' Data
2099 '
2100 ' Spacings for first 14 directors
2110 DATA 0.075, 0.180, 0.215, 0.250, 0.280, 0.300, 0.315
2120 DATA 0.330, 0.345, 0.360, 0.375, 0.390, 0.400, 0.400
2130 ' All spacings beyond D13 are equal to last entry ^
2139 '
2140 'First number in each data line is element diameter.
2150 'Next 4 numbers are K1-K4, used to determine element lengths.
2160 DATA .001,.4711,.018,.08398,.965
2170 DATA .003,.462,.01941,.08543,.9697
2180 DATA .005,.4538,.02117,.0951,1.007
2190 DATA .007,.4491,.02274,.08801,.9004
2200 DATA .01,.4421,.02396,.1027,1.038
2210 DATA .015,.4358,.02558,.1149,1.034
2220 DATA .02,.4268,.02614,.1112,1.036
2298 '
2299 ' Convert date to dd-mon-yr format
2300 IF D$ = "" THEN D$ = DATE$
2310 MONTH% = VAL(LEFT$(DATE$, 2)): MONTH% = MONTH% * 3 - 2
2320 DAY$ = MID$(DATE$, 4, 2)
2330 YEAR$ = RIGHT$(DATE$, 4)
2340 IF YEAR$ < "1989" THEN D$ = "": RETURN
2350 MONTH$ = MID$("JanFebMarAprMayJunJulAugSepOctNovDec", MONTH%, 3)
2360 D$ = DAY$ + " " + MONTH$ + " " + YEAR$
2370 PRINT TAB(32); CHR$(30); D$
2380 RETURN
2497 '
2498 '  **** SUBROUTINE TO DISPLAY/PRINT SUMMARY DATA ****
2499 '
2500 CLS
2510 PRINT #1, "      --------------------- DL6WU-YAGI DESIGN SUMMARY ";
2520 PRINT #1, "----------------------": PRINT #1,
2530 PRINT #1, USING "            Design frequency = ####.### MHz"; F
2540 PRINT #1, "          Number of elements ="; M + 2
2550 IF E$ <> "3" THEN PRINT #1, USING "      Boom diameter = ###.## mm = ##.### inches = #.### wavelengths"; BD * MM; BD * INCH; BD
2560 PRINT #1, "      Element diameters:"
2570 PRINT #1, USING "              Driven element = ##.## mm = ##.#### inches = #.### wavelengths"; DD * MM; DD * INCH; DD
2580 PRINT #1, USING "          Parasitic elements = ##.## mm = ##.#### inches = #.### wavelengths"; ED * MM; ED * INCH; ED
2590 PRINT #1, USING "      Electrical boom length = ##### mm = ####.# inches  = ##.## wavelengths"; LL * MM; LL * INCH; LL
2600 PRINT #1, "                            (allow for overhang when cutting boom to length)"
2610 PRINT #1, "      Estimated performance:"
2620 PRINT #1, USING "                        Gain = ##.# dBd"; G1
2630 BH = 30 - 3.14 * (G1 - 14)  'Correlation from published patterns of DL6WU yagis
2640 PRINT #1, USING "        Horizontal beamwidth = ##.# deg"; BH
2650 BV = BH / COS(BH / (2 * 57))  'Over-estimates BV for shorter yagis
2660 PRINT #1, USING "          Vertical beamwidth = ##.# deg"; BV
2670 SH = 51 / BH
2680 PRINT #1, "      Suggested stacking distances for 2 yagis:"
2690 PRINT #1, USING "                  Horizontal = #### mm = ###.# inches = #.## wavelengths"; SH * MM; SH * INCH; SH
2700 SV = 51 / BV
2710 PRINT #1, USING "                    Vertical = #### mm = ###.# inches = #.## wavelengths"; SV * MM; SV * INCH; SV
2720 PRINT #1, : IF BC$ = "1" THEN PRINT #1, "      You have chosen your own element-mounting method or boom correction,": GOTO 2770
2730 IF E$ = "3" THEN PRINT #1, "      Elements are INSULATED FROM the metal boom, or the boom material is "
2740 IF E$ = "3" THEN PRINT #1, "      nonconducting. NO BOOM-EFFECT CORRECTION HAS BEEN APPLIED."
2750 IF E$ = "1" THEN PRINT #1, "      Elements are SECURELY CONNECTED to the metal boom,"
2760 IF E$ = "2" THEN PRINT #1, "      Elements are INSULATED THROUGH the metal boom,"
2770 IF E$ <> "3" THEN PRINT #1, USING "      and a boom-effect correction of #.## of the boom diameter has been applied."; BC1
2780 PRINT #1,
2790 DIMTOL = .003
2800 PRINT #1, "      Dimensional tolerance required for element lengths:"
2810 PRINT #1, USING "                +/- ##.## mm = #.### inches = #.### wavelengths"; DIMTOL * MM; DIMTOL * INCH; DIMTOL
2820 PRINT #1,
2830 RETURN
2997 '
2998 '  **** SUBROUTINE TO DISPLAY DIMENSIONS TO SCREEN ****
2999 '
3000 CLS
3010 PRINT TAB(12); "CUMULATIVE"; TAB(65); "ELEMENT"
3020 PRINT TAB(13); "SPACING"; TAB(65); "LENGTH"
3030 PRINT TAB(10); "-------------"; TAB(61); "--------------"
3040 PRINT TAB(12); "mm"; TAB(19); "inches"; TAB(62); "mm"; TAB(70); "inches"
3050 PRINT
3060 PRINT TAB(11); "Zero";
3070 PRINT TAB(20); "Zero";
3080 PRINT TAB(29); USING "REFL ----------|----------   #####.##   "; R * MM;
3090 PRINT TAB(69); USING "###.###"; R * INCH
3100 PRINT TAB(44); "|"
3110 PRINT TAB(8); USING "#####.#"; SR * MM;
3120 PRINT TAB(19); USING "##.###"; SR * INCH;
3130 PRINT TAB(29); USING "D.E.  =========|=========    #####.##   "; DE * MM;
3140 PRINT TAB(69); USING "###.###"; DE * INCH
3150 NLINE = 11: FOR N = 1 TO M
3160 PRINT TAB(44); "|"
3170 PRINT TAB(8); USING "#####.#"; T(N) * MM;
3180 PRINT TAB(18); USING "###.###"; T(N) * INCH;
3190 PRINT TAB(29);
3200 IF N <= 9 THEN PRINT USING "D" + STR$(N) + "    --------|--------     #####.##   "; D(N) * MM;
3210 IF N > 9 THEN PRINT USING "D" + STR$(N) + "   --------|--------     #####.##   "; D(N) * MM;
3220 PRINT TAB(69); USING "###.###"; D(N) * INCH
3230 NLINE = NLINE + 2
3240 IF NLINE > 24 THEN LOCATE 25, 7: PRINT "Press Enter > "; : T$ = INPUT$(1): CLS : NLINE = 1
3250 NEXT N
3260 RETURN
3450 '
3460 '  **** SUBROUTINE TO LPRINT DIMENSIONS ****
3470 '
3497 '
3500 LPRINT : LPRINT : LPRINT
3510 LPRINT TAB(12); "CUMULATIVE"; TAB(64); "ELEMENT"
3520 LPRINT TAB(13); "SPACING"; TAB(64); "LENGTH"
3530 LPRINT TAB(10); "-------------"; TAB(61); "--------------"
3540 LPRINT TAB(12); "mm"; TAB(19); "inches"; TAB(61); "mm"; TAB(70); "inches"
3550 LPRINT
3560 LPRINT TAB(11); "Zero";
3570 LPRINT TAB(20); "Zero";
3580 LPRINT TAB(29); USING "REFL ----------|----------   ####.##    "; R * MM;
3590 LPRINT TAB(69); USING "###.###"; R * INCH
3600 LPRINT TAB(44); "|"
3610 LPRINT TAB(8); USING "#####.#"; SR * MM;
3620 LPRINT TAB(18); USING "###.###"; SR * INCH;
3630 LPRINT TAB(29); USING "D.E.  =========|=========    ####.##    "; DE * MM;
3640 LPRINT TAB(69); USING "###.###"; DE * INCH: NLINE = 11
3650 FOR N = 1 TO M
3660 LPRINT TAB(44); "|"
3670 LPRINT TAB(8); USING "#####.#"; T(N) * MM;
3680 LPRINT TAB(18); USING "###.###"; T(N) * INCH;
3690 LPRINT TAB(29);
3700 IF N <= 9 THEN LPRINT USING "D" + STR$(N) + "    --------|--------     ####.##    "; D(N) * MM;
3710 IF N > 9 THEN LPRINT USING "D" + STR$(N) + "   --------|--------     ####.##    "; D(N) * MM;
3720 LPRINT TAB(69); USING "###.###"; D(N) * INCH
3730 NLINE = NLINE + 2
3740 IF NLINE > MAXLEN THEN LPRINT FF$; : LPRINT : LPRINT : LPRINT : NLINE = 4
3750 NEXT N
3760 LPRINT FF$;
3770 PRINT : PRINT STRING$(69, "*"): PRINT
3780 RETURN

