# SSmeta

Написать приложение для частных мастеров по осмечиванию квартир и помещений.
Используемые яп: котлин, пайтон, с#?

Пользователь приложения при встрече с заказчиком должен замерить помещение по типу замера натяжных потолков. Т.е. начиная с левого угла промерить периметр помещения по  часовой стрелке. Померить необходимые для вычисления площади диагонали, высоту помещения, проемы. Определиться с материалами. Приложение должно оформить спецификацию материалов, смету работ. Вероятно также стоит спроектировать возможность внесения данных заказчика и помещения, для оформления стандартного договора подряда.

Работа с приложением и замерами следующая:
1. Замерщик считает количество углов, вносит в приложение.
2. Приложение выдает таблицу необходимых сторон по типу AB, BC, CD и т.д.
3. Замерщик замеряет начиная с левого угла по часовой стрелке и заполняет таблицу.
4. Следующий этап выдается таблица всех возможных диагоналей
5. Замерщик определяет какие из диагоналей нужны, снимает замер, вносит в таблицу. По мере заполнения таблицы диагоналей, не нужные диагонали блокируются.
6. Заполняются значение высоты помещения
7.  Снимаются замеры проемов начиная с нижнего левого угла по периметру, чтоб определить местоположение на стене снимается расстояние от нижнего левого угла до пола и до левой стены, также снимаются необходимые диагонали, в общем принцип тот же, что и при замере площади.
Замеры проемов нужны чтобы расчитать площадь стен, а также учесть в смете отделку откосов, поэтому нужно различать замер проема двери и замер проема окна, так как проем окна требует(как правило) отделки правого, левого и верхнего откоса одним типом материала, а нижней части другого (подоконника). В случае с проемом двери, отделка может не требоваться если устанавливается дверь, или требуется отделка только верхней и боковых частей
8. Должна быть возможность внесения в таблицу работ не возможных учесть и расчитать автоматически
9  Должна быть возможность корректировки автоматически расчитанных данных.




