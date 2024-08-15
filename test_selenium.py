import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class FlaskAppTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()  # Fecha o navegador após cada teste

    def test_home_page(self):
        self.driver.get("http://127.0.0.1:5000/curriculo")  # Acessa a página inicial
        time.sleep(1)
        self.assertIn(
            "Currículo Vitae", self.driver.page_source
        )  # Verifica se "Lista de Livros" está na página

    def test_user_login(self):
        self.driver.get("http://127.0.0.1:5000/login")  # Acessa a página de login
        time.sleep(1)

        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys("admin")  # Digita o nome de usuário
        time.sleep(1)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys("senha123")
        time.sleep(1)

        # Digita a senha
        password_input.send_keys(
            Keys.RETURN
        )  # Simula o Enter para submeter o formulário
        time.sleep(1)

        self.assertIn(
            "Biblioteca", self.driver.page_source
        )  # Verifica se o login foi bem-sucedido


if __name__ == "__main__":
    unittest.main()
    