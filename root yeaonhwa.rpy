#Персонажи и их значение
define s = Character('Юн Сынхён', color="#4682B4", image='shc')
define y = Character('Син Ёнхва', color="#DEB887")
define l = Character('СяоЛу', color="#4AB077")
define t = Character('Такеши', color="#B03080")
define p = Character('Офицер Пак', color="#c8ffc8")
define oxrannik = Character('Охранник', color="#c8ffc8")
define criminalist = Character('Криминалист', color="#c8ffc8")
define goskim = Character('Господин Ким')
define of1 = Character('Офицер 1')
define of2 =Character ('Офицер 2')

init python: #Енхва
    loyaltyy = 0#помарка для меня, а так береться из пролога
    vscritie_loyalti = 0
    reactionlutrushobi_loyalti = 0
    infavtrushobi=loyalti = 0 
    dogovor=0
    nadaviti=False
    molodec=False
    dolboeb=0
    vmeshatca=0
    podojdat=0

# Игра начинается здесь:
label root_enhwa:

#Локация – квартира. 
s "Я думаю, что версия капитана более правдоподобна. "

y "Сначала - поговорим с отцом убитой и, если повезет, с дворецким. Потом будем отталкиваться от результата."

"Ёнхва достал из заднего кармана брюк телефон. С минуту он искал что-то. Атмосфера всё же была чрезмерно угнетающей, и по большей части, её создавал Юн Сынхен. "
"Необходимость находится среди преступников без возможности их задержать, вводила его в бешенство. Помимо этого он замечал настороженные взгляды капитана." 
"Лу вздохнул и заговорил первым."

l "Я так понимаю, вы все решили? Если да, то я пошел." 

y "Хорошо. Пиши, если узнаешь что-то новое."

"Ёнхва встал с дивана, когда Лу подошел к нему. Син слегка похлопал того по плечу и улыбнулся. Лу проигнорировал жест старшего и продолжил свой путь по направлению к входной двери. "

"Сынхен облегченно выдохнул, как только захлопнулась входная дверь. Всё же, СяоЛу чересчур сильно напрягал Юна. "
"Ёнхва вопросительно взглянул на Такеши. Хакер удивленно поднял голову, замечая резко оборвавшийся диалог и повисшую тишину. "
"Выражение лица Ёнхва показалось Сынхену спокойным, можно сказать даже ободряющим. Не смотря на это, Такеши замешкался, будто обдумывал свои дальнейшие действия. "

y "А ты пробиваешь транзакцию."

t "А я пробиваю транзакцию… А зачем я пробиваю транзакцию?"

y "Оттуда можно узнать много чего полезного. Например, кто ее делал, зачем ее делал, кому ее делал, логика понятна?"

t "Понятна. Кажется. "


y "Так что ты делаешь?"


t "Я пробиваю транзакцию."

y "Вот и славно. А информацию присылаешь мне. "


if loyaltyy == 1:
    "Син разговаривал с Такеши подозрительно мягко, без каких либо шутливых слов, и раскладывал для него каждое действие пошагово, уточняя какие либо детали. "
    "Словно говорил с маленьким ребенком. Сынхен в очередной раз поражался умению Ёнхва находить подход к людям. "

if loyaltyy == 0:
    "Син разговаривал с Такеши подозрительно мягко, без каких либо шутливых слов, нежели с Сынхёном, и раскладывал для него каждое действие пошагово, уточняя какие либо детали."
    " И даже сейчас мужчина продиктовал адрес своей электронной почты еще раз, чтобы точно убедиться о направлении информации в нужное место."

t "Все записал. Слушаю и повинуюсь. "

"Смартфон неожиданно завибрировал. Ёнхва приподнял брови, проследив взглядом до источника звука. Он взял телефон, просматривая уведомления. Зависнув на пару секунд и большим пальцем смахивая ненужное в сторону, он наконец отправил короткое сообщение и игриво ухмыльнулся, явно довольный собой."

y "Поехали, пупсик. "

"Мужчина демонстративно помахал телефоном, привлекая внимание остальных. "

if loyaltyy == 1:

  s "Появились новые данные?"

  y "Пока еще нет, но есть одна мысль."

