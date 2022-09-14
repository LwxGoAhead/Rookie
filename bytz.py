import pandas as pd
import openpyxl

# df_source = pd.read_excel(r'D:\G.O.A.T\bycz-triz\绩效统计-202201.xlsx',index_col=0,header=1)
# col = []
# aim_Sheet = pd.DataFrame(columns=col)
# #df_source = df_source.columns.get_level_values(0).values
# # df_source = df_source.reset_index(drop=True)
# # df_source = df_source.dropna(subset=['员工姓名'])
# # df_source = df_source.drop(index=0)
# # df_aim['姓名'] = df_source['员工姓名']
# # for i in df_source['员工姓名'].values:
# #     if df_source.loc[df_source['员工姓名'] == i]['实际工时（小时）'].values ==df_source.loc[df_source['员工姓名'] == i]['填报工时（小时）'].values:
# #         df_aim.loc[df_aim['姓名'] == i]['工时评价分数'].values = 100
# print(df_source.columns)
#f_source.to_excel(r'D:\G.O.A.T\bycz-triz\test1.xlsx')
# import xlwings as xw
# from future.moves import sys
#
# file_string = r"D:\G.O.A.T\bycz-triz\绩效统计-202201.xlsx"  # 修改为实际路径及文件名
#
# if __name__ == '__main__':
#     app = xw.App(visible=True, add_book=False)
#     app.display_alerts = False
#     app.screen_updating = False
#     try:
#         wb = app.books.open(file_string)
#         sht = wb.sheets[0]
#         rng = sht['A1:T1']
#
#         for j in range(0, len(rng.value[0])):  # 取第一行的数据
#             sht.range((5, j + 1)).value = rng.value[0][j]
#             if rng.value[0][j] is None and j > 0:
#                 sht.range((5, j + 1)).value = rng.value[0][j - 1]
#
#             if rng.value[1][j] != None:  # 合并第二行
#                 sht.range((5, j + 1)).value = sht.range((5, j + 1)).value + rng.value[1][j]
#
#         wb.save()
#         wb.close()
#     except:
#         print("Unexpected error:", sys.exc_info()[0])
#     app.quit()
# input()
wb = openpyxl.load_workbook(r'D:\G.O.A.T\bycz-triz\绩效统计-202201.xlsx')
sheet = wb['202201']
print(sheet['C2'].value)