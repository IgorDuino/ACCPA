# Generated from stellaParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,88,708,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,1,1,1,1,1,
        1,2,1,2,1,2,1,3,1,3,5,3,48,8,3,10,3,12,3,51,9,3,1,3,5,3,54,8,3,10,
        3,12,3,57,9,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,5,5,68,8,5,10,
        5,12,5,71,9,5,1,5,1,5,1,6,5,6,76,8,6,10,6,12,6,79,9,6,1,6,1,6,1,
        6,1,6,1,6,1,6,5,6,87,8,6,10,6,12,6,90,9,6,3,6,92,8,6,1,6,1,6,1,6,
        3,6,97,8,6,1,6,1,6,1,6,1,6,5,6,103,8,6,10,6,12,6,106,9,6,3,6,108,
        8,6,1,6,1,6,5,6,112,8,6,10,6,12,6,115,9,6,1,6,1,6,1,6,1,6,1,6,5,
        6,122,8,6,10,6,12,6,125,9,6,1,6,1,6,1,6,1,6,1,6,5,6,132,8,6,10,6,
        12,6,135,9,6,1,6,1,6,1,6,1,6,1,6,5,6,142,8,6,10,6,12,6,145,9,6,3,
        6,147,8,6,1,6,1,6,1,6,3,6,152,8,6,1,6,1,6,1,6,1,6,5,6,158,8,6,10,
        6,12,6,161,9,6,3,6,163,8,6,1,6,1,6,5,6,167,8,6,10,6,12,6,170,9,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,3,6,189,8,6,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,3,9,
        202,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,5,9,320,8,9,10,9,12,9,323,9,9,3,9,325,8,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,337,8,9,10,9,12,9,
        340,9,9,3,9,342,8,9,1,9,1,9,1,9,1,9,1,9,5,9,349,8,9,10,9,12,9,352,
        9,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,360,8,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,5,9,369,8,9,10,9,12,9,372,9,9,3,9,374,8,9,1,9,1,9,1,9,1,9,1,
        9,1,9,5,9,382,8,9,10,9,12,9,385,9,9,3,9,387,8,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,401,8,9,10,9,12,9,404,9,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,413,8,9,10,9,12,9,416,9,9,1,9,1,9,
        1,9,1,9,1,9,1,9,5,9,424,8,9,10,9,12,9,427,9,9,1,9,1,9,1,9,1,9,1,
        9,1,9,3,9,435,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,487,8,9,10,9,12,9,490,9,9,3,9,492,
        8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,3,9,510,8,9,5,9,512,8,9,10,9,12,9,515,9,9,1,10,1,10,1,10,1,10,
        1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,3,13,
        533,8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,13,5,13,550,8,13,10,13,12,13,553,9,13,3,13,555,
        8,13,1,13,1,13,1,13,1,13,1,13,5,13,562,8,13,10,13,12,13,565,9,13,
        3,13,567,8,13,1,13,1,13,1,13,1,13,1,13,5,13,574,8,13,10,13,12,13,
        577,9,13,3,13,579,8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,3,13,603,8,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,5,15,617,8,15,10,15,12,15,620,9,15,3,15,622,8,15,1,
        15,1,15,1,15,1,15,1,15,5,15,629,8,15,10,15,12,15,632,9,15,1,15,1,
        15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,644,8,15,10,15,12,
        15,647,9,15,3,15,649,8,15,1,15,1,15,1,15,1,15,1,15,5,15,656,8,15,
        10,15,12,15,659,9,15,1,15,1,15,1,15,1,15,1,15,1,15,5,15,667,8,15,
        10,15,12,15,670,9,15,3,15,672,8,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,689,8,15,1,15,
        1,15,1,15,5,15,694,8,15,10,15,12,15,697,9,15,1,16,1,16,1,16,1,16,
        1,17,1,17,1,17,3,17,706,8,17,1,17,0,2,18,30,18,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,0,0,828,0,36,1,0,0,0,2,39,1,0,0,0,
        4,42,1,0,0,0,6,45,1,0,0,0,8,58,1,0,0,0,10,62,1,0,0,0,12,188,1,0,
        0,0,14,190,1,0,0,0,16,192,1,0,0,0,18,434,1,0,0,0,20,516,1,0,0,0,
        22,520,1,0,0,0,24,524,1,0,0,0,26,602,1,0,0,0,28,604,1,0,0,0,30,688,
        1,0,0,0,32,698,1,0,0,0,34,702,1,0,0,0,36,37,3,6,3,0,37,38,5,0,0,
        1,38,1,1,0,0,0,39,40,3,18,9,0,40,41,5,0,0,1,41,3,1,0,0,0,42,43,3,
        30,15,0,43,44,5,0,0,1,44,5,1,0,0,0,45,49,3,8,4,0,46,48,3,10,5,0,
        47,46,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,55,1,
        0,0,0,51,49,1,0,0,0,52,54,3,12,6,0,53,52,1,0,0,0,54,57,1,0,0,0,55,
        53,1,0,0,0,55,56,1,0,0,0,56,7,1,0,0,0,57,55,1,0,0,0,58,59,5,51,0,
        0,59,60,5,39,0,0,60,61,5,2,0,0,61,9,1,0,0,0,62,63,5,41,0,0,63,64,
        5,65,0,0,64,69,5,84,0,0,65,66,5,1,0,0,66,68,5,84,0,0,67,65,1,0,0,
        0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,1,0,0,0,71,69,
        1,0,0,0,72,73,5,2,0,0,73,11,1,0,0,0,74,76,3,14,7,0,75,74,1,0,0,0,
        76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,80,1,0,0,0,79,77,1,
        0,0,0,80,81,5,44,0,0,81,82,5,83,0,0,82,91,5,3,0,0,83,88,3,16,8,0,
        84,85,5,1,0,0,85,87,3,16,8,0,86,84,1,0,0,0,87,90,1,0,0,0,88,86,1,
        0,0,0,88,89,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,91,83,1,0,0,0,91,
        92,1,0,0,0,92,93,1,0,0,0,93,96,5,4,0,0,94,95,5,9,0,0,95,97,3,30,
        15,0,96,94,1,0,0,0,96,97,1,0,0,0,97,107,1,0,0,0,98,99,5,60,0,0,99,
        104,3,30,15,0,100,101,5,1,0,0,101,103,3,30,15,0,102,100,1,0,0,0,
        103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,108,1,0,0,0,
        106,104,1,0,0,0,107,98,1,0,0,0,107,108,1,0,0,0,108,109,1,0,0,0,109,
        113,5,5,0,0,110,112,3,12,6,0,111,110,1,0,0,0,112,115,1,0,0,0,113,
        111,1,0,0,0,113,114,1,0,0,0,114,116,1,0,0,0,115,113,1,0,0,0,116,
        117,5,57,0,0,117,118,3,18,9,0,118,119,5,6,0,0,119,189,1,0,0,0,120,
        122,3,14,7,0,121,120,1,0,0,0,122,125,1,0,0,0,123,121,1,0,0,0,123,
        124,1,0,0,0,124,126,1,0,0,0,125,123,1,0,0,0,126,127,5,79,0,0,127,
        128,5,44,0,0,128,129,5,83,0,0,129,133,5,14,0,0,130,132,5,83,0,0,
        131,130,1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,
        134,136,1,0,0,0,135,133,1,0,0,0,136,137,5,15,0,0,137,146,5,3,0,0,
        138,143,3,16,8,0,139,140,5,1,0,0,140,142,3,16,8,0,141,139,1,0,0,
        0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,1,0,0,0,144,147,1,0,0,
        0,145,143,1,0,0,0,146,138,1,0,0,0,146,147,1,0,0,0,147,148,1,0,0,
        0,148,151,5,4,0,0,149,150,5,9,0,0,150,152,3,30,15,0,151,149,1,0,
        0,0,151,152,1,0,0,0,152,162,1,0,0,0,153,154,5,60,0,0,154,159,3,30,
        15,0,155,156,5,1,0,0,156,158,3,30,15,0,157,155,1,0,0,0,158,161,1,
        0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,163,1,0,0,0,161,159,1,
        0,0,0,162,153,1,0,0,0,162,163,1,0,0,0,163,164,1,0,0,0,164,168,5,
        5,0,0,165,167,3,12,6,0,166,165,1,0,0,0,167,170,1,0,0,0,168,166,1,
        0,0,0,168,169,1,0,0,0,169,171,1,0,0,0,170,168,1,0,0,0,171,172,5,
        57,0,0,172,173,3,18,9,0,173,174,5,6,0,0,174,189,1,0,0,0,175,176,
        5,62,0,0,176,177,5,83,0,0,177,178,5,7,0,0,178,189,3,30,15,0,179,
        180,5,67,0,0,180,181,5,62,0,0,181,182,5,7,0,0,182,189,3,30,15,0,
        183,184,5,67,0,0,184,185,5,68,0,0,185,186,5,83,0,0,186,187,5,8,0,
        0,187,189,3,30,15,0,188,77,1,0,0,0,188,123,1,0,0,0,188,175,1,0,0,
        0,188,179,1,0,0,0,188,183,1,0,0,0,189,13,1,0,0,0,190,191,5,49,0,
        0,191,15,1,0,0,0,192,193,5,83,0,0,193,194,5,8,0,0,194,195,3,30,15,
        0,195,17,1,0,0,0,196,197,6,9,-1,0,197,435,5,61,0,0,198,435,5,42,
        0,0,199,435,5,64,0,0,200,202,5,23,0,0,201,200,1,0,0,0,201,202,1,
        0,0,0,202,203,1,0,0,0,203,435,5,86,0,0,204,435,5,85,0,0,205,435,
        5,83,0,0,206,435,5,73,0,0,207,208,5,74,0,0,208,209,5,3,0,0,209,210,
        3,18,9,0,210,211,5,4,0,0,211,435,1,0,0,0,212,213,5,75,0,0,213,214,
        5,5,0,0,214,215,3,18,9,0,215,216,5,6,0,0,216,217,5,76,0,0,217,218,
        5,5,0,0,218,219,3,26,13,0,219,220,5,10,0,0,220,221,3,18,9,0,221,
        222,5,6,0,0,222,435,1,0,0,0,223,224,5,75,0,0,224,225,5,5,0,0,225,
        226,3,18,9,0,226,227,5,6,0,0,227,228,5,65,0,0,228,229,5,5,0,0,229,
        230,3,18,9,0,230,231,5,6,0,0,231,435,1,0,0,0,232,233,5,48,0,0,233,
        234,5,3,0,0,234,235,3,18,9,0,235,236,5,4,0,0,236,435,1,0,0,0,237,
        238,5,50,0,0,238,239,5,3,0,0,239,240,3,18,9,0,240,241,5,4,0,0,241,
        435,1,0,0,0,242,243,5,38,0,0,243,244,5,3,0,0,244,245,3,18,9,0,245,
        246,5,1,0,0,246,247,3,18,9,0,247,248,5,4,0,0,248,435,1,0,0,0,249,
        250,5,27,0,0,250,251,5,3,0,0,251,252,3,18,9,0,252,253,5,4,0,0,253,
        435,1,0,0,0,254,255,5,28,0,0,255,256,5,3,0,0,256,257,3,18,9,0,257,
        258,5,4,0,0,258,435,1,0,0,0,259,260,5,29,0,0,260,261,5,3,0,0,261,
        262,3,18,9,0,262,263,5,4,0,0,263,435,1,0,0,0,264,265,5,58,0,0,265,
        266,5,3,0,0,266,267,3,18,9,0,267,268,5,4,0,0,268,435,1,0,0,0,269,
        270,5,55,0,0,270,271,5,3,0,0,271,272,3,18,9,0,272,273,5,4,0,0,273,
        435,1,0,0,0,274,275,5,30,0,0,275,276,5,3,0,0,276,277,3,18,9,0,277,
        278,5,4,0,0,278,435,1,0,0,0,279,280,5,31,0,0,280,281,5,3,0,0,281,
        282,3,18,9,0,282,283,5,4,0,0,283,435,1,0,0,0,284,285,5,43,0,0,285,
        286,5,3,0,0,286,287,3,18,9,0,287,288,5,4,0,0,288,435,1,0,0,0,289,
        290,5,32,0,0,290,291,5,3,0,0,291,292,3,18,9,0,292,293,5,1,0,0,293,
        294,3,18,9,0,294,295,5,1,0,0,295,296,3,18,9,0,296,297,5,4,0,0,297,
        435,1,0,0,0,298,299,5,45,0,0,299,300,5,14,0,0,300,301,3,30,15,0,
        301,302,5,15,0,0,302,303,3,18,9,33,303,435,1,0,0,0,304,305,5,63,
        0,0,305,306,5,14,0,0,306,307,3,30,15,0,307,308,5,15,0,0,308,309,
        3,18,9,32,309,435,1,0,0,0,310,311,5,72,0,0,311,435,3,18,9,26,312,
        313,5,24,0,0,313,435,3,18,9,25,314,315,5,44,0,0,315,324,5,3,0,0,
        316,321,3,16,8,0,317,318,5,1,0,0,318,320,3,16,8,0,319,317,1,0,0,
        0,320,323,1,0,0,0,321,319,1,0,0,0,321,322,1,0,0,0,322,325,1,0,0,
        0,323,321,1,0,0,0,324,316,1,0,0,0,324,325,1,0,0,0,325,326,1,0,0,
        0,326,327,5,4,0,0,327,328,5,5,0,0,328,329,5,57,0,0,329,330,3,18,
        9,0,330,331,5,6,0,0,331,435,1,0,0,0,332,341,5,5,0,0,333,338,3,18,
        9,0,334,335,5,1,0,0,335,337,3,18,9,0,336,334,1,0,0,0,337,340,1,0,
        0,0,338,336,1,0,0,0,338,339,1,0,0,0,339,342,1,0,0,0,340,338,1,0,
        0,0,341,333,1,0,0,0,341,342,1,0,0,0,342,343,1,0,0,0,343,435,5,6,
        0,0,344,345,5,5,0,0,345,350,3,22,11,0,346,347,5,1,0,0,347,349,3,
        22,11,0,348,346,1,0,0,0,349,352,1,0,0,0,350,348,1,0,0,0,350,351,
        1,0,0,0,351,353,1,0,0,0,352,350,1,0,0,0,353,354,5,6,0,0,354,435,
        1,0,0,0,355,356,5,12,0,0,356,359,5,83,0,0,357,358,5,7,0,0,358,360,
        3,18,9,0,359,357,1,0,0,0,359,360,1,0,0,0,360,361,1,0,0,0,361,435,
        5,13,0,0,362,363,5,54,0,0,363,364,3,18,9,0,364,373,5,5,0,0,365,370,
        3,24,12,0,366,367,5,11,0,0,367,369,3,24,12,0,368,366,1,0,0,0,369,
        372,1,0,0,0,370,368,1,0,0,0,370,371,1,0,0,0,371,374,1,0,0,0,372,
        370,1,0,0,0,373,365,1,0,0,0,373,374,1,0,0,0,374,375,1,0,0,0,375,
        376,5,6,0,0,376,435,1,0,0,0,377,386,5,14,0,0,378,383,3,18,9,0,379,
        380,5,1,0,0,380,382,3,18,9,0,381,379,1,0,0,0,382,385,1,0,0,0,383,
        381,1,0,0,0,383,384,1,0,0,0,384,387,1,0,0,0,385,383,1,0,0,0,386,
        378,1,0,0,0,386,387,1,0,0,0,387,388,1,0,0,0,388,435,5,15,0,0,389,
        390,5,46,0,0,390,391,3,18,9,0,391,392,5,59,0,0,392,393,3,18,9,0,
        393,394,5,40,0,0,394,395,3,18,9,6,395,435,1,0,0,0,396,397,5,52,0,
        0,397,402,3,20,10,0,398,399,5,1,0,0,399,401,3,20,10,0,400,398,1,
        0,0,0,401,404,1,0,0,0,402,400,1,0,0,0,402,403,1,0,0,0,403,405,1,
        0,0,0,404,402,1,0,0,0,405,406,5,47,0,0,406,407,3,18,9,5,407,435,
        1,0,0,0,408,409,5,53,0,0,409,414,3,20,10,0,410,411,5,1,0,0,411,413,
        3,20,10,0,412,410,1,0,0,0,413,416,1,0,0,0,414,412,1,0,0,0,414,415,
        1,0,0,0,415,417,1,0,0,0,416,414,1,0,0,0,417,418,5,47,0,0,418,419,
        3,18,9,4,419,435,1,0,0,0,420,421,5,79,0,0,421,425,5,14,0,0,422,424,
        5,83,0,0,423,422,1,0,0,0,424,427,1,0,0,0,425,423,1,0,0,0,425,426,
        1,0,0,0,426,428,1,0,0,0,427,425,1,0,0,0,428,429,5,15,0,0,429,435,
        3,18,9,3,430,431,5,3,0,0,431,432,3,18,9,0,432,433,5,4,0,0,433,435,
        1,0,0,0,434,196,1,0,0,0,434,198,1,0,0,0,434,199,1,0,0,0,434,201,
        1,0,0,0,434,204,1,0,0,0,434,205,1,0,0,0,434,206,1,0,0,0,434,207,
        1,0,0,0,434,212,1,0,0,0,434,223,1,0,0,0,434,232,1,0,0,0,434,237,
        1,0,0,0,434,242,1,0,0,0,434,249,1,0,0,0,434,254,1,0,0,0,434,259,
        1,0,0,0,434,264,1,0,0,0,434,269,1,0,0,0,434,274,1,0,0,0,434,279,
        1,0,0,0,434,284,1,0,0,0,434,289,1,0,0,0,434,298,1,0,0,0,434,304,
        1,0,0,0,434,310,1,0,0,0,434,312,1,0,0,0,434,314,1,0,0,0,434,332,
        1,0,0,0,434,344,1,0,0,0,434,355,1,0,0,0,434,362,1,0,0,0,434,377,
        1,0,0,0,434,389,1,0,0,0,434,396,1,0,0,0,434,408,1,0,0,0,434,420,
        1,0,0,0,434,430,1,0,0,0,435,513,1,0,0,0,436,437,10,29,0,0,437,438,
        5,24,0,0,438,512,3,18,9,30,439,440,10,28,0,0,440,441,5,25,0,0,441,
        512,3,18,9,29,442,443,10,27,0,0,443,444,5,36,0,0,444,512,3,18,9,
        28,445,446,10,24,0,0,446,447,5,22,0,0,447,512,3,18,9,25,448,449,
        10,23,0,0,449,450,5,23,0,0,450,512,3,18,9,24,451,452,10,22,0,0,452,
        453,5,56,0,0,453,512,3,18,9,23,454,455,10,13,0,0,455,456,5,16,0,
        0,456,512,3,18,9,14,457,458,10,12,0,0,458,459,5,17,0,0,459,512,3,
        18,9,13,460,461,10,11,0,0,461,462,5,18,0,0,462,512,3,18,9,12,463,
        464,10,10,0,0,464,465,5,19,0,0,465,512,3,18,9,11,466,467,10,9,0,
        0,467,468,5,20,0,0,468,512,3,18,9,10,469,470,10,8,0,0,470,471,5,
        21,0,0,471,512,3,18,9,9,472,473,10,7,0,0,473,474,5,70,0,0,474,512,
        3,18,9,8,475,476,10,57,0,0,476,477,5,26,0,0,477,512,5,83,0,0,478,
        479,10,56,0,0,479,480,5,26,0,0,480,512,5,86,0,0,481,482,10,31,0,
        0,482,491,5,3,0,0,483,488,3,18,9,0,484,485,5,1,0,0,485,487,3,18,
        9,0,486,484,1,0,0,0,487,490,1,0,0,0,488,486,1,0,0,0,488,489,1,0,
        0,0,489,492,1,0,0,0,490,488,1,0,0,0,491,483,1,0,0,0,491,492,1,0,
        0,0,492,493,1,0,0,0,493,512,5,4,0,0,494,495,10,30,0,0,495,496,5,
        14,0,0,496,497,3,30,15,0,497,498,5,15,0,0,498,512,1,0,0,0,499,500,
        10,21,0,0,500,501,5,37,0,0,501,512,3,30,15,0,502,503,10,20,0,0,503,
        504,5,69,0,0,504,505,5,37,0,0,505,512,3,30,15,0,506,507,10,1,0,0,
        507,509,5,2,0,0,508,510,3,18,9,0,509,508,1,0,0,0,509,510,1,0,0,0,
        510,512,1,0,0,0,511,436,1,0,0,0,511,439,1,0,0,0,511,442,1,0,0,0,
        511,445,1,0,0,0,511,448,1,0,0,0,511,451,1,0,0,0,511,454,1,0,0,0,
        511,457,1,0,0,0,511,460,1,0,0,0,511,463,1,0,0,0,511,466,1,0,0,0,
        511,469,1,0,0,0,511,472,1,0,0,0,511,475,1,0,0,0,511,478,1,0,0,0,
        511,481,1,0,0,0,511,494,1,0,0,0,511,499,1,0,0,0,511,502,1,0,0,0,
        511,506,1,0,0,0,512,515,1,0,0,0,513,511,1,0,0,0,513,514,1,0,0,0,
        514,19,1,0,0,0,515,513,1,0,0,0,516,517,3,26,13,0,517,518,5,7,0,0,
        518,519,3,18,9,0,519,21,1,0,0,0,520,521,5,83,0,0,521,522,5,7,0,0,
        522,523,3,18,9,0,523,23,1,0,0,0,524,525,3,26,13,0,525,526,5,10,0,
        0,526,527,3,18,9,0,527,25,1,0,0,0,528,529,5,12,0,0,529,532,5,83,
        0,0,530,531,5,7,0,0,531,533,3,26,13,0,532,530,1,0,0,0,532,533,1,
        0,0,0,533,534,1,0,0,0,534,603,5,13,0,0,535,536,5,48,0,0,536,537,
        5,3,0,0,537,538,3,26,13,0,538,539,5,4,0,0,539,603,1,0,0,0,540,541,
        5,50,0,0,541,542,5,3,0,0,542,543,3,26,13,0,543,544,5,4,0,0,544,603,
        1,0,0,0,545,554,5,5,0,0,546,551,3,26,13,0,547,548,5,1,0,0,548,550,
        3,26,13,0,549,547,1,0,0,0,550,553,1,0,0,0,551,549,1,0,0,0,551,552,
        1,0,0,0,552,555,1,0,0,0,553,551,1,0,0,0,554,546,1,0,0,0,554,555,
        1,0,0,0,555,556,1,0,0,0,556,603,5,6,0,0,557,566,5,5,0,0,558,563,
        3,28,14,0,559,560,5,1,0,0,560,562,3,28,14,0,561,559,1,0,0,0,562,
        565,1,0,0,0,563,561,1,0,0,0,563,564,1,0,0,0,564,567,1,0,0,0,565,
        563,1,0,0,0,566,558,1,0,0,0,566,567,1,0,0,0,567,568,1,0,0,0,568,
        603,5,6,0,0,569,578,5,14,0,0,570,575,3,26,13,0,571,572,5,1,0,0,572,
        574,3,26,13,0,573,571,1,0,0,0,574,577,1,0,0,0,575,573,1,0,0,0,575,
        576,1,0,0,0,576,579,1,0,0,0,577,575,1,0,0,0,578,570,1,0,0,0,578,
        579,1,0,0,0,579,580,1,0,0,0,580,603,5,15,0,0,581,582,5,38,0,0,582,
        583,5,3,0,0,583,584,3,26,13,0,584,585,5,1,0,0,585,586,3,26,13,0,
        586,587,5,4,0,0,587,603,1,0,0,0,588,603,5,42,0,0,589,603,5,61,0,
        0,590,603,5,64,0,0,591,603,5,86,0,0,592,593,5,58,0,0,593,594,5,3,
        0,0,594,595,3,26,13,0,595,596,5,4,0,0,596,603,1,0,0,0,597,603,5,
        83,0,0,598,599,5,3,0,0,599,600,3,26,13,0,600,601,5,4,0,0,601,603,
        1,0,0,0,602,528,1,0,0,0,602,535,1,0,0,0,602,540,1,0,0,0,602,545,
        1,0,0,0,602,557,1,0,0,0,602,569,1,0,0,0,602,581,1,0,0,0,602,588,
        1,0,0,0,602,589,1,0,0,0,602,590,1,0,0,0,602,591,1,0,0,0,602,592,
        1,0,0,0,602,597,1,0,0,0,602,598,1,0,0,0,603,27,1,0,0,0,604,605,5,
        83,0,0,605,606,5,7,0,0,606,607,3,26,13,0,607,29,1,0,0,0,608,609,
        6,15,-1,0,609,689,5,33,0,0,610,689,5,34,0,0,611,612,5,44,0,0,612,
        621,5,3,0,0,613,618,3,30,15,0,614,615,5,1,0,0,615,617,3,30,15,0,
        616,614,1,0,0,0,617,620,1,0,0,0,618,616,1,0,0,0,618,619,1,0,0,0,
        619,622,1,0,0,0,620,618,1,0,0,0,621,613,1,0,0,0,621,622,1,0,0,0,
        622,623,1,0,0,0,623,624,5,4,0,0,624,625,5,9,0,0,625,689,3,30,15,
        14,626,630,5,80,0,0,627,629,5,83,0,0,628,627,1,0,0,0,629,632,1,0,
        0,0,630,628,1,0,0,0,630,631,1,0,0,0,631,633,1,0,0,0,632,630,1,0,
        0,0,633,634,5,26,0,0,634,689,3,30,15,13,635,636,5,66,0,0,636,637,
        5,83,0,0,637,638,5,26,0,0,638,689,3,30,15,12,639,648,5,5,0,0,640,
        645,3,30,15,0,641,642,5,1,0,0,642,644,3,30,15,0,643,641,1,0,0,0,
        644,647,1,0,0,0,645,643,1,0,0,0,645,646,1,0,0,0,646,649,1,0,0,0,
        647,645,1,0,0,0,648,640,1,0,0,0,648,649,1,0,0,0,649,650,1,0,0,0,
        650,689,5,6,0,0,651,652,5,5,0,0,652,657,3,32,16,0,653,654,5,1,0,
        0,654,656,3,32,16,0,655,653,1,0,0,0,656,659,1,0,0,0,657,655,1,0,
        0,0,657,658,1,0,0,0,658,660,1,0,0,0,659,657,1,0,0,0,660,661,5,6,
        0,0,661,689,1,0,0,0,662,671,5,12,0,0,663,668,3,34,17,0,664,665,5,
        1,0,0,665,667,3,34,17,0,666,664,1,0,0,0,667,670,1,0,0,0,668,666,
        1,0,0,0,668,669,1,0,0,0,669,672,1,0,0,0,670,668,1,0,0,0,671,663,
        1,0,0,0,671,672,1,0,0,0,672,673,1,0,0,0,673,689,5,13,0,0,674,675,
        5,14,0,0,675,676,3,30,15,0,676,677,5,15,0,0,677,689,1,0,0,0,678,
        689,5,35,0,0,679,689,5,77,0,0,680,681,5,71,0,0,681,689,3,30,15,4,
        682,689,5,78,0,0,683,689,5,83,0,0,684,685,5,3,0,0,685,686,3,30,15,
        0,686,687,5,4,0,0,687,689,1,0,0,0,688,608,1,0,0,0,688,610,1,0,0,
        0,688,611,1,0,0,0,688,626,1,0,0,0,688,635,1,0,0,0,688,639,1,0,0,
        0,688,651,1,0,0,0,688,662,1,0,0,0,688,674,1,0,0,0,688,678,1,0,0,
        0,688,679,1,0,0,0,688,680,1,0,0,0,688,682,1,0,0,0,688,683,1,0,0,
        0,688,684,1,0,0,0,689,695,1,0,0,0,690,691,10,11,0,0,691,692,5,22,
        0,0,692,694,3,30,15,12,693,690,1,0,0,0,694,697,1,0,0,0,695,693,1,
        0,0,0,695,696,1,0,0,0,696,31,1,0,0,0,697,695,1,0,0,0,698,699,5,83,
        0,0,699,700,5,8,0,0,700,701,3,30,15,0,701,33,1,0,0,0,702,705,5,83,
        0,0,703,704,5,8,0,0,704,706,3,30,15,0,705,703,1,0,0,0,705,706,1,
        0,0,0,706,35,1,0,0,0,58,49,55,69,77,88,91,96,104,107,113,123,133,
        143,146,151,159,162,168,188,201,321,324,338,341,350,359,370,373,
        383,386,402,414,425,434,488,491,509,511,513,532,551,554,563,566,
        575,578,602,618,621,630,645,648,657,668,671,688,695,705
    ]

