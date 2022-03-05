# hse_hw1_meth
Изучение глобального изменения уровня CpG метилирования ДНК при раннем эмбриональном развитии мыши
## [Google Colab link](https://colab.research.google.com/drive/1lTmqBHPXeiX-GZQMxfl7XUzR-kQB5bwS?usp=sharing)
## 1. Особенности бисульфитного секвенирования
### Per base sequence content
В ДНК\РНК секвенировании в соответствии со вторым правилом Чаргаффа мы получаем риды, в которых в среднем содержание аденинов совпадает с содержанием теминов, а цитозинов - с гуанинов. В бисульфитном секвенировании большая часть цитозинов превращается в тимины, в результате чего мы наблюдаем на графике сильно заниженное содержание цитозинов и сильно завышенное содержание тиминов.
### Per sequence GC content
В ДНК\РНК секвенировании несмещенного образца распределение GC содержания в ридах должно быть близким к нормальному распределению, построенному на основе GC содержания в исследуемых данных. В бисульфитном секвенировании из-за превращения метилированных цитозинов в тимины мы можем получить распределение сильно отличающиеся от нормального.
## 2.
### a) Число ридов, закартированных на интересующие участки
Cell type | Reads mapped at 11347700-11367700 | Reads mapped at 40185800-40195800 |
 --- |--- |---
8 cell | 1090 | 464
ICM | 1456 | 630
Epiblast | 2328 | 1062
### b) Сколько процентов прочтений дуплицированно в каждом из образцов?
Cell type | Duplication % |
 --- |---
8 cell | 18.31
ICM | 9.08
Epiblast | 2.92
### e) Гистограммы распределения метилирования цитозинов по хромосоме
#### 8 cell
![](images/8_cell_hist.png)
#### ICM
![](images/icm_hist.png)
#### Epiblast
![](images/epiblast_hist.png)
### f) Визуализиция уровня метилирования и покрытия для каждого образца
#### 8 cell
![](images/cell8_track.png)
#### ICM
![](images/icm_track.png)
#### Epiblast
![](images/epiblast_track.png)
