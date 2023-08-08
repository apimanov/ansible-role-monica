import os
import pytest
import http.client

@pytest.mark.parametrize('rpm', [
'nginx',
'mariadb',
'php73-php-fpm'
])
def test_pkg(host, rpm):
    package = host.package(rpm)
    assert package.is_installed

def test_connection():
    path = "/"
    conn = http.client.HTTPConnection("monica")
    conn.request("GET", path)
    response = conn.getresponse()
    status_code = response.status
    assert status_code == 200, "if True - it's ok"
    conn.close()




    