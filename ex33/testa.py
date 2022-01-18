import unittest
from conta import Conta
class TestConta(unittest.TestCase):
    def setUp(self):
        self.conta = Conta("mr.teabag ", 2, 1000)
    def test_dono(self):
        assert self.conta.dono == "Mr.Teabag "
    def test_taxa_de_juro(self):
        self.assertIsInstance(self.conta.taxa_de_juro,(int, float))
        self.assertGreaterEqual(self.conta.taxa_de_juro, 0)
    def test_saldo(self):
        self.assertIsInstance(self.conta.saldo,(str))
        self.assertGreaterEqual(self.conta.saldo, 0)
        self.conta.saldo = -10
        self.assertGreaterEqual(self.conta.saldo, 0)
    def test_capitaliza(self):
        self.conta.capitaliza()
        self.assertAlmostEqual(self.conta.saldo, 1020)
    def test_cobra_comissao(self):
        # tem valor que chegue
        self.conta.saldo = 1000
        valor = 10
        cobrado = self.conta.cobra_comissao(valor)
        self.assertAlmostEqual(self.conta.saldo, 990)
        self.assertEqual(cobrado, 10)
        # nao tem valor que chegue
        self.conta.saldo = 100
        valor = 200
        cobrado = self.conta.cobra_comissao(valor)
        self.assertAlmostEqual(self.conta.saldo, 0)
        self.assertEqual(100, cobrado)
    def test_faz_levantamento(self):
        self.conta.saldo = 1000
        valor = 100
        resp = self.conta.faz_levantamento(valor)
        self.assertTrue(resp)
        self.assertAlmostEqual(self.conta.saldo, 900)
        self.conta.saldo = 100
        valor = 200
        resp = self.conta.faz_levantamento(valor)
        self.assertFalse(resp)
        self.assertAlmostEqual(self.conta.saldo, 100)
    def test_faz_deposito(self):
        self.conta.saldo = 1000
        valor = 100
        self.conta.faz_deposito(valor)
        self.assertAlmostEqual(self.conta.saldo, 1100)
unittest.main()
