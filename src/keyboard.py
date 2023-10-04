from src.item import Item


class MixinLanguage:
    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self.__language = language

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, other_language):
        if other_language in ['RU', 'EN']:
            self.__language = other_language
        else:
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
            return self
        self.language = 'EN'
        return self


class Keyboard(MixinLanguage, Item):
    pass
