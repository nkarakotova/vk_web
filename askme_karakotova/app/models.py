from django.db import models

ANSWERS = [
	{
		'id': answer_id,
		'text': f'Text of answer #{answer_id}',
		'rating': f'{answer_id}'

	} for answer_id in range(10)
]

QUESTIONS = [
	{
		'id': question_id,
		'title': f'Question #{question_id}',
		'text': f'Text of question #{question_id}',
		'answers_number': question_id * question_id,
		'rating': f'{question_id}',
		'answers': ANSWERS,
		'tags': ['kotiki', 'sobachki', 'zayki']

	} for question_id in range(10)
]

IS_AUTHORISATED = False

POPULAR_TAGS = [
	{'name': 'kotiki', 'style': 'custom-tags-max-popular'},
	{'name': 'sobachki', 'style': 'custom-tags-popular'},
	{'name': 'zayki', 'style': 'custom-tags-min-popular'},
]

BEST_MEMBERS = [
	{'name': 'Mr. Korgi'},
	{'name': 'Mr. Zaits'},
	{'name': 'Mr. Kot'},
]
