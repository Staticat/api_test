from logs.log import log1
def assert_(request):
    assert ('"repNote":"SUCCESS"') in request.text
    assert request.status_code == 200

