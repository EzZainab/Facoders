'''
** لا تنسوا التعديل على readme اذا استخدمتوا جت هب
week-4: Lists and for loop

المطلوب بهذا التحدي كتابة برنامج يقوم بالطلب من المستخدم (الأهل أو المعلمة) بإدخال اسم الطالب٫ فيعيد اسم الطالب بالإضافة إلى مجموع علاماته.
*أرجو كتابة رسالة الطلب كما هي في الأسفل
Enter student's name

علامات الطلاب وأسماؤهم مخزنة بداخل القوائم التالية٬ أرجو نسخها كما هي:
s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]

ملاحظة:
إذا أدخل المستخدم اسم غير موجود ستظهر له ملاحظة بأن الاسم غير مسجل٫ والمجموع صفر

مثال:
Enter student's name: Ayamn
Student is not recorded 0

مثال ٢:
Enter student's name: Sami
Sami 96

لتسليم التحدي املأي الاستمارة التالية:
https://goo.gl/forms/DsQzfc06FpDsHKcM2

ملاحظات:
* آخر يوم للتسليم هو يوم الأحد
** لتسليم التحدي بدون استخدام جت هب ارسلي صورة على الخاص للكود، تأكدي منها جيدا قبل الارسال لا تقبل الا صورة واحدة ثم املأي الاستمارة'''

s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]
name=input("Enter student's name: ")
if (name==s1[0]):
    print(s1[0] +" " + str(sum(s1[1:6])))
elif(name==s2[0]):
    print(s2[0] +" " + str(sum(s2[1:6])))
elif(name==s3[0]):
    print(s3[0] +" " + str(sum(s3[1:6])))
else:
    print("Student is not recorded 0")
