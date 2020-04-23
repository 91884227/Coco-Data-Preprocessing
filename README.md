# Coco-Data-Preprocessing


## usage
python Coco_preprocessing.py coco_title_category_1_to_100_MAX_3.csv

即可產生 

coco_title_category_1_to_100_MAX_3_adjust.npy

_Remark:_ file的格式必須為:


| title | time | 
| -------- | -------- | 
|      |      |

## what this program do 
將
:::info

\n                        沒勞保也能改領1~3萬「救助金」！\u3000申請核定後最快24hrs發放！\n                    

:::

轉換成

:::info

沒勞保也能改領1~3萬「救助金」！ 申請核定後最快24hrs發放！

:::

並將長度小於10的title　刪除



# Coco-Data-Preprocessing
