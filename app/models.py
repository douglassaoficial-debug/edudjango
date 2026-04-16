from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    carga_horaria = models.IntegerField()
    nivel = models.CharField(max_length=50)

    def __str__(self): #EQUIVALENTE AO GETTER EM POO
        return self.nome

class Avaliacao(models.Model):
    # Uma tupla de opções para o Dropdown
    NOTAS_CHOICES = [
        ('1', '⭐ (1) Ruim'),
        ('2', '⭐⭐ (2) Regular'),
        ('3', '⭐⭐⭐ (3) Bom'),
        ('4', '⭐⭐⭐⭐ (4) Muito Bom'),
        ('5', '⭐⭐⭐⭐⭐ (5) Excelente'),
    ]

    nome_aluno = models.CharField(max_length=100)
    nome_curso = models.ForeignKey (Curso, on_delete=models.CASCADE) #Aqui, o atributo nome_curso vira uma lista dos objetos disponiveis do model Curso 
    nota = models.CharField(max_length=1, choices=NOTAS_CHOICES)
    comentario = models.TextField()

    def __str__(self):
        return f"Avaliação de {self.nome_aluno} para o curso {self.nome_curso} - Nota: {self.nota}"