if loyaltyy == 0:
  "Не дождавшись ответной реакции, Ёнхва мгновенно изменился в лице и убрал гаджет в передний карман своих брюк. "
  s "…"

  y "Что?"

  s "Ничего."

  y "Вот и поговорили. "

  "Сынхен раздражался от вечной недосказанности Ёнхва. Тот делал все самостоятельно, абсолютно не интересуясь мнением сержанта, а только после удосужился рассказать о намерениях Юну. "
  "Возможно, капитан считал, что поступает верно, но Сынхен предполагал, что напарники - это люди, которые в своем общем деле полностью доверяют друг другу. И потому-то он и сердился, что рамки его представлений с громким треском разрушались." 
s"Мы сейчас едем к отцу убитой?"

y "Получается, что так. Собирайся. "

s "А с ним что?"

"Сынхен кивнул в сторону Такеши."

y "А он тут посидит. Ему отсвечивать нельзя."

t "Да я и не собирался. У тебя покушать есть?"

y "Все что найдешь - все твоё. "

t "Уху! Вкусняшки!"

"Сынхен недовольно вздохнул и направился на выход. Ему совершенно не по душе был стиль работы начальника, но выбор был невелик. К тому же Ёнхва определенно знает, что делает, даже если другим это не нравится."
" Мужчина ведь довольно давно работает в полиции, да и к тому же, был начитанным и сосредоточенным. Иногда даже казался чересчур серьезным, собранным как сегодня. "
"Юн не готов был признаться себе, но начинал привыкать и даже проникаться уважением к Сину за его отношение к делу. "

y "Такеши, мы ушли. "

"Сынхен вышел из квартиры. За ним последовал Ёнхва, тихо прикрывая за собой дверь."


#Локация - парковка у дома Ёнхва. (парковка бек, спрайты снизу)
"Сынхен быстрым шагом направлялся к машине, оставленной капитаном на стоянке возле здания. Ёнхва, еле поспевая за ним, насвистывал ту же мелодию, что и в коридоре. Он прекрасно осознавал, что ключи до сих пор у него в кармане и самодовольно ухмылялся. Юн остановился, ожидая напарника." 

s "Вы слишком расслаблены, нет?"

y "С чего ты это взял? Я обдумываю, что мы будем говорить отцу погибшей. "

s "Как-то странно вы обдумываете."

"Он посмотрел на руки мужчины, что держали связку ключей, которые бились друг о друга и неприятно звенели."

y "Работа работой, но для начала кофе, потом все остальное. Садись."


#Локация - машина. (все цг)

"Сынхен вот уже семь минут ждет своего напарника в машине. Они остановились у какой-то маленькой кофейни, которую, наверное, Юн бы даже не заметил, проходя мимо. "
"Солнце уже было уже не таким активным, постепенно скрываясь за рядами домов. Парень высматривал силуэт Ёнхва и через пару минут все же заметил знакомую фигуру. "
"Мужчина обогнул машину спереди и занял свое место за рулем. Руки его были заняты стаканами с кофе, меньший из которых он торжественно передал Сынхену."
"Освободившись от ноши, капитан сразу достал из бардачка сигарету. Салон с наглухо закрытыми окнами моментально наполнился крепким дымом."

s "А вы никогда не задумывались, что курить за рулем - опасно? "

y "А что в этом опасного?"

"Машина двинулась вперед. Син выехал на главную дорогу, следуя навигатору к дому Кан Наён. "

s 'В смысле "что"? А если сигарета упадет на вас? А если вы отвлечетесь? А если…'

y "А если я сейчас резко заторможу ты ударишься башкой об панель или обольешься очень горячим кофе."

s "…"

y "Что ты от меня хочешь? Ты до этого ездил со мной и все было нормально, тебя за жопу кто-то укусил? "

s "При чем тут моя жопа? Почему вы постоянно шутите свои тупые пошлые шутки? Вы - капитан! Вы мой начальник!"
s" Но вы продолжаете вести себя как маленький, невоспитанный… "

y "Как кто?"

s "…"

y "Не-не-не. Что ты замолчал? Мне прям интересно."

