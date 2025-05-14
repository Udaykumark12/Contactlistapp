# from youtubecls.a.a import APIS
#
# import pytest
#
#
#
# @pytest.fixture(scope="module")
# def apis():
#     return APIS()
#
# def test_a(apis):
#     resp=apis.gett("users")
#     resp=resp.json()
#     print(resp)
#
#
# def test_b(apis):
#     resp = apis.delete_id()
#     assert resp.status_code == 405
#     print(resp.text)
#
#     # # Handle empty response body gracefully
#     # try:
#     #     res = resp.json()
#     #     print(res)
#     # except requests.exceptions.JSONDecodeError:
#     #     print("No JSON response body.")
#
#
