from django.shortcuts import render


# Create your views here.
def home(request):
	return render(request, 'sl/home.html')


def user_detail(request, uid):
	users_data = {
		1: {
			'name': 'Белогорский МО',
			'logo': 'faw0y357am736w3eppfhl5ufude7h4i5.png',
			'resources': [
				'Глина',
				'Песок',
				'Песчано-гравийная смесь',
				'Транспортная доступность'
			],
			'events': [
				'Восстановление кирпичного завода',
				'Расширение номенклатуры выпускаемой продукции'
			]
		},
		3: {
			'name': 'Ивановский МО',
			'logo': '84c4b4e347a16c88c5fe44e1a7826242.png',
			'resources': [
				'Глина для производства кирпича М 100,150',
				'Песок карьерный',
				'Песчано-гравийная смесь природная',
				'Товарный бетон',
			],
			'events': [
				'Транспортно-логистический комплекс «Сухой порт Благовещенск»',
				'Строительство кирпичного завода',
				'Строительство завода по производству керамзита и изделий из него',
				'Завод по переработке цементного клинкера'
			]
		},
		9: {
			'name': 'Завитинский  МО',
			'logo': '3b82a1bfbdbaac22450b1cfe07ba2bda.png',
			'resources': [
				'Глина',
				'Песок'
			],
			'events': [
				'Подготовка специалистов строительной отрасли на базе аграрного колледжа',
				'Расширение производства окон',
				'Расширение производства тротуарной плитки',
				'Расширении базы автотранспортного предприятия'
			]
		},
		10: {
			'name': 'г. Райчихинск',
			'logo': '83d4e8a4991c2829347c2eaaa8ff54e0.png',
			'resources': [
				'Наличие строительной компании с развитой материально-технической базой',
				'Райчихинский индустриальный техникум',
				'Производство асфальта',
				'Транспортные компании по перевозке крупных грузов',
				'Пассажирское автотранспортное предприятие'
			],
			'events': [
				'Расширение производственных мощностей на имеющемся строительно-монтажном предприятии',
				'Внедрение новых специальностей на базе индустриального техникума',
				'подготовка (ускоренная) специалистов высокого спроса на базе центра занятости'
			]
		},
		2: {
			'name': 'Бурейский  МО',
			'logo': '73dfb1ac3ce9c0209c3721b06f1888b6.png',
			'resources': [
				'Дармоканское местороджение - кварцевый песок',
				'Производство щебня, отсева',
				'Производство ЖБИ',
				'Производство тротуарной плитки',
				'Границы ТОСЭР',
				'Возможность создания технопарков',
				'Производство пенобетона'
			],
			'events': [
				'Разработка месторождения кварцевого песка',
				'расширение границ ТОСЭР',
				'расширение номенклатуры производимой продукции на действующем заводе по производству ЖБИ'
			]
		},
		5: {
			'name': 'Благовещенский МО',
			'logo': 'cb9e3d79f69aeccca94e8ec3f01f4f6f.png',
			'resources': [
				'Добыча ПГС, глины и строительного камня',
				'Производство красного кирпича',
				'Производство изделий из бетона',
				'Производство асфальтобетонных смесей',
			],
			'events': [
				'Использование имущественного комплекса Таможенно-логистического терминала “Кани-Курган”',
				'Создание завода по производству товарного бетона на ТОР',
				'Создание предпрития по производству изделий из цемента на ТОР',
				'Создание склада хранения металлоконструкций',
				'Расширение номенклатуры выпускаемой продукции на действующем кирпичном заводе'
			]
		},
		8: {
			'name': 'Тамбовский МО',
			'logo': '5235e43a26d9e45f3cb774e546e74c40.png',
			'resources': [
				'Производство красного кирпича, ж/б труб',
				'Глина',
				'Амурский казачий колледж'
			],
			'events': [
				'Расширение номенклатуры выпускаемой продукции на действующем кирпичном заводе',
				'Создание транспортно логистического узла',
				'Подготовка специалистов строительной отрасли, на базе Амурского казачьего колледжа'
			]
		},
		4: {
			'name': 'Константиновский МР',
			'logo': '1ad2ec59d3599c841e4f33eea643a8f2.png',
			'resources': [
				'Глина для красного кирпича',
				'ПГС для товарного бетона и дорог',
				'Товарный бетон',
				'1 подрядчик для строительства МКД, 2 для ИЖС',
			],
			'events': [
				'Возобновление работы кирпичного завода',
				'Задействование 3-х производителей товарного бетона',
				'Изготовление бетонных МАФов для благоустройства территорий МКД'
			]
		},
		7: {
			'name': 'пгт Прогресс',
			'logo': 'gerb-pgt.-Progress.jpg',
			'resources': [
				'Песок',
				'Песчано-гравийная смесь'
			],
			'events': [
				'Расширение производства ЖБИ (перекрытия, лестничные марши, сваи)',
				'Мусороперерабатывающий завод ТКО + сортировочный завод по резине и строительному мусору'
			]
		},
		6: {
			'name': 'Архаринский МО',
			'logo': '7809233945411e67f8ff3c5453c299a6.png',
			'resources': [
				'Лес',
				'Песчано-гравийная смесь',
				'Песок',
				'Товарный бетон',
				'Щебень',
				'Бурые угли',
				'Бентонитовые глины',
				'Базальты',
				'Известняк',
				'Известняковая мука, торф, сапропель, сурьма, фосфатно-карбонатное сырьё',
				'Туф'
			],
			'events': [
				'Изготовление пескоблоков',
				'Создание предприятия по деревообработке, производству пиломатериалов и изделий из дерева',
				'Открытие цементного завода'
			]
		},
	}

	data = users_data[uid]
	return render(request, 'sl/user-detail.html', {
		'name': data['name'],
		'logo': data['logo'],
		'resources': data['resources'],
		'events': data['events']
	})