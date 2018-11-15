PRODUCTS = [
    # название, цена
    ['яблоки', 100],
    ['швейцарский сыр', 1500],
    ['красная рыба', 450]
]


def get_max_product_length(purchases):
    products_lengths = [len(product) for product, price in purchases]
    return max(products_lengths)


def generate_raw_cheque(purchases):
    max_cheque_product_width = get_max_product_length(purchases)
    max_cheque_price_width = 10  # 99999 руб.
    space = 5  # space between product and price
    line_length = max_cheque_product_width + space + max_cheque_price_width
    return [
        '{:<{}}{}{:>{}}'.format(
            product,
            max_cheque_product_width,
            ' ' * space,
            '{} руб.'.format(price),
            max_cheque_price_width
        )
        for product, price in purchases
    ], line_length


def beautify_cheque(raw_cheque):
    vertical_border = '|'
    horizontal_border = '-'
    raw_cheque_list, line_length = raw_cheque
    # add empty strings
    temporary_cheque = add_items_to_start_and_end(
        raw_cheque_list,
        ' ',
        line_length
    )
    # add vertical borders
    cheque_with_borders = [
        '{}{}{}'.format(
            vertical_border,
            position,
            vertical_border
        ) for position in temporary_cheque
    ]
    # add horizontal borders (+2 for vertical borders)
    beautiful_cheque = add_items_to_start_and_end(
        cheque_with_borders,
        horizontal_border,
        line_length + 2
    )
    return beautiful_cheque


def add_items_to_start_and_end(_list, filler, length):
    _list.insert(0, '{}'.format(filler * length))
    _list.append('{}'.format(filler * length))
    return _list


def print_cheque(cheque_data):
    for line in cheque_data:
        print(line)


if __name__ == '__main__':
    cheque = beautify_cheque(generate_raw_cheque(PRODUCTS))
    print_cheque(cheque)