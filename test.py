from app import Login

# Importamos a biblioteca de testes
import unittest


class TestHomeView(unittest.TestCase):

    '''
      Como todos os 3 casos de teste fazem um get na home "/"
      da nossa aplicacao, definimos a funcao setUp. Ela e executada
      automaticamente sempre que o Pytest instancia a classe TestHomeView.
      A funcao setUp e semelhante a um metodo construtor.
    '''

    def setUp(self):
        app = Login.test_client()
        data = {
            "firstName": "Lucas",
            "lastName": "Noblat",
            "email": "lucasnoblat1@gmail.com",
            "password": "123456",
            "nameStarWars": "Dar"
        }
        self.response = app.post('/login', data=data)


    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        self.assertIn('application/json', self.response.content_type)