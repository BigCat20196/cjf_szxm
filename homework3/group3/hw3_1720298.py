'''2k = -9    变量命名不能是数字开头
    #if 2k>= 0:     if不该缩进

    #with = 2k +"正数"    with是关键字不能用于变量名
    
    

else:

    #print(2K+ '负数")   #符号错误:单双引号混用;变量名错误;int和str不能用+连接
    
'''
#正确的如下
_2k = -9
if _2k>= 0:
    with_ = str(_2k) +"正数"
    print(with_)
else:
    print(_2k, '负数')
    