s "Вы ведете себя, как неразумный ребенок! Постоянно говорите загадками, тащите меня куда-то, работаете не по правилам! И втягиваете в это Меня! "
s "Я ваш напарник, а не секретарша! Вы с самого первого дня издеваетесь надо мной! Вы специально это делаете?!"

if loyaltyy == 1:

  y "…"

  "Ёнхва бросил взгляд на Сынхен и проехав некоторое время молча, открыл окно с его стороны. "
  y "Все сказал?"

  s "Да."

  y "Ну и славно. Наконец-то ты начал говорить словами через рот. Кажется все-таки офицер Пак должен мне десятку. "


  s "Что?"


  y "Он думал, что твой язык так глубоко в заднице, что тебе понадобится хотя бы месяц. Но нет, ты прям молодец, справился раньше. "

  s "Что?"

  y "Я терпеть не могу лизоблюдов и подхалимов. Если тебе что-то не нравится - скажи в лицо. Это лучше, чем сидеть и крыть хуями за спиной. "

  s "А чем эта ситуация отличается от ситуации в баре? Я же мог вам отказать."

  "Выражение лица капитана из расслабленного стало серьезным. "

  y "Не путай честность и пренебрежение субординацией. Я, как ты и сказал, капитан. Поэтому, если разговор касается дела, то решения, как и их последствия - это уже моя юрисдикция. "
  $molodec=True

if loyaltyy == 0: 

  "Ёнхва резко свернул на обочину и надавил на тормоз. Он нахмурился, уставившись вперед немигающим взглядом."

  y"Да. И?"

  s"..."

  y "Да, я делаю это специально. И что? Чего замолчал?"

  s "Капитан!"

  y "Я капитан, тут ты прав. А ты - сосунок, пришедший в отдел без году неделя и пытаешься меня учить? Если тебе что-то не нравится - отстегивай ремень и уебывай голой степью. "

  s "…"

  y "Чего заткнулся? Уже не так все хуево? А теперь слушай сюда, я тебе не твой батя и вытирать сопли я не намерен. "
  y"Ты думаешь, что отучившись с отличием в академии, имея на руках хорошие рекомендации и медали по боевым искусствам перед тобой должна разложиться красная дорожка и я должен тебя целовать в зад за то, какой ты классный? "
  y"Если быть честным - я согласился на твой перевод, только потому что ты ЗАЕБАЛ СВОЕГО КАПИТАНА КИМА СВОИМИ ВЫЕБОНАМИ!"
  y"И мне стало интересно, что такого ты мог сделать, чтобы вывести из себя самого спокойного человека, которого я знаю. И теперь я вижу."

  s "…"

  y "Подытожим. Ты, Юн Сынхен, пока работаешь в этом отделе, и моя секретарша, и слуга, и, если мне будет надо, еще и наложница. "
  y"Не нравится - вали нахуй. Остаешься - хлебало на ноль. Все всё поняли и приняли?"

  "Сынхен, невольно напрягшись и слегка вжавшись в кресло, никак не среагировал на вопрос. Немного потупив, он только поправил ремень и отвернулся к окну. "

  y "Вот и чудненько. "

  "Капитан снова завел двигатель и вернулся на дорогу. Остаток пути они преодолели в напряженном молчании. "
  $dolboeb+=1

#Локация - Дом Наён. (бек)

y "Неплохой домик.  "

s "Мы тут уже были."

y "Меня в тот раз отвлек рафинированный мудак в галстуке."

s "Ясно."

"Поднявшись на крыльцо вперед сержанта, Енхва нажал на звонок. Дверь открыл уже знакомый им дворецкий, услужливо пропуская парочку внутрь. "

#Локация - дом Наен внутри
y "Добрый день, мы в господину Киму. "

"Дворецкий кивнул и попросил подождать, отправляясь в глубину дома и оставляя полицейских в прихожей. Сынхен внимательно осмотрелся."

s "Тут слишком чисто."


y "Хах, а разве это плохо?" 

s "Наоборот. Подозрительно скорее. "


"Енхва казалось готов был ответить, но дворецкий уже вернулся, вежливо улыбаясь.  "
"Он оповестил нежданных гостей о том, что отец Наён готов принять их в собственном кабинете. Мужчина попросил следовать за ним. "
"Просторные полупустые коридоры, дорогие вазы на полу и картины на стенах - всё это встречалось им на пути. "