class stellaParser ( Parser ):

    grammarFileName = "stellaParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "';'", "'('", "')'", "'{'", "'}'", 
                     "'='", "':'", "'->'", "'=>'", "'|'", "'<|'", "'|>'", 
                     "'['", "']'", "'<'", "'<='", "'>'", "'>='", "'=='", 
                     "'!='", "'+'", "'-'", "'*'", "'/'", "'.'", "'List::head'", 
                     "'List::isempty'", "'List::tail'", "'Nat::pred'", "'Nat::iszero'", 
                     "'Nat::rec'", "'Bool'", "'Nat'", "'Unit'", "'and'", 
                     "'as'", "'cons'", "'core'", "'else'", "'extend'", "'false'", 
                     "'fix'", "'fn'", "'fold'", "'if'", "'in'", "'inl'", 
                     "'inline'", "'inr'", "'language'", "'let'", "'letrec'", 
                     "'match'", "'not'", "'or'", "'return'", "'succ'", "'then'", 
                     "'throws'", "'true'", "'type'", "'unfold'", "'unit'", 
                     "'with'", "'\\u00B5'", "'exception'", "'variant'", 
                     "'cast'", "':='", "'&'", "'new'", "'panic!'", "'throw'", 
                     "'try'", "'catch'", "'Top'", "'Bot'", "'generic'", 
                     "'forall'" ]

    symbolicNames = [ "<INVALID>", "Surrogate_id_SYMB_0", "Surrogate_id_SYMB_1", 
                      "Surrogate_id_SYMB_2", "Surrogate_id_SYMB_3", "Surrogate_id_SYMB_4", 
                      "Surrogate_id_SYMB_5", "Surrogate_id_SYMB_6", "Surrogate_id_SYMB_7", 
                      "Surrogate_id_SYMB_8", "Surrogate_id_SYMB_9", "Surrogate_id_SYMB_10", 
                      "Surrogate_id_SYMB_11", "Surrogate_id_SYMB_12", "Surrogate_id_SYMB_13", 
                      "Surrogate_id_SYMB_14", "Surrogate_id_SYMB_15", "Surrogate_id_SYMB_16", 
                      "Surrogate_id_SYMB_17", "Surrogate_id_SYMB_18", "Surrogate_id_SYMB_19", 
                      "Surrogate_id_SYMB_20", "Surrogate_id_SYMB_21", "Surrogate_id_SYMB_22", 
                      "Surrogate_id_SYMB_23", "Surrogate_id_SYMB_24", "Surrogate_id_SYMB_25", 
                      "Surrogate_id_SYMB_26", "Surrogate_id_SYMB_27", "Surrogate_id_SYMB_28", 
                      "Surrogate_id_SYMB_29", "Surrogate_id_SYMB_30", "Surrogate_id_SYMB_31", 
                      "Surrogate_id_SYMB_32", "Surrogate_id_SYMB_33", "Surrogate_id_SYMB_34", 
                      "Surrogate_id_SYMB_35", "Surrogate_id_SYMB_36", "Surrogate_id_SYMB_37", 
                      "Surrogate_id_SYMB_38", "Surrogate_id_SYMB_39", "Surrogate_id_SYMB_40", 
                      "Surrogate_id_SYMB_41", "Surrogate_id_SYMB_42", "Surrogate_id_SYMB_43", 
                      "Surrogate_id_SYMB_44", "Surrogate_id_SYMB_45", "Surrogate_id_SYMB_46", 
                      "Surrogate_id_SYMB_47", "Surrogate_id_SYMB_48", "Surrogate_id_SYMB_49", 
                      "Surrogate_id_SYMB_50", "Surrogate_id_SYMB_51", "Surrogate_id_SYMB_52", 
                      "Surrogate_id_SYMB_53", "Surrogate_id_SYMB_54", "Surrogate_id_SYMB_55", 
                      "Surrogate_id_SYMB_56", "Surrogate_id_SYMB_57", "Surrogate_id_SYMB_58", 
                      "Surrogate_id_SYMB_59", "Surrogate_id_SYMB_60", "Surrogate_id_SYMB_61", 
                      "Surrogate_id_SYMB_62", "Surrogate_id_SYMB_63", "Surrogate_id_SYMB_64", 
                      "Surrogate_id_SYMB_65", "EXCEPTION", "VARIANT", "CAST", 
                      "ASSIGN", "REF_TYPE", "REFERENCE", "PANIC", "THROW", 
                      "TRY", "CATCH", "TOP_TYPE", "BOTTOM_TYPE", "GENERIC", 
                      "FORALL", "COMMENT_antlr_builtin", "MULTICOMMENT_antlr_builtin", 
                      "StellaIdent", "ExtensionName", "MemoryAddress", "INTEGER", 
                      "WS", "ErrorToken" ]

    RULE_start_Program = 0
    RULE_start_Expr = 1
    RULE_start_Type = 2
    RULE_program = 3
    RULE_languageDecl = 4
    RULE_extension = 5
    RULE_decl = 6
    RULE_annotation = 7
    RULE_paramDecl = 8
    RULE_expr = 9
    RULE_patternBinding = 10
    RULE_binding = 11
    RULE_matchCase = 12
    RULE_pattern = 13
    RULE_labelledPattern = 14
    RULE_stellatype = 15
    RULE_recordFieldType = 16
    RULE_variantFieldType = 17

    ruleNames =  [ "start_Program", "start_Expr", "start_Type", "program", 
                   "languageDecl", "extension", "decl", "annotation", "paramDecl", 
                   "expr", "patternBinding", "binding", "matchCase", "pattern", 
                   "labelledPattern", "stellatype", "recordFieldType", "variantFieldType" ]

    EOF = Token.EOF
    Surrogate_id_SYMB_0=1
    Surrogate_id_SYMB_1=2
    Surrogate_id_SYMB_2=3
    Surrogate_id_SYMB_3=4
    Surrogate_id_SYMB_4=5
    Surrogate_id_SYMB_5=6
    Surrogate_id_SYMB_6=7
    Surrogate_id_SYMB_7=8
    Surrogate_id_SYMB_8=9
    Surrogate_id_SYMB_9=10
    Surrogate_id_SYMB_10=11
    Surrogate_id_SYMB_11=12
    Surrogate_id_SYMB_12=13
    Surrogate_id_SYMB_13=14
    Surrogate_id_SYMB_14=15
    Surrogate_id_SYMB_15=16
    Surrogate_id_SYMB_16=17
    Surrogate_id_SYMB_17=18
    Surrogate_id_SYMB_18=19
    Surrogate_id_SYMB_19=20
    Surrogate_id_SYMB_20=21
    Surrogate_id_SYMB_21=22
    Surrogate_id_SYMB_22=23
    Surrogate_id_SYMB_23=24
    Surrogate_id_SYMB_24=25
    Surrogate_id_SYMB_25=26
    Surrogate_id_SYMB_26=27
    Surrogate_id_SYMB_27=28
    Surrogate_id_SYMB_28=29
    Surrogate_id_SYMB_29=30
    Surrogate_id_SYMB_30=31
    Surrogate_id_SYMB_31=32
    Surrogate_id_SYMB_32=33
    Surrogate_id_SYMB_33=34
    Surrogate_id_SYMB_34=35
    Surrogate_id_SYMB_35=36
    Surrogate_id_SYMB_36=37
    Surrogate_id_SYMB_37=38
    Surrogate_id_SYMB_38=39
    Surrogate_id_SYMB_39=40
    Surrogate_id_SYMB_40=41
    Surrogate_id_SYMB_41=42
    Surrogate_id_SYMB_42=43
    Surrogate_id_SYMB_43=44
    Surrogate_id_SYMB_44=45
    Surrogate_id_SYMB_45=46
    Surrogate_id_SYMB_46=47
    Surrogate_id_SYMB_47=48
    Surrogate_id_SYMB_48=49
    Surrogate_id_SYMB_49=50
    Surrogate_id_SYMB_50=51
    Surrogate_id_SYMB_51=52
    Surrogate_id_SYMB_52=53
    Surrogate_id_SYMB_53=54
    Surrogate_id_SYMB_54=55
    Surrogate_id_SYMB_55=56
    Surrogate_id_SYMB_56=57
    Surrogate_id_SYMB_57=58
    Surrogate_id_SYMB_58=59
    Surrogate_id_SYMB_59=60
    Surrogate_id_SYMB_60=61
    Surrogate_id_SYMB_61=62
    Surrogate_id_SYMB_62=63
    Surrogate_id_SYMB_63=64
    Surrogate_id_SYMB_64=65
    Surrogate_id_SYMB_65=66
    EXCEPTION=67
    VARIANT=68
    CAST=69
    ASSIGN=70
    REF_TYPE=71
    REFERENCE=72
    PANIC=73
    THROW=74
    TRY=75
    CATCH=76
    TOP_TYPE=77
    BOTTOM_TYPE=78
    GENERIC=79
    FORALL=80
    COMMENT_antlr_builtin=81
    MULTICOMMENT_antlr_builtin=82
    StellaIdent=83
    ExtensionName=84
    MemoryAddress=85
    INTEGER=86
    WS=87
    ErrorToken=88

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Start_ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.x = None # ProgramContext

        def EOF(self):
            return self.getToken(stellaParser.EOF, 0)

        def program(self):
            return self.getTypedRuleContext(stellaParser.ProgramContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_start_Program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart_Program" ):
                return visitor.visitStart_Program(self)
            else:
                return visitor.visitChildren(self)




    def start_Program(self):

        localctx = stellaParser.Start_ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start_Program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            localctx.x = self.program()
            self.state = 37
            self.match(stellaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Start_ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.x = None # ExprContext

        def EOF(self):
            return self.getToken(stellaParser.EOF, 0)

        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_start_Expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart_Expr" ):
                return visitor.visitStart_Expr(self)
            else:
                return visitor.visitChildren(self)




    def start_Expr(self):

        localctx = stellaParser.Start_ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_start_Expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            localctx.x = self.expr(0)
            self.state = 40
            self.match(stellaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Start_TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.x = None # StellatypeContext

        def EOF(self):
            return self.getToken(stellaParser.EOF, 0)

        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_start_Type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart_Type" ):
                return visitor.visitStart_Type(self)
            else:
                return visitor.visitChildren(self)




    def start_Type(self):

        localctx = stellaParser.Start_TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_start_Type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            localctx.x = self.stellatype(0)
            self.state = 43
            self.match(stellaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._extension = None # ExtensionContext
            self.extensions = list() # of ExtensionContexts
            self._decl = None # DeclContext
            self.decls = list() # of DeclContexts

        def languageDecl(self):
            return self.getTypedRuleContext(stellaParser.LanguageDeclContext,0)


        def extension(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExtensionContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExtensionContext,i)


        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.DeclContext)
            else:
                return self.getTypedRuleContext(stellaParser.DeclContext,i)


        def getRuleIndex(self):
            return stellaParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = stellaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.languageDecl()
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 46
                localctx._extension = self.extension()
                localctx.extensions.append(localctx._extension)
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 44)) & ~0x3f) == 0 and ((1 << (_la - 44)) & 34368389153) != 0):
                self.state = 52
                localctx._decl = self.decl()
                localctx.decls.append(localctx._decl)
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LanguageDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stellaParser.RULE_languageDecl

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LanguageCoreContext(LanguageDeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.LanguageDeclContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_50(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_50, 0)
        def Surrogate_id_SYMB_38(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_38, 0)
        def Surrogate_id_SYMB_1(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_1, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLanguageCore" ):
                return visitor.visitLanguageCore(self)
            else:
                return visitor.visitChildren(self)



    def languageDecl(self):

        localctx = stellaParser.LanguageDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_languageDecl)
        try:
            localctx = stellaParser.LanguageCoreContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(stellaParser.Surrogate_id_SYMB_50)
            self.state = 59
            self.match(stellaParser.Surrogate_id_SYMB_38)
            self.state = 60
            self.match(stellaParser.Surrogate_id_SYMB_1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExtensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stellaParser.RULE_extension

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AnExtensionContext(ExtensionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExtensionContext
            super().__init__(parser)
            self._ExtensionName = None # Token
            self.extensionNames = list() # of Tokens
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_40(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_40, 0)
        def Surrogate_id_SYMB_64(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_64, 0)
        def Surrogate_id_SYMB_1(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_1, 0)
        def ExtensionName(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.ExtensionName)
            else:
                return self.getToken(stellaParser.ExtensionName, i)
        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnExtension" ):
                return visitor.visitAnExtension(self)
            else:
                return visitor.visitChildren(self)



    def extension(self):

        localctx = stellaParser.ExtensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_extension)
        self._la = 0 # Token type
        try:
            localctx = stellaParser.AnExtensionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(stellaParser.Surrogate_id_SYMB_40)
            self.state = 63
            self.match(stellaParser.Surrogate_id_SYMB_64)
            self.state = 64
            localctx._ExtensionName = self.match(stellaParser.ExtensionName)
            localctx.extensionNames.append(localctx._ExtensionName)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 65
                self.match(stellaParser.Surrogate_id_SYMB_0)
                self.state = 66
                localctx._ExtensionName = self.match(stellaParser.ExtensionName)
                localctx.extensionNames.append(localctx._ExtensionName)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(stellaParser.Surrogate_id_SYMB_1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stellaParser.RULE_decl

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DeclTypeAliasContext(DeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.DeclContext
            super().__init__(parser)
            self.name = None # Token
            self.atype = None # StellatypeContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_61(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_61, 0)
        def Surrogate_id_SYMB_6(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_6, 0)
        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclTypeAlias" ):
                return visitor.visitDeclTypeAlias(self)
            else:
                return visitor.visitChildren(self)


    class DeclExceptionTypeContext(DeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.DeclContext
            super().__init__(parser)
            self.exceptionType = None # StellatypeContext
            self.copyFrom(ctx)

        def EXCEPTION(self):
            return self.getToken(stellaParser.EXCEPTION, 0)
        def Surrogate_id_SYMB_61(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_61, 0)
        def Surrogate_id_SYMB_6(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_6, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclExceptionType" ):
                return visitor.visitDeclExceptionType(self)
            else:
                return visitor.visitChildren(self)


    class DeclFunContext(DeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.DeclContext
            super().__init__(parser)
            self._annotation = None # AnnotationContext
            self.annotations = list() # of AnnotationContexts
            self.name = None # Token
            self._paramDecl = None # ParamDeclContext
            self.paramDecls = list() # of ParamDeclContexts
            self.returnType = None # StellatypeContext
            self._stellatype = None # StellatypeContext
            self.throwTypes = list() # of StellatypeContexts
            self._decl = None # DeclContext
            self.localDecls = list() # of DeclContexts
            self.returnExpr = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_43(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_43, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_56(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_56, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def Surrogate_id_SYMB_8(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_8, 0)
        def Surrogate_id_SYMB_59(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_59, 0)
        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.AnnotationContext)
            else:
                return self.getTypedRuleContext(stellaParser.AnnotationContext,i)

        def paramDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ParamDeclContext)
            else:
                return self.getTypedRuleContext(stellaParser.ParamDeclContext,i)

        def stellatype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.StellatypeContext)
            else:
                return self.getTypedRuleContext(stellaParser.StellatypeContext,i)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.DeclContext)
            else:
                return self.getTypedRuleContext(stellaParser.DeclContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclFun" ):
                return visitor.visitDeclFun(self)
            else:
                return visitor.visitChildren(self)


    class DeclExceptionVariantContext(DeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.DeclContext
            super().__init__(parser)
            self.name = None # Token
            self.variantType = None # StellatypeContext
            self.copyFrom(ctx)

        def EXCEPTION(self):
            return self.getToken(stellaParser.EXCEPTION, 0)
        def VARIANT(self):
            return self.getToken(stellaParser.VARIANT, 0)
        def Surrogate_id_SYMB_7(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_7, 0)
        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclExceptionVariant" ):
                return visitor.visitDeclExceptionVariant(self)
            else:
                return visitor.visitChildren(self)


    class DeclFunGenericContext(DeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.DeclContext
            super().__init__(parser)
            self._annotation = None # AnnotationContext
            self.annotations = list() # of AnnotationContexts
            self.name = None # Token
            self._StellaIdent = None # Token
            self.generics = list() # of Tokens
            self._paramDecl = None # ParamDeclContext
            self.paramDecls = list() # of ParamDeclContexts
            self.returnType = None # StellatypeContext
            self._stellatype = None # StellatypeContext
            self.throwTypes = list() # of StellatypeContexts
            self._decl = None # DeclContext
            self.localDecls = list() # of DeclContexts
            self.returnExpr = None # ExprContext
            self.copyFrom(ctx)

        def GENERIC(self):
            return self.getToken(stellaParser.GENERIC, 0)
        def Surrogate_id_SYMB_43(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_43, 0)
        def Surrogate_id_SYMB_13(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_13, 0)
        def Surrogate_id_SYMB_14(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_14, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_56(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_56, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def StellaIdent(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.StellaIdent)
            else:
                return self.getToken(stellaParser.StellaIdent, i)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def Surrogate_id_SYMB_8(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_8, 0)
        def Surrogate_id_SYMB_59(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_59, 0)
        def annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.AnnotationContext)
            else:
                return self.getTypedRuleContext(stellaParser.AnnotationContext,i)

        def paramDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ParamDeclContext)
            else:
                return self.getTypedRuleContext(stellaParser.ParamDeclContext,i)

        def stellatype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.StellatypeContext)
            else:
                return self.getTypedRuleContext(stellaParser.StellatypeContext,i)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.DeclContext)
            else:
                return self.getTypedRuleContext(stellaParser.DeclContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclFunGeneric" ):
                return visitor.visitDeclFunGeneric(self)
            else:
                return visitor.visitChildren(self)



    def decl(self):

        localctx = stellaParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_decl)
        self._la = 0 # Token type
        try:
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                localctx = stellaParser.DeclFunContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==49:
                    self.state = 74
                    localctx._annotation = self.annotation()
                    localctx.annotations.append(localctx._annotation)
                    self.state = 79
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 80
                self.match(stellaParser.Surrogate_id_SYMB_43)
                self.state = 81
                localctx.name = self.match(stellaParser.StellaIdent)
                self.state = 82
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==83:
                    self.state = 83
                    localctx._paramDecl = self.paramDecl()
                    localctx.paramDecls.append(localctx._paramDecl)
                    self.state = 88
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 84
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 85
                        localctx._paramDecl = self.paramDecl()
                        localctx.paramDecls.append(localctx._paramDecl)
                        self.state = 90
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 93
                self.match(stellaParser.Surrogate_id_SYMB_3)
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 94
                    self.match(stellaParser.Surrogate_id_SYMB_8)
                    self.state = 95
                    localctx.returnType = self.stellatype(0)


                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==60:
                    self.state = 98
                    self.match(stellaParser.Surrogate_id_SYMB_59)
                    self.state = 99
                    localctx._stellatype = self.stellatype(0)
                    localctx.throwTypes.append(localctx._stellatype)
                    self.state = 104
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 100
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 101
                        localctx._stellatype = self.stellatype(0)
                        localctx.throwTypes.append(localctx._stellatype)
                        self.state = 106
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 109
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((((_la - 44)) & ~0x3f) == 0 and ((1 << (_la - 44)) & 34368389153) != 0):
                    self.state = 110
                    localctx._decl = self.decl()
                    localctx.localDecls.append(localctx._decl)
                    self.state = 115
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 116
                self.match(stellaParser.Surrogate_id_SYMB_56)
                self.state = 117
                localctx.returnExpr = self.expr(0)
                self.state = 118
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 2:
                localctx = stellaParser.DeclFunGenericContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==49:
                    self.state = 120
                    localctx._annotation = self.annotation()
                    localctx.annotations.append(localctx._annotation)
                    self.state = 125
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 126
                self.match(stellaParser.GENERIC)
                self.state = 127
                self.match(stellaParser.Surrogate_id_SYMB_43)
                self.state = 128
                localctx.name = self.match(stellaParser.StellaIdent)
                self.state = 129
                self.match(stellaParser.Surrogate_id_SYMB_13)
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==83:
                    self.state = 130
                    localctx._StellaIdent = self.match(stellaParser.StellaIdent)
                    localctx.generics.append(localctx._StellaIdent)
                    self.state = 135
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 136
                self.match(stellaParser.Surrogate_id_SYMB_14)
                self.state = 137
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==83:
                    self.state = 138
                    localctx._paramDecl = self.paramDecl()
                    localctx.paramDecls.append(localctx._paramDecl)
                    self.state = 143
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 139
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 140
                        localctx._paramDecl = self.paramDecl()
                        localctx.paramDecls.append(localctx._paramDecl)
                        self.state = 145
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 148
                self.match(stellaParser.Surrogate_id_SYMB_3)
                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 149
                    self.match(stellaParser.Surrogate_id_SYMB_8)
                    self.state = 150
                    localctx.returnType = self.stellatype(0)


                self.state = 162
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==60:
                    self.state = 153
                    self.match(stellaParser.Surrogate_id_SYMB_59)
                    self.state = 154
                    localctx._stellatype = self.stellatype(0)
                    localctx.throwTypes.append(localctx._stellatype)
                    self.state = 159
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 155
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 156
                        localctx._stellatype = self.stellatype(0)
                        localctx.throwTypes.append(localctx._stellatype)
                        self.state = 161
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 164
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((((_la - 44)) & ~0x3f) == 0 and ((1 << (_la - 44)) & 34368389153) != 0):
                    self.state = 165
                    localctx._decl = self.decl()
                    localctx.localDecls.append(localctx._decl)
                    self.state = 170
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 171
                self.match(stellaParser.Surrogate_id_SYMB_56)
                self.state = 172
                localctx.returnExpr = self.expr(0)
                self.state = 173
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 3:
                localctx = stellaParser.DeclTypeAliasContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 175
                self.match(stellaParser.Surrogate_id_SYMB_61)
                self.state = 176
                localctx.name = self.match(stellaParser.StellaIdent)
                self.state = 177
                self.match(stellaParser.Surrogate_id_SYMB_6)
                self.state = 178
                localctx.atype = self.stellatype(0)
                pass

            elif la_ == 4:
                localctx = stellaParser.DeclExceptionTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 179
                self.match(stellaParser.EXCEPTION)
                self.state = 180
                self.match(stellaParser.Surrogate_id_SYMB_61)
                self.state = 181
                self.match(stellaParser.Surrogate_id_SYMB_6)
                self.state = 182
                localctx.exceptionType = self.stellatype(0)
                pass

            elif la_ == 5:
                localctx = stellaParser.DeclExceptionVariantContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 183
                self.match(stellaParser.EXCEPTION)
                self.state = 184
                self.match(stellaParser.VARIANT)
                self.state = 185
                localctx.name = self.match(stellaParser.StellaIdent)
                self.state = 186
                self.match(stellaParser.Surrogate_id_SYMB_7)
                self.state = 187
                localctx.variantType = self.stellatype(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stellaParser.RULE_annotation

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class InlineAnnotationContext(AnnotationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.AnnotationContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_48(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_48, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInlineAnnotation" ):
                return visitor.visitInlineAnnotation(self)
            else:
                return visitor.visitChildren(self)



    def annotation(self):

        localctx = stellaParser.AnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_annotation)
        try:
            localctx = stellaParser.InlineAnnotationContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(stellaParser.Surrogate_id_SYMB_48)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.paramType = None # StellatypeContext

        def Surrogate_id_SYMB_7(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_7, 0)

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_paramDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamDecl" ):
                return visitor.visitParamDecl(self)
            else:
                return visitor.visitChildren(self)




    def paramDecl(self):

        localctx = stellaParser.ParamDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_paramDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            localctx.name = self.match(stellaParser.StellaIdent)
            self.state = 193
            self.match(stellaParser.Surrogate_id_SYMB_7)
            self.state = 194
            localctx.paramType = self.stellatype(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stellaParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class FoldContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.type_ = None # StellatypeContext
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_44(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_44, 0)
        def Surrogate_id_SYMB_13(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_13, 0)
        def Surrogate_id_SYMB_14(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_14, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)

        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFold" ):
                return visitor.visitFold(self)
            else:
                return visitor.visitChildren(self)


    class AddContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_21(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_21, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class IsZeroContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.n = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_30(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_30, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsZero" ):
                return visitor.visitIsZero(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.name = None # Token
            self.copyFrom(ctx)

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class TypeAbstractionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self._StellaIdent = None # Token
            self.generics = list() # of Tokens
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def GENERIC(self):
            return self.getToken(stellaParser.GENERIC, 0)
        def Surrogate_id_SYMB_13(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_13, 0)
        def Surrogate_id_SYMB_14(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_14, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def StellaIdent(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.StellaIdent)
            else:
                return self.getToken(stellaParser.StellaIdent, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeAbstraction" ):
                return visitor.visitTypeAbstraction(self)
            else:
                return visitor.visitChildren(self)


    class DivideContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_24(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_24, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivide" ):
                return visitor.visitDivide(self)
            else:
                return visitor.visitChildren(self)


    class LessThanContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_15(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_15, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessThan" ):
                return visitor.visitLessThan(self)
            else:
                return visitor.visitChildren(self)


    class DotRecordContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.label = None # Token
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_25(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_25, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDotRecord" ):
                return visitor.visitDotRecord(self)
            else:
                return visitor.visitChildren(self)


    class GreaterThanContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_17(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_17, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterThan" ):
                return visitor.visitGreaterThan(self)
            else:
                return visitor.visitChildren(self)


    class EqualContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_19(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_19, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqual" ):
                return visitor.visitEqual(self)
            else:
                return visitor.visitChildren(self)


    class ThrowContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def THROW(self):
            return self.getToken(stellaParser.THROW, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThrow" ):
                return visitor.visitThrow(self)
            else:
                return visitor.visitChildren(self)


    class MultiplyContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_23(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_23, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiply" ):
                return visitor.visitMultiply(self)
            else:
                return visitor.visitChildren(self)


    class ConstMemoryContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.mem = None # Token
            self.copyFrom(ctx)

        def MemoryAddress(self):
            return self.getToken(stellaParser.MemoryAddress, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstMemory" ):
                return visitor.visitConstMemory(self)
            else:
                return visitor.visitChildren(self)


    class ListContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self._expr = None # ExprContext
            self.exprs = list() # of ExprContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_13(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_13, 0)
        def Surrogate_id_SYMB_14(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_14, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList" ):
                return visitor.visitList(self)
            else:
                return visitor.visitChildren(self)


    class TryCatchContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.tryExpr = None # ExprContext
            self.pat = None # PatternContext
            self.fallbackExpr = None # ExprContext
            self.copyFrom(ctx)

        def TRY(self):
            return self.getToken(stellaParser.TRY, 0)
        def Surrogate_id_SYMB_4(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_4)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_4, i)
        def Surrogate_id_SYMB_5(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_5)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_5, i)
        def CATCH(self):
            return self.getToken(stellaParser.CATCH, 0)
        def Surrogate_id_SYMB_9(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_9, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)

        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTryCatch" ):
                return visitor.visitTryCatch(self)
            else:
                return visitor.visitChildren(self)


    class HeadContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.list_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_26(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_26, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHead" ):
                return visitor.visitHead(self)
            else:
                return visitor.visitChildren(self)


    class NotEqualContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_20(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_20, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotEqual" ):
                return visitor.visitNotEqual(self)
            else:
                return visitor.visitChildren(self)


    class ConstUnitContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_63(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_63, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstUnit" ):
                return visitor.visitConstUnit(self)
            else:
                return visitor.visitChildren(self)


    class SequenceContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr1 = None # ExprContext
            self.expr2 = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_1(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_1, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSequence" ):
                return visitor.visitSequence(self)
            else:
                return visitor.visitChildren(self)


    class ConstFalseContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_41(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_41, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstFalse" ):
                return visitor.visitConstFalse(self)
            else:
                return visitor.visitChildren(self)


    class AbstractionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self._paramDecl = None # ParamDeclContext
            self.paramDecls = list() # of ParamDeclContexts
            self.returnExpr = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_43(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_43, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_56(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_56, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def paramDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ParamDeclContext)
            else:
                return self.getTypedRuleContext(stellaParser.ParamDeclContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstraction" ):
                return visitor.visitAbstraction(self)
            else:
                return visitor.visitChildren(self)


    class ConstIntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.sign = None # Token
            self.n = None # Token
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(stellaParser.INTEGER, 0)
        def Surrogate_id_SYMB_22(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_22, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstInt" ):
                return visitor.visitConstInt(self)
            else:
                return visitor.visitChildren(self)


    class VariantContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.label = None # Token
            self.rhs = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_11(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_11, 0)
        def Surrogate_id_SYMB_12(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_12, 0)
        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)
        def Surrogate_id_SYMB_6(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_6, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariant" ):
                return visitor.visitVariant(self)
            else:
                return visitor.visitChildren(self)


    class ConstTrueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_60(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_60, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstTrue" ):
                return visitor.visitConstTrue(self)
            else:
                return visitor.visitChildren(self)


    class SubtractContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_22(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_22, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubtract" ):
                return visitor.visitSubtract(self)
            else:
                return visitor.visitChildren(self)


    class TypeCastContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.type_ = None # StellatypeContext
            self.copyFrom(ctx)

        def CAST(self):
            return self.getToken(stellaParser.CAST, 0)
        def Surrogate_id_SYMB_36(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_36, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeCast" ):
                return visitor.visitTypeCast(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.condition = None # ExprContext
            self.thenExpr = None # ExprContext
            self.elseExpr = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_45(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_45, 0)
        def Surrogate_id_SYMB_58(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_58, 0)
        def Surrogate_id_SYMB_39(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_39, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)


    class ApplicationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.fun = None # ExprContext
            self._expr = None # ExprContext
            self.args = list() # of ExprContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitApplication" ):
                return visitor.visitApplication(self)
            else:
                return visitor.visitChildren(self)


    class DerefContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_23(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_23, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeref" ):
                return visitor.visitDeref(self)
            else:
                return visitor.visitChildren(self)


    class IsEmptyContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.list_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_27(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_27, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsEmpty" ):
                return visitor.visitIsEmpty(self)
            else:
                return visitor.visitChildren(self)


    class PanicContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PANIC(self):
            return self.getToken(stellaParser.PANIC, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPanic" ):
                return visitor.visitPanic(self)
            else:
                return visitor.visitChildren(self)


    class LessThanOrEqualContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_16(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_16, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLessThanOrEqual" ):
                return visitor.visitLessThanOrEqual(self)
            else:
                return visitor.visitChildren(self)


    class SuccContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.n = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_57(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_57, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSucc" ):
                return visitor.visitSucc(self)
            else:
                return visitor.visitChildren(self)


    class InlContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_47(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_47, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInl" ):
                return visitor.visitInl(self)
            else:
                return visitor.visitChildren(self)


    class GreaterThanOrEqualContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_18(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_18, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGreaterThanOrEqual" ):
                return visitor.visitGreaterThanOrEqual(self)
            else:
                return visitor.visitChildren(self)


    class InrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_49(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_49, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInr" ):
                return visitor.visitInr(self)
            else:
                return visitor.visitChildren(self)


    class MatchContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self._matchCase = None # MatchCaseContext
            self.cases = list() # of MatchCaseContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_53(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_53, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def matchCase(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.MatchCaseContext)
            else:
                return self.getTypedRuleContext(stellaParser.MatchCaseContext,i)

        def Surrogate_id_SYMB_10(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_10)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_10, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatch" ):
                return visitor.visitMatch(self)
            else:
                return visitor.visitChildren(self)


    class LogicNotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_54(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_54, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicNot" ):
                return visitor.visitLogicNot(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisedExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesisedExpr" ):
                return visitor.visitParenthesisedExpr(self)
            else:
                return visitor.visitChildren(self)


    class TailContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.list_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_28(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_28, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTail" ):
                return visitor.visitTail(self)
            else:
                return visitor.visitChildren(self)


    class RecordContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self._binding = None # BindingContext
            self.bindings = list() # of BindingContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def binding(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.BindingContext)
            else:
                return self.getTypedRuleContext(stellaParser.BindingContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecord" ):
                return visitor.visitRecord(self)
            else:
                return visitor.visitChildren(self)


    class LogicAndContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_35(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_35, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicAnd" ):
                return visitor.visitLogicAnd(self)
            else:
                return visitor.visitChildren(self)


    class TypeApplicationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.fun = None # ExprContext
            self._stellatype = None # StellatypeContext
            self.types = list() # of StellatypeContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_13(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_13, 0)
        def Surrogate_id_SYMB_14(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_14, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeApplication" ):
                return visitor.visitTypeApplication(self)
            else:
                return visitor.visitChildren(self)


    class LetRecContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self._patternBinding = None # PatternBindingContext
            self.patternBindings = list() # of PatternBindingContexts
            self.body = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_52(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_52, 0)
        def Surrogate_id_SYMB_46(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_46, 0)
        def patternBinding(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.PatternBindingContext)
            else:
                return self.getTypedRuleContext(stellaParser.PatternBindingContext,i)

        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetRec" ):
                return visitor.visitLetRec(self)
            else:
                return visitor.visitChildren(self)


    class LogicOrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_55(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_55, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicOr" ):
                return visitor.visitLogicOr(self)
            else:
                return visitor.visitChildren(self)


    class TryWithContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.tryExpr = None # ExprContext
            self.fallbackExpr = None # ExprContext
            self.copyFrom(ctx)

        def TRY(self):
            return self.getToken(stellaParser.TRY, 0)
        def Surrogate_id_SYMB_4(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_4)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_4, i)
        def Surrogate_id_SYMB_5(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_5)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_5, i)
        def Surrogate_id_SYMB_64(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_64, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTryWith" ):
                return visitor.visitTryWith(self)
            else:
                return visitor.visitChildren(self)


    class PredContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.n = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_29(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_29, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPred" ):
                return visitor.visitPred(self)
            else:
                return visitor.visitChildren(self)


    class TypeAscContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.type_ = None # StellatypeContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_36(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_36, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeAsc" ):
                return visitor.visitTypeAsc(self)
            else:
                return visitor.visitChildren(self)


    class NatRecContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.n = None # ExprContext
            self.initial = None # ExprContext
            self.step = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_31(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_31, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNatRec" ):
                return visitor.visitNatRec(self)
            else:
                return visitor.visitChildren(self)


    class UnfoldContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.type_ = None # StellatypeContext
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_62(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_62, 0)
        def Surrogate_id_SYMB_13(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_13, 0)
        def Surrogate_id_SYMB_14(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_14, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)

        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnfold" ):
                return visitor.visitUnfold(self)
            else:
                return visitor.visitChildren(self)


    class RefContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def REFERENCE(self):
            return self.getToken(stellaParser.REFERENCE, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRef" ):
                return visitor.visitRef(self)
            else:
                return visitor.visitChildren(self)


    class DotTupleContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.index = None # Token
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_25(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_25, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def INTEGER(self):
            return self.getToken(stellaParser.INTEGER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDotTuple" ):
                return visitor.visitDotTuple(self)
            else:
                return visitor.visitChildren(self)


    class FixContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.expr_ = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_42(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_42, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFix" ):
                return visitor.visitFix(self)
            else:
                return visitor.visitChildren(self)


    class LetContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self._patternBinding = None # PatternBindingContext
            self.patternBindings = list() # of PatternBindingContexts
            self.body = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_51(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_51, 0)
        def Surrogate_id_SYMB_46(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_46, 0)
        def patternBinding(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.PatternBindingContext)
            else:
                return self.getTypedRuleContext(stellaParser.PatternBindingContext,i)

        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLet" ):
                return visitor.visitLet(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.lhs = None # ExprContext
            self.rhs = None # ExprContext
            self.copyFrom(ctx)

        def ASSIGN(self):
            return self.getToken(stellaParser.ASSIGN, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)


    class TupleContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self._expr = None # ExprContext
            self.exprs = list() # of ExprContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple" ):
                return visitor.visitTuple(self)
            else:
                return visitor.visitChildren(self)


    class ConsListContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.ExprContext
            super().__init__(parser)
            self.head = None # ExprContext
            self.tail = None # ExprContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_37(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_37, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_0(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_0, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.ExprContext)
            else:
                return self.getTypedRuleContext(stellaParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConsList" ):
                return visitor.visitConsList(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = stellaParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                localctx = stellaParser.ConstTrueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 197
                self.match(stellaParser.Surrogate_id_SYMB_60)
                pass

            elif la_ == 2:
                localctx = stellaParser.ConstFalseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 198
                self.match(stellaParser.Surrogate_id_SYMB_41)
                pass

            elif la_ == 3:
                localctx = stellaParser.ConstUnitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 199
                self.match(stellaParser.Surrogate_id_SYMB_63)
                pass

            elif la_ == 4:
                localctx = stellaParser.ConstIntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 200
                    localctx.sign = self.match(stellaParser.Surrogate_id_SYMB_22)


                self.state = 203
                localctx.n = self.match(stellaParser.INTEGER)
                pass

            elif la_ == 5:
                localctx = stellaParser.ConstMemoryContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 204
                localctx.mem = self.match(stellaParser.MemoryAddress)
                pass

            elif la_ == 6:
                localctx = stellaParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 205
                localctx.name = self.match(stellaParser.StellaIdent)
                pass

            elif la_ == 7:
                localctx = stellaParser.PanicContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 206
                self.match(stellaParser.PANIC)
                pass

            elif la_ == 8:
                localctx = stellaParser.ThrowContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 207
                self.match(stellaParser.THROW)
                self.state = 208
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 209
                localctx.expr_ = self.expr(0)
                self.state = 210
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 9:
                localctx = stellaParser.TryCatchContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 212
                self.match(stellaParser.TRY)
                self.state = 213
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 214
                localctx.tryExpr = self.expr(0)
                self.state = 215
                self.match(stellaParser.Surrogate_id_SYMB_5)
                self.state = 216
                self.match(stellaParser.CATCH)
                self.state = 217
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 218
                localctx.pat = self.pattern()
                self.state = 219
                self.match(stellaParser.Surrogate_id_SYMB_9)
                self.state = 220
                localctx.fallbackExpr = self.expr(0)
                self.state = 221
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 10:
                localctx = stellaParser.TryWithContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 223
                self.match(stellaParser.TRY)
                self.state = 224
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 225
                localctx.tryExpr = self.expr(0)
                self.state = 226
                self.match(stellaParser.Surrogate_id_SYMB_5)
                self.state = 227
                self.match(stellaParser.Surrogate_id_SYMB_64)
                self.state = 228
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 229
                localctx.fallbackExpr = self.expr(0)
                self.state = 230
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 11:
                localctx = stellaParser.InlContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 232
                self.match(stellaParser.Surrogate_id_SYMB_47)
                self.state = 233
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 234
                localctx.expr_ = self.expr(0)
                self.state = 235
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 12:
                localctx = stellaParser.InrContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 237
                self.match(stellaParser.Surrogate_id_SYMB_49)
                self.state = 238
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 239
                localctx.expr_ = self.expr(0)
                self.state = 240
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 13:
                localctx = stellaParser.ConsListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 242
                self.match(stellaParser.Surrogate_id_SYMB_37)
                self.state = 243
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 244
                localctx.head = self.expr(0)
                self.state = 245
                self.match(stellaParser.Surrogate_id_SYMB_0)
                self.state = 246
                localctx.tail = self.expr(0)
                self.state = 247
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 14:
                localctx = stellaParser.HeadContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 249
                self.match(stellaParser.Surrogate_id_SYMB_26)
                self.state = 250
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 251
                localctx.list_ = self.expr(0)
                self.state = 252
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 15:
                localctx = stellaParser.IsEmptyContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 254
                self.match(stellaParser.Surrogate_id_SYMB_27)
                self.state = 255
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 256
                localctx.list_ = self.expr(0)
                self.state = 257
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 16:
                localctx = stellaParser.TailContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 259
                self.match(stellaParser.Surrogate_id_SYMB_28)
                self.state = 260
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 261
                localctx.list_ = self.expr(0)
                self.state = 262
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 17:
                localctx = stellaParser.SuccContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 264
                self.match(stellaParser.Surrogate_id_SYMB_57)
                self.state = 265
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 266
                localctx.n = self.expr(0)
                self.state = 267
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 18:
                localctx = stellaParser.LogicNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 269
                self.match(stellaParser.Surrogate_id_SYMB_54)
                self.state = 270
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 271
                localctx.expr_ = self.expr(0)
                self.state = 272
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 19:
                localctx = stellaParser.PredContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 274
                self.match(stellaParser.Surrogate_id_SYMB_29)
                self.state = 275
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 276
                localctx.n = self.expr(0)
                self.state = 277
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 20:
                localctx = stellaParser.IsZeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 279
                self.match(stellaParser.Surrogate_id_SYMB_30)
                self.state = 280
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 281
                localctx.n = self.expr(0)
                self.state = 282
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 21:
                localctx = stellaParser.FixContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 284
                self.match(stellaParser.Surrogate_id_SYMB_42)
                self.state = 285
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 286
                localctx.expr_ = self.expr(0)
                self.state = 287
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 22:
                localctx = stellaParser.NatRecContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 289
                self.match(stellaParser.Surrogate_id_SYMB_31)
                self.state = 290
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 291
                localctx.n = self.expr(0)
                self.state = 292
                self.match(stellaParser.Surrogate_id_SYMB_0)
                self.state = 293
                localctx.initial = self.expr(0)
                self.state = 294
                self.match(stellaParser.Surrogate_id_SYMB_0)
                self.state = 295
                localctx.step = self.expr(0)
                self.state = 296
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 23:
                localctx = stellaParser.FoldContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 298
                self.match(stellaParser.Surrogate_id_SYMB_44)
                self.state = 299
                self.match(stellaParser.Surrogate_id_SYMB_13)
                self.state = 300
                localctx.type_ = self.stellatype(0)
                self.state = 301
                self.match(stellaParser.Surrogate_id_SYMB_14)
                self.state = 302
                localctx.expr_ = self.expr(33)
                pass

            elif la_ == 24:
                localctx = stellaParser.UnfoldContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 304
                self.match(stellaParser.Surrogate_id_SYMB_62)
                self.state = 305
                self.match(stellaParser.Surrogate_id_SYMB_13)
                self.state = 306
                localctx.type_ = self.stellatype(0)
                self.state = 307
                self.match(stellaParser.Surrogate_id_SYMB_14)
                self.state = 308
                localctx.expr_ = self.expr(32)
                pass

            elif la_ == 25:
                localctx = stellaParser.RefContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 310
                self.match(stellaParser.REFERENCE)
                self.state = 311
                localctx.expr_ = self.expr(26)
                pass

            elif la_ == 26:
                localctx = stellaParser.DerefContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 312
                self.match(stellaParser.Surrogate_id_SYMB_23)
                self.state = 313
                localctx.expr_ = self.expr(25)
                pass

            elif la_ == 27:
                localctx = stellaParser.AbstractionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 314
                self.match(stellaParser.Surrogate_id_SYMB_43)
                self.state = 315
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 324
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==83:
                    self.state = 316
                    localctx._paramDecl = self.paramDecl()
                    localctx.paramDecls.append(localctx._paramDecl)
                    self.state = 321
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 317
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 318
                        localctx._paramDecl = self.paramDecl()
                        localctx.paramDecls.append(localctx._paramDecl)
                        self.state = 323
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 326
                self.match(stellaParser.Surrogate_id_SYMB_3)
                self.state = 327
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 328
                self.match(stellaParser.Surrogate_id_SYMB_56)
                self.state = 329
                localctx.returnExpr = self.expr(0)
                self.state = 330
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 28:
                localctx = stellaParser.TupleContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 332
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 341
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -6560200659394605016) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 6852353) != 0):
                    self.state = 333
                    localctx._expr = self.expr(0)
                    localctx.exprs.append(localctx._expr)
                    self.state = 338
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 334
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 335
                        localctx._expr = self.expr(0)
                        localctx.exprs.append(localctx._expr)
                        self.state = 340
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 343
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 29:
                localctx = stellaParser.RecordContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 344
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 345
                localctx._binding = self.binding()
                localctx.bindings.append(localctx._binding)
                self.state = 350
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 346
                    self.match(stellaParser.Surrogate_id_SYMB_0)
                    self.state = 347
                    localctx._binding = self.binding()
                    localctx.bindings.append(localctx._binding)
                    self.state = 352
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 353
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 30:
                localctx = stellaParser.VariantContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 355
                self.match(stellaParser.Surrogate_id_SYMB_11)
                self.state = 356
                localctx.label = self.match(stellaParser.StellaIdent)
                self.state = 359
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 357
                    self.match(stellaParser.Surrogate_id_SYMB_6)
                    self.state = 358
                    localctx.rhs = self.expr(0)


                self.state = 361
                self.match(stellaParser.Surrogate_id_SYMB_12)
                pass

            elif la_ == 31:
                localctx = stellaParser.MatchContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 362
                self.match(stellaParser.Surrogate_id_SYMB_53)
                self.state = 363
                self.expr(0)
                self.state = 364
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 373
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2595485433173397544) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 4718593) != 0):
                    self.state = 365
                    localctx._matchCase = self.matchCase()
                    localctx.cases.append(localctx._matchCase)
                    self.state = 370
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==11:
                        self.state = 366
                        self.match(stellaParser.Surrogate_id_SYMB_10)
                        self.state = 367
                        localctx._matchCase = self.matchCase()
                        localctx.cases.append(localctx._matchCase)
                        self.state = 372
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 375
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 32:
                localctx = stellaParser.ListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 377
                self.match(stellaParser.Surrogate_id_SYMB_13)
                self.state = 386
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & -6560200659394605016) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 6852353) != 0):
                    self.state = 378
                    localctx._expr = self.expr(0)
                    localctx.exprs.append(localctx._expr)
                    self.state = 383
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 379
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 380
                        localctx._expr = self.expr(0)
                        localctx.exprs.append(localctx._expr)
                        self.state = 385
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 388
                self.match(stellaParser.Surrogate_id_SYMB_14)
                pass

            elif la_ == 33:
                localctx = stellaParser.IfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 389
                self.match(stellaParser.Surrogate_id_SYMB_45)
                self.state = 390
                localctx.condition = self.expr(0)
                self.state = 391
                self.match(stellaParser.Surrogate_id_SYMB_58)
                self.state = 392
                localctx.thenExpr = self.expr(0)
                self.state = 393
                self.match(stellaParser.Surrogate_id_SYMB_39)
                self.state = 394
                localctx.elseExpr = self.expr(6)
                pass

            elif la_ == 34:
                localctx = stellaParser.LetContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 396
                self.match(stellaParser.Surrogate_id_SYMB_51)
                self.state = 397
                localctx._patternBinding = self.patternBinding()
                localctx.patternBindings.append(localctx._patternBinding)
                self.state = 402
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 398
                    self.match(stellaParser.Surrogate_id_SYMB_0)
                    self.state = 399
                    localctx._patternBinding = self.patternBinding()
                    localctx.patternBindings.append(localctx._patternBinding)
                    self.state = 404
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 405
                self.match(stellaParser.Surrogate_id_SYMB_46)
                self.state = 406
                localctx.body = self.expr(5)
                pass

            elif la_ == 35:
                localctx = stellaParser.LetRecContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 408
                self.match(stellaParser.Surrogate_id_SYMB_52)
                self.state = 409
                localctx._patternBinding = self.patternBinding()
                localctx.patternBindings.append(localctx._patternBinding)
                self.state = 414
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 410
                    self.match(stellaParser.Surrogate_id_SYMB_0)
                    self.state = 411
                    localctx._patternBinding = self.patternBinding()
                    localctx.patternBindings.append(localctx._patternBinding)
                    self.state = 416
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 417
                self.match(stellaParser.Surrogate_id_SYMB_46)
                self.state = 418
                localctx.body = self.expr(4)
                pass

            elif la_ == 36:
                localctx = stellaParser.TypeAbstractionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 420
                self.match(stellaParser.GENERIC)
                self.state = 421
                self.match(stellaParser.Surrogate_id_SYMB_13)
                self.state = 425
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==83:
                    self.state = 422
                    localctx._StellaIdent = self.match(stellaParser.StellaIdent)
                    localctx.generics.append(localctx._StellaIdent)
                    self.state = 427
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 428
                self.match(stellaParser.Surrogate_id_SYMB_14)
                self.state = 429
                localctx.expr_ = self.expr(3)
                pass

            elif la_ == 37:
                localctx = stellaParser.ParenthesisedExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 430
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 431
                localctx.expr_ = self.expr(0)
                self.state = 432
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 513
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 511
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        localctx = stellaParser.MultiplyContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 436
                        if not self.precpred(self._ctx, 29):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 29)")
                        self.state = 437
                        self.match(stellaParser.Surrogate_id_SYMB_23)
                        self.state = 438
                        localctx.right = self.expr(30)
                        pass

                    elif la_ == 2:
                        localctx = stellaParser.DivideContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 439
                        if not self.precpred(self._ctx, 28):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 28)")
                        self.state = 440
                        self.match(stellaParser.Surrogate_id_SYMB_24)
                        self.state = 441
                        localctx.right = self.expr(29)
                        pass

                    elif la_ == 3:
                        localctx = stellaParser.LogicAndContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 442
                        if not self.precpred(self._ctx, 27):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 27)")
                        self.state = 443
                        self.match(stellaParser.Surrogate_id_SYMB_35)
                        self.state = 444
                        localctx.right = self.expr(28)
                        pass

                    elif la_ == 4:
                        localctx = stellaParser.AddContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 445
                        if not self.precpred(self._ctx, 24):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 24)")
                        self.state = 446
                        self.match(stellaParser.Surrogate_id_SYMB_21)
                        self.state = 447
                        localctx.right = self.expr(25)
                        pass

                    elif la_ == 5:
                        localctx = stellaParser.SubtractContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 448
                        if not self.precpred(self._ctx, 23):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 23)")
                        self.state = 449
                        self.match(stellaParser.Surrogate_id_SYMB_22)
                        self.state = 450
                        localctx.right = self.expr(24)
                        pass

                    elif la_ == 6:
                        localctx = stellaParser.LogicOrContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 451
                        if not self.precpred(self._ctx, 22):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 22)")
                        self.state = 452
                        self.match(stellaParser.Surrogate_id_SYMB_55)
                        self.state = 453
                        localctx.right = self.expr(23)
                        pass

                    elif la_ == 7:
                        localctx = stellaParser.LessThanContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 454
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 455
                        self.match(stellaParser.Surrogate_id_SYMB_15)
                        self.state = 456
                        localctx.right = self.expr(14)
                        pass

                    elif la_ == 8:
                        localctx = stellaParser.LessThanOrEqualContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 457
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 458
                        self.match(stellaParser.Surrogate_id_SYMB_16)
                        self.state = 459
                        localctx.right = self.expr(13)
                        pass

                    elif la_ == 9:
                        localctx = stellaParser.GreaterThanContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 460
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 461
                        self.match(stellaParser.Surrogate_id_SYMB_17)
                        self.state = 462
                        localctx.right = self.expr(12)
                        pass

                    elif la_ == 10:
                        localctx = stellaParser.GreaterThanOrEqualContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 463
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 464
                        self.match(stellaParser.Surrogate_id_SYMB_18)
                        self.state = 465
                        localctx.right = self.expr(11)
                        pass

                    elif la_ == 11:
                        localctx = stellaParser.EqualContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 466
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 467
                        self.match(stellaParser.Surrogate_id_SYMB_19)
                        self.state = 468
                        localctx.right = self.expr(10)
                        pass

                    elif la_ == 12:
                        localctx = stellaParser.NotEqualContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 469
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 470
                        self.match(stellaParser.Surrogate_id_SYMB_20)
                        self.state = 471
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 13:
                        localctx = stellaParser.AssignContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.lhs = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 472
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 473
                        self.match(stellaParser.ASSIGN)
                        self.state = 474
                        localctx.rhs = self.expr(8)
                        pass

                    elif la_ == 14:
                        localctx = stellaParser.DotRecordContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.expr_ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 475
                        if not self.precpred(self._ctx, 57):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 57)")
                        self.state = 476
                        self.match(stellaParser.Surrogate_id_SYMB_25)
                        self.state = 477
                        localctx.label = self.match(stellaParser.StellaIdent)
                        pass

                    elif la_ == 15:
                        localctx = stellaParser.DotTupleContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.expr_ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 478
                        if not self.precpred(self._ctx, 56):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 56)")
                        self.state = 479
                        self.match(stellaParser.Surrogate_id_SYMB_25)
                        self.state = 480
                        localctx.index = self.match(stellaParser.INTEGER)
                        pass

                    elif la_ == 16:
                        localctx = stellaParser.ApplicationContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.fun = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 481
                        if not self.precpred(self._ctx, 31):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 31)")
                        self.state = 482
                        self.match(stellaParser.Surrogate_id_SYMB_2)
                        self.state = 491
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & -6560200659394605016) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 6852353) != 0):
                            self.state = 483
                            localctx._expr = self.expr(0)
                            localctx.args.append(localctx._expr)
                            self.state = 488
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==1:
                                self.state = 484
                                self.match(stellaParser.Surrogate_id_SYMB_0)
                                self.state = 485
                                localctx._expr = self.expr(0)
                                localctx.args.append(localctx._expr)
                                self.state = 490
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 493
                        self.match(stellaParser.Surrogate_id_SYMB_3)
                        pass

                    elif la_ == 17:
                        localctx = stellaParser.TypeApplicationContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.fun = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 494
                        if not self.precpred(self._ctx, 30):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 30)")
                        self.state = 495
                        self.match(stellaParser.Surrogate_id_SYMB_13)

                        self.state = 496
                        localctx._stellatype = self.stellatype(0)
                        localctx.types.append(localctx._stellatype)
                        self.state = 497
                        self.match(stellaParser.Surrogate_id_SYMB_14)
                        pass

                    elif la_ == 18:
                        localctx = stellaParser.TypeAscContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.expr_ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 499
                        if not self.precpred(self._ctx, 21):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 21)")
                        self.state = 500
                        self.match(stellaParser.Surrogate_id_SYMB_36)
                        self.state = 501
                        localctx.type_ = self.stellatype(0)
                        pass

                    elif la_ == 19:
                        localctx = stellaParser.TypeCastContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.expr_ = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 502
                        if not self.precpred(self._ctx, 20):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 20)")
                        self.state = 503
                        self.match(stellaParser.CAST)
                        self.state = 504
                        self.match(stellaParser.Surrogate_id_SYMB_36)
                        self.state = 505
                        localctx.type_ = self.stellatype(0)
                        pass

                    elif la_ == 20:
                        localctx = stellaParser.SequenceContext(self, stellaParser.ExprContext(self, _parentctx, _parentState))
                        localctx.expr1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 506
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 507
                        self.match(stellaParser.Surrogate_id_SYMB_1)
                        self.state = 509
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                        if la_ == 1:
                            self.state = 508
                            localctx.expr2 = self.expr(0)


                        pass

             
                self.state = 515
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PatternBindingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.pat = None # PatternContext
            self.rhs = None # ExprContext

        def Surrogate_id_SYMB_6(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_6, 0)

        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)


        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_patternBinding

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternBinding" ):
                return visitor.visitPatternBinding(self)
            else:
                return visitor.visitChildren(self)




    def patternBinding(self):

        localctx = stellaParser.PatternBindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_patternBinding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            localctx.pat = self.pattern()
            self.state = 517
            self.match(stellaParser.Surrogate_id_SYMB_6)
            self.state = 518
            localctx.rhs = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BindingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token
            self.rhs = None # ExprContext

        def Surrogate_id_SYMB_6(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_6, 0)

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_binding

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinding" ):
                return visitor.visitBinding(self)
            else:
                return visitor.visitChildren(self)




    def binding(self):

        localctx = stellaParser.BindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_binding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            localctx.name = self.match(stellaParser.StellaIdent)
            self.state = 521
            self.match(stellaParser.Surrogate_id_SYMB_6)
            self.state = 522
            localctx.rhs = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatchCaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.pattern_ = None # PatternContext
            self.expr_ = None # ExprContext

        def Surrogate_id_SYMB_9(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_9, 0)

        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)


        def expr(self):
            return self.getTypedRuleContext(stellaParser.ExprContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_matchCase

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatchCase" ):
                return visitor.visitMatchCase(self)
            else:
                return visitor.visitChildren(self)




    def matchCase(self):

        localctx = stellaParser.MatchCaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_matchCase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            localctx.pattern_ = self.pattern()
            self.state = 525
            self.match(stellaParser.Surrogate_id_SYMB_9)
            self.state = 526
            localctx.expr_ = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stellaParser.RULE_pattern

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PatternConsContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.head = None # PatternContext
            self.tail = None # PatternContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_37(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_37, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_0(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_0, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.PatternContext)
            else:
                return self.getTypedRuleContext(stellaParser.PatternContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternCons" ):
                return visitor.visitPatternCons(self)
            else:
                return visitor.visitChildren(self)


    class PatternTupleContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self._pattern = None # PatternContext
            self.patterns = list() # of PatternContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.PatternContext)
            else:
                return self.getTypedRuleContext(stellaParser.PatternContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternTuple" ):
                return visitor.visitPatternTuple(self)
            else:
                return visitor.visitChildren(self)


    class PatternListContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self._pattern = None # PatternContext
            self.patterns = list() # of PatternContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_13(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_13, 0)
        def Surrogate_id_SYMB_14(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_14, 0)
        def pattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.PatternContext)
            else:
                return self.getTypedRuleContext(stellaParser.PatternContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternList" ):
                return visitor.visitPatternList(self)
            else:
                return visitor.visitChildren(self)


    class PatternRecordContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self._labelledPattern = None # LabelledPatternContext
            self.patterns = list() # of LabelledPatternContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def labelledPattern(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.LabelledPatternContext)
            else:
                return self.getTypedRuleContext(stellaParser.LabelledPatternContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternRecord" ):
                return visitor.visitPatternRecord(self)
            else:
                return visitor.visitChildren(self)


    class PatternVariantContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.label = None # Token
            self.pattern_ = None # PatternContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_11(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_11, 0)
        def Surrogate_id_SYMB_12(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_12, 0)
        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)
        def Surrogate_id_SYMB_6(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_6, 0)
        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternVariant" ):
                return visitor.visitPatternVariant(self)
            else:
                return visitor.visitChildren(self)


    class PatternIntContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.n = None # Token
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(stellaParser.INTEGER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternInt" ):
                return visitor.visitPatternInt(self)
            else:
                return visitor.visitChildren(self)


    class PatternInrContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.pattern_ = None # PatternContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_49(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_49, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternInr" ):
                return visitor.visitPatternInr(self)
            else:
                return visitor.visitChildren(self)


    class PatternTrueContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_60(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_60, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternTrue" ):
                return visitor.visitPatternTrue(self)
            else:
                return visitor.visitChildren(self)


    class PatternInlContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.pattern_ = None # PatternContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_47(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_47, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternInl" ):
                return visitor.visitPatternInl(self)
            else:
                return visitor.visitChildren(self)


    class PatternVarContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.name = None # Token
            self.copyFrom(ctx)

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternVar" ):
                return visitor.visitPatternVar(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesisedPatternContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.pattern_ = None # PatternContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesisedPattern" ):
                return visitor.visitParenthesisedPattern(self)
            else:
                return visitor.visitChildren(self)


    class PatternSuccContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.pattern_ = None # PatternContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_57(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_57, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternSucc" ):
                return visitor.visitPatternSucc(self)
            else:
                return visitor.visitChildren(self)


    class PatternFalseContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_41(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_41, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternFalse" ):
                return visitor.visitPatternFalse(self)
            else:
                return visitor.visitChildren(self)


    class PatternUnitContext(PatternContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.PatternContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_63(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_63, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatternUnit" ):
                return visitor.visitPatternUnit(self)
            else:
                return visitor.visitChildren(self)



    def pattern(self):

        localctx = stellaParser.PatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_pattern)
        self._la = 0 # Token type
        try:
            self.state = 602
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                localctx = stellaParser.PatternVariantContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 528
                self.match(stellaParser.Surrogate_id_SYMB_11)
                self.state = 529
                localctx.label = self.match(stellaParser.StellaIdent)
                self.state = 532
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 530
                    self.match(stellaParser.Surrogate_id_SYMB_6)
                    self.state = 531
                    localctx.pattern_ = self.pattern()


                self.state = 534
                self.match(stellaParser.Surrogate_id_SYMB_12)
                pass

            elif la_ == 2:
                localctx = stellaParser.PatternInlContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 535
                self.match(stellaParser.Surrogate_id_SYMB_47)
                self.state = 536
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 537
                localctx.pattern_ = self.pattern()
                self.state = 538
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 3:
                localctx = stellaParser.PatternInrContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 540
                self.match(stellaParser.Surrogate_id_SYMB_49)
                self.state = 541
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 542
                localctx.pattern_ = self.pattern()
                self.state = 543
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 4:
                localctx = stellaParser.PatternTupleContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 545
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 554
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2595485433173397544) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 4718593) != 0):
                    self.state = 546
                    localctx._pattern = self.pattern()
                    localctx.patterns.append(localctx._pattern)
                    self.state = 551
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 547
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 548
                        localctx._pattern = self.pattern()
                        localctx.patterns.append(localctx._pattern)
                        self.state = 553
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 556
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 5:
                localctx = stellaParser.PatternRecordContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 557
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 566
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==83:
                    self.state = 558
                    localctx._labelledPattern = self.labelledPattern()
                    localctx.patterns.append(localctx._labelledPattern)
                    self.state = 563
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 559
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 560
                        localctx._labelledPattern = self.labelledPattern()
                        localctx.patterns.append(localctx._labelledPattern)
                        self.state = 565
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 568
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 6:
                localctx = stellaParser.PatternListContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 569
                self.match(stellaParser.Surrogate_id_SYMB_13)
                self.state = 578
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2595485433173397544) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 4718593) != 0):
                    self.state = 570
                    localctx._pattern = self.pattern()
                    localctx.patterns.append(localctx._pattern)
                    self.state = 575
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 571
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 572
                        localctx._pattern = self.pattern()
                        localctx.patterns.append(localctx._pattern)
                        self.state = 577
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 580
                self.match(stellaParser.Surrogate_id_SYMB_14)
                pass

            elif la_ == 7:
                localctx = stellaParser.PatternConsContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 581
                self.match(stellaParser.Surrogate_id_SYMB_37)
                self.state = 582
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 583
                localctx.head = self.pattern()
                self.state = 584
                self.match(stellaParser.Surrogate_id_SYMB_0)
                self.state = 585
                localctx.tail = self.pattern()
                self.state = 586
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 8:
                localctx = stellaParser.PatternFalseContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 588
                self.match(stellaParser.Surrogate_id_SYMB_41)
                pass

            elif la_ == 9:
                localctx = stellaParser.PatternTrueContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 589
                self.match(stellaParser.Surrogate_id_SYMB_60)
                pass

            elif la_ == 10:
                localctx = stellaParser.PatternUnitContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 590
                self.match(stellaParser.Surrogate_id_SYMB_63)
                pass

            elif la_ == 11:
                localctx = stellaParser.PatternIntContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 591
                localctx.n = self.match(stellaParser.INTEGER)
                pass

            elif la_ == 12:
                localctx = stellaParser.PatternSuccContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 592
                self.match(stellaParser.Surrogate_id_SYMB_57)
                self.state = 593
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 594
                localctx.pattern_ = self.pattern()
                self.state = 595
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass

            elif la_ == 13:
                localctx = stellaParser.PatternVarContext(self, localctx)
                self.enterOuterAlt(localctx, 13)
                self.state = 597
                localctx.name = self.match(stellaParser.StellaIdent)
                pass

            elif la_ == 14:
                localctx = stellaParser.ParenthesisedPatternContext(self, localctx)
                self.enterOuterAlt(localctx, 14)
                self.state = 598
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 599
                localctx.pattern_ = self.pattern()
                self.state = 600
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelledPatternContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.label = None # Token
            self.pattern_ = None # PatternContext

        def Surrogate_id_SYMB_6(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_6, 0)

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def pattern(self):
            return self.getTypedRuleContext(stellaParser.PatternContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_labelledPattern

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabelledPattern" ):
                return visitor.visitLabelledPattern(self)
            else:
                return visitor.visitChildren(self)




    def labelledPattern(self):

        localctx = stellaParser.LabelledPatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_labelledPattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            localctx.label = self.match(stellaParser.StellaIdent)
            self.state = 605
            self.match(stellaParser.Surrogate_id_SYMB_6)
            self.state = 606
            localctx.pattern_ = self.pattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StellatypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stellaParser.RULE_stellatype

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class TypeTupleContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self._stellatype = None # StellatypeContext
            self.types = list() # of StellatypeContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def stellatype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.StellatypeContext)
            else:
                return self.getTypedRuleContext(stellaParser.StellatypeContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeTuple" ):
                return visitor.visitTypeTuple(self)
            else:
                return visitor.visitChildren(self)


    class TypeTopContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOP_TYPE(self):
            return self.getToken(stellaParser.TOP_TYPE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeTop" ):
                return visitor.visitTypeTop(self)
            else:
                return visitor.visitChildren(self)


    class TypeBoolContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_32(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_32, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeBool" ):
                return visitor.visitTypeBool(self)
            else:
                return visitor.visitChildren(self)


    class TypeRefContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.type_ = None # StellatypeContext
            self.copyFrom(ctx)

        def REF_TYPE(self):
            return self.getToken(stellaParser.REF_TYPE, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeRef" ):
                return visitor.visitTypeRef(self)
            else:
                return visitor.visitChildren(self)


    class TypeRecContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.var = None # Token
            self.type_ = None # StellatypeContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_65(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_65, 0)
        def Surrogate_id_SYMB_25(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_25, 0)
        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeRec" ):
                return visitor.visitTypeRec(self)
            else:
                return visitor.visitChildren(self)


    class TypeSumContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.left = None # StellatypeContext
            self.right = None # StellatypeContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_21(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_21, 0)
        def stellatype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.StellatypeContext)
            else:
                return self.getTypedRuleContext(stellaParser.StellatypeContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSum" ):
                return visitor.visitTypeSum(self)
            else:
                return visitor.visitChildren(self)


    class TypeVarContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.name = None # Token
            self.copyFrom(ctx)

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeVar" ):
                return visitor.visitTypeVar(self)
            else:
                return visitor.visitChildren(self)


    class TypeVariantContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self._variantFieldType = None # VariantFieldTypeContext
            self.fieldTypes = list() # of VariantFieldTypeContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_11(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_11, 0)
        def Surrogate_id_SYMB_12(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_12, 0)
        def variantFieldType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.VariantFieldTypeContext)
            else:
                return self.getTypedRuleContext(stellaParser.VariantFieldTypeContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeVariant" ):
                return visitor.visitTypeVariant(self)
            else:
                return visitor.visitChildren(self)


    class TypeUnitContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_34(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_34, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeUnit" ):
                return visitor.visitTypeUnit(self)
            else:
                return visitor.visitChildren(self)


    class TypeNatContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_33(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_33, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeNat" ):
                return visitor.visitTypeNat(self)
            else:
                return visitor.visitChildren(self)


    class TypeBottomContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOTTOM_TYPE(self):
            return self.getToken(stellaParser.BOTTOM_TYPE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeBottom" ):
                return visitor.visitTypeBottom(self)
            else:
                return visitor.visitChildren(self)


    class TypeParensContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self.type_ = None # StellatypeContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeParens" ):
                return visitor.visitTypeParens(self)
            else:
                return visitor.visitChildren(self)


    class TypeFunContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self._stellatype = None # StellatypeContext
            self.paramTypes = list() # of StellatypeContexts
            self.returnType = None # StellatypeContext
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_43(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_43, 0)
        def Surrogate_id_SYMB_2(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_2, 0)
        def Surrogate_id_SYMB_3(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_3, 0)
        def Surrogate_id_SYMB_8(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_8, 0)
        def stellatype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.StellatypeContext)
            else:
                return self.getTypedRuleContext(stellaParser.StellatypeContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeFun" ):
                return visitor.visitTypeFun(self)
            else:
                return visitor.visitChildren(self)


    class TypeForAllContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self._StellaIdent = None # Token
            self.types = list() # of Tokens
            self.type_ = None # StellatypeContext
            self.copyFrom(ctx)

        def FORALL(self):
            return self.getToken(stellaParser.FORALL, 0)
        def Surrogate_id_SYMB_25(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_25, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)

        def StellaIdent(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.StellaIdent)
            else:
                return self.getToken(stellaParser.StellaIdent, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeForAll" ):
                return visitor.visitTypeForAll(self)
            else:
                return visitor.visitChildren(self)


    class TypeRecordContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self._recordFieldType = None # RecordFieldTypeContext
            self.fieldTypes = list() # of RecordFieldTypeContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_4(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_4, 0)
        def Surrogate_id_SYMB_5(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_5, 0)
        def recordFieldType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stellaParser.RecordFieldTypeContext)
            else:
                return self.getTypedRuleContext(stellaParser.RecordFieldTypeContext,i)

        def Surrogate_id_SYMB_0(self, i:int=None):
            if i is None:
                return self.getTokens(stellaParser.Surrogate_id_SYMB_0)
            else:
                return self.getToken(stellaParser.Surrogate_id_SYMB_0, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeRecord" ):
                return visitor.visitTypeRecord(self)
            else:
                return visitor.visitChildren(self)


    class TypeListContext(StellatypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stellaParser.StellatypeContext
            super().__init__(parser)
            self._stellatype = None # StellatypeContext
            self.types = list() # of StellatypeContexts
            self.copyFrom(ctx)

        def Surrogate_id_SYMB_13(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_13, 0)
        def Surrogate_id_SYMB_14(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_14, 0)
        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeList" ):
                return visitor.visitTypeList(self)
            else:
                return visitor.visitChildren(self)



    def stellatype(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = stellaParser.StellatypeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_stellatype, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 688
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                localctx = stellaParser.TypeBoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 609
                self.match(stellaParser.Surrogate_id_SYMB_32)
                pass

            elif la_ == 2:
                localctx = stellaParser.TypeNatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 610
                self.match(stellaParser.Surrogate_id_SYMB_33)
                pass

            elif la_ == 3:
                localctx = stellaParser.TypeFunContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 611
                self.match(stellaParser.Surrogate_id_SYMB_43)
                self.state = 612
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 621
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 17652315607080) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 153633) != 0):
                    self.state = 613
                    localctx._stellatype = self.stellatype(0)
                    localctx.paramTypes.append(localctx._stellatype)
                    self.state = 618
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 614
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 615
                        localctx._stellatype = self.stellatype(0)
                        localctx.paramTypes.append(localctx._stellatype)
                        self.state = 620
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 623
                self.match(stellaParser.Surrogate_id_SYMB_3)
                self.state = 624
                self.match(stellaParser.Surrogate_id_SYMB_8)
                self.state = 625
                localctx.returnType = self.stellatype(14)
                pass

            elif la_ == 4:
                localctx = stellaParser.TypeForAllContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 626
                self.match(stellaParser.FORALL)
                self.state = 630
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==83:
                    self.state = 627
                    localctx._StellaIdent = self.match(stellaParser.StellaIdent)
                    localctx.types.append(localctx._StellaIdent)
                    self.state = 632
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 633
                self.match(stellaParser.Surrogate_id_SYMB_25)
                self.state = 634
                localctx.type_ = self.stellatype(13)
                pass

            elif la_ == 5:
                localctx = stellaParser.TypeRecContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 635
                self.match(stellaParser.Surrogate_id_SYMB_65)
                self.state = 636
                localctx.var = self.match(stellaParser.StellaIdent)
                self.state = 637
                self.match(stellaParser.Surrogate_id_SYMB_25)
                self.state = 638
                localctx.type_ = self.stellatype(12)
                pass

            elif la_ == 6:
                localctx = stellaParser.TypeTupleContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 639
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 648
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 17652315607080) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 153633) != 0):
                    self.state = 640
                    localctx._stellatype = self.stellatype(0)
                    localctx.types.append(localctx._stellatype)
                    self.state = 645
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 641
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 642
                        localctx._stellatype = self.stellatype(0)
                        localctx.types.append(localctx._stellatype)
                        self.state = 647
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 650
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 7:
                localctx = stellaParser.TypeRecordContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 651
                self.match(stellaParser.Surrogate_id_SYMB_4)
                self.state = 652
                localctx._recordFieldType = self.recordFieldType()
                localctx.fieldTypes.append(localctx._recordFieldType)
                self.state = 657
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 653
                    self.match(stellaParser.Surrogate_id_SYMB_0)
                    self.state = 654
                    localctx._recordFieldType = self.recordFieldType()
                    localctx.fieldTypes.append(localctx._recordFieldType)
                    self.state = 659
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 660
                self.match(stellaParser.Surrogate_id_SYMB_5)
                pass

            elif la_ == 8:
                localctx = stellaParser.TypeVariantContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 662
                self.match(stellaParser.Surrogate_id_SYMB_11)
                self.state = 671
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==83:
                    self.state = 663
                    localctx._variantFieldType = self.variantFieldType()
                    localctx.fieldTypes.append(localctx._variantFieldType)
                    self.state = 668
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==1:
                        self.state = 664
                        self.match(stellaParser.Surrogate_id_SYMB_0)
                        self.state = 665
                        localctx._variantFieldType = self.variantFieldType()
                        localctx.fieldTypes.append(localctx._variantFieldType)
                        self.state = 670
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 673
                self.match(stellaParser.Surrogate_id_SYMB_12)
                pass

            elif la_ == 9:
                localctx = stellaParser.TypeListContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 674
                self.match(stellaParser.Surrogate_id_SYMB_13)
                self.state = 675
                localctx._stellatype = self.stellatype(0)
                localctx.types.append(localctx._stellatype)
                self.state = 676
                self.match(stellaParser.Surrogate_id_SYMB_14)
                pass

            elif la_ == 10:
                localctx = stellaParser.TypeUnitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 678
                self.match(stellaParser.Surrogate_id_SYMB_34)
                pass

            elif la_ == 11:
                localctx = stellaParser.TypeTopContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 679
                self.match(stellaParser.TOP_TYPE)
                pass

            elif la_ == 12:
                localctx = stellaParser.TypeRefContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 680
                self.match(stellaParser.REF_TYPE)
                self.state = 681
                localctx.type_ = self.stellatype(4)
                pass

            elif la_ == 13:
                localctx = stellaParser.TypeBottomContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 682
                self.match(stellaParser.BOTTOM_TYPE)
                pass

            elif la_ == 14:
                localctx = stellaParser.TypeVarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 683
                localctx.name = self.match(stellaParser.StellaIdent)
                pass

            elif la_ == 15:
                localctx = stellaParser.TypeParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 684
                self.match(stellaParser.Surrogate_id_SYMB_2)
                self.state = 685
                localctx.type_ = self.stellatype(0)
                self.state = 686
                self.match(stellaParser.Surrogate_id_SYMB_3)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 695
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = stellaParser.TypeSumContext(self, stellaParser.StellatypeContext(self, _parentctx, _parentState))
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_stellatype)
                    self.state = 690
                    if not self.precpred(self._ctx, 11):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                    self.state = 691
                    self.match(stellaParser.Surrogate_id_SYMB_21)
                    self.state = 692
                    localctx.right = self.stellatype(12) 
                self.state = 697
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RecordFieldTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.label = None # Token
            self.type_ = None # StellatypeContext

        def Surrogate_id_SYMB_7(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_7, 0)

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_recordFieldType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecordFieldType" ):
                return visitor.visitRecordFieldType(self)
            else:
                return visitor.visitChildren(self)




    def recordFieldType(self):

        localctx = stellaParser.RecordFieldTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_recordFieldType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 698
            localctx.label = self.match(stellaParser.StellaIdent)
            self.state = 699
            self.match(stellaParser.Surrogate_id_SYMB_7)
            self.state = 700
            localctx.type_ = self.stellatype(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariantFieldTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.label = None # Token
            self.type_ = None # StellatypeContext

        def StellaIdent(self):
            return self.getToken(stellaParser.StellaIdent, 0)

        def Surrogate_id_SYMB_7(self):
            return self.getToken(stellaParser.Surrogate_id_SYMB_7, 0)

        def stellatype(self):
            return self.getTypedRuleContext(stellaParser.StellatypeContext,0)


        def getRuleIndex(self):
            return stellaParser.RULE_variantFieldType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariantFieldType" ):
                return visitor.visitVariantFieldType(self)
            else:
                return visitor.visitChildren(self)




    def variantFieldType(self):

        localctx = stellaParser.VariantFieldTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_variantFieldType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 702
            localctx.label = self.match(stellaParser.StellaIdent)
            self.state = 705
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 703
                self.match(stellaParser.Surrogate_id_SYMB_7)
                self.state = 704
                localctx.type_ = self.stellatype(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expr_sempred
        self._predicates[15] = self.stellatype_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 29)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 28)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 27)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 24)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 23)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 22)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 12:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 13:
                return self.precpred(self._ctx, 57)
         

            if predIndex == 14:
                return self.precpred(self._ctx, 56)
         

            if predIndex == 15:
                return self.precpred(self._ctx, 31)
         

            if predIndex == 16:
                return self.precpred(self._ctx, 30)
         

            if predIndex == 17:
                return self.precpred(self._ctx, 21)
         

            if predIndex == 18:
                return self.precpred(self._ctx, 20)
         

            if predIndex == 19:
                return self.precpred(self._ctx, 1)
         

    def stellatype_sempred(self, localctx:StellatypeContext, predIndex:int):
            if predIndex == 20:
                return self.precpred(self._ctx, 11)
         




