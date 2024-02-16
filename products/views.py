from django.shortcuts import render


def index(request):
    context = {
        'title': 'WebStore',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'WebStore - Product',
        'products': [
            {
                'image': '/static/vendor/img/products/Adidas-hoodie.png',
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'price': '6990',
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
            },
            {
                'image': '/static/vendor/img/products/Adidas-hoodie.png',
                'name': 'Худи черноо цвета с монограммами adidas Originals',
                'price': '69990',
                'description': 'Мягка ткань для свитшотов. Стиль и комфорт – это образ жизни.'
            },
            {
                'image': '/static/vendor/img/products/Adidas-hoodie.png',
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'price': '6940',
                'c': 'Мягкая ткан для свитшотов. Стиль и комфорт – это образ жизни.'
            }
        ]

    }
    return render(request, 'products/products.html', context)