#Локация - кабинета отца Наён
"Они остановились напротив одной из многочисленных дверей, ничем не отличавшихся друг от друга."
" Сынхен взглянул на своего напарника, который сейчас источал лишь абсолютное спокойствие и уверенность. "

"Сам кабинет был минималистично обставлен, за широким, почти пустым столом сидел мужчина средних лет. "


y" Добрый день. Мы с вами еще не встречались. Капитан Син Енхва, Мы расследуем дело об убийстве вашей дочери Ким Наён. "

goskim "И чем я вам могу быть полезен? "

y "Для продолжения расследования, нам нужно провести вскрытие. Требуется ваше разрешение…"

goskim "А с чего вы решили, что я хочу, чтобы вскрытие было?"


"Сынхен впервые видел, чтобы его начальника кто-то заткнул таким образом. На секунду ему показалось, что капитан даже растерялся. Но только на секунду. "

s "...Чтобы мы раскрыли дело? "
goskim" … Сколько вы служите в полиции, капитан?"
y "А какое это имеет значение?"
goskim "Я помню, как ваш отец с гордостью о вас отзывался. "
"Ёнхва нахмурился. Сержант буквально услышал, как заскрипели его зубы. "
goskim "Я его знал до того, как он вступил в должность комиссара и я надеялся, что у такого талантливого человека, будет такой же сын. Может, ваш отец ошибается?"
y "К чему вы клоните, господин Ким? "
goskim "Дело полиции - раскрывать преступления, а не клянчить у скорбящего отца упростить им жизнь. Не так ли?"
s '“Погодите-ка. Что сейчас происходит?”'
"Сынхен смотрел то на капитана, то на господина Кима. "
s '“При чем тут капитан и его отец? Ощущение, что этот господин Ким что-то скрывает.”'
"Сынхен уже был готов вступить в разговор, но его опередил Ёнхва. На его лице появилась улыбка, которая не соответствовала ситуации. От этого у сержанта по спине побежали мурашки. "
y "Почему вы не хотите сотрудничать с нами? Или у вас есть секреты, более страшные, чем смерть дочери?"
"Мужчина заметно напрягся. Он сжал руки в кулаки и опустил взгляд, избегая контакта с капитаном."
y 'Нормальный “скорбящий” родитель сделал бы все, чтобы нашли убийцу его ребенка. Что могло так повлиять на вас? Она нашла украденные вами деньги? '
y"Или же застала кого-то под вашим столом? О… Или она отказалась оказаться под этим столом?"
"Мимо головы Ёнхва пролетел стакан, со звоном разбиваясь об пол. Господин Ким вскочил с места. Его всего трясло от злости, лицо покраснело. "
goskim "Выметайтесь из моего дома! Вы ничего не получите! "
s '“Если мы сейчас просто уйдем, то расследование встанет. Надо что-то сделать.”'
menu:
    "Попытаться договориться": 
     $dogovor+=1
     jump dogovor
    "Попытаться надавить": 
     $nadavit = True
     jump nadaviti
