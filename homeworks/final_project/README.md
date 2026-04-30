# Финальный проект

## Пул статей

* [Recommender Systems with Generative Retrieval](https://arxiv.org/abs/2305.05065)
* [Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations](https://arxiv.org/abs/2402.17152)
* [TwHIN: Embedding the Twitter Heterogeneous Information Network for Personalized Recommendation](https://arxiv.org/abs/2202.05387)
* [MultiBiSage: A Web-Scale Recommendation System Using Multiple Bipartite Graphs at Pinterest](https://arxiv.org/abs/2205.10666)
* [Density Weighting for Multi-Interest Personalized Recommendation](https://arxiv.org/abs/2308.01563)
* [Hiformer: Heterogeneous Feature Interactions Learning with Transformers for Recommender Systems](https://arxiv.org/abs/2311.05884)
* [TokenMixer-Large: Scaling Up Large Ranking Models in Industrial Recommenders](https://arxiv.org/abs/2602.06563)
* [OneTrans: Unified Feature Interaction and Sequence Modeling with One Transformer in Industrial Recommender](https://arxiv.org/abs/2510.26104)
* [MixFormer: Co-Scaling Up Dense and Sequence in Industrial Recommenders](https://arxiv.org/abs/2602.14110)
* [Retrieval with Learned Similarities](https://arxiv.org/abs/2407.15462)
* [Empowering Long-tail Item Recommendation through Cross Decoupling Network (CDN)](https://arxiv.org/abs/2210.14309)
* [Modeling Task Relationships in Multi-task Learning withMulti-gate Mixture-of-Experts](https://dl.acm.org/doi/pdf/10.1145/3219819.3220007)

Можно предложить свою статью, которой нет в пуле, но это надо сделать в личном порядке и согласовать до 5-го мая.

## Этапы сдачи финального проекта

Все дедлайны, кроме последнего - в 15:00. Присылать артифакты надо в соответствующее задание в энитаске. Дедлайны, кроме последнего (9-го июня), мягкие; за каждый день просрочки штраф - минус 0.5 балла.

### До 12-го мая
* Нужно разбиться на команды по **три человека** и выбрать капитана
    * капитан присылает в энитаске все артефакты для своей команды
* Нужно выбрать статью и написать **mini-abstract**, который объясняет:
    * почему выбрана именно эта тема/статья
    * чем она заинтересовала, почему команда считает её актуальной
    * что планируете исследовать

### До 19-го мая
* Нужно прислать критику статьи и research plan
* Что должно быть в критике
    * Ключевые тезисы статьи
    * Слабости / ограничения работы
    * Проблемы - воспроизводимость, валидность выбора датасетов и экспериметнального сетапа (оценки качества и тд)
* Что должно быть в research proposal
    * Какие датасеты вы планируете использовать и какой протокол оценки качества
    * Какие бейзлайны будете обучать
    * Какие ставите перед собой research quetions

### До 2-го июня
* Нужно прислать ссылку на репозиторий с кодом и на pdf отчёт (до трёх страниц)
* Репозиторий с кодом должен быть самодостаточен для запуска всех экспериментов из отчёта
    * Инструкция для запуска в README
* Pdf отчёт должен содержать:
    * мини-абстракт
    * описание экспериментального сетапа (датасеты, протокол оценки качества, бейзлайны)
    * список RQ (research questions)
    * экспериментальную секцию с результатами экспериментов и выводами по ним

### На занятии 9-го июня 
* К занятию нужно приготовить десятиминутную презентацию своей работы
* Рассказать про решаемую задачу, ключевую идею, эксперименты, выводы, инсайты

## Оценка (максимум 10 баллов)
* **Воспроизводимость (3):** Код запускается и выдаёт правильные результаты (те же, что репортятся в статье)
* **Experimental Validity (3):** Правильный сетап оценки качества, бейзлайны, датасеты
* **Research Depth (2):** Правильно сформулированные гипотезы, правильно выбранные эксперименты для подтверждения этих гипотез, полноценные выводы по экспериментам
* **Presentation Quality (2):** Оценивается качества абстракта, отчета, репозитория с кодом и презентации в совокупности

## Дополнительные комментарии
* Если что-то не сработало - это нормально. Отрицательный результат тоже можно оформить как эксперимент. Но если в статье совсем ничего не завелось - это уже плохо
* В статьях про скейлинг (где сильно увеличивают модели) нужно ограничиться разумными масштабами, на которые есть ресурсы. В пуле нет статей, в которых единственная новизна - это скейлинг, в каждой статье как правило есть более фундаментальные изменения
* Много информации про корректные сетапы оценки качества и типичные ошибки в таких проектах можно почерпнуть из семинара [DeepRecSys, cеминар 3: Рексистемы глазами исследователя](https://www.youtube.com/watch?v=tnrw1quaZF0&t=2633s)
