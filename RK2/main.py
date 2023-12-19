from operator import itemgetter

class Detail:
    def __init__(self, id, name, weight, comp_id):
        self.id = id
        self.name = name
        self.weight = weight
        self.comp_id = comp_id

class Manufacturer:
    def __init__(self, detail_id, name):
        self.id = detail_id
        self.name = name

class ManufacturerDetail:
    def __init__(self, manufact_id, detail_id):
        self.manufact_id = manufact_id
        self.detail_id = detail_id

def create_manufacturers():
    return [
        Manufacturer(1, 'Ява'),
        Manufacturer(2, 'Волга'),
        Manufacturer(3, 'ВАЗ'),
        Manufacturer(4, 'Тройка'),
        Manufacturer(5, 'Мальборо')
    ]

def create_details():
    return [
        Detail(1, 'болт', 173, 1),
        Detail(2, 'винт', 140,  2),
        Detail(3, 'штуцер', 97, 3),
        Detail(4, 'шуруп', 201, 4)
    ]

def create_manufacturer_details():
    return [
        ManufacturerDetail(1, 1),
        ManufacturerDetail(1, 2),
        ManufacturerDetail(2, 2),
        ManufacturerDetail(2, 4),
        ManufacturerDetail(3, 3),
        ManufacturerDetail(4, 2),
        ManufacturerDetail(4, 4),
        ManufacturerDetail(5, 2),
        ManufacturerDetail(5, 3),
        ManufacturerDetail(5, 4)
    ]

def get_one_to_many(details, manufacturers):
    return [(d.name, d.weight, m.name)
            for d in details
            for m in manufacturers
            if d.id == m.id
            ]

def get_many_to_many(one_to_many, manufacturer_details):
    many_to_many_temp = [(m.name, md.manufact_id, md.detail_id)
                         for m in manufacturers
                         for md in manufacturer_details
                         if m.id == md.manufact_id
                         ]
    return [(d.name, d.weight, manufact_name)
            for manufact_name, manufact_id, detail_id in many_to_many_temp
            for d in details if d.id == detail_id
            ]

def task_a2(one_to_many):
    res_2_unsorted = []
    for m in set(item[2] for item in one_to_many):
        m_details = list(filter(lambda i: i[2] == m, one_to_many))
        if len(m_details) > 0:
            m_weights = [weight for _, weight, _ in m_details]
            m_weights_sum = sum(m_weights)
            res_2_unsorted.append((m, m_weights_sum))
    return sorted(res_2_unsorted, key=itemgetter(1), reverse=True)

def task_a3(many_to_many):
    res_3 = {}
    for m in set(item[2] for item in many_to_many):
        if 'о' in m:
            m_details = list(filter(lambda i: i[2] == m, many_to_many))
            m_details_names = [x for x, _, _ in m_details]
            res_3[m] = m_details_names
    return res_3

def main():
    details = create_details()
    manufacturers = create_manufacturers()
    manufacturer_details = create_manufacturer_details()

    one_to_many = get_one_to_many(details, manufacturers)
    many_to_many = get_many_to_many(one_to_many, manufacturer_details)

    print('Задание A1')
    res_1 = sorted(one_to_many, key=itemgetter(2))
    print(res_1)

    print('Задание A2')
    res_2 = task_a2(one_to_many)
    print(res_2)

    print('Задание А3')
    res_3 = task_a3(many_to_many)
    print(res_3)

if __name__ == '__main__':
    main()