#В институте биоинформатики по офису передвигается робот. Недавно студенты из группы программистов написали для него программу, по которой робот, когда заходит в комнату, считает количество программистов в ней и произносит его вслух: "n программистов".
#Для того, чтобы это звучало правильно, для каждого n нужно использовать верное окончание слова.
#Напишите программу, считывающую с пользовательского ввода целое число n (неотрицательное), выводящее это число в консоль вместе с правильным образом изменённым словом "программист", для того, чтобы робот мог нормально общаться с людьми, например: 1 программист, 2 программиста, 5 программистов.
#В комнате может быть очень много программистов. Проверьте, что ваша программа правильно обработает все случаи, как минимум до 1000 человек.
#Дополнительный комментарий к условию:
#Обратите внимание, что задача не так проста, как кажется на первый взгляд. Если ваше решение не проходит какой-то тест, это значит, что вы не рассмотрели какой-то из случаев входных данных (число программистов
#0≤n≤1000). Обязательно проверяйте свои решения на дополнительных значениях, а не только на тех, что приведены в условии задания.
#Так как задание повышенной сложности, вручную код решений проверяться не будет. Если вы столкнулись с ошибкой в первых четырёх тестах, проверьте, что вы используете только русские символы для ответа. В остальных случаях ищите ошибку в логике работы программы.

n = (input())

if n in ['2','3','4','22', '23', '24', '42', '43', '44','62', '63', '64', '82', '83', '84',
         '102', '103','104', '122', '123', '124','142', '143', '144','162', '163', '164','182', '183', '184',
         '202','203','204','222', '223', '224', '242', '243', '244','262', '263', '264', '282', '283', '284',
         '302','303','304','322', '323', '324', '342', '343', '344','362', '363', '364', '382', '383', '384',
         '402','403','404','422', '423', '424', '442', '443', '444','462', '463', '464', '482', '483', '484',
         '502','503','504','522', '523', '524', '542', '543', '544','562', '563', '564', '582', '583', '584',
         '602','603','604','622', '623', '624', '642', '643', '644','662', '663', '664', '682', '683', '684',
         '702','703','704','722', '723', '724', '742', '743', '744','762', '763', '764', '782', '783', '784',
         '802','803','804','822', '823', '824', '842', '843', '844','862', '863', '864', '882', '883', '884',
         '902','903','904','922', '923', '924', '942', '943', '944','962', '963', '964', '982', '983', '984',
         '32', '33','34','52', '53','54','72', '73','74','92', '93','94',
         '132', '133','134','152', '153','154','172', '173','174','192', '193','194',
         '232', '233','234','252', '523','254','272', '273','274','292', '293','294',
         '332', '333','334','352', '353','354','372', '373','374','392', '393','394',
         '432', '433','434','452', '453','454','472', '473','474','492', '493','494',
         '532', '533','534','552', '553','554','572', '573','574','592', '593','594',
         '632', '633','634','652', '653','654','672', '673','674','692', '693','694',
         '732', '733','734','752', '753','754','772', '773','774','792', '793','794',
         '832', '833','834','852', '853','854','872', '873','874','892', '893','894',
         '932', '933','934','952', '953','954','972', '973','974','992', '993','994',]:
    print (n + ' программиста')
elif n in ['1','21','41','61','81','101','121','141','161','181','201','221','241','261','281','301','321','341','361', '381',
           '401','421','441','461','481','501','521','541','561','581','601','621','641','661','681',
           '701','721','741','761','781','801','821','841','861','881','901','921','941','961','981',
           '31','51','71','91','131','151','171','191','231','251','271','291','331','351','371','391',
           '431','451','471','941','531','551','571','591','631','651','671','691','731','751','771','791',
           '831','851','871','891','931','951','971','991']:
   print(n + ' программист')
else:
    print(n + ' программистов')
