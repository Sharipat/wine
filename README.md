# New Russian wine

Website of the original wine store "New Russian Wine".

## Launch

- Download the code
- In the root of the folder, create a .env file, in which write 
```python
  FILENAME='/path to file.xlsx'
```
- Launch the site with the command 
  ```python
     python3 main.py
```

- Go to the website at [http://127.0.0.1:8000](http://127.0.0.1:8000).


## *Product table*

If you need to add new products, change the attached .xlsx file or create a new file according to the example:

| **Category**    |      **Name**       |   **Variety**   | **Price**|      **Picture**         |    **Promotion**     |
| --------------- | ------------------- | --------------- | -------- | ------------------------ | -------------------- |
| Белые вина      | Белая леди          | Дамский пальчик | 399      | belaya_ledi.png          |      Best Offer      |
| Напитки         | Коньяк классический |                 | 350      | konyak_klassicheskyi.png |                      |
| Красные вина    | Киндзмараули        | Саперави        | 550      | kindzmarauli.png         |                      |

- When you add the line “Best offer”, a corresponding plate will appear on the product image. 
- The categories Promotion and Variety are optional, the remaining categories are required.


## Project goals

The code is written for educational purposes - this is a lesson in the course on Python and web development on the site [Devman](https://dvmn.org).