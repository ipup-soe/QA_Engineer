import pytest
import requests

"""
Для запуска тестов на вход нужно передать параметр запуска:
    --url=<адресс сайта>
    --status_code=<ожидаемоый статус-код ответа>
    
    параметры по умолчанию: 
    --url=https://ya.ru 
    --status_code=200
"""

def test_status_resp(base_url, base_status_code):
    resp = requests.get(base_url)
    assert resp.status_code == base_status_code
