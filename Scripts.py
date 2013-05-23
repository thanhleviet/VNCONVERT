# Simple script for conversion of Vietnamese encoding
# Use at your own risk!!
# Ninomax - thanhlv@oucru.org
# 19/01/2010 - Version 1.0
# Mapping team - The Oxford University Clinical Research Unit, Ha Noi
import arcgisscripting
gp = arcgisscripting.create(9.3)
def Convert(str,s,d):
    global _Unicode, _TCVN3, _KhongDau
    result = u''
    for c in str:
        idx = s.find(c)
        if idx >= 0:
            c = d[idx]
        result += c
    return result
# Array of characters (Using Tuple instead of List)
_Unicode = (
    #'Ã?Ã?ÄƒÄ?Ä?Ä?ÃªÃŠÃ?Ã?Æ?Æ?Æ?Æ?'
    u'âÂăĂđĐêÊôÔơƠưƯ'
    #u'\xe2\xc2\u0103\u0102\u0111\u0110\xea\xca\xf4\xd4\u01a1\u01a0\u01b0\u01af'
    #'Ã?Ã?Ã?Ã?áº?áº?Ã?Ãƒáº?áº?áº?áº?áº?áº?áº?áº?áº?áºªáº?áº?áº?áº?áº?áº?áº?áº?áºµáº?áº?áº?'
    u'áÁàÀảẢãÃạẠấẤầẦẩẨẫẪậẬắẮằẰẳẲẵẴặẶ'
    #u'\xe1\xc1\xe0\xc0\u1ea3\u1ea2\xe3\xc3\u1ea1\u1ea0\u1ea5\u1ea4\u1ea7\u1ea6\u1ea9\u1ea8\u1eab\u1eaa\u1ead\u1eac\u1eaf\u1eae\u1eb1\u1eb0\u1eb3\u1eb2\u1eb5\u1eb4\u1eb7\u1eb6'
    #'Ã?Ã?Ã?Ã?áº?áººáº?áº?áº?áº?áº?áº?á??á??á?ƒá??á??á??á??á??Ã?Ã?Ã?ÃŒá??á??Ä?Ä?á??á?Š'
    u'éÉèÈẻẺẽẼẹẸếẾềỀểỂễỄệỆíÍìÌỉỈĩĨịỊ'
    #u'\xe9\xc9\xe8\xc8\u1ebb\u1eba\u1ebd\u1ebc\u1eb9\u1eb8\u1ebf\u1ebe\u1ec1\u1ec0\u1ec3\u1ec2\u1ec5\u1ec4\u1ec7\u1ec6\xed\xcd\xec\xcc\u1ec9\u1ec8\u0129\u0128\u1ecb\u1eca'
    #'Ã?Ã?Ã?Ã?á??á?ŽÃµÃ?á??á?Œá??á??á??á??á??á??á??á??á??á??á??á?šá??á?œá?Ÿá?žá??á??á??á??'
    u'óÓòÒỏỎõÕọỌốỐồỒổỔỗỖộỘớỚờỜởỞỡỠợỢ'
    #u'\xf3\xd3\xf2\xd2\u1ecf\u1ece\xf5\xd5\u1ecd\u1ecc\u1ed1\u1ed0\u1ed3\u1ed2\u1ed5\u1ed4\u1ed7\u1ed6\u1ed9\u1ed8\u1edb\u1eda\u1edd\u1edc\u1edf\u1ede\u1ee1\u1ee0\u1ee3\u1ee2'
    #'ÃºÃšÃ?Ã?á??á??Å?Å?á??á??á??á??á??á?ªá??á??á??á??á??á??á??á??á??á??á??á??á?µá??Ã?Ã?'
    u'úÚùÙủỦũŨụỤứỨừỪửỬữỮựỰỳỲỷỶỹỸỵỴýÝ'
    #u'\xfa\xda\xf9\xd9\u1ee7\u1ee6\u0169\u0168\u1ee5\u1ee4\u1ee9\u1ee8\u1eeb\u1eea\u1eed\u1eec\u1eef\u1eee\u1ef1\u1ef0\u1ef3\u1ef2\u1ef7\u1ef6\u1ef9\u1ef8\u1ef5\u1ef4\xfd\xdd'
)
_KhongDau = (
    u'aAaAdDeEoOoOuU'
    u'aAaAaAaAaAaAaAaAaAaAaAaAaAaAaA'
    u'eEeEeEeEeEeEeEeEeEeEiIiIiIiIiI'
    u'oOoOoOoOoOoOoOoOoOoOoOoOoOoOoO'
    u'uUuUuUuUuUuUuUuUuUuUyYyYyYyYyY'
)
_TCVN3= (
 	#'Â?Â?Â?Â?Â?Â?ÂªÂ?Â?Â?Â?Â?Â?Â?'
    u'©¢¨¡®§ª£«¤¬¥­¦'
    #'\xa9\xa2\xa8\xa1\xae\xa7\xaa\xa3\xab\xa4\xac\xa5\xad\xa6'
    #'Â?Â?ÂµÂµÂ?Â?Â?Â?Â?Â?ÃŠÃŠÃ?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Â?Â?Â?Â?Â?Â?Â?Â?Ã?Ã?'
    u'¸¸µµ¶¶··¹¹ÊÊÇÇÈÈÉÉËË¾¾»»¼¼½½ÆÆ'
    #'\xb8\xb8\xb5\xb5\xb6\xb6\xb7\xb7\xb9\xb9\xca\xca\xc7\xc7\xc8\xc8\xc9\xc9\xcb\xcb\xbe\xbe\xbb\xbb\xbc\xbc\xbd\xbd\xc6\xc6'
    #'Ã?Ã?ÃŒÃŒÃŽÃŽÃ?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?ÃœÃœÃžÃž'
    u'ÐÐÌÌÎÎÏÏÑÑÕÕÒÒÓÓÔÔÖÖÝÝ××ØØÜÜÞÞ'
    #u'\xcf\xcf\xd1\xd1\xd5\xd5\xd2\xd2\xd3\xd3\xd4\xd4\xd6\xd6\xdd\xdd\xd7\xd7\xd8\xd8\xdc\xdc\xde\xde'
    #'Ã?Ã?ÃŸÃŸÃ?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?ÃªÃªÃ?Ã?Ã?Ã?Ã?Ã?'
    u'ããßßááââääèèååææççééííêêëëììîî'
    #'\xe2\xe2\xe4\xe4\xe8\xe8\xe5\xe5\xe6\xe6\xe7\xe7\xe9\xe9\xed\xed\xea\xea\xeb\xeb\xec\xec\xee\xee'
    #'Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?Ã?ÃµÃµÃ?Ã?Ã?Ã?Ã?Ã?ÃºÃºÃ?Ã?Ã?Ã?Ã?Ã?Ã?Ã?'
    u'óóïïññòòôôøøõõöö÷÷ùùúúûûüüþþýý'
    #'\xf3\xf3\xef\xef\xf1\xf1\xf2\xf2\xf4\xf4\xf8\xf8\xf5\xf5\xf6\xf6\xf7\xf7\xf9\xf9\xfa\xfa\xfb\xfb\xfc\xfc\xfe\xfe\xfd\xfd'
)

