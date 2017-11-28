class ProductGroup():
    # Класс, описывающий товарную группу. Содержит следующие параметры:
    # number - Номер товарной группы
    # nameW  - Рабочее название, использующееся как название таблиц или вкладок
    # nameM  - Основное название, использующееся в том числе и как тип прибора
    # nameC  - Название соответствующей категории в 1С
    def __init__(self, number, nameW, nameM, nameC):
        self.number = int(number)
        self.nameW = nameW
        self.nameM = nameM
        self.nameC = nameC

