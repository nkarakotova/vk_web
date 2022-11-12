from django.db import models

QUESTIONS = [
	{
		'id': question_id,
		'title': f'Question #{question_id}',
		'text': f'Text of question #{question_id}',
		'answers_number': question_id * question_id,
		'rating': f'{question_id}'

	} for question_id in range(10)
]


ANSWERS = [
	{
		'id': answer_id,
		'text': f'Text of question #{answer_id}',
		'rating': f'{answer_id}'

	} for answer_id in range(10)
]