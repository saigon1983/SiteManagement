class SKU():

    def __init__(self, mainData, productGroups, properties):
        self.initMainData(mainData)
        self.initProductGroups(productGroups)
        self.initProperties(properties)

    def initMainData(self, mainData):
        errorMessage_1 = 'Ошибка при создании номенклатуры! '
        errorMessage_2 = ', поэтому создание номенклатуры невозможно!'
        if isinstance(mainData, dict):
            if len(mainData) > 0:
                self.article    = mainData['Article']   # Артикул товара
                self.genus      = mainData['Genus']     # Тип товара
                self.brand      = mainData['Brand']     # Бренд товара
                self.model      = mainData['Model']     # Модель товара
                return
            else:
                errorMessage_1 += 'Словарь mainData пуст'
        else:
            errorMessage_1 += 'mainData не является словарем'
        raise TypeError(errorMessage_1 + errorMessage_2)

    def initProductGroups(self, productGroups):
        pass

    def initProperties(self, properties):
        pass