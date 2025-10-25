mablaq_kharid = int(input())

if mablaq_kharid > 50000 : 
    mablaq_takhfif = 0.2 * mablaq_kharid
elif 20000 <= mablaq_kharid <= 50000 : 
    mablaq_takhfif = 0.1 * mablaq_kharid
else :
    mablaq_takhfif = 0 

total = mablaq_kharid-mablaq_takhfif
print(f"{total:.0f}")  
