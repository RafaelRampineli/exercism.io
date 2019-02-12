from datetime import timedelta
# timedelta = expressa a diferença entre 2 datas. Adicionando os segundos 1E9
def add_gigasecond(birth_date):
	return birth_date + timedelta(seconds=1E9)