def ConvertEncoding(input_fc,input_fd,newfd,sE,dE):
    global gp
    rows = gp.updatecursor(input_fc)
    result = gp.GetCount_management(input_fc)
    count = int(result.GetOutput(0))
    gp.SetProgressor("step", "Reading", 0, count, 1)
    for row in iter(rows.next, None):
        string1 = row.GetValue(input_fd)
        if  string1.strip() <> "":
            newvalue =  Convert(row.GetValue(input_fd),sE,dE)
            row.SetValue(newfd,newvalue)
            rows.UpdateRow(row)
        else:
            row.SetValue(newfd,"")
            rows.UpdateRow(row)
        gp.SetProgressorPosition()
    gp.ResetProgressor()
    del rows
    del row
#Input paramaters
inputShapefile = gp.GetParameterAsText(0)
inputFields = gp.GetParameterAsText(1)
outputShapefile = gp.GetParameterAsText(2)
from_to = gp.GetParameterAsText(3)
#Processing block
gp.toolbox = "management"
try:
    #Copy to new shapefile
    gp.CopyFeatures_management(inputShapefile,outputShapefile)
    # Add new field for storing result
    #gp.AddField(outputShapefile,newField,"TEXT","#","#",254)#,"#","NON_NULLABLE","NON_REQUIRED","#")
    #Processing conversion of encoding
    inputFL = inputFields.split(";")
    for inputField in inputFL:
        if from_to =="TCVN3 sang KhongDau":
            ConvertEncoding(outputShapefile,inputField,inputField,_TCVN3,_KhongDau)
        elif from_to =="TCVN3 sang Unicode":
            ConvertEncoding(outputShapefile,inputField,inputField,_TCVN3,_Unicode)
        elif from_to =="Unicode sang KhongDau":
            ConvertEncoding(outputShapefile,inputField,inputField,_Unicode,_KhongDau)
        elif from_to =="Unicode sang TCVN3":
            ConvertEncoding(outputShapefile,inputField,inputField,_Unicode,_TCVN3)
    gp.AddMessage("Finish!")
    gp.AddMessage(from_to)
#Free resources
except:
    gp.GetMessage(2)
del gp