label dogovor:
            "Сынхен сделал пару шагов вперед, приближаясь к отцу покойной. Сержанту было тяжело держать себя в руках, когда с ним разговаривали на повышенных тонах. "
            "Юн попытался с максимальной осторожностью подойти ближе к раздраженному мужчине и заговорить как можно спокойнее."
            s "Господин Ким, послушайте. Мы здесь для того, чтобы ускорить процесс расследования. Я думаю, что все в этой комнате заинтересованы в скорейшей поимке преступника."
            s" Я очень сочувствую вашей потере, но нам нужна ваша помощь. "
            goskim "Я непонятно выразился?"
            y "…"
            s "Прошу прощения за моего напарника. Он как и я хочет добиться истины, чтобы виновные были наказаны. Вы же не хотите, чтобы подобная ситуация произошла снова?"
            goskim "Мальчик, мне плевать на остальных. Моя дочь уже мертва, какое мне дело до проблем других людей."
            s "То есть, вам все равно? Да, она мертва и человек, который виноват в ее смерти, сейчас на свободе. Живет, ест, пьет. На это вам тоже плевать?"
            goskim "…"
            "Мужчина замер, будто отключившись от реальности. Взгляд метался из стороны в сторону, глаза наполнялись слезами, руки затряслись, а ноги подкашивались. Он сел в кресло, прикрыв лицо рукой, и устало выдохнул."
 
            goskim "Я всё подпишу."
            "Он взял в руку ручку, лежавшую неподалеку, и посмотрел на следователей. Син моментально положил перед ним бумаги. Отец Наён не стал вчитываться в каждое предложение, а просто поставил свою подпись в самом низу. "
            goskim "Я хочу знать правду о смерти моей Наён. А теперь пошли вон отсюда. "
  
            s "Мы сделаем всё, что в наших силах."
            "Мужчина лишь махнул рукой, отворачиваясь от них. "
            "Ёнхва забрал со стола подписанный документ и направился к выходу, подзывая за собой Сынхёна."
            #Локация - цг машина
            "Сынхен сел в машину, аккуратно прикрывая за собой дверь. Он до сих пор не верил, что у него получилось. Ёнхва оказался рядом, его настроение было странно приподнятым." 
            y "А ты… молодец! Не растерялся. "
  
            s "Я выполнял свою работу."
            y "Ой да ладно тебе, пупсик! Научись принимать комплименты."
            s "…" 
            s "{color=#900020}Спасибо.{/color}" 

            'Капитан быстро нашел номер судмеда и нажал на кнопку “вызов”. '

            y "Алло. Да, дали добро, подпись есть, завтра завезу. Хорошо. Договорились."
            jump continue

label nadaviti:
             "Сынхен сделал шаг навстречу. "

             s "Вы отдаете себе отчет, что говорите с представителем власти, Мистер Ким? "

             "Сержант почти впритык подошел к отцу погибшей. Во взгляде того читался мимолетный страх, вновь сменившийся на раздражение. "


             goskim "Да как ты…"

             s "Послушайте, господин! Ваша дочь - жертва убийства. Улик практически нет, мразь, которая это сделала, гуляет на свободе и возможно составляет план на новое преступление."
             s" И то, что в препятствуете расследованию, вызывает подозрения, не находите?"

             goskim "Мальчик, мне плевать на остальных. Моя дочь уже мертва, какое мне дело до проблем других людей."

             s "Как скажете, Мистер Ким. Мы в любом случае добьемся своего."

             "Ёнхва молча пошёл в сторону выхода, Сынхен раздраженно вздохнул и последовал за напарником. "

             s "А вот капитан кажется был прав насчет вас и вашей дочери. "

             goskim" Выметайтесь из моего дома!"

             #Локация - цг машина

             "Сынхен сел в машину, захлопывая дверь. Он хотел было начать говорить, но его перебил капитан."

             y "Ты блять понимаешь во что нас ввязал? У нас была простая задача - получить ебучую подпись." 
             y'Но ты блядь решил показать, какой ты “плахой палицейский” и не просто просрал все, так еще и обрубил нам даже шанс продвинуться в этом блядском деле?'
             y"Красавчик просто. "

             s"А что я должен делать? Беру пример с вас, капитан."

             "Ёнхва демонстративно отворачивается и достает телефон."

             y "Здравствуйте. Нет, согласия у нас нет. Я знаю, вскрывайте, под мою ответственность. "

             s "Вы с ума сошли?!"

             y "Ебало на ноль. "
             jump continue

label continue:

"Через пару секунд зазвонил телефон."

t" Алло, дядь. Я тут кое-что нашел."

y "Плательщика? Кидай адрес, сразу съездим. "

t "Не-не-не! Тут лучше! "

y "Оу, слушаю."

t "У вас на столе в зале лежала визитка ресторанчика корейской кухни. "

y "Так. И?"

t "А вы уже заказывали там? Там вкусно?"

s "…"

y "… Погоди. Ты серьезно?"

t "Ну, у вас в холодосе мышь повесилась. А я кушать хочу. "

y "… Лучше закажи курочку. "

t "На вас тоже?"

y "Да."

s "…"

y "А по поводу поручения, которое я тебе дал, есть что-нибудь?"

t "А. Ну. Вообще ничего. "

y  "И что ты будешь делать?  "

