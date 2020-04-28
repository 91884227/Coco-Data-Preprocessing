# Coco-Data-Preprocessing


## usage

```
python Coco_preprocessing.py Filename
```
Filename 為檔案名稱
即可產生 
Filename_adjust.npy

### example 
```
coco_title_category_1_to_100_MAX_3.csv
```
即可產生 
coco_title_category_1_to_100_MAX_3_adjust.csv

_Remark:_ file的格式必須為:


| title | time | 
| -------- | -------- | 
|      |      |

## what this program do 
將

`\n                        沒勞保也能改領1~3萬「救助金」！\u3000申請核定後最快24hrs發放！\n                   ` 

轉換成

`沒勞保也能改領1~3萬「救助金」！ 申請核定後最快24hrs發放！`

並將長度小於10的title　刪除



