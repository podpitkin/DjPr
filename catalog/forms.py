from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    FORBIDDEN_WORDS = [
            'казино',
            'криптовалюта',
            'крипта',
            'биржа',
            'дешево',
            'бесплатно',
            'обман',
            'полиция',
            'радар',
        ]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Название продукта'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Описание продукта', 'rows': 4})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Цена в рублях'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['created_at'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Дата создания'})
        self.fields['updated_at'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Дата последнего изменения'})

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price is not None and price < 0:
            raise ValidationError('Цена не может быть отрицательной. Пожалуйста, введите корректное значение.')

        return price


    def clean_name(self):
        name = self.cleaned_data.get('name')

        if name:
            name_lower = name.lower()
            for forbidden_word in self.FORBIDDEN_WORDS:
                if forbidden_word in name_lower:
                    raise ValidationError(
                        f'Название содержит запрещенное слово "{forbidden_word}". '
                        f'Измените название продукта.'
                    )

        return name


    def clean_description(self):
        description = self.cleaned_data.get('description')

        if description:
            description_lower = description.lower()
            for forbidden_word in self.FORBIDDEN_WORDS:
                if forbidden_word in description_lower:
                    raise ValidationError(
                        f'Описание содержит запрещенное слово "{forbidden_word}". '
                        f'Измените название продукта.'
                    )

        return description


    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data