t "Может быть я смогу достать что-то из переписок и соцсетей этой девочки. Может быть она куда-то собиралась."

y "Умница. Все, что найдешь - сразу мне. "

t "Я все понял, я все сделаю. "

y "Все. Клади трубку, я за рулем."

if nadavit=True:
  "Юн обомлел, наблюдая за резко изменившимся настроем мужчины. Наблюдая, как Син перешел от пассивно-агрессивного общение с ним к буквально сюсюканью с хакером, сержант испытывал отвращенеи к лицемерности капитана. "
  "Сынхен с самого начала не понимал методы работы Ёнхва. То, как капитан изворачивался, врал, использовал незаконные способы  получения информации - все это не вписывалось в картину идеального следователя. "


if dogovor=1:
  "Юн с интересом наблюдал за тем, как Ёнхва общался с Такеши. Он с первых дней заметил, что капитан может находить общий язык почти со всеми. "
  "И несмотря на то, что его методы не всегда законны, но они приносят результат. "

  "Но в разговоре с господином Кимом, что-то пошло не так. "
  "Кажется, тема отца для капитана была по-настоящему болезненной, коль заставила того потерять контроль над собой. "
  "Сынхен, до этого скорее идеализируя самого Ёнхва и его родителя, от этих размышлений нахмурился. "

s '“Как же это раздражает.”'

"Глубоко задумавшись, Сынхен не сразу заметил изменение вида за окном. Они двигались явно не в участок. "

s "Погодите, а куда мы едем?"

y "Везу тебя домой."

s "Капитан, но мой дом в другой стороне..."

y "Пупсик, может сначала хотя бы кофе? А потом уже к тебе."

s "КАПИТАН СИН!"

y "Ладно, расслабь булки. "

#Локация - дом Сынхен

'''Тут что-то происходит. Его подвез ЁНхва.
цг дома. 
Продведение итога. 
Что нибудь еще. 
Плюс-минус лояльность 
Подводка к тому, что нужно быть умнее. '''

#Локация - офис

"Утро встретило Сынхена в офисе привычным гулом голосов и запахом кофе с соседней заправки. "
"Среди ползающих туда-сюда еще сонных полицейских, бодрым казался только Енхва."
" Направившись в сторону Юна, он ловко обогнул напарника, исчезая в соседнем крыле. "

y "Нужно кое-что уладить. Скоро вернусь."

"Сынхен даже не пытался выяснить причину скоро ухода начальника. Устало выдохнув, он пошел к своему столу. "

"Пока он пытался устроиться хоть как-то удобно на офисном стуле, краем уха он уловил разговор пары коллег, застрявших у кофе-машины. "

of1 "Да я говорю тебе!"

of2 "Слушай, ну не похож он на богатенького…"

of1"Ты в глаза долбишься? Сам подумай, он в пришел отдел сразу после выпуска с рекомендацией чуть ли не от президента. "

of1 "А тот проеб? Ты хоть раз видел, то после такого кого-то сразу ставили на должность капитана? Через два года после начала работы!" 

of2 "Хм… "

of1 "А почему не офицер Пак? Пришли они в одно время, косяков с его стороны не было, вообще классный мужик. "

of2 "Но он же не сидит на жопе в офисе, обязанности выполняет, бегает как все. "

of1 "Ой он просто пытается прикрыть себе зад! Если бы не носился, то вызвал бы больше подозрений!"

of2 "Не думаю, что Ёнхва пропихнули. Мы бы как сыр в масле катались всем офисом, если б это было правдой."

"Юн расслышал имя капитана, прежде чем диалог в его голове принял окончательный облик. "

if molodec==1: 
  s'“Я терпеть не могу лизоблюдов и подхалимов. Если тебе что-то не нравится - скажи в лицо.”'
  s '“Понятно, что Ёнхва имел в виду…”'

s '“Им что, заняться нечем?”'

of1 "Это тут причем?! "

of2 'Посуди сам. Будь он таким “саженцем”, он бы либо подмазывал нас, либо получал плюхи, которых нет у других. '

of2 "И чего-то я не замечал у него в кабинете фонтан с виски-кола.  "

of1 "Но бухать на рабочем месте это не мешает, заметь. "

