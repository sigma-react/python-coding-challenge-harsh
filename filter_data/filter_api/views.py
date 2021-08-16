from rest_framework.response import Response
from rest_framework.views import APIView
from prettytable import PrettyTable
import pandas as pd

table = PrettyTable()
table.field_names = ['id', 'name', 'price', 'expires']


class FilterApi(APIView):
    def post(self,request):
        input_data = request.POST.get("input_data")
        data_read = pd.read_csv("F:\PycharmProjects\pythonProject\products.csv")

        data_list = input_data.split(" ")

        min_value = float(data_list[0])

        max_value = float(data_list[1])

        start_date = data_list[2].split("-")

        end_date = data_list[3].split("-")

        prices = list(data_read["price"])

        filtered_price = []

        # print(prices)

        for i in prices:
            if min_value <= i <= max_value:
                if i not in filtered_price:
                    filtered_price.append(i)

        first_start = start_date[0].lower()
        end_start = end_date[0].lower()
        months = {"jan": 1, "feb": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7, "aug": 8,
                  "sep": 9, "oct": 10,
                  "nov": 11, "dec": 12}
        first_month = months[first_start]
        end_month = months[end_start]

        # expires = list(data_read["expires"])
        expires_list = []
        for x in filtered_price:
            expires_element = list(data_read[data_read.price == x].expires)
            for d in expires_element:
                if d not in expires_list:
                    try:
                        ids = data_read[(data_read.expires == d) & (data_read.price == x)].id
                        names = data_read[(data_read.expires == d) & (data_read.price == x)].name
                        list_maker = [int(ids), list(names)[0], x, d]
                        expires_list.append(list_maker)
                    except Exception:
                        pass

        for j in expires_list:
            dates = j[3].split("/")
            mon = int(dates[0])
            day = int(dates[1])
            year = int(dates[2])

            if int(start_date[2]) <= year <= int(end_date[2]):
                if first_month <= mon <= end_month:
                    if int(start_date[1]) <= day <= int(end_date[1]):
                        table.add_row(j)

        print(table)
        table.clear_rows()

        return Response(table)
