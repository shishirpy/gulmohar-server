import pytest

from broker import MajorDomoBroker, Service



class TestBroker():
    def test_destroy_broker(self):
        mdb = MajorDomoBroker()
        m = mdb.destroy()
        assert m is None

    def test_process_client(self):
        mdb = MajorDomoBroker()

        try:
            mdb.process_client("abc", [123])
        except AssertionError:
            assert True


    # def test_internal_service(self, monkeypatch):
    #     mdb = MajorDomoBroker()

    #     def mockreturn():
    #         return ['']

    #     try:
    #         mdb.service_internal(b"abc", range(10))


    def test_require_service(self):
        mdb = MajorDomoBroker()

        try:
            mdb.require_service(None)
        except AssertionError:
            assert True

        service = mdb.require_service(b'abc')
        print(type(service))
        assert isinstance(service, Service)