menu:
   "Вмешаться в разговор.":
    $vmeshatca+=1
    jump vmeshatca

   "Подождать":
    $podojdat+=1
    jump podojdat

label vmeshatca:
"Сынхен не выдержал, поднялся с места и быстрым шагом направился в сторону коллег, которые теперь не вызывали у него ни капли уважения."
"При виде пылающего лица Юна оба сплетника в один момент замолкли, их глаза забегали."
of1  "О, сержант Юн, доброе утро! Как вам у нас, все нравится?"
"Сынхен смерил его холодным взглядом. Его до глубины души бесило то, что сослуживец так бесстыдно улыбался, хотя еще пару секунд назад поливал помоями его начальника."
of2  "Вы что-то хотели?"
s  "Мне кажется, или вы задержались у кофе машины? "

of1  "Не понял. "

of2 "О, вы у нас не давно. Еще кажется не разобрались с местными порядками. "

s " А устав в этом отделе работает как-то по особому? Или у вас закончились нераскрытые дела, коллеги?"
"Один из сослуживцев усмехнулся и потер переносицу. "
of1 " Очередной выпускник академии, который еще не познал все прелести работы в этой сфере."
"Теперь они переглядывались друг с другом, еле сдерживая смех. "
of1  "Обсуждать кого-то или что-то – это признак здорового общества. Так везде. И работе это не мешает."
"Юн нервно сжал кулаки. "
s '“Сынхен, терпи. Потом будут проблемы. Потом придется писать объяснительную.”'
of2  "Ничего, поработаешь с капитаном и тоже найдешь сотню причин его обосрать. "
of1  "Не забудь рассказать нам. Вместе обсудим. "
s '“Придется писать объяснительную…”'

s "Так, Биба и Боба, если у вас есть запасная почка, это не значит, что нужно ее использовать. Соберите свои важные мнения в ладошку и займитесь делом. "

of1 "Ты кем себя возомнил, сопляк! "

s  "Я - Юн Сынхен, сержант Центрального департамента по гражданским делам 12-ого района, подчиненный и напарник капитана Син Ёнхва! "
y  "Сержант Юн!"

"По спине пробежался холодок. Разгоревшаяся было ярость сразу сошла на нет. Голос капитана прозвучал за спиной Юна."
" Выражение лиц полицейских, еще недавно насмехающихся над сержантом моментально изменились. Сам Юн повернуться не решался. "

y  "А я тебя и искал. Пройди в мой кабинет, пожалуйста."

"Сынхен почувствовал, что его зовут явно не кофе попить. "

s '“Дерьмо…” '

if dolboeb==1:

  s "Нашли место языками чесать. Как вы еще в полиции держитесь?"

  "Сослуживцы, услышав реплику Сынхена сразу замолчали, обращая свое внимание на сержанта. "

  of1 "Чего сказал? "

  "Сынхен встал с места и подошел вплотную к полицейским."
  jump continue1

jump continue1

label podojdat:

s "Говорю вам больше нечем заняться? "

of2 "Эй, мальчик, а ты не обнаглел?"

of1 "А, я понял. Это же напарник капитана. Новенький."

of2 "Точняк. Решил впрячься за любимого начальника?"

"Полицейские засмеялись, подначивая друг друга. "

s "… Вместо того, чтобы языками чесать шли бы работать. Время отдыха закончилось десять минут назад."

"Один из офицеров толкнул сержанта в плечо и оскалился. "

of1 "Слушай сюда, малец…"
p "Что здесь происходит?!"

"Трое сотрудников сделали шаг в сторону друг от друга." 

of2 " Мы, это… Повздорили чутка. Бывает." 

p "Я видел. Оба ко мне с объяснительной. "

"Полицейские ушли вместе с офицером Паком и проследив за ними взглядом, Сынхен увидел капитана. "
"Ёнхва стоял рядом со своим кабинетом, сурово смотря на сержанта. Их взгляды встретились и тот жестом указал следовать за ним."

jump continue1

label continue1:

#Локация - офис Енхва

"Дверь с глухим хлопком закрылась за спиной у Сынхена. Ёнхва сел в свое кресло и указал жестом на диван. Сынхен приглашением не воспользовался. "

y "И что это было?"

s "Вы о чем?"

