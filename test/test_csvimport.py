#!/usr/bin/python env

import unittest
import base

import asm3.csvimport

class TestCSVImport(unittest.TestCase):

    def tearDown(self):
        base.execute("DELETE FROM animal WHERE AnimalName = 'TestioCSV'")

    def test_csvimport(self):
        csvdata = "ANIMALNAME,ANIMALSEX,ANIMALAGE\n\"TestioCSV\",\"Male\",\"2\"\n"
        asm3.csvimport.csvimport(base.get_dbo(), csvdata)

