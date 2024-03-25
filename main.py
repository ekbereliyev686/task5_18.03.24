# 1. Maliyyə Sənayesi:
# Tapşırıq: Büdcə aləti yaradın
# Təsvir: Tələbələr aylıq xərclər və gəlirlər üçün daxil olan Python proqramı yaradacaqlar. Funksiya ümumi xərcləri, ümumi gəliri almalı və ayın qalan büdcəsini hesablamalıdır.



def finance():
    cost_list=[]
    for i in range(3):
        product=(input("Xerclediyinizin adini daxil edin :"))
        price=int(input("Xerclediyinizin qiymetini daxil edin :"))
        cost=0
        cost+=price
        month_cost={
        "product":product,
        'price':price
        }
        cost_list.append(month_cost)   
    budget=int(input("Ayliq geliri daxil edin:"))

    residue=budget-cost
    
    print(f"Szin ayliq xercleriniz cemi {cost} . Ayliq qaliq budceniz {residue}")

finance()





# 2.Səhiyyə Sənayesi:
# Tapşırıq: BMI Kalkulyatorunu tərtib edin.
# Təsvir: Python funksiyalarından istifadə edərək Bədən Kütləsi İndeksi (BMI) kalkulyatoru yaradın. İstifadəçilərdən parametr olaraq çəkilərini (kiloqramla) və boylarını (metrlə) daxil etmələri təklif edilməlidir və proqram BMI-ni hesablayıb çap etməlidir. Əlavə olaraq, istifadəçiyə BMI kateqoriyası (məsələn, az çəki, normal çəki, artıq çəki və ya piylənmə) haqqında rəy bildirin.



def bmi_calculation(height,weight):
    bmi=int(weight/height**2)
    if bmi <=18:
        print(f"Siz cekiniz azdir. Sizin beden kutle indeksiniz {bmi}")
    elif bmi >18 and bmi<=25:
        print(f"Sizin cekiniz normaldir. Sizin beden kutle indeksiniz {bmi} ")
    elif bmi >25 and bmi<30:
        print(f"Sizde artiq ceki var. Sizin beden kutle indeksiniz {bmi} ")
    else:
        print(f"Siz obezsiniz. Sizin beden kutle indeksiniz {bmi}")


bmi_calculation(1.50,88)



# 3.Təhsil Sənayesi:
# Tapşırıq: Tələbə Qiymət Kalkulyatoru.
# Təsvir: Müxtəlif fənlər üzrə topladıqları ballara əsasən tələbələrin qiymətlərini hesablamaq üçün proqram yaradın. İstifadəçidən hər bir fənn üzrə xalları daxil etməyi, orta qiyməti hesablamağı və onların fəaliyyəti haqqında rəy bildirməyi təklif edin (məsələn, məktub qiymətləri). Orta hesablamaq və qiyməti müəyyən etmək üçün funksiyalardan istifadə edin və qiymətləndirmə meyarları üçün if-else ifadələrini birləşdirin. Qeyd: Bu taskdan bütün biliklərinizi maksimum istifadə edin və məntiqli kod yazmağa çalışın



algebra=int(input(" Cebrden aldiginiz qiymeti daxil edin :"))
chemistry=int(input("Kimyadan aldiginiz qiymeti daxil edin :"))
biology=int(input("Biologiyuadan aldiginiz  qiymeti daxil edin :"))
physics=int(input("Fizikadan aldiginiz qiymeti daxil edin :"))
geography=int(input("Cografiyadan aldiginiz qiymeti daxil edin :"))

   

def students(*args):
    total=0
    for a in args:
        total+=a/5

    if total>91 and total<100:
       print(f"Sizin yekun baliniz {total} .Qiymetlendirme 'Ela'")
    elif total>81 and total<90:
        print(f"Sizin yekun baliniz {total} .Qiymetlendirme 'Cox Yaxsi'")
    elif total>71 and total<80:
        print(f"Sizin yekun baliniz {total} .Qiymetlendirme 'Yaxsi'")
    elif total>61 and total<70:
        print(f"Sizin yekun baliniz {total} .Qiymetlendirme 'Kafi'")
    elif total>51 and total<60:
        print(f"Sizin yekun baliniz {total} .Qiymetlendirme 'Qenaetbexs'")
    else:
        print(f"Sizin yekun baliniz {total} .Qiymetlendirme 'Qeyri-Kafi'")


students(algebra,chemistry,biology,physics,geography)