y "Не прикидывайся дурочкой. Что произошло?"

if loyaltyy == 2: 

    s "…Вы сами говорили, что любая претензия должна быть высказана в лицо."

    y "Я не так сказал. Но допустим. "

    s "И я высказал. "

    y "И что тебе это дало?"

    s "…"

    y 'Что по твоей логике должно было произойти, когда ты сказал этим двоим “в лицо”?'

    s "А я что должен был стоять и смотреть? Слушать, как вас поливают г…" 

    y "Гавном?"

    s "Да! "

    y "И ты, пупсик, решил встать грудью между теми двумя балбесами и моей гордостью, так?"

    s "… "

    "Енхва откинулся в кресле и усмехнулся. Казалось, ситуация забавляла его так же сильно, как злила Сынхена. "

    y "Послушай, ты конечно у нас мамкин защитник, блюститель устава и прочее… Но в следующий раз не ввязывайся в это. "

    s "Почему?!"

    y "Эти идиоты живут свою скучную жизнь, чем еще им заняться, как не обсуждать мою блистательную натуру? "
    y"Тем более ни на что новое у них мозгов не хватит. Я на этой телеге про отца еду с начала работы в отделе. "

    "После этих слов гнев немного отпустил, и Сынхен сел на диван."

    s"И вы нормально к этому относитесь?"

    y "А как мне к этому относится? Злиться? Жаловаться? Плакать? Пупсик, мнение мыши кошку не заботит. "

    s "… "
    y "Если обращать внимание на все, то можно поехать кукухой. Или начать пить, как я. Ты можешь гавкаться со всеми вокруг. "
    y "Изменит ли это что-то? Нет. Станет ли меньше слухов? Тоже нет. Тогда в чем смысл?"

    s "…"


if loyaltyy == 1 and  molodec:

    s "…Вы сами говорили, что любая претензия должна быть высказана в лицо."

    y "Когда я такое говорил? "

    s "…"

    y "Вспомни о чем шла речь. Я говорил обо всех или конкретно о себе?"

    s "… Вы говорили о себе."

    y "Тогда в чем проблема?"

    s "То есть для вас нормально, что вас обсуждают за спиной? "

    y "Да вообще пофиг. Пусть обсуждают, надо же малышам пар выпустить."

    s "Но это неправильно! Они нарушают рабочую обстановку!"

    y "Прям нарушают? Прям всем или только тебе?"

    s "Какое это имеет значение? "

    y "Слушай, если тебе скучно живется и тебе хочется ввязаться в перепалку, тогда лучше займись делом. Либо подумай, то ли это место, в котором ты хочешь работать?"

    s "…"

    y"Эти чуваки обсуждают меня не потому что у них жизнь хорошая. Ты в первую очередь следи за собой. "

    s "… Как скажете. "

if loyaltyy == 0:
    s "А я разве прикидываюсь? "

    y "Значит ты дурочка?"

    s "Что вам от меня надо? У вас есть какое-то задание для меня?"

    y "Прикидываться долбоебом, так до конца? Ясно. Хорошо. Ты скажи мне, пупсик, на кой хер ввязался в спор с этими идиотами?"

    s "А с чего вы взяли, что это был спор? Это рабочее место, тут надо работать! "

    y "А ты чем занимался? "

    s "Уже было рабочее время и я поступил так, как должен был поступить. Правила для всех одинаковые и исключений быть не должно. "

    y "Хорошо, они ужасные. Выговор им и штраф. Но как это касается тебя?"

    s "…"

    y "У них есть свое начальство, ты им никто. Так с какого хера ты решил, что можешь наводить порядок в офисе? Кто дал тебе это право? "

    s "Но вас как капитана не было на месте!"

    y "С чего ты взял, что я не был на рабочем месте? Мне перед тобой тоже отчитываться? "

    s "… Никак нет."

    y "Так вот. Послушай сюда, щенок. Ты здесь никто. По документам ты - сержант, мой напарник, и прочее-прочее. А по факту… я думаю ты сам понял, нет смысла повторять. "

    s "…"

    y "Займись работой и прекращай страдать херней. "
if molodec==1:
    s'“Может он и прав.”'

    y "Расслабь булки и направь энергию на полезные вещи. "




return