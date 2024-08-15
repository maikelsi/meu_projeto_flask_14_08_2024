import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


@pytest.fixture
def driver():
    driver = webdriver.Firefox()  # Inicia o navegador Firefox
    yield driver
    driver.quit()  # Fecha o navegador após cada teste


def test_home_page(driver):
    driver.get("http://127.0.0.1:5000/curriculo")  # Acessa a página do currículo
    time.sleep(1)
    assert (
        "Currículo Vitae" in driver.page_source
    )  # Verifica se "Currículo Vitae" está na página


def test_user_login(driver):
    driver.get("http://127.0.0.1:5000/login")  # Acessa a página de login
    time.sleep(1)

    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys("admin")  # Digita o nome de usuário
    time.sleep(1)

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("senha123")  # Digita a senha
    time.sleep(1)

    password_input.send_keys(Keys.RETURN)  # Simula o Enter para submeter o formulário
    time.sleep(1)

    assert "Biblioteca" in driver.page_source  # Verifica se o login foi bem-sucedido
