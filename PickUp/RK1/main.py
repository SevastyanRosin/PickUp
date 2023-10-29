from operator import itemgetter

class detail:
    def __init__(self, id, name, weight, comp_id):
        self.id = id
        self.name = name
        self.weight = weight
        self.comp_id = comp_id

class manufact:
    def __init__(self, detail_id, name):
        self.id = detail_id
        self.name = name

class manudet:
    def __init__(self, manufact_id, detail_id):
        self.manufact_id = manufact_id
        self.detail_id = detail_id

manufacts = [
    manufact(1, 'Ява'),
    manufact(2, 'Волга'),
    manufact(3, 'ВАЗ'),
    manufact(4, 'Тройка'),
    manufact(5, 'Мальборо')
]

details = [
    detail(1, 'болт', 173, 1),
    detail(2, 'винт', 140,  2),
    detail(3, 'штуцер', 97, 3),
    detail(4, 'шуруп', 201, 4)
]

manufacts_details = [
    manudet(1, 1),
    manudet(1, 2),
    manudet(2, 2),
    manudet(2, 4),
    manudet(3, 3),
    manudet(4, 2),
    manudet(4, 4),
    manudet(5, 2),
    manudet(5, 3),
    manudet(5, 4)
]

def main():
    one_to_many = [(d.name, d.weight, m.name)
                   for d in details
                   for m in manufacts
                   if d.id == m.id
                   ]
    many_to_many_temp = [(m.name, md.manufact_id, md.detail_id)
                         for m in manufacts
                         for md in manufacts_details
                         if m.id == md.manufact_id
                         ]
    many_to_many = [(d.name, d.weight, manufact_name)
                    for manufact_name, manufact_id, detail_id in many_to_many_temp
                    for d in details if d.id == detail_id
                    ]

    print('Задание A1')
    res_1 = sorted(one_to_many, key=itemgetter(2))
    print(res_1)

    print('Задание A2')
    res_2_unsorted = []
    for m in manufacts:
        m_details = list(filter(lambda i: i[2]==m.name, one_to_many))
        if len(m_details) > 0:
            m_weights = [weight for _,weight,_ in m_details]
            m_weights_sum = sum(m_weights)
            res_2_unsorted.append((m.name, m_weights_sum))
    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse = True)
    print(res_2)

    print('Задание А3')
    res_3 = {}
    for m in manufacts:
        if 'о' in m.name:
            m_details = list(filter(lambda i: i[2]==m.name, many_to_many))
            m_details_names = [x for x,_,_ in m_details]
            res_3[m.name] = m_details_names
    print(res_3)
if __name__ == '__main__':